# Japan Rail Explorer

Mapa interactivo de las líneas de tren y metro de Japón, con estaciones, trenes y datos curiosos.
La primera fase cubre **Tokio** (24 líneas); la idea es ir ampliando poco a poco al resto del país.

- Trazados y estaciones reales, sacados de [OpenStreetMap](https://www.openstreetmap.org/).
- Ficha de cada línea (recorrido con numeración de estaciones, transbordos, trenes, datos curiosos).
- Ficha de cada estación (líneas, estación anterior/siguiente en cada línea, transbordos a pie).
- Ficha de cada serie de tren.
- Buscador (español, romaji o japonés: `shinjuku`, `新宿`, `JY`…), filtros por operador, modo oscuro y móvil.
- Enlaces compartibles: `#/line/yamanote`, `#/station/shinjuku`, `#/train/e235-0`.

## Estructura

```
config/            ← lo que se edita a mano
  lines.json       líneas: color, código, relación OSM, datos curiosos, trenes
  stations.json    datos curiosos por estación (clave = id de estación)
  trains.json      series de trenes
tools/
  build_data.py    descarga de OSM + mezcla con config → web/data/network.json
web/               ← la web estática (lo que se publica)
  index.html
  css/app.css
  js/app.js        router (#/…), buscador
  js/map.js        mapa Leaflet
  js/views.js      fichas del panel lateral
  js/data.js       carga de datos y consultas
  data/network.json  (generado, no editar)
  vendor/leaflet/  Leaflet 1.9.4 (local, sin CDN)
```

No hay dependencias ni paso de compilación en la web: son ficheros estáticos.
El script de datos solo necesita Python 3.9+ (librería estándar).

## Ver la web en local

Cualquier servidor estático sirve, apuntando a `web/`:

```bash
python3 -m http.server 8000 -d web
```

y abrir <http://localhost:8000>. (Abrir `index.html` con doble clic no funciona: el navegador bloquea la carga de `network.json` desde `file://`.)

En el servidor actual está publicada en `http://192.168.0.215:8080/japan-rail/` (nginx, `location /japan-rail/` → `web/`).

## Regenerar los datos

```bash
python3 tools/build_data.py            # usa la caché local si existe
python3 tools/build_data.py --refresh  # vuelve a descargar todo de OSM
```

Las descargas se guardan en `tools/.cache/` (ignorada por git). La API pública de Overpass
a veces limita peticiones (HTTP 429); el script reintenta solo.

## Añadir una línea nueva

1. Busca la línea en [openstreetmap.org](https://www.openstreetmap.org/) y abre su relación de tipo *route*
   (una sola dirección basta). Apunta el número de relación.
2. Añade una entrada en `config/lines.json`:
   ```json
   {
     "id": "tokaido-shinkansen", "code": "JT", "color": "#0072BA",
     "name": "Tōkaidō Shinkansen", "ja": "東海道新幹線", "en": "Tōkaidō Shinkansen",
     "operator": "jr-central", "type": "shinkansen", "osm": [123456],
     "opened": 1964, "length_km": 515.4,
     "trains": ["n700s"],
     "summary": "…", "facts": ["…"]
   }
   ```
   Si el operador o el tipo son nuevos, añádelos en `operators` / `types`. Los ramales se añaden como
   relaciones extra en `osm` (la primera es la que fija el orden de estaciones).
3. `python3 tools/build_data.py` y recarga la web. El script avisa de estaciones sin nombre, trenes
   desconocidos o claves de `stations.json` que no coinciden con ninguna estación.

Para añadir datos a una estación, usa su id (lo ves en la URL: `#/station/<id>`) en `config/stations.json`.

## Hoja de ruta

- [ ] Shinkansen Tōkaidō y Tōhoku (primer salto fuera de Tokio)
- [ ] Líneas privadas de Tokio (Tōkyū, Odakyū, Keiō, Seibu, Tōbu, Keikyū, Keisei)
- [ ] Osaka / Kansai
- [ ] Fotos de trenes y estaciones (Wikimedia Commons, con autoría y licencia)
- [ ] Viajeros diarios por estación

## Créditos y licencias

- Trazados y estaciones: © colaboradores de OpenStreetMap, licencia [ODbL](https://www.openstreetmap.org/copyright).
- Mapa base: © [CARTO](https://carto.com/attributions), datos © OpenStreetMap.
- [Leaflet](https://leafletjs.com/) (BSD-2-Clause).
- Textos y datos curiosos: redacción propia, revisados a mano. Si ves un error, abre un issue.
