#!/usr/bin/env python3
"""Auditoría de cobertura: qué estaciones de Japón faltan, prefectura a prefectura.

Pregunta a OpenStreetMap por todas las estaciones (tren, metro, tranvía, monorraíl) de cada
prefectura y compara con web/data/network.json. Se cuenta por estaciones, no por rutas, porque
en Japón las líneas casi nunca están mapeadas como relaciones: lo que siempre está son las
estaciones, y la mayoría llevan «KSJ2:LIN», el nombre oficial de su línea según el Ministerio
de Territorio, que sirve para agrupar lo que falta.

Uso:
    python3 tools/audit_coverage.py                 # usa la caché (tools/.cache/pref-*.json)
    python3 tools/audit_coverage.py --refresh       # vuelve a descargarlo todo
    python3 tools/audit_coverage.py --only 01 13    # sólo esas prefecturas

Resultado: AUDITORIA.md, tools/.cache/audit.json y un resumen por pantalla.
"""
import argparse
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_data import CACHE, CONFIG, JA_ALIASES, OUT as NETWORK, ROOT, haversine_m, ja_key, load_json, normalize_ja, overpass  # noqa: E402

# las 47 prefecturas, en el orden oficial (el código es el de ISO 3166-2:JP)
PREFECTURES = [
    ("01", "Hokkaidō"), ("02", "Aomori"), ("03", "Iwate"), ("04", "Miyagi"), ("05", "Akita"),
    ("06", "Yamagata"), ("07", "Fukushima"), ("08", "Ibaraki"), ("09", "Tochigi"), ("10", "Gunma"),
    ("11", "Saitama"), ("12", "Chiba"), ("13", "Tokio"), ("14", "Kanagawa"), ("15", "Niigata"),
    ("16", "Toyama"), ("17", "Ishikawa"), ("18", "Fukui"), ("19", "Yamanashi"), ("20", "Nagano"),
    ("21", "Gifu"), ("22", "Shizuoka"), ("23", "Aichi"), ("24", "Mie"), ("25", "Shiga"),
    ("26", "Kioto"), ("27", "Ōsaka"), ("28", "Hyōgo"), ("29", "Nara"), ("30", "Wakayama"),
    ("31", "Tottori"), ("32", "Shimane"), ("33", "Okayama"), ("34", "Hiroshima"), ("35", "Yamaguchi"),
    ("36", "Tokushima"), ("37", "Kagawa"), ("38", "Ehime"), ("39", "Kōchi"), ("40", "Fukuoka"),
    ("41", "Saga"), ("42", "Nagasaki"), ("43", "Kumamoto"), ("44", "Ōita"), ("45", "Miyazaki"),
    ("46", "Kagoshima"), ("47", "Okinawa"),
]
STATION_Q = '["railway"~"^(station|halt|tram_stop)$"]'
CLOSED_RE = re.compile(r"(廃止|廃駅|跡)")


AREAS = CACHE / "pref-areas.json"


def area_ids():
    """Identificador de área OSM de cada prefectura; se resuelve una vez y se guarda en caché,
    porque buscarla por su código ISO en cada consulta hace que Overpass agote el tiempo."""
    if AREAS.exists():
        return load_json(AREAS)
    d = overpass('[out:json][timeout:200];relation["ISO3166-2"~"^JP-"]["admin_level"="4"];out tags;')
    ids = {e["tags"]["ISO3166-2"][3:]: 3600000000 + e["id"] for e in d["elements"] if e["tags"].get("ISO3166-2")}
    AREAS.write_text(json.dumps(ids, indent=1), encoding="utf-8")
    return ids


def fetch_prefecture(code, refresh):
    """Todas las estaciones de una prefectura, por su área administrativa en OSM."""
    path = CACHE / f"pref-{code}.json"
    if path.exists() and not refresh:
        return load_json(path)
    print(f"descargando prefectura {code}…", file=sys.stderr)
    q = f'[out:json][timeout:600];area({area_ids()[code]});node(area){STATION_Q};out tags center;'
    data = overpass(q)
    if not data.get("elements"):  # Overpass devuelve vacío cuando falla: no es una prefectura sin trenes
        raise RuntimeError(f"la prefectura {code} vino vacía; vuelve a intentarlo (--only {code} --refresh)")
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    time.sleep(3)  # cortesía con el servidor público
    return data


def line_of(tags):
    """Nombre de la línea de una estación: el oficial del Ministerio, o el operador, o nada."""
    name = tags.get("KSJ2:LIN") or ""
    if not name:
        op = tags.get("operator") or tags.get("network") or ""
        name = f"(sin línea) {op}".strip()
    return name or "(sin línea)"


