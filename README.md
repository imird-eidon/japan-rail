# Japan Rail Explorer

Mapa interactivo de las líneas de tren y metro de Japón, con estaciones, trenes y datos curiosos.
Ahora cubre **toda la red Shinkansen** y 365 líneas con 4486 estaciones y 182 series de trenes.
Diez prefecturas están completas al 100 % frente a OpenStreetMap (Tokio, Kanagawa, Chiba, Saitama, Kioto, Ōsaka,
Nara, Hyōgo, Shiga y Aichi) y el conjunto de Japón va por el 50 % de sus estaciones.
La idea es ir ampliando poco a poco al resto del país. El detalle, en [INVENTARIO.md](INVENTARIO.md).

- Trazados y estaciones reales, sacados de [OpenStreetMap](https://www.openstreetmap.org/).
- Ficha de cada línea (recorrido con numeración de estaciones, transbordos, trenes, datos curiosos).
- Ficha de cada estación (líneas, estación anterior/siguiente en cada línea, transbordos a pie).
- Ficha de cada serie de tren, con foto, por qué líneas y tramos circula y en qué estaciones pasa.
- En cada estación, los trenes que pasan por ella.
- Menú «Ir a…» para centrar el mapa en cualquiera de las 19 ciudades o en todo Japón.
- Buscador (español, romaji o japonés: `shinjuku`, `新宿`, `JY`…), filtros por operador, modo oscuro y móvil.
- Enlaces compartibles: `#/line/yamanote`, `#/station/shinjuku`, `#/train/e235-0`.

## Estructura

```
config/            ← lo que se edita a mano
  lines.json       líneas: color, código, relación OSM, datos curiosos, trenes
  stations.json    datos curiosos por estación (clave = id de estación)
  trains.json      series de trenes y por dónde circulan (runs)
  photos.json      (generado por fetch_photos.py) fotos: fichero, autor, licencia
  overrides.json   correcciones a errores de OSM (nombres, códigos de estación)
tools/
  build_data.py    descarga de OSM + mezcla con config → web/data/network.json
  fetch_photos.py  descarga fotos de Wikimedia Commons → web/img/trains/ + config/photos.json
web/               ← la web estática (lo que se publica)
  index.html
  css/app.css
  js/app.js        router (#/…), buscador
  js/map.js        mapa Leaflet
  js/views.js      fichas del panel lateral
  js/data.js       carga de datos y consultas
  data/network.json  (generado, no editar)
  img/trains/      fotos de trenes en WebP (800 px) y miniaturas en thumb/ (360 px), generadas
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

Publicada en <https://japanrail.alvaroom.org/> (Cloudflare Tunnel → nginx en `192.168.0.215:8080`, que sirve `web/`
en `/` y también en `/japan-rail/` por compatibilidad con los enlaces antiguos).

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
   Si el operador o el tipo son nuevos, añádelos en `operators` / `types`. Claves opcionales:
   - `osm` con varias relaciones: la primera fija el orden; las demás añaden trazado (ramales).
   - `extra_stops`: relaciones de otros servicios de las que solo se toman paradas (útil cuando
     ningún servicio para en todas las estaciones, como en el Hokuriku Shinkansen).
   - `section: ["desde", "hasta"]` (nombres japoneses): recorta una relación más larga a ese tramo
     (p. ej. el Yamagata Shinkansen sale del servicio Tsubasa Tokio–Shinjō).
   - `order: "geometry"`: ordena las estaciones por su posición sobre la vía.
   - `order: "code"`: ordena por el código de estación (útil con vías dobles o cuádruples).
   - `osm_ways` (`{filter, bbox}`): para líneas que no tienen relación *route* en OSM (p. ej. la línea
     principal Keihan): el trazado sale de las vías que cumplen el filtro y las paradas, de las
     `stop_position` que hay sobre ellas.
   - `region`: `japan` (Shinkansen), `tokyo`, `kyoto`… Las regiones se definen arriba, en `regions`;
     las que tienen `bounds` tienen su botón en el mapa.
   - `extra_nodes`: paradas sueltas por id de nodo OSM; `station_order`: orden explícito (nombres japoneses);
     `no_extrapolate`: no deducir códigos en los extremos.
   - `trains`: series que recorren la línea entera.
3. `python3 tools/build_data.py` y recarga la web. El script avisa de estaciones sin nombre, trenes
   desconocidos o claves de `stations.json` que no coinciden con ninguna estación.

## Añadir un tren

En `config/trains.json`. Para decir por dónde pasa, usa `runs` (los tramos con nombres japoneses):

```json
{ "id": "sk-e6", "name": "Serie E6", "operator": "jr-east", "introduced": 2013, "cars": 7,
  "wiki": "E6 Series Shinkansen",
  "runs": [ { "line": "tohoku-shinkansen", "from": "東京", "to": "盛岡" }, { "line": "akita-shinkansen" } ] }
```

Para los trenes que ya no circulan (o que dejaron alguna línea), usa `history` con los años, y
`retired` si se retiró del todo:

```json
{ "id": "jnr-205", "name": "Serie 205", "operator": "jnr", "introduced": 1985,
  "history": [ { "line": "yamanote", "years": [1985, 2005] }, { "line": "saikyo", "years": [1989, 2016] } ] }
```

Un tren puede tener `runs` y `history` a la vez (el 700 sigue en el San'yō y dejó el Tōkaidō en 2020).
Los años salen de los artículos de Wikipedia de cada serie.

Para la foto: `wiki` (artículo de la Wikipedia en inglés; se usa su imagen principal) o `photo_file`
(`"File:…jpg"` de Wikimedia Commons, para elegir una concreta). Después:

```bash
python3 tools/fetch_photos.py sk-e6   # descarga la foto, la pasa a WebP y guarda autor y licencia
python3 tools/build_data.py
```

`fetch_photos.py` necesita `cwebp` (`apt install webp`): guarda cada foto en WebP a 800 px y una miniatura
de 360 px para listas y tarjetas.

Solo se aceptan licencias libres; la autoría y la licencia se muestran bajo cada foto.

En `config/overrides.json` se corrigen los fallos de OSM: `station_names_en` (romaji que falta),
`station_codes` (numeración), `ja_aliases` (dos nombres para la misma estación, como 近鉄京都 → 京都) y
`stop_nodes` (paradas sin nombre, por número de nodo OSM).

## Añadir una ciudad

1. Añade la región en `regions` de `config/lines.json`, con `bounds` para que tenga botón en el mapa.
2. Añade sus líneas con `"region": "<id>"` y sus trenes en `trains.json`.
3. `python3 tools/build_data.py` y revisa los avisos (romaji, códigos, paradas sin nombre).

Para añadir datos a una estación, usa su id (lo ves en la URL: `#/station/<id>`) en `config/stations.json`.

## Inventario y hoja de ruta

**[INVENTARIO.md](INVENTARIO.md)** tiene la foto completa: qué hay por región, los huecos que se detectan solos
en los datos (líneas sin trenes, estaciones grandes sin datos curiosos…) y la lista de lo que queda por fases.
Una ciudad sólo se da por hecha cuando la auditoría no le encuentra ni una línea ni una estación de menos;
el estado de cada una está en la tabla «Cobertura por ciudad» del inventario.

**[AUDITORIA.md](AUDITORIA.md)** compara todas las rutas de OpenStreetMap de cada zona con los datos (`python3 tools/audit_coverage.py`)
y sirve para detectar líneas o estaciones que faltan. El inventario se regenera al ejecutar `tools/build_data.py`; la lista de pendientes se edita en `config/roadmap.json`
(las líneas, trenes y regiones se marcan como hechos solos en cuanto existen en los datos).

## Hoja de ruta (resumen)

- [x] Red Shinkansen completa, con fotos de los trenes
- [x] Completar Tokio: JR East restantes, compañías privadas y Yokohama (fase 1)
- [x] Kioto
- [x] Ōsaka, Kōbe y resto de Kansai (fase 2)
- [x] Fotos de todos los trenes y trenes históricos con sus años de servicio
- [x] Nagoya, Fukuoka, Sapporo, Sendai, Hiroshima y los tranvías de otras ciudades (fase 3)
- [x] Sapporo al completo: JR Hakodate, Chitose entera y sus trenes (fase 3c)
- [ ] El resto de ciudades, una a una y cerrando cada una del todo (fase 3c)
- [ ] Fotos de estaciones
- [ ] Servicios (Nozomi, Hikari, Kodama…) y en qué estaciones para cada uno
- [ ] Viajeros diarios por estación

## Créditos y licencias

- Trazados y estaciones: © colaboradores de OpenStreetMap, licencia [ODbL](https://www.openstreetmap.org/copyright).
- Mapa base: teselas estándar de OpenStreetMap ([política de uso](https://operations.osmfoundation.org/policies/tiles/)); si el tráfico crece habrá que pasar a un proveedor propio.
- [Leaflet](https://leafletjs.com/) (BSD-2-Clause).
- Fotos de trenes: Wikimedia Commons; autor y licencia (CC BY-SA, etc.) en `config/photos.json` y bajo cada foto.
- Textos y datos curiosos: redacción propia, revisados a mano. Si ves un error, abre un issue.
