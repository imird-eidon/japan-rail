// Mapa Leaflet: líneas, estaciones, resaltado, filtros y botones de centrado.
import { esc, textOn, groupOf, isShinkansen } from "./data.js";

const L = window.L;
// Teselas estándar de OSM; el tono claro/oscuro se consigue con un filtro CSS (.basemap en app.css)
const TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";
const JAPAN_BOUNDS = [[31.2, 129.6], [41.95, 141.2]]; // de Kagoshima a Hakodate
const MAX_BOUNDS = [[20, 118], [50, 156]];           // no dejar que el mapa se vaya muy lejos
const STATION_MIN_ZOOM = 12;
const LABEL_MIN_ZOOM = 12;

export function createMap(el, net, { onLine, onStation }) {
  const darkQuery = matchMedia("(prefers-color-scheme: dark)");
  const theme = () => (darkQuery.matches ? "dark" : "light");

  const map = L.map(el, {
    zoomControl: false, minZoom: 5, maxZoom: 18, zoomSnap: 0.5,
    maxBounds: MAX_BOUNDS, maxBoundsViscosity: 0.8,
  }).setView([35.69, 139.74], 12);
  L.control.zoom({ position: "topright", zoomInTitle: "Acercar", zoomOutTitle: "Alejar" }).addTo(map);
  L.control.scale({ imperial: false, position: "bottomright" }).addTo(map);

  L.tileLayer(TILE_URL, {
    maxZoom: 19, className: "basemap",
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  map.createPane("lines").style.zIndex = 410;
  map.createPane("stations").style.zIndex = 420;
  map.createPane("labels").style.zIndex = 630;
  const lineRenderer = L.canvas({ pane: "lines", tolerance: 6 });
  const stationRenderer = L.canvas({ pane: "stations", tolerance: 4 });

  // ---------------------------------------------------------------- estado
  const state = { focusLine: null, focusStation: null, focusLines: null, hidden: new Set() };
  const lineLayers = new Map();     // id -> { casing, stroke, bounds, line }
  const stationMarkers = new Map(); // id -> circleMarker
  const stationLayer = L.layerGroup().addTo(map);
  const labelLayer = L.layerGroup().addTo(map);
  let pulse = null;

  const casingColor = () => (theme() === "dark" ? "#16181d" : "#ffffff");
  const weight = (line) => {
    const z = map.getZoom();
    if (isShinkansen(line)) return z < 8 ? 3 : z < 11 ? 4 : z < 15 ? 5 : 7;
    return z < 9 ? 1.5 : z < 11 ? 2.5 : z < 13 ? 3.5 : z < 15 ? 5 : 7;
  };

  // ---------------------------------------------------------------- líneas
  for (const line of net.lines) {
    const casing = L.polyline(line.geometry, { renderer: lineRenderer, color: casingColor(), interactive: false, lineCap: "round" });
    const stroke = L.polyline(line.geometry, { renderer: lineRenderer, color: line.color, lineCap: "round", lineJoin: "round" });
    stroke.bindTooltip(
      `<span class="badge" style="--c:${line.color};--t:${textOn(line.color)}">${esc(line.code)}</span> ${esc(line.name)}`,
      { sticky: true, className: "map-tip", direction: "top", offset: [0, -8] });
    stroke.on("click", (e) => { L.DomEvent.stop(e); onLine(line.id); });
    stroke.on("mouseover", () => hoverLine(line.id, true));
    stroke.on("mouseout", () => hoverLine(line.id, false));
    lineLayers.set(line.id, { casing, stroke, bounds: stroke.getBounds(), line });
  }

  // ---------------------------------------------------------------- estaciones
  for (const st of net.stationList) {
    const marker = L.circleMarker([st.lat, st.lon], { renderer: stationRenderer, bubblingMouseEvents: false });
    const seen = new Set();
    const codes = st.lines
      .filter((x) => !x.code || !seen.has(x.code) && seen.add(x.code))
      .map((x) => [net.lineById.get(x.line), x.code])
      .map(([l, code]) => `<span class="badge" style="--c:${l.color};--t:${textOn(l.color)}">${esc(code || l.code)}</span>`)
      .join("");
    marker.bindTooltip(`<strong>${esc(st.name)}</strong> <span class="ja">${esc(st.ja)}</span><div class="tip-codes">${codes}</div>`,
      { className: "map-tip", direction: "top", offset: [0, -6] });
    marker.on("click", () => onStation(st.id));
    marker.on("mouseover", () => {
      marker._base = { radius: marker.options.radius, weight: marker.options.weight };
      marker.setStyle({ radius: (marker.options.radius || 4) + 3, weight: 3 });
    });
    marker.on("mouseout", () => { if (marker._base) marker.setStyle(marker._base); });
    stationMarkers.set(st.id, marker);
    st._shinkansen = st.lineIds.some((id) => isShinkansen(net.lineById.get(id)));
  }

  // ---------------------------------------------------------------- render
  const visibleLine = (line) => !state.hidden.has(groupOf(line));

  function focusedLineSet() {
    if (state.focusLine) return new Set([state.focusLine]);
    if (state.focusStation) return new Set(net.stations[state.focusStation].lineIds);
    if (state.focusLines) return state.focusLines;
    return null;
  }

  /** Engorda la línea bajo el cursor, para que se note qué se va a abrir al pulsar. */
  function hoverLine(id, on) {
    const l = lineLayers.get(id);
    if (!l || !map.hasLayer(l.stroke)) return;
    const focusSet = focusedLineSet();
    if (focusSet && !focusSet.has(id)) return;   // atenuada: no reacciona
    const w = weight(l.line) + (focusSet ? 2 : 0);
    const extra = Math.max(4, Math.round(w * 0.8));   // que se note también en zooms lejanos
    l.stroke.setStyle({ weight: on ? w + extra : w });
    l.casing.setStyle({ weight: w + (focusSet ? 5 : 3) + (on ? extra : 0) });
    if (on) { l.casing.bringToFront(); l.stroke.bringToFront(); }
  }

  function styleLines() {
    const focusSet = focusedLineSet();
    for (const [id, { casing, stroke, line }] of lineLayers) {
      const show = visibleLine(line);
      for (const layer of [casing, stroke]) {
        if (show && !map.hasLayer(layer)) layer.addTo(map);
        if (!show && map.hasLayer(layer)) layer.remove();
      }
      if (!show) continue;
      const w = weight(line);
      const dim = focusSet && !focusSet.has(id);
      const hl = focusSet && focusSet.has(id);
      casing.setStyle({ weight: w + (hl ? 5 : 3), opacity: dim ? 0 : 0.9, color: casingColor() });
      stroke.setStyle({ weight: hl ? w + 2 : w, opacity: dim ? 0.13 : 0.95 });
    }
    // las resaltadas, encima
    if (focusSet) for (const id of focusSet) {
      const l = lineLayers.get(id);
      if (l && map.hasLayer(l.stroke)) { l.casing.bringToFront(); l.stroke.bringToFront(); }
    }
  }

  function styleStations() {
    const z = map.getZoom();
    const focusSet = focusedLineSet();
    const focusLine = state.focusLine && net.lineById.get(state.focusLine);
    const dark = theme() === "dark";
    stationLayer.clearLayers();
    labelLayer.clearLayers();
    for (const st of net.stationList) {
      const lines = st.lineIds.filter((id) => visibleLine(net.lineById.get(id)));
      if (!lines.length) continue;
      if (focusSet && !lines.some((id) => focusSet.has(id))) continue;
      // sin foco: estaciones del Shinkansen siempre; las demás al acercarse (los grandes nudos, un poco antes)
      if (!focusSet && !st._shinkansen && z < STATION_MIN_ZOOM && (lines.length < 3 || z < 10)) continue;
      const hub = lines.length > 1;
      const first = net.lineById.get(state.focusLine || lines[0]);
      const far = z < 9;
      stationMarkers.get(st.id).setStyle({
        radius: (hub ? 5 : 3.5) + (z >= 15 ? 1.5 : 0) - (far ? 1.5 : 0),
        weight: far ? 1.5 : 2,
        color: hub ? (dark ? "#f2f2f2" : "#1a1a1a") : first.color,
        fillColor: dark ? "#1d2027" : "#ffffff",
        fillOpacity: 1,
      });
      stationLayer.addLayer(stationMarkers.get(st.id));
      if (focusLine && (z >= LABEL_MIN_ZOOM || isShinkansen(focusLine))) {
        labelLayer.addLayer(L.tooltip({ permanent: true, direction: "right", offset: [6, 0], className: "stn-label", pane: "labels", interactive: false })
          .setLatLng([st.lat, st.lon]).setContent(esc(st.name)));
      }
    }
  }

  function render() { styleLines(); styleStations(); }

  map.on("zoomend", render);
  darkQuery.addEventListener("change", render);

  // ---------------------------------------------------------------- menú «Ir a…»
  // Lugares: todo Japón, cada región con «bounds» y los lugares extra de lines.json → places (ciudades con tranvía…)
  const places = [
    { id: "japan", name: "Todo Japón", ja: "日本", bounds: JAPAN_BOUNDS },
    ...Object.entries(net.regions || {}).filter(([, r]) => r.bounds).map(([id, r]) => ({ id, ...r })),
    ...(net.places || []),
  ];
  const GoControl = L.Control.extend({
    options: { position: "topright" },
    onAdd() {
      const box = L.DomUtil.create("div", "leaflet-bar go-control");
      box.innerHTML = `
        <button type="button" class="go-toggle" aria-haspopup="true" aria-expanded="false" title="Centrar el mapa en…">Ir a ▾</button>
        <ul class="go-menu" role="menu" hidden>${places.map((p) => `
          <li role="none"><button type="button" role="menuitem" data-go="${esc(p.id)}">${esc(p.name)} <span class="ja">${esc(p.ja || "")}</span></button></li>`).join("")}
        </ul>`;
      const toggle = box.querySelector(".go-toggle"), menu = box.querySelector(".go-menu");
      const open = (v) => { menu.hidden = !v; toggle.setAttribute("aria-expanded", String(v)); };
      L.DomEvent.disableClickPropagation(box);
      L.DomEvent.disableScrollPropagation(box);
      toggle.addEventListener("click", () => open(menu.hidden));
      menu.addEventListener("click", (e) => {
        const b = e.target.closest("[data-go]");
        if (!b) return;
        open(false);
        api.showPlace(b.dataset.go);
      });
      document.addEventListener("click", (e) => { if (!box.contains(e.target)) open(false); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape") open(false); });
      return box;
    },
  });
  new GoControl().addTo(map);

  // ---------------------------------------------------------------- API
  const pad = () => (matchMedia("(max-width: 820px)").matches ? [20, 20] : [40, 40]);

  function setPulse(st) {
    pulse?.remove();
    pulse = null;
    if (!st) return;
    pulse = L.marker([st.lat, st.lon], {
      interactive: false, pane: "labels",
      icon: L.divIcon({ className: "pulse", html: "<span></span>", iconSize: [18, 18] }),
    }).addTo(map);
  }

  const api = {
    overview({ fit = false } = {}) {
      state.focusLine = state.focusStation = state.focusLines = null;
      setPulse(null);
      render();
      if (fit) map.fitBounds(net.regions.tokyo.bounds, { animate: false });
    },
    showPlace(id) {
      const p = places.find((x) => x.id === id);
      if (p) map.flyToBounds(p.bounds, { padding: id === "japan" ? pad() : [0, 0], duration: 0.8 });
    },
    /** Resalta varias líneas (p. ej. las de un tren) y encuadra el conjunto. */
    focusLines(ids, { animate = true } = {}) {
      state.focusLine = state.focusStation = null;
      state.focusLines = new Set(ids);
      setPulse(null);
      render();
      const b = L.latLngBounds([]);
      for (const id of ids) if (lineLayers.has(id)) b.extend(lineLayers.get(id).bounds);
      if (!b.isValid()) return;
      if (animate) map.flyToBounds(b, { padding: pad(), duration: 0.6 });
      else map.fitBounds(b, { padding: pad(), animate: false });
    },
    focusLine(id, { animate = true } = {}) {
      state.focusLine = id;
      state.focusStation = state.focusLines = null;
      setPulse(null);
      render();
      const l = lineLayers.get(id);
      if (!l) return;
      if (animate) map.flyToBounds(l.bounds, { padding: pad(), duration: 0.6 });
      else map.fitBounds(l.bounds, { padding: pad(), animate: false });
    },
    focusStation(id, { animate = true } = {}) {
      const st = net.stations[id];
      if (!st) return;
      state.focusLine = state.focusLines = null;
      state.focusStation = id;
      render();
      setPulse(st);
      const z = Math.max(map.getZoom(), 14.5);
      if (animate) map.flyTo([st.lat, st.lon], z, { duration: 0.6 });
      else map.setView([st.lat, st.lon], z, { animate: false });
    },
    setHidden(groups) {
      state.hidden = new Set(groups);
      render();
    },
    invalidate() { map.invalidateSize(); },
  };

  render();
  Object.assign(api, { _map: map, _lines: lineLayers });   // acceso para pruebas
  return api;
}
