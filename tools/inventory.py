#!/usr/bin/env python3
"""Genera INVENTARIO.md: lo que hay, los huecos detectados y lo que queda.

«Lo que hay» y «Huecos» salen de web/data/network.json; «Lo que queda», de config/roadmap.json
(los elementos con line/train/region se marcan solos cuando existen en los datos).

Uso:
    python3 tools/inventory.py      # también lo ejecuta build_data.py al terminar
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NETWORK = ROOT / "web" / "data" / "network.json"
ROADMAP = ROOT / "config" / "roadmap.json"
OUT = ROOT / "INVENTARIO.md"
SITE = "https://japanrail.alvaroom.org"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def link(kind, id_, text):
    return f"[{text}]({SITE}/#/{kind}/{id_})"


def pct(a, b):
    return f"{round(100 * a / b)} %" if b else "—"


def main():
    net = load(NETWORK)
    road = load(ROADMAP) if ROADMAP.exists() else {"phases": []}
    lines, stations, trains = net["lines"], net["stations"], net["trains"]
    regions = net.get("regions", {})
    ops = net["operators"]
    line_by_id = {l["id"]: l for l in lines}
    region_of = {l["id"]: l.get("region", "japan") for l in lines}

    cur_by_line, hist_by_line = defaultdict(list), defaultdict(list)
    for t in trains:
        for lid in t.get("lines", []):
            cur_by_line[lid].append(t)
        for h in t.get("history", []):
            hist_by_line[h["line"]].append(t)

    st_regions = defaultdict(set)
    for s in stations.values():
        for x in s["lines"]:
            st_regions[region_of[x["line"]]].add(s["id"])

    def train_region(t):
        ids = t.get("lines") or [h["line"] for h in t.get("history", [])]
        return region_of.get(ids[0]) if ids else None

    out = []
    w = out.append
    w("# Inventario de Japan Rail Explorer\n")
    w(f"> Generado automáticamente por `tools/inventory.py` a partir de los datos ({net['generated'][:10]}). "
      "No lo edites a mano: cambia `config/` y vuelve a generar.\n")

    # ---------------------------------------------------------------- resumen
    w("## Resumen\n")
    w("| Región | Líneas | Estaciones | Trenes actuales | Trenes históricos |")
    w("|---|--:|--:|--:|--:|")
    for rid, r in regions.items():
        ls = [l for l in lines if l.get("region") == rid]
        if not ls:
            continue
        tr = [t for t in trains if train_region(t) == rid]
        w(f"| {r['name']} {r.get('ja', '')} | {len(ls)} | {len(st_regions[rid])} | "
          f"{sum(1 for t in tr if t.get('lines'))} | {sum(1 for t in tr if not t.get('lines'))} |")
    photos = sum(1 for t in trains if t.get("photo"))
    st_facts = sum(1 for s in stations.values() if s.get("facts"))
    w(f"| **Total** | **{len(lines)}** | **{len(stations)}** | "
      f"**{sum(1 for t in trains if t.get('lines'))}** | **{sum(1 for t in trains if not t.get('lines'))}** |\n")
    w(f"- Fotos de trenes: **{photos} de {len(trains)}** ({pct(photos, len(trains))}).")
    w(f"- Estaciones con datos curiosos: **{st_facts} de {len(stations)}** ({pct(st_facts, len(stations))}).")
    w(f"- Datos curiosos en total: **{sum(len(x.get('facts', [])) for x in [*lines, *stations.values(), *trains])}**.\n")

    # ---------------------------------------------------------------- lo que hay
    w("## Lo que hay\n")
    for rid, r in regions.items():
        ls = [l for l in lines if l.get("region") == rid]
        if not ls:
            continue
        w(f"### {r['name']} {r.get('ja', '')}\n")
        w("| Código | Línea | Operador | Est. | Trenes actuales | Históricos | Datos |")
        w("|---|---|---|--:|---|---|--:|")
        for l in ls:
            cur = ", ".join(t["name"] for t in cur_by_line[l["id"]]) or "—"
            hist = ", ".join(t["name"] for t in sorted(hist_by_line[l["id"]], key=lambda t: t.get("introduced", 0))) or "—"
            w(f"| {l['code']} | {link('line', l['id'], l['name'])} | {ops.get(l['operator'], {}).get('name', l['operator'])} "
              f"| {len(l['stations'])} | {cur} | {hist} | {len(l.get('facts', []))} |")
        w("")

    # ---------------------------------------------------------------- huecos
    w("## Huecos detectados\n")
    w("Salen solos de los datos: son buenas tareas pequeñas para ir completando.\n")
    no_cur = [l for l in lines if not cur_by_line[l["id"]]]
    no_hist = [l for l in lines if not hist_by_line[l["id"]]]
    no_photo = [t for t in trains if not t.get("photo")]
    no_tfacts = [t for t in trains if not t.get("facts")]
    no_code = [l for l in lines
               if any(x["code"] for s in l["stations"] for x in stations[s]["lines"] if x["line"] == l["id"])
               and any(not x["code"] for s in l["stations"] for x in stations[s]["lines"] if x["line"] == l["id"])]

    def lst(items, kind, name=lambda x: x["name"]):
        return ", ".join(link(kind, x["id"], name(x)) for x in items) if items else "ninguna 🎉"

    w(f"- **Líneas sin trenes actuales** ({len(no_cur)}): {lst(no_cur, 'line')}")
    w(f"- **Trenes sin foto** ({len(no_photo)}): {lst(no_photo, 'train')}")
    w(f"- **Líneas con numeración incompleta** ({len(no_code)}): {lst(no_code, 'line')}")
    w(f"- **Trenes sin datos curiosos** ({len(no_tfacts)} de {len(trains)}).")
    w(f"- **Líneas sin trenes históricos** ({len(no_hist)} de {len(lines)}):")
    for rid, r in regions.items():
        ls = [l for l in no_hist if l.get("region") == rid]
        if ls:
            w(f"  - {r['name']}: {lst(ls, 'line')}")
    # grandes estaciones sin datos
    big = sorted((s for s in stations.values() if not s.get("facts") and len(s["lines"]) >= 3),
                 key=lambda s: -len(s["lines"]))
    w(f"- **Grandes estaciones (3+ líneas) sin datos curiosos** ({len(big)}): "
      + (", ".join(f"{link('station', s['id'], s['name'])} ({len(s['lines'])})" for s in big) or "ninguna 🎉"))
    w("")

    # ---------------------------------------------------------------- lo que queda
    w("## Lo que queda\n")
    w("La lista de huecos respecto a OpenStreetMap está en [AUDITORIA.md](AUDITORIA.md) (`tools/audit_coverage.py`).\n")
    w("Por fases. Las casillas de líneas, trenes y regiones se marcan solas cuando existen en los datos.\n")
    train_ids = {t["id"] for t in trains}
    total = done_n = 0
    for ph in road["phases"]:
        items = [it for g in ph["groups"] for it in g["items"]]
        done = [it for it in items if is_done(it, line_by_id, train_ids, regions, lines)]
        total += len(items)
        done_n += len(done)
        w(f"### {ph['title']} ({len(done)}/{len(items)})\n")
        if ph.get("why"):
            w(f"_{ph['why']}_\n")
        for g in ph["groups"]:
            w(f"**{g['title']}**\n")
            for it in g["items"]:
                text = it.get("name") or it.get("task")
                w(f"- [{'x' if is_done(it, line_by_id, train_ids, regions, lines) else ' '}] {text}")
            w("")
    out.insert(3, f"**Progreso de la hoja de ruta: {done_n} de {total} tareas.**\n")

    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {done_n}/{total} tareas de la hoja de ruta")


def is_done(it, line_by_id, train_ids, regions, lines):
    if "line" in it:
        return it["line"] in line_by_id
    if "lines" in it:
        return all(l in line_by_id for l in it["lines"])
    if "train" in it:
        return it["train"] in train_ids
    if "region" in it:
        return any(l.get("region") == it["region"] for l in lines)
    return bool(it.get("done"))


if __name__ == "__main__":
    main()