def label_gaps(by_line, max_km=20):
    """Las estaciones sin «KSJ2:LIN» heredan la línea de la estación etiquetada más cercana."""
    known = [(s, line) for line, sts in by_line.items() if not line.startswith("(sin línea)") for s in sts]
    if not known:
        return
    for line in [k for k in by_line if k == "(sin línea)"]:  # las que sí traen operador se quedan juntas
        rest = []
        for st in by_line[line]:
            near = min(known, key=lambda k: haversine_m((st["lat"], st["lon"]), (k[0]["lat"], k[0]["lon"])))
            d = haversine_m((st["lat"], st["lon"]), (near[0]["lat"], near[0]["lon"]))
            if d < max_km * 1000:
                by_line[near[1]].append(st)
            else:
                rest.append(st)
        if rest:
            by_line[line] = rest
        else:
            del by_line[line]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--only", nargs="*", default=None, help="códigos de prefectura (01, 13, 27…)")
    args = ap.parse_args()

    JA_ALIASES.update(load_json(CONFIG / "overrides.json").get("ja_aliases", {}))
    net = load_json(NETWORK)
    ours = defaultdict(list)
    for s in net["stations"].values():
        ours[ja_key(s["ja"])].append((s["lat"], s["lon"]))

    def covered(ja, pt):
        return any(haversine_m(pt, p) < 1200 for p in ours.get(ja_key(ja), []))

    prefs = [(c, n) for c, n in PREFECTURES if not args.only or c in args.only]
    report, summary = {}, []
    for code, name in prefs:
        try:
            data = fetch_prefecture(code, args.refresh)
        except RuntimeError as e:  # se deja fuera del informe: sin datos no se puede decir que esté completa
            print(f"[{code}] {name}: {e}", file=sys.stderr)
            continue
        seen, missing_by_line, total = set(), defaultdict(list), 0
        for e in data["elements"]:
            t = e.get("tags", {})
            ja = normalize_ja(t.get("name", ""))
            if not ja or CLOSED_RE.search(t.get("name", "")) or t.get("disused") or t.get("abandoned"):
                continue
            key = (ja_key(ja), round(e["lat"], 3), round(e["lon"], 3))
            if key in seen:  # andenes y paradas duplicadas de la misma estación
                continue
            seen.add(key)
            total += 1
            if not covered(ja, (e["lat"], e["lon"])):
                missing_by_line[line_of(t)].append({"ja": ja, "en": t.get("name:en", ""),
                                                    "lat": round(e["lat"], 5), "lon": round(e["lon"], 5)})
        label_gaps(missing_by_line)
        missing = sum(len(v) for v in missing_by_line.values())
        report[code] = {"name": name, "total": total, "missing": missing,
                        "lines": {k: v for k, v in sorted(missing_by_line.items(), key=lambda kv: -len(kv[1]))}}
        summary.append((code, name, total, missing))
        print(f"[{code}] {name:12} {total - missing:4}/{total:<4} estaciones "
              f"({round(100 * (total - missing) / total) if total else 100} %)"
              + (f" · faltan {missing} en {len(missing_by_line)} líneas" if missing else " ✅"))

    old = load_json(CACHE / "audit.json") if (CACHE / "audit.json").exists() and args.only else {}
    if not isinstance(old, dict):  # formato antiguo (lista por zonas)
        old = {}
    old.update(report)
    (CACHE / "audit.json").write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding="utf-8")
    write_report(old)
    tot = sum(r["total"] for r in old.values())
    miss = sum(r["missing"] for r in old.values())
    print(f"\nJapón: {tot - miss} de {tot} estaciones ({round(100 * (tot - miss) / tot) if tot else 0} %)",
          file=sys.stderr)


def write_report(report):
    """AUDITORIA.md: cobertura por prefectura y, dentro, qué líneas faltan."""
    from datetime import date
    r = ["# Auditoría de cobertura\n",
         f"> Generado por `tools/audit_coverage.py` el {date.today():%Y-%m-%d}. Compara todas las estaciones "
         "de OpenStreetMap de cada prefectura con las de la web. Las líneas que faltan se agrupan por su nombre "
         "oficial (etiqueta `KSJ2:LIN`, del Ministerio de Territorio).\n"]
    tot = sum(x["total"] for x in report.values())
    miss = sum(x["missing"] for x in report.values())
    r.append(f"**Japón: {tot - miss} de {tot} estaciones ({round(100 * (tot - miss) / tot) if tot else 0} %).**\n")
    r.append("| Prefectura | Estaciones | Tenemos | Faltan | Cobertura |")
    r.append("|---|--:|--:|--:|--:|")
    for code, x in sorted(report.items()):
        pct = round(100 * (x["total"] - x["missing"]) / x["total"]) if x["total"] else 100
        r.append(f"| [{x['name']}](#{code}-{x['name'].lower()}) | {x['total']} | {x['total'] - x['missing']} "
                 f"| {x['missing']} | {pct} % |")
    r.append("")
    for code, x in sorted(report.items()):
        r.append(f"## {code} {x['name']}\n")
        if not x["missing"]:
            r.append("Completa ✅\n")
            continue
        r.append("| Línea | Faltan | Estaciones |")
        r.append("|---|--:|---|")
        for line, sts in x["lines"].items():
            names = "、".join(s["ja"] for s in sts[:12]) + ("…" if len(sts) > 12 else "")
            r.append(f"| {line} | {len(sts)} | {names} |")
        r.append("")
    (ROOT / "AUDITORIA.md").write_text("\n".join(r) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
