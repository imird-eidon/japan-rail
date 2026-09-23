#!/usr/bin/env python3
"""Auditoría de cobertura: qué líneas y estaciones de OSM faltan en nuestras regiones.

Descarga todas las rutas ferroviarias (tren, metro, tranvía, monorraíl) de cada zona con sus paradas,
comprueba qué paradas no están en web/data/network.json y agrupa lo que falta por línea.

Uso:
    python3 tools/audit_coverage.py            # usa la caché (tools/.cache/audit-*.json)
    python3 tools/audit_coverage.py --refresh  # vuelve a descargar

Resultado: AUDITORIA.md (informe legible), tools/.cache/audit.json y un resumen por pantalla.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_data import CACHE, CONFIG, JA_ALIASES, OUT as NETWORK, ROOT, haversine_m, ja_key, load_json, normalize_ja, overpass  # noqa: E402

ZONES = {
    "tokyo": (35.25, 139.10, 36.15, 140.40),
    "kansai": (34.45, 135.05, 35.15, 136.05),
    "nagoya": (34.85, 136.60, 35.40, 137.25),
    "fukuoka": (33.45, 130.25, 33.75, 130.60),
    "sapporo": (42.95, 141.20, 43.15, 141.55),
    "sendai": (38.15, 140.75, 38.35, 141.10),
    "hiroshima": (34.28, 132.25, 34.52, 132.60),
    # ciudades con tranvía
    "nagasaki": (32.70, 129.83, 32.80, 129.92),
    "kumamoto": (32.77, 130.66, 32.83, 130.78),
    "kagoshima": (31.53, 130.51, 31.62, 130.58),
    "hakodate": (41.75, 140.70, 41.81, 140.80),
    "okayama": (34.64, 133.89, 34.69, 133.95),
    "kochi": (33.52, 133.40, 33.60, 133.68),
    "toyama": (36.68, 137.18, 36.78, 137.25),
    "matsuyama": (33.82, 132.74, 33.86, 132.80),
    "toyohashi": (34.72, 137.37, 34.78, 137.42),
    "fukui": (35.95, 136.15, 36.10, 136.25),
}
# servicios que no son líneas (expresos, trenes directos, turísticos de temporada…)
SERVICE_RE = re.compile(r"特急|急行|快速|ライナー|直通|臨時|区間|準急|通勤|新幹線|のぞみ|ひかり|こだま|はやぶさ|やまびこ|"
                        r"とき|かがやき|はくたか|あさま|つばさ|こまち|なすの|たにがわ|さくら|みずほ|つばめ|かもめ|"
                        r"成田エクスプレス|踊り子|あずさ|かいじ|ひたち|ときわ|はるか|サンダーバード|くろしお|"
                        r"寝台|サンライズ|SL|ロマンスカー|スカイライナー|ラピート|ひのとり|しまかぜ|あをによし|"
                        r"こうのとり|はまかぜ|まいづる|きのさき|はしだて|しおさい|さざなみ|わかしお|ふじさん|はこね|"
                        r"ちちぶ|むさし|日光|きぬがわ|リバティ|スペーシア|けごん|アクセス|列車|エクスプレス|"
                        r"宗谷|オホーツク|北斗|おおぞら|とかち|大雪|サロベツ|ライラック|カムイ|すずらん|エアポート|"
                        r"ひだ|しなの|しらさぎ|ソニック|ゆふ|みどり|ハウステンボス|にちりん|きりしま|ひゅうが|"
                        r"ミュースカイ|μSKY|パノラマ|やくも|スーパー")


def base_name(name):
    """«京急本線 普通 (品川 → 浦賀)» → «京急本線»: nombre de la línea sin servicio ni sentido."""
    name = re.sub(r"[（(].*?[)）]", "", name)
    name = re.split(r"[:：]|\s[=-]+>|→", name)[0]
    name = re.sub(r"(各駅停車|普通|上り|下り|内回り|外回り)", "", name)
    return name.strip(" ・")


def fetch_zone(zone, bbox, refresh):
    path = CACHE / f"audit-{zone}.json"
    if path.exists() and not refresh:
        return load_json(path)
    b = ",".join(map(str, bbox))
    q = (f'[out:json][timeout:300];relation["type"="route"]["route"~"^(train|subway|tram|light_rail|monorail)$"]({b})->.r;'
         '.r out body;node(r.r)["name"]->.n;.n out;')
    print(f"descargando {zone}…", file=sys.stderr)
    data = overpass(q)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


ZONE_NAMES = {"tokyo": "Área de Tokio (Tokio, Kanagawa, Saitama, Chiba)", "kansai": "Kansai (Kioto, Ōsaka, Kōbe, Nara, Shiga)",
              "nagoya": "Nagoya", "fukuoka": "Fukuoka", "sapporo": "Sapporo", "sendai": "Sendai", "hiroshima": "Hiroshima",
              "nagasaki": "Nagasaki", "kumamoto": "Kumamoto", "kagoshima": "Kagoshima", "hakodate": "Hakodate",
              "okayama": "Okayama", "kochi": "Kōchi", "toyama": "Toyama", "matsuyama": "Matsuyama",
              "toyohashi": "Toyohashi", "fukui": "Fukui"}


def write_report(out):
    """AUDITORIA.md: lo que OSM tiene en nuestras zonas y nosotros no."""
    from datetime import date
    r = ["# Auditoría de cobertura\n",
         f"> Generado por `tools/audit_coverage.py` el {date.today():%Y-%m-%d}: compara todas las rutas ferroviarias de "
         "OpenStreetMap en cada zona con los datos de la web. Las que interesa añadir se pasan a `config/roadmap.json`.\n"]
    for zone, title in ZONE_NAMES.items():
        items = [o for o in out if o["zone"] == zone]
        r.append(f"## {title}\n")
        for kind, head in (("línea que falta", "Líneas que faltan"), ("estaciones que faltan", "Estaciones que faltan en líneas que ya están")):
            sel = [o for o in items if o["kind"] == kind]
            r.append(f"### {head} ({len(sel)})\n")
            r.append("| Línea (OSM) | Nombre en inglés | Faltan | Ejemplos |")
            r.append("|---|---|--:|---|")
            for o in sel:
                r.append(f"| {o['name']} | {o['en']} | {len(o['missing'])}/{o['total']} | {'、'.join(o['missing'][:5])} |")
            r.append("")
    (ROOT / "AUDITORIA.md").write_text("\n".join(r) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    JA_ALIASES.update(load_json(CONFIG / "overrides.json").get("ja_aliases", {}))
    net = load_json(NETWORK)
    ours = [(ja_key(s["ja"]), (s["lat"], s["lon"])) for s in net["stations"].values()]
    by_key = defaultdict(list)
    for k, pt in ours:
        by_key[k].append(pt)

    def covered(ja, pt):
        return any(haversine_m(pt, p) < 1500 for p in by_key.get(ja_key(ja), []))

    lines = {}
    for zone, bbox in ZONES.items():
        data = fetch_zone(zone, bbox, args.refresh)
        nodes = {e["id"]: e for e in data["elements"] if e["type"] == "node"}
        for rel in (e for e in data["elements"] if e["type"] == "relation"):
            t = rel.get("tags", {})
            name = t.get("name", "")
            if not name or SERVICE_RE.search(name) or t.get("route") == "bus":
                continue
            stops = []
            for m in rel["members"]:
                n = nodes.get(m["ref"]) if m["type"] == "node" and m.get("role", "").startswith("stop") else None
                if n:
                    ja = normalize_ja(n["tags"].get("name", ""))
                    if ja:
                        stops.append((ja, (n["lat"], n["lon"])))
            if not stops:
                continue
            key = base_name(name)
            info = lines.setdefault(key, {"name": key, "en": re.sub(r"\s*\(.*", "", t.get("name:en", "")),
                                          "operator": t.get("operator", ""), "zone": zone,
                                          "relations": [], "stations": {}, "missing": {}})
            info["relations"].append(rel["id"])
            for ja, pt in stops:
                info["stations"][ja] = pt
                if not covered(ja, pt):
                    info["missing"][ja] = [round(pt[0], 5), round(pt[1], 5)]

    gaps = sorted((l for l in lines.values() if l["missing"]),
                  key=lambda l: (l["zone"], -len(l["missing"]) / max(1, len(l["stations"]))))
    out = []
    for l in gaps:
        share = len(l["missing"]) / len(l["stations"])
        out.append({**{k: l[k] for k in ("name", "en", "operator", "zone")},
                    "relations": sorted(set(l["relations"]))[:4],
                    "total": len(l["stations"]), "missing": sorted(l["missing"]),
                    "kind": "línea que falta" if share > 0.6 else "estaciones que faltan"})
    (CACHE / "audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    # las cajas auditadas, para que el inventario sepa qué parte del país no se ha comprobado
    (CACHE / "audit-zones.json").write_text(json.dumps(ZONES, ensure_ascii=False, indent=1), encoding="utf-8")
    write_report(out)
    for o in out:
        print(f"[{o['zone']}] {o['kind']:22} {o['name'][:28]:28} {o['en'][:32]:32} {len(o['missing']):3}/{o['total']:<3} "
              f"{' '.join(o['missing'][:6])}")
    print(f"\n{len(out)} líneas con huecos", file=sys.stderr)


if __name__ == "__main__":
    main()
