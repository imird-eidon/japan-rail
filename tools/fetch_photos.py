#!/usr/bin/env python3
"""Descarga fotos de trenes desde Wikimedia Commons y guarda su autoría y licencia.

Para cada tren de config/trains.json con:
  "photo_file": "File:Nombre.jpg"   → usa ese fichero de Commons (recomendado: control total), o
  "wiki": "Título del artículo"     → usa la imagen principal del artículo en la Wikipedia en inglés.
  "photo_search": "texto"           → busca en Commons y toma la primera foto con licencia libre
                                       (revísala: conviene fijarla luego con photo_file).

Resultado (necesita `cwebp`: apt install webp):
  web/img/trains/<id>.webp        foto de hasta 800 px de ancho (ficha del tren)
  web/img/trains/thumb/<id>.webp  miniatura de 360 px (listas y tarjetas)
  config/photos.json              {id: {src, thumb, file, author, license, license_url, source}}

Uso:
    python3 tools/fetch_photos.py            # solo las que faltan
    python3 tools/fetch_photos.py --refresh  # vuelve a descargarlas todas
    python3 tools/fetch_photos.py sk-e5      # solo esos ids
    python3 tools/fetch_photos.py --convert  # pasa a WebP las .jpg que queden (sin volver a descargar)

Solo se aceptan licencias libres (CC BY, CC BY-SA, CC0, dominio público).
"""
import argparse
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRAINS = ROOT / "config" / "trains.json"
PHOTOS = ROOT / "config" / "photos.json"
IMG_DIR = ROOT / "web" / "img" / "trains"
WIDTH = 960           # tamaño que se descarga de Commons
FULL_WIDTH = 800      # tamaño publicado (el panel mide 400 px; 800 para pantallas de alta densidad)
THUMB_WIDTH = 360     # miniaturas de listas y tarjetas
QUALITY = "75"
PORTRAIT_WIDTH = 500  # Commons sirve miniaturas en tamaños fijos (500, 960…): las verticales, a 500
UA = "japan-rail-explorer/0.1 (hobby project; https://github.com/imird-eidon/japan-rail)"
FREE = re.compile(r"^(CC BY(-SA)? \d|CC0|Public domain|PD)", re.I)


def api(host, **params):
    params.update(format="json", formatversion=2)
    url = f"https://{host}/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def lead_image(title):
    d = api("en.wikipedia.org", action="query", titles=title, prop="pageimages", piprop="name", redirects=1)
    page = d["query"]["pages"][0]
    name = page.get("pageimage")
    return f"File:{name}" if name else None


def search_file(query):
    d = api("commons.wikimedia.org", action="query", list="search", srsearch=f"{query} filetype:bitmap",
            srnamespace=6, srlimit=10)
    for hit in d["query"]["search"]:
        title = hit["title"]
        if not re.search(r"\.(jpe?g|png)$", title, re.I) or re.search(r"(?i)logo|inside|interior|seat|sign|map|LED|display|headmark", title):
            continue
        try:
            if FREE.match(file_info(title)["license"]):
                return title
        except LookupError:
            continue
    return None


def clean(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = html.unescape(re.sub(r"\s+", " ", s)).strip()
    return re.split(r"\s+This (photo|image|file) was taken", s)[0].strip()  # texto de plantillas de cámara


def file_info(file, width=WIDTH):
    d = api("commons.wikimedia.org", action="query", titles=file, prop="imageinfo",
            iiprop="url|extmetadata|size", iiurlwidth=width)
    page = d["query"]["pages"][0]
    if page.get("missing"):
        raise LookupError(f"{file} no existe en Commons")
    ii = page["imageinfo"][0]
    if width == WIDTH and ii.get("height", 0) > ii.get("width", 0) > 0:
        return file_info(file, PORTRAIT_WIDTH)
    if ii.get("width", 0) <= width and width == WIDTH and ii.get("width", 0) > 1:
        # si el original es más estrecho, Commons devuelve el original (a veces pesadísimo): pedimos miniatura
        return file_info(file, ii["width"] - 1)
    meta = ii.get("extmetadata", {})
    val = lambda k: meta.get(k, {}).get("value", "")
    return {
        "thumb": ii["thumburl"],
        "file": page["title"],
        "author": clean(val("Artist")) or "Autor desconocido",
        "license": clean(val("LicenseShortName")),
        "license_url": val("LicenseUrl"),
        "source": ii["descriptionurl"],
    }


def download(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        path.write_bytes(r.read())


def to_webp(src, tid):
    """Convierte la descarga a WebP (foto y miniatura) y borra el original."""
    thumb_dir = IMG_DIR / "thumb"
    thumb_dir.mkdir(exist_ok=True)
    full, thumb = IMG_DIR / f"{tid}.webp", thumb_dir / f"{tid}.webp"
    for out, width in ((full, FULL_WIDTH), (thumb, THUMB_WIDTH)):
        subprocess.run(["cwebp", "-quiet", "-q", QUALITY, "-m", "6", "-metadata", "none",
                        "-resize", str(width), "0", str(src), "-o", str(out)], check=True)
    src.unlink()
    return {"src": f"img/trains/{full.name}", "thumb": f"img/trains/thumb/{thumb.name}"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--convert", action="store_true", help="convierte a WebP las .jpg existentes")
    args = ap.parse_args()

    trains = json.loads(TRAINS.read_text(encoding="utf-8"))
    photos = json.loads(PHOTOS.read_text(encoding="utf-8")) if PHOTOS.exists() else {}
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    if args.convert:
        for jpg in sorted(IMG_DIR.glob("*.jpg")):
            tid = jpg.stem
            if tid in photos:
                photos[tid].update(to_webp(jpg, tid))
        PHOTOS.write_text(json.dumps(dict(sorted(photos.items())), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"convertidas; {sum(1 for p in photos.values() if p['src'].endswith('.webp'))} fotos en WebP")
        return

    for t in trains:
        tid = t["id"]
        if args.ids and tid not in args.ids:
            continue
        if not (t.get("photo_file") or t.get("wiki") or t.get("photo_search")):
            continue
        if tid in photos and not args.refresh and not args.ids:
            continue
        try:
            file = t.get("photo_file") or (t.get("photo_search") and search_file(t["photo_search"])) \
                or (t.get("wiki") and lead_image(t["wiki"]))
            if not file:
                print(f"  {tid}: no encuentro foto (wiki/photo_search)", file=sys.stderr)
                continue
            info = file_info(file)
            if not FREE.match(info["license"]):
                print(f"  {tid}: {file} tiene licencia «{info['license']}», no se usa", file=sys.stderr)
                continue
            out = IMG_DIR / f"{tid}.download"
            download(info.pop("thumb"), out)
            photos[tid] = {**to_webp(out, tid), **info}
            size = (IMG_DIR / f"{tid}.webp").stat().st_size // 1024
            print(f"  {tid}: {info['file']} · {info['license']} · {info['author'][:60]} ({size} KB)")
            time.sleep(1)
        except Exception as e:  # una foto que falla no debe parar el resto
            print(f"  {tid}: error {e}", file=sys.stderr)

    PHOTOS.write_text(json.dumps(dict(sorted(photos.items())), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(photos)} fotos en {PHOTOS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
