#!/usr/bin/env python3
"""Genera web/data/network.json a partir de config/*.json + OpenStreetMap.

Uso:
    python3 tools/build_data.py            # usa la caché de tools/.cache si existe
    python3 tools/build_data.py --refresh  # vuelve a descargar todo de Overpass

Solo usa la librería estándar de Python (3.9+).
Datos de trazado y estaciones © colaboradores de OpenStreetMap (ODbL).
"""
import argparse
import json
import math
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, OrderedDict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
CACHE = ROOT / "tools" / ".cache"
OUT = ROOT / "web" / "data" / "network.json"

ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]
USER_AGENT = "japan-rail-explorer/0.1 (hobby project; build script)"

MERGE_SAME_NAME_M = 1200   # misma estación (mismo nombre japonés) en líneas distintas
NEARBY_M = 350             # estaciones distintas pero conectadas a pie
SIMPLIFY_DEG = 0.000015    # ~1,5 m de tolerancia al simplificar el trazado
PLATFORM_ROLES = {"platform", "platform_entry_only", "platform_exit_only"}


# ---------------------------------------------------------------- utilidades
def log(*a):
    print(*a, file=sys.stderr)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def haversine_m(a, b):
    lat1, lon1 = map(math.radians, a)
    lat2, lon2 = map(math.radians, b)
    h = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    return 2 * 6371000 * math.asin(math.sqrt(h))


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slugify(s):
    s = strip_accents(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# Nombres que OSM escribe distinto para la misma estación (se completa con overrides.json → ja_aliases)
JA_ALIASES = {"新線新宿": "新宿"}


PLATFORM_RE = re.compile(r"(\d+\s*(番|号)(線|のりば|ホーム)?|のりば|方面|ホーム)")


def normalize_ja(name):
    """Nombre japonés para mostrar: sin sufijos entre paréntesis/〈〉, sin «駅» ni texto de andén.
    Devuelve "" si el nombre es solo un andén («鞍馬方面のりば»): la parada se asigna luego a la estación más cercana."""
    name = re.sub(r"[（(〈<].*?[)）〉>]", "", name).strip()
    m = re.match(r"^(.+?)駅(?!前)(.+)$", name)          # «宝ヶ池駅2番線» → «宝ヶ池» (pero no «大塚駅前»)
    if m and PLATFORM_RE.search(m.group(2)):
        name = m.group(1)
    elif PLATFORM_RE.search(name) and "駅" not in name:
        return ""
    name = name.removesuffix("駅")
    return JA_ALIASES.get(name, name)


def ja_key(name):
    """Clave para agrupar: unifica variantes de kana pequeñas (市ヶ谷 = 市ケ谷)."""
    return name.translate(str.maketrans({"ヶ": "ケ", "ヵ": "カ"})) if name else name


def normalize_code(ref, line_code):
    """Código de numeración (JY17, G09, Mb03…) solo si pertenece a esta línea.
    OSM a veces pone el código de la compañía con la que hay servicio directo (p. ej. DT01 en Shibuya)."""
    for part in (ref or "").split(";"):
        part = part.strip().replace(" ", "").removeprefix("JR-").replace("-", "")
        m = re.fullmatch(r"([A-Za-z]{1,2})(\d{1,2})", part)
        if not m:
            continue
        prefix = m.group(1)
        if prefix.upper() == line_code or (prefix[0] == line_code and prefix[1:].islower()):
            return f"{prefix[0].upper()}{prefix[1:]}{int(m.group(2)):02d}"
    return None


def fill_codes(order, line_id, line_code, extrapolate=True):
    """Rellena códigos que faltan cuando los vecinos permiten deducirlos (numeración correlativa)."""
    def num(c):
        code = c["lines"].get(line_id)
        m = code and re.fullmatch(r"([A-Za-z]+)(\d+)", code)
        return (m.group(1), int(m.group(2))) if m and m.group(1) == line_code else None

    known = [(i, num(c)) for i, c in enumerate(order) if num(c)]
    filled = 0
    for (i, (_, a)), (j, (_, b)) in zip(known, known[1:]):
        if j - i > 1 and abs(b - a) == j - i:
            step = 1 if b > a else -1
            for k in range(i + 1, j):
                order[k]["lines"][line_id] = f"{line_code}{a + step * (k - i):02d}"
                filled += 1
    # extremos: se extrapola si los dos códigos conocidos más cercanos son coherentes entre sí
    if len(known) > 1 and extrapolate:
        for (i, (_, x)), (j, (_, y)), ks in ((known[0], known[1], range(known[0][0] - 1, -1, -1)),
                                             (known[-1], known[-2], range(known[-1][0] + 1, len(order)))):
            if abs(x - y) != abs(i - j):
                continue
            step = 1 if (x - y) * (i - j) > 0 else -1  # la numeración crece o decrece con el orden
            for k in ks:
                n = x + step * (k - i)
                if n < 1 or order[k]["lines"].get(line_id):
                    break
                order[k]["lines"][line_id] = f"{line_code}{n:02d}"
                filled += 1
    return filled


# ---------------------------------------------------------------- Overpass
def overpass(query):
    """Consulta Overpass. Ante un 429 (límite de peticiones) espera y reintenta en el servidor principal;
    ante otros fallos prueba los espejos."""
    last = None
    ep_i = 0
    for attempt in range(10):
        ep = ENDPOINTS[ep_i % len(ENDPOINTS)]
        try:
            req = urllib.request.Request(
                ep, data=urllib.parse.urlencode({"data": query}).encode(),
                headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                wait = 30
            else:
                ep_i += 1
                wait = 10
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            ep_i += 1
            wait = 10
        log(f"    {ep.split('/')[2]}: {last} — reintento en {wait}s")
        time.sleep(wait)
    raise RuntimeError(f"Overpass no responde: {last}")


def fetch_relation(rel_id, refresh):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"relation-{rel_id}.json"
    if path.exists() and not refresh:
        return load_json(path)
    log(f"  descargando relación {rel_id}…")
    # las relaciones de línea (no de servicio) a veces no llevan paradas como miembros:
    # pedimos también las estaciones que están sobre sus vías, como respaldo
    full = (f"[out:json][timeout:240];relation({rel_id})->.r;.r out geom;node(r.r);out;way(r.r)->.w;"
            '(node(around.w:60)["railway"~"^(station|halt|stop)$"];'
            ' node(around.w:60)["public_transport"="stop_position"];);out;')
    simple = f"[out:json][timeout:240];relation({rel_id})->.r;.r out geom;node(r.r);out;"
    data = {}
    for q in (full, simple):  # buscar estaciones alrededor de la vía es caro: si no sale, vamos a lo básico
        try:
            data = overpass(q)
        except RuntimeError as e:
            log(f"    consulta completa fallida ({e}); pruebo la sencilla")
            continue
        if any(e["type"] == "relation" for e in data.get("elements", [])):
            break
    if not any(e["type"] == "relation" for e in data.get("elements", [])):
        raise RuntimeError(f"La relación {rel_id} no existe o vino vacía")
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    time.sleep(5)  # cortesía con el servidor público
    return data


def fetch_ways(line, refresh):
    """Líneas sin relación route en OSM: trazado = vías que cumplen el filtro; paradas = stop_position sobre ellas."""
    import hashlib
    q = line["osm_ways"]
    bbox = ",".join(str(x) for x in q["bbox"])
    query = (f'[out:json][timeout:180];{q["filter"]}({bbox})->.w;.w out geom;'
             'node(w.w)["name"]->.n;.n out;')
    if q.get("nearby"):  # estaciones mapeadas junto a la vía y no sobre ella (radio en metros, 80 por defecto)
        r = 80 if q["nearby"] is True else int(q["nearby"])
        query += (f'(node(around.w:{r})["railway"~"^(station|halt|stop|tram_stop)$"];'
                  f' node(around.w:{r})["public_transport"~"^(stop_position|station)$"];);out;')
    key = hashlib.sha1(query.encode()).hexdigest()[:12]
    path = CACHE / f"ways-{line['id']}-{key}.json"
    CACHE.mkdir(parents=True, exist_ok=True)
    if path.exists() and not refresh:
        return load_json(path)
    log(f"  descargando vías de {line['id']}…")
    data = overpass(query)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    time.sleep(5)
    return data


def fetch_nodes(ids, refresh):
    ids = sorted(ids)
    path = CACHE / f"nodes-{'-'.join(map(str, ids))[:120]}.json"
    if path.exists() and not refresh:
        return load_json(path)
    log(f"  descargando nodos {ids}…")
    data = overpass(f"[out:json];node(id:{','.join(map(str, ids))});out;")
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


def parse_ways(data, trams=False):
    segments, stops = [], []
    for e in data["elements"]:
        if e["type"] == "way" and "geometry" in e:
            if e.get("tags", {}).get("service"):  # apartaderos, cocheras, desvíos
                continue
            segments.append([(round(p["lat"], 7), round(p["lon"], 7)) for p in e["geometry"] if p])
        elif e["type"] == "node":
            t = e.get("tags", {})
            kinds = ("stop", "halt", "station") + (("tram_stop",) if trams else ())
            # exigimos etiqueta ferroviaria: si no, entran las paradas de autobús, que en Japón
            # también son «public_transport=stop_position» y están pegadas a la vía en las estaciones
            ferroviario = t.get("railway") in kinds or any(
                t.get(k) == "yes" for k in ("train", "subway", "monorail", "light_rail", "funicular"))
            if ferroviario:
                stops.append(e)
    return segments, stops


# ---------------------------------------------------------------- geometría
def merge_chains(segments):
    """Une tramos de vía que comparten extremos en cadenas lo más largas posible.
    Recorre un índice de extremos, así que escala bien con relaciones de miles de tramos."""
    segs = [list(sg) for sg in segments if len(sg) >= 2]
    ends = {}
    for i, sg in enumerate(segs):
        ends.setdefault(sg[0], []).append(i)
        ends.setdefault(sg[-1], []).append(i)
    used = [False] * len(segs)

    def take(point):
        for j in ends.get(point, []):
            if not used[j]:
                used[j] = True
                sg = segs[j]
                return sg if sg[0] == point else sg[::-1]
        return None

    chains = []
    # empezar por extremos "sueltos" (grado impar) da cadenas más largas
    order = sorted(range(len(segs)), key=lambda i: min(len(ends[segs[i][0]]), len(ends[segs[i][-1]])))
    for i in order:
        if used[i]:
            continue
        used[i] = True
        chain = list(segs[i])
        while (nxt := take(chain[-1])) is not None:
            chain += nxt[1:]
        while (prv := take(chain[0])) is not None:
            chain = prv[::-1] + chain[1:]
        chains.append(chain)
    return chains


def simplify(points, tol):
    """Ramer–Douglas–Peucker iterativo."""
    if len(points) < 3:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        s, e = stack.pop()
        (y1, x1), (y2, x2) = points[s], points[e]
        dx, dy = x2 - x1, y2 - y1
        norm = math.hypot(dx, dy)
        best, idx = 0.0, None
        for k in range(s + 1, e):
            y0, x0 = points[k]
            if norm == 0:  # tramo cerrado (líneas circulares): distancia al punto
                d = math.hypot(x0 - x1, y0 - y1)
            else:
                d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / norm
            if d > best:
                best, idx = d, k
        if idx is not None and best > tol:
            keep[idx] = True
            stack += [(s, idx), (idx, e)]
    return [p for p, k in zip(points, keep) if k]


def chain_length_km(chain):
    return sum(haversine_m(chain[i], chain[i + 1]) for i in range(len(chain) - 1)) / 1000


# ---------------------------------------------------------------- proceso
def parse_relation(data):
    rel = next(e for e in data["elements"] if e["type"] == "relation")
    nodes = {e["id"]: e for e in data["elements"] if e["type"] == "node"}
    segments, stops = [], []
    for m in rel["members"]:
        if m["type"] == "way" and m.get("role", "") not in PLATFORM_ROLES and "geometry" in m:
            segments.append([(round(p["lat"], 7), round(p["lon"], 7)) for p in m["geometry"] if p])
        elif m["type"] == "node" and m.get("role", "").startswith("stop"):
            n = nodes.get(m["ref"])
            if n:
                stops.append(n)
    if not stops:  # relación sólo de trazado: las paradas son las estaciones que hay junto a sus vías
        for n in nodes.values():
            t = n.get("tags", {})
            name = t.get("name", "")
            if not name or "信号場" in name:  # los apartaderos no son paradas
                continue
            if t.get("railway") in ("station", "halt", "stop") or (
                    t.get("public_transport") == "stop_position" and t.get("train") == "yes"):
                stops.append(n)
    return rel, segments, stops


def nearest_vertex(chain, pt):
    best = min(range(len(chain)), key=lambda i: (chain[i][0] - pt[0]) ** 2 + ((chain[i][1] - pt[1]) * 0.81) ** 2)
    return best, haversine_m(chain[best], pt)


def cut_section(line, stops, chains, warnings, max_gap_m=3000):
    """Recorta paradas y trazado al tramo line['section'] = [desde, hasta] (nombres japoneses)."""
    a_ja, b_ja = line["section"]
    idx = {ja_key(s["ja"]): i for i, s in enumerate(stops)}
    if ja_key(a_ja) not in idx or ja_key(b_ja) not in idx:
        warnings.append(f"{line['id']}: el tramo {a_ja}–{b_ja} no está en las paradas de la relación")
        return stops, chains
    ia, ib = idx[ja_key(a_ja)], idx[ja_key(b_ja)]
    a_pt, b_pt = stops[ia]["pt"], stops[ib]["pt"]
    # con varias relaciones (order=geometry) el orden aún no es fiable: se filtra después por posición
    if line.get("order") != "geometry":
        stops = stops[ia:ib + 1] if ia <= ib else stops[ib:ia + 1][::-1]
    out = []
    for ch in chains:
        (i, da), (j, db) = nearest_vertex(ch, a_pt), nearest_vertex(ch, b_pt)
        if da < max_gap_m and db < max_gap_m and i != j:
            out.append(ch[i:j + 1] if i < j else ch[j:i + 1][::-1])
    if not out:
        warnings.append(f"{line['id']}: no se pudo recortar el trazado a {a_ja}–{b_ja}; se deja completo")
        return stops, chains
    return stops, out


def stitch(chains):
    """Encadena tramos sueltos por sus extremos más cercanos en un único recorrido
    (solo para medir posiciones; el dibujo usa los tramos originales)."""
    rest = sorted(chains, key=chain_length_km, reverse=True)
    path = list(rest.pop(0))
    while rest:
        best = None
        for k, ch in enumerate(rest):
            for rev in (False, True):
                c = ch[::-1] if rev else ch
                for at_end in (True, False):
                    d = haversine_m(path[-1], c[0]) if at_end else haversine_m(c[-1], path[0])
                    if best is None or d < best[0]:
                        best = (d, k, c, at_end)
        _, k, c, at_end = best
        rest.pop(k)
        path = path + c if at_end else c + path
    return path


def order_along(stops, chains, max_off_m=1500):
    """Ordena paradas por su posición a lo largo del tramo más largo; descarta las que quedan fuera."""
    main = stitch(chains)
    cum = [0.0]
    for k in range(1, len(main)):
        cum.append(cum[-1] + haversine_m(main[k - 1], main[k]))
    placed = []
    for s in stops:
        i, d = nearest_vertex(main, s["pt"])
        if d > max_off_m or (i == 0 and d > 800) or (i == len(main) - 1 and d > 800):
            continue  # fuera del tramo
        placed.append((cum[i], s))
    return [s for _, s in sorted(placed, key=lambda x: x[0])]


def order_nearest(stops):
    """Ordena las paradas encadenando la más cercana desde un extremo de la línea.
    Va mejor que seguir el trazado cuando la vía viene partida en muchos tramos sueltos."""
    if len(stops) < 3:
        return stops
    pts = [s["pt"] for s in stops]
    c = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
    far = max(range(len(pts)), key=lambda i: haversine_m(pts[i], c))
    start = max(range(len(pts)), key=lambda i: haversine_m(pts[i], pts[far]))   # el extremo opuesto
    order, used = [start], {start}
    while len(order) < len(pts):
        last = pts[order[-1]]
        nxt = min((i for i in range(len(pts)) if i not in used), key=lambda i: haversine_m(pts[i], last))
        order.append(nxt)
        used.add(nxt)
    return [stops[i] for i in order]


def resolve_trains(trains, lines, stations, warnings):
    """Calcula por qué líneas y estaciones pasa cada tren.
    Fuentes: 'runs' en trains.json ([{line, from?, to?}], nombres japoneses) y 'trains' en lines.json (línea entera)."""
    by_id = {l["id"]: l for l in lines}
    ja_to_idx = {l["id"]: {ja_key(stations[sid]["ja"]): i for i, sid in enumerate(l["stations"])} for l in lines}
    def resolve(t, r):
        """Devuelve (tramo resuelto, ids de estaciones) o None si la línea no existe."""
        line = by_id.get(r["line"])
        if not line:
            warnings.append(f"trains.json: {t['id']} usa la línea desconocida '{r['line']}'")
            return None
        idx = ja_to_idx[line["id"]]
        for k in ("from", "to"):
            if k in r and ja_key(r[k]) not in idx:
                warnings.append(f"trains.json: {t['id']}: «{r[k]}» no está en {line['id']}")
        a = idx.get(ja_key(r.get("from")), 0)
        b = idx.get(ja_key(r.get("to")), len(line["stations"]) - 1)
        lo, hi = min(a, b), max(a, b)
        item = {"line": line["id"]}
        if lo > 0 or hi < len(line["stations"]) - 1:
            item.update({"from": line["stations"][lo], "to": line["stations"][hi]})
        if "years" in r:
            item["years"] = r["years"]
        return item, line["stations"][lo:hi + 1]

    for t in trains:
        # historia: por dónde circuló y cuándo ([{line, years: [desde, hasta], from?, to?}])
        past, past_served = [], []
        for r in t.get("history", []):
            if (res := resolve(t, r)):
                past.append(res[0])
                past_served += [x for x in res[1] if x not in past_served]
        t["history"] = sorted(past, key=lambda h: h["years"][0] or t.get("introduced", 0))
        for sid in past_served:
            stations[sid].setdefault("past_trains", []).append(t["id"])

        runs = list(t.get("runs", []))
        runs += [{"line": l["id"]} for l in lines if t["id"] in l.get("trains", []) and
                 not any(r["line"] == l["id"] for r in runs)]
        resolved, served = [], []
        for r in runs:
            if (res := resolve(t, r)):
                resolved.append(res[0])
                served += [x for x in res[1] if x not in served]
        t["runs"] = resolved
        t["lines"] = [r["line"] for r in resolved]
        for sid in served:
            stations[sid].setdefault("trains", []).append(t["id"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="ignora la caché y descarga de nuevo")
    args = ap.parse_args()

    cfg = load_json(CONFIG / "lines.json")
    station_extra = {k: v for k, v in load_json(CONFIG / "stations.json").items() if not k.startswith("_")}
    trains = load_json(CONFIG / "trains.json")
    overrides = load_json(CONFIG / "overrides.json")
    names_en = overrides.get("station_names_en", {})
    code_fixes = overrides.get("station_codes", {})
    stop_names = overrides.get("stop_nodes", {})  # nodo OSM → nombre japonés (paradas sin nombre)
    JA_ALIASES.update(overrides.get("ja_aliases", {}))
    train_ids = {t["id"] for t in trains}

    clusters = []          # estaciones agrupadas: {ja, pts, en: Counter, lines: OrderedDict}
    out_lines = []
    warnings = []

    for line in cfg["lines"]:
        log(f"· {line['id']}")
        chains_raw, stops = [], []
        seen = set()
        # 'osm': relaciones que aportan trazado y paradas (la 1.ª fija el orden; las demás, p. ej. ramales, añaden)
        # 'extra_stops': relaciones de otros servicios de las que solo se toman paradas que falten
        sources = [(r, True) for r in line["osm"]] + [(r, False) for r in line.get("extra_stops", [])]
        if "osm_ways" in line:  # stops_only: el trazado sale de la relación y de las vías solo las paradas
            sources.append(("ways", not line["osm_ways"].get("stops_only")))
        if "extra_nodes" in line:  # paradas sueltas por id de nodo OSM (p. ej. un terminal que está en otra línea)
            sources.append(("nodes", False))
        for rel_id, use_geometry in sources:
            if rel_id == "ways":
                segs, rel_stops = parse_ways(fetch_ways(line, args.refresh), line["osm_ways"].get("nearby"))
            elif rel_id == "nodes":
                segs, rel_stops = [], fetch_nodes(line["extra_nodes"], args.refresh)["elements"]
            else:
                rel, segs, rel_stops = parse_relation(fetch_relation(rel_id, args.refresh))
            if use_geometry:
                chains_raw += segs
            for s in rel_stops:
                t = s.get("tags", {})
                ja = stop_names.get(str(s["id"])) or normalize_ja(t.get("name", ""))
                if not ja:
                    near = min(clusters, key=lambda c: haversine_m(c["pts"][0], (s["lat"], s["lon"])), default=None)
                    if near and haversine_m(near["pts"][0], (s["lat"], s["lon"])) < 400:
                        ja = near["ja"]  # andén sin nombre de estación: se une a la estación de al lado
                    else:
                        warnings.append(f"{line['id']}: parada sin nombre utilizable «{t.get('name', '')}» (nodo {s['id']})")
                        continue
                if ja_key(ja) in seen:
                    continue
                seen.add(ja_key(ja))
                en = strip_accents(t.get("name:en") or t.get("name:ja-Latn") or t.get("name:ja_rm") or "")
                en = re.sub(r"\s*[(\"'〈<].*?[)\"'〉>]\s*", " ", en).removesuffix(" Station").strip()
                en = names_en.get(ja, en)  # la corrección manual se respeta tal cual
                stops.append({"ja": ja, "en": en, "pt": (s["lat"], s["lon"]),
                              "code": normalize_code(t.get("ref"), line["code"])})

        if line.get("skip_stations"):  # paradas que la caja de vías arrastra de más (líneas que siguen más allá)
            skip = {ja_key(n) for n in line["skip_stations"]}
            stops = [st for st in stops if ja_key(st["ja"]) not in skip]

        for st in stops:  # las correcciones de código se aplican ya, para que order=code las tenga en cuenta
            st["code"] = code_fixes.get(line["id"], {}).get(st["ja"], st["code"])
        chains = merge_chains(chains_raw)
        if "section" in line:
            stops, chains = cut_section(line, stops, chains, warnings)
        if line.get("order") == "geometry":
            stops = order_along(stops, chains)
        elif line.get("order") == "nearest":
            stops = order_nearest(stops)
        elif line.get("station_order"):  # orden explícito (nombres japoneses) para relaciones caóticas
            pos = {ja_key(n): i for i, n in enumerate(line["station_order"])}
            if line.get("strict_order"):  # sólo las de la lista: descarta lo que arrastran las vías vecinas
                stops = [st for st in stops if ja_key(st["ja"]) in pos]
            stops.sort(key=lambda st: pos.get(ja_key(st["ja"]), len(pos)))
        elif line.get("order") == "code":  # todas las paradas numeradas: el código manda (vías dobles, cuádruples…)
            stops.sort(key=lambda st: int(re.sub(r"\D", "", st["code"] or "999")))

        order = []
        for st in stops:
            cl = next((c for c in clusters if c["key"] == ja_key(st["ja"]) and
                       haversine_m(c["pts"][0], st["pt"]) < MERGE_SAME_NAME_M), None)
            if cl is None:
                cl = {"key": ja_key(st["ja"]), "ja": st["ja"], "pts": [], "en": Counter(), "lines": OrderedDict()}
                clusters.append(cl)
            cl["pts"].append(st["pt"])
            if st["en"]:
                cl["en"][st["en"]] += 1
            cl["lines"][line["id"]] = st["code"]
            order.append(cl)

        for c in order:
            fix = code_fixes.get(line["id"], {}).get(c["ja"])
            if fix:
                c["lines"][line["id"]] = fix
        if (n := fill_codes(order, line["id"], line["code"], not line.get("no_extrapolate"))):
            log(f"    {n} códigos de estación deducidos por numeración correlativa")
        codes = [c["lines"].get(line["id"]) for c in order if c["lines"].get(line["id"])]
        if dup := sorted({x for x in codes if codes.count(x) > 1}):
            warnings.append(f"{line['id']}: códigos repetidos {dup} (revisa OSM u overrides.json)")
        missing = sum(1 for c in order if not c["lines"].get(line["id"]))
        if missing and codes:  # líneas sin numeración (p. ej. Shinkansen) no avisan
            warnings.append(f"{line['id']}: {missing} estaciones sin código de numeración")
        drawn_km = sum(chain_length_km(c) for c in chains)
        chains = [[[round(la, 5), round(lo, 5)] for la, lo in simplify(c, SIMPLIFY_DEG)] for c in chains]
        for tid in line.get("trains", []):
            if tid not in train_ids:
                warnings.append(f"{line['id']}: tren desconocido '{tid}'")
        out_lines.append({**{k: v for k, v in line.items() if k not in ("osm", "section", "order", "extra_stops", "osm_ways", "extra_nodes", "no_extrapolate", "station_order", "skip_stations", "strict_order")},
                          "osm": line["osm"],
                          "stations": order,   # se sustituye por ids más abajo
                          "drawn_km": round(drawn_km, 1),
                          "geometry": chains})
        log(f"    {len(order)} estaciones · {len(chains)} tramos · {drawn_km:.1f} km dibujados")

    # ids estables (se asignan en el orden de lines.json, así Tokio conserva los suyos)
    region_of = {l["id"]: l.get("region", "japan") for l in cfg["lines"]}
    areas = [(p["id"], p["bounds"]) for p in cfg.get("places", [])] + \
            [(r, v["bounds"]) for r, v in cfg.get("regions", {}).items() if v.get("bounds")]

    MARGIN = 0.25  # las cajas de places/regions encuadran el centro urbano: aquí interesa el área metropolitana

    def place_of(pos):
        """Ciudad (de places/regions) que contiene esa posición, para desempatar nombres repetidos."""
        hits = [(haversine_m(pos, ((s_ + n_) / 2, (w + e) / 2)), pid)
                for pid, ((s_, w), (n_, e)) in areas
                if s_ - MARGIN <= pos[0] <= n_ + MARGIN and w - MARGIN <= pos[1] <= e + MARGIN]
        return min(hits)[1] if hits else None  # la ciudad más cercana: Kōbe y Ōsaka se solapan
    used = {}
    for c in clusters:
        if not c["en"]:
            warnings.append(f"«{c['ja']}» no tiene nombre en romaji (añádelo en overrides.json)")
        en = c["en"].most_common(1)[0][0] if c["en"] else c["ja"]
        base = slugify(en) or f"st-{len(used)}"
        c["pos"] = (sum(p[0] for p in c["pts"]) / len(c["pts"]), sum(p[1] for p in c["pts"]) / len(c["pts"]))
        sid = base
        if sid in used:  # mismo nombre en otra ciudad (p. ej. Ōmiya en Saitama y en Kioto)
            suffix = place_of(c["pos"]) or region_of[next(iter(c["lines"]))]
            sid = base if base == suffix or base.endswith(f"-{suffix}") else f"{base}-{suffix}"
        n = 2
        while sid in used:
            sid = f"{base}-{n}"
            n += 1
        used[sid] = c
        c["id"], c["en_name"] = sid, en

    stations = {}
    for c in clusters:
        extra = station_extra.get(c["id"], {})
        stations[c["id"]] = {
            "id": c["id"], "name": c["en_name"], "ja": c["ja"],
            "lat": round(c["pos"][0], 6), "lon": round(c["pos"][1], 6),
            "lines": [{"line": l, "code": code} for l, code in c["lines"].items()],
            **({"summary": extra["summary"]} if "summary" in extra else {}),
            **({"facts": extra["facts"]} if "facts" in extra else {}),
        }
    for sid, st in stations.items():
        near = []
        for oid, o in stations.items():
            if oid == sid:
                continue
            d = haversine_m((st["lat"], st["lon"]), (o["lat"], o["lon"]))
            if d < NEARBY_M:
                near.append((round(d), oid))
        if near:
            st["nearby"] = [{"station": oid, "m": d} for d, oid in sorted(near)]

    for lid, fixes in code_fixes.items():
        for ja in fixes:
            if not any(c["ja"] == ja and lid in c["lines"] for c in clusters):
                warnings.append(f"overrides.json: «{ja}» no está en la línea {lid}")
    for k in station_extra:
        if k not in stations:
            warnings.append(f"config/stations.json: '{k}' no coincide con ninguna estación")

    for l in out_lines:
        l["stations"] = [c["id"] for c in l["stations"]]
        if not l.get("summary") and l["stations"]:  # resumen automático para las líneas sin texto propio
            a, b = stations[l["stations"][0]]["name"], stations[l["stations"][-1]]["name"]
            l["summary"] = f"Recorrido circular con {len(l['stations'])} paradas, desde {a}." if l.get("loop") else f"De {a} a {b}."

    resolve_trains(trains, out_lines, stations, warnings)
    photos = load_json(CONFIG / "photos.json") if (CONFIG / "photos.json").exists() else {}
    for t in trains:
        for k in ("wiki", "photo_file", "photo_search"):
            t.pop(k, None)
        if t["id"] in photos:
            t["photo"] = photos[t["id"]]

    network = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "region": "Japón",
        "attribution": "Trazados y estaciones © colaboradores de OpenStreetMap (ODbL)",
        "regions": cfg.get("regions", {}),
        "places": cfg.get("places", []),
        "operators": cfg["operators"],
        "types": cfg["types"],
        "lines": out_lines,
        "stations": stations,
        "trains": trains,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(network, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    log(f"\n{len(out_lines)} líneas · {len(stations)} estaciones · "
        f"{OUT.stat().st_size / 1024:.0f} KB → {OUT.relative_to(ROOT)}")
    if warnings:
        log("\nAvisos:")
        for w in warnings:
            log("  - " + w)

    # inventario (INVENTARIO.md) siempre al día con los datos
    sys.path.insert(0, str(Path(__file__).parent))
    import inventory
    inventory.main()


if __name__ == "__main__":
    main()
