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


# Nombres que OSM escribe distinto para la misma estación (clave de agrupación → nombre canónico)
JA_ALIASES = {"新線新宿": "新宿"}


def normalize_ja(name):
    """Nombre japonés para mostrar: sin sufijos entre paréntesis/〈〉 ni «駅»."""
    name = re.sub(r"[（(〈<].*?[)）〉>]", "", name)
    name = name.strip().removesuffix("駅")
    return JA_ALIASES.get(name, name)


def ja_key(name):
    """Clave para agrupar: unifica variantes de kana pequeñas (市ヶ谷 = 市ケ谷)."""
    return name.translate(str.maketrans({"ヶ": "ケ", "ヵ": "カ"})) if name else name


def normalize_code(ref, line_code):
    """Código de numeración (JY17, G09, Mb03…) solo si pertenece a esta línea.
    OSM a veces pone el código de la compañía con la que hay servicio directo (p. ej. DT01 en Shibuya)."""
    for part in (ref or "").split(";"):
        part = part.strip().replace(" ", "").replace("-", "")
        m = re.fullmatch(r"([A-Za-z]{1,2})(\d{1,2})", part)
        if not m:
            continue
        prefix = m.group(1)
        if prefix.upper() == line_code or (prefix[0] == line_code and prefix[1:].islower()):
            return f"{prefix[0].upper()}{prefix[1:]}{int(m.group(2)):02d}"
    return None


def fill_codes(order, line_id, line_code):
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
    if len(known) > 1:
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
    data = overpass(f"[out:json][timeout:120];relation({rel_id});out geom;relation({rel_id});node(r);out;")
    if not any(e["type"] == "relation" for e in data.get("elements", [])):
        raise RuntimeError(f"La relación {rel_id} no existe o vino vacía")
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    time.sleep(5)  # cortesía con el servidor público
    return data


# ---------------------------------------------------------------- geometría
def merge_chains(segments):
    """Une tramos de vía que comparten extremos en cadenas lo más largas posible."""
    chains = [list(s) for s in segments if len(s) >= 2]
    merged = True
    while merged:
        merged = False
        for i in range(len(chains)):
            for j in range(i + 1, len(chains)):
                a, b = chains[i], chains[j]
                if a[-1] == b[0]:
                    chains[i] = a + b[1:]
                elif a[-1] == b[-1]:
                    chains[i] = a + b[-2::-1]
                elif a[0] == b[-1]:
                    chains[i] = b + a[1:]
                elif a[0] == b[0]:
                    chains[i] = b[::-1] + a[1:]
                else:
                    continue
                del chains[j]
                merged = True
                break
            if merged:
                break
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
        norm = math.hypot(dx, dy) or 1e-12
        best, idx = 0.0, None
        for k in range(s + 1, e):
            y0, x0 = points[k]
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
    return rel, segments, stops


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
    train_ids = {t["id"] for t in trains}

    clusters = []          # estaciones agrupadas: {ja, pts, en: Counter, lines: OrderedDict}
    out_lines = []
    warnings = []

    for line in cfg["lines"]:
        log(f"· {line['id']}")
        chains_raw, order = [], []
        for rel_id in line["osm"]:  # la 1.ª fija el orden; las demás (ramales) añaden lo que falte
            rel, segs, stops = parse_relation(fetch_relation(rel_id, args.refresh))
            chains_raw += segs
            for s in stops:
                t = s.get("tags", {})
                ja = normalize_ja(t.get("name", ""))
                if not ja:
                    warnings.append(f"{line['id']}: parada sin nombre (nodo {s['id']})")
                    continue
                en = strip_accents(names_en.get(ja) or t.get("name:en") or t.get("name:ja-Latn") or t.get("name:ja_rm") or "")
                en = re.sub(r"\s*[(\"'〈<].*?[)\"'〉>]\s*", " ", en).removesuffix(" Station").strip()
                pt = (s["lat"], s["lon"])
                code = normalize_code(t.get("ref"), line["code"])
                # buscar cluster existente
                cl = next((c for c in clusters if c["key"] == ja_key(ja) and
                           haversine_m(c["pts"][0], pt) < MERGE_SAME_NAME_M), None)
                if cl is None:
                    cl = {"key": ja_key(ja), "ja": ja, "pts": [], "en": Counter(), "lines": OrderedDict()}
                    clusters.append(cl)
                cl["pts"].append(pt)
                if en:
                    cl["en"][en] += 1
                if line["id"] not in cl["lines"] or (code and not cl["lines"][line["id"]]):
                    cl["lines"][line["id"]] = code
                if not any(o is cl for o in order):
                    order.append(cl)

        for c in order:
            fix = code_fixes.get(line["id"], {}).get(c["ja"])
            if fix:
                c["lines"][line["id"]] = fix
        if (n := fill_codes(order, line["id"], line["code"])):
            log(f"    {n} códigos de estación deducidos por numeración correlativa")
        codes = [c["lines"].get(line["id"]) for c in order if c["lines"].get(line["id"])]
        if dup := sorted({x for x in codes if codes.count(x) > 1}):
            warnings.append(f"{line['id']}: códigos repetidos {dup} (revisa OSM u overrides.json)")
        missing = sum(1 for c in order if not c["lines"].get(line["id"]))
        if missing:
            warnings.append(f"{line['id']}: {missing} estaciones sin código de numeración")
        chains = merge_chains(chains_raw)
        drawn_km = sum(chain_length_km(c) for c in chains)
        chains = [[[round(la, 5), round(lo, 5)] for la, lo in simplify(c, SIMPLIFY_DEG)] for c in chains]
        for tid in line.get("trains", []):
            if tid not in train_ids:
                warnings.append(f"{line['id']}: tren desconocido '{tid}'")
        out_lines.append({**{k: v for k, v in line.items() if k != "osm"},
                          "osm": line["osm"],
                          "stations": order,   # se sustituye por ids más abajo
                          "drawn_km": round(drawn_km, 1),
                          "geometry": chains})
        log(f"    {len(order)} estaciones · {len(chains)} tramos · {drawn_km:.1f} km dibujados")

    # ids estables
    used = {}
    for c in clusters:
        if not c["en"]:
            warnings.append(f"«{c['ja']}» no tiene nombre en romaji (añádelo en overrides.json)")
        en = c["en"].most_common(1)[0][0] if c["en"] else c["ja"]
        base = slugify(en) or f"st-{len(used)}"
        sid = base
        n = 2
        while sid in used:
            sid = f"{base}-{n}"
            n += 1
        used[sid] = c
        c["id"], c["en_name"] = sid, en
        lat = sum(p[0] for p in c["pts"]) / len(c["pts"])
        lon = sum(p[1] for p in c["pts"]) / len(c["pts"])
        c["pos"] = (lat, lon)

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

    network = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "region": "Tokio",
        "attribution": "Trazados y estaciones © colaboradores de OpenStreetMap (ODbL)",
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


if __name__ == "__main__":
    main()
