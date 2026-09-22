// Mapa Leaflet: líneas, estaciones, resaltado y filtros.
import { esc, textOn } from "./data.js";

const L = window.L;
const TILE = (theme) => `https://{s}.basemaps.cartocdn.com/${theme === "dark" ? "dark_all" : "light_all"}/{z}/{x}/{y}{r}.png`;
const STATION_MIN_ZOOM = 12;
const LABEL_MIN_ZOOM = 12;

export function createMap(el, net, { onLine, onStation }) {
  const darkQuery = matchMedia("(prefers-color-scheme: dark)");
  const theme = () => (darkQuery.matches ? "dark" : "light");

  const map = L.map(el, { zoomControl: false, minZoom: 9, maxZoom: 18, zoomSnap: 0.5 })
    .setView([35.69, 139.74], 12);
  L.control.zoom({ position: "topright" }).addTo(map);
  L.control.scale({ imperial: false, position: "bottomright" }).addTo(map);

  const tiles = L.tileLayer(TILE(theme()), {
    subdomains: "abcd", maxZoom: 20,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
  }).addTo(map);

  map.createPane("lines").style.zIndex = 410;
  map.createPane("stations").style.zIndex = 420;
  map.createPane("labels").style.zIndex = 630;
  const lineRenderer = L.canvas({ pane: "lines", tolerance: 6 });
  const stationRenderer = L.canvas({ pane: "stations", tolerance: 4 });

  // ---------------------------------------------------------------- estado
  const state = { focusLine: null, focusStation: null, hiddenOps: new Set() };
  const lineLayers = new Map();     // id -> { casing, stroke, bounds }
  const stationMarkers = new Map(); // id -> circleMarker
  const stationLayer = L.layerGroup().addTo(map);
  const labelLayer = L.layerGroup().addTo(map);
  let pulse = null;

  const casingColor = () => (theme() === "dark" ? "#16181d" : "#ffffff");
  const weight = () => {
    const z = map.getZoom();
    return z < 11 ? 2.5 : z < 13 ? 3.5 : z < 15 ? 5 : 7;
  };

  // ---------------------------------------------------------------- líneas
  for (const line of net.lines) {
    const latlngs = line.geometry;
    const casing = L.polyline(latlngs, { renderer: lineRenderer, color: casingColor(), interactive: false, lineCap: "round" });
    const stroke = L.polyline(latlngs, { renderer: lineRenderer, color: line.color, lineCap: "round", lineJoin: "round" });
    stroke.bindTooltip(
      `<span class="badge" style="--c:${line.color};--t:${textOn(line.color)}">${esc(line.code)}</span> ${esc(line.name)}`,
      { sticky: true, className: "map-tip", direction: "top", offset: [0, -8] });
    stroke.on("click", (e) => { L.DomEvent.stop(e); onLine(line.id); });
    lineLayers.set(line.id, { casing, stroke, bounds: stroke.getBounds(), line });
  }

  // ---------------------------------------------------------------- estaciones
  for (const st of net.stationList) {
    const marker = L.circleMarker([st.lat, st.lon], { renderer: stationRenderer, bubblingMouseEvents: false });
    const codes = st.lines
      .map((l) => net.lineById.get(l.line))
      .map((l, i) => `<span class="badge" style="--c:${l.color};--t:${textOn(l.color)}">${esc(st.lines[i].code || l.code)}</span>`)
      .join("");
    marker.bindTooltip(`<strong>${esc(st.name)}</strong> <span class="ja">${esc(st.ja)}</span><div class="tip-codes">${codes}</div>`,
      { className: "map-tip", direction: "top", offset: [0, -6] });
    marker.on("click", () => onStation(st.id));
    stationMarkers.set(st.id, marker);
  }

  // ---------------------------------------------------------------- render
  const visibleLine = (line) => !state.hiddenOps.has(line.operator);

  function styleLines() {
    const w = weight();
    const focusSet = focusedLineSet();
    for (const [id, { casing, stroke, line }] of lineLayers) {
      const show = visibleLine(line);
      for (const layer of [casing, stroke]) {
        if (show && !map.hasLayer(layer)) layer.addTo(map);
        if (!show && map.hasLayer(layer)) layer.remove();
      }
      if (!show) continue;
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

  function focusedLineSet() {
    if (state.focusLine) return new Set([state.focusLine]);
    if (state.focusStation) return new Set(net.stations[state.focusStation].lineIds);
    return null;
  }

  function styleStations() {
    const z = map.getZoom();
    const focusSet = focusedLineSet();
    const dark = theme() === "dark";
    stationLayer.clearLayers();
    labelLayer.clearLayers();
    for (const st of net.stationList) {
      const lines = st.lineIds.filter((id) => visibleLine(net.lineById.get(id)));
      if (!lines.length) continue;
      const inFocus = focusSet ? lines.some((id) => focusSet.has(id)) : true;
      if (focusSet && !inFocus) continue;
      if (!focusSet && z < STATION_MIN_ZOOM && lines.length < 3) continue;
      const hub = lines.length > 1;
      const first = net.lineById.get(state.focusLine || lines[0]);
      const m = stationMarkers.get(st.id);
      m.setStyle({
        radius: (hub ? 5 : 3.5) + (z >= 15 ? 1.5 : 0),
        weight: 2,
        color: hub ? (dark ? "#f2f2f2" : "#1a1a1a") : first.color,
        fillColor: dark ? "#1d2027" : "#ffffff",
        fillOpacity: 1,
      });
      stationLayer.addLayer(m);
      if (state.focusLine && z >= LABEL_MIN_ZOOM) {
        labelLayer.addLayer(L.tooltip({ permanent: true, direction: "right", offset: [6, 0], className: "stn-label", pane: "labels", interactive: false })
          .setLatLng([st.lat, st.lon]).setContent(esc(st.name)));
      }
    }
  }

  function render() { styleLines(); styleStations(); }

  map.on("zoomend", render);
  darkQuery.addEventListener("change", () => { tiles.setUrl(TILE(theme())); render(); });

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
      state.focusLine = state.focusStation = null;
      setPulse(null);
      render();
      if (fit) map.flyToBounds(visibleBounds(), { padding: pad(), duration: 0.6 });
    },
    focusLine(id) {
      state.focusLine = id;
      state.focusStation = null;
      setPulse(null);
      render();
      const l = lineLayers.get(id);
      if (l) map.flyToBounds(l.bounds, { padding: pad(), duration: 0.6 });
    },
    focusStation(id) {
      const st = net.stations[id];
      if (!st) return;
      state.focusLine = null;
      state.focusStation = id;
      render();
      setPulse(st);
      map.flyTo([st.lat, st.lon], Math.max(map.getZoom(), 14.5), { duration: 0.6 });
    },
    setHiddenOperators(set) {
      state.hiddenOps = new Set(set);
      render();
    },
    invalidate() { map.invalidateSize(); },
  };

  function visibleBounds() {
    const b = L.latLngBounds([]);
    for (const { bounds, line } of lineLayers.values()) if (visibleLine(line)) b.extend(bounds);
    return b.isValid() ? b : L.latLngBounds([[35.6, 139.6], [35.8, 139.9]]);
  }

  render();
  return api;
}
