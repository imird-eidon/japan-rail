// Carga de network.json, índices y consultas sobre la red.

export async function loadNetwork(url = "data/network.json") {
  const res = await fetch(url, { cache: "no-cache" });
  if (!res.ok) throw new Error(`No se pudo cargar ${url} (HTTP ${res.status})`);
  const net = await res.json();
  buildIndexes(net);
  return net;
}

function buildIndexes(net) {
  net.lineById = new Map(net.lines.map((l) => [l.id, l]));
  net.trainById = new Map(net.trains.map((t) => [t.id, t]));
  net.stationList = Object.values(net.stations);

  // grupos del mapa y de la lista = regiones (Shinkansen, Tokio, Kioto…), en el orden de lines.json
  const used = new Set(net.lines.map(groupOf));
  const order = [...Object.keys(net.regions || {}), ...used];  // primero el orden de lines.json → regions
  net.groups = [...new Set(order)].filter((id) => used.has(id))
    .map((id) => ({ id, ...(net.regions?.[id] || { name: id }) }));

  // build_data.py ya calcula t.lines y st.trains; esto es solo por si faltan
  for (const t of net.trains) t.lines ??= [];
  for (const s of net.stationList) s.trains ??= [];
  for (const s of net.stationList) {
    s.lineIds = s.lines.map((l) => l.line);
    s._search = norm(`${s.name} ${s.ja} ${s.lines.map((l) => l.code || "").join(" ")}`);
  }
  for (const l of net.lines) l._search = norm(`${l.name} ${l.en} ${l.ja} ${l.code} ${l.id}`);
  for (const t of net.trains) t._search = norm(`${t.name} ${t.id}`);
}

export const isShinkansen = (line) => line.type === "shinkansen" || line.type === "mini-shinkansen";
/** Grupo (región) de una línea para filtros y listados: "japan" (Shinkansen), "tokyo", "kyoto"… */
export const groupOf = (line) => line.region || (isShinkansen(line) ? "japan" : "tokyo");
/** Región principal de un tren: la de su primera línea actual (o histórica). */
export const trainRegion = (net, t) => {
  const id = t.lines[0] || t.history?.[0]?.line;
  return id ? groupOf(net.lineById.get(id)) : null;
};

/** Minúsculas y sin acentos/macrones, para comparar textos. */
export const norm = (s) =>
  String(s ?? "").normalize("NFKD").replace(/[̀-ͯ]/g, "").toLowerCase();

export const esc = (s) =>
  String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

/** Color de texto legible (negro o blanco) sobre un color de línea. */
export function textOn(hex) {
  const n = parseInt(hex.replace("#", ""), 16);
  const [r, g, b] = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map((v) => {
    v /= 255;
    return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  });
  const L = 0.2126 * r + 0.7152 * g + 0.0722 * b;
  return L > 0.4 ? "#111" : "#fff";
}

/** Estación anterior y siguiente de `stationId` en `line`. */
export function neighbours(line, stationId) {
  const i = line.stations.indexOf(stationId);
  if (i < 0) return {};
  const n = line.stations.length;
  const prev = i > 0 ? line.stations[i - 1] : line.loop ? line.stations[n - 1] : null;
  const next = i < n - 1 ? line.stations[i + 1] : line.loop ? line.stations[0] : null;
  return { prev, next };
}

/** Todos los datos curiosos, con la entidad a la que pertenecen. */
export function allFacts(net) {
  const out = [];
  for (const l of net.lines) for (const f of l.facts || []) out.push({ text: f, type: "line", id: l.id, label: l.name });
  for (const s of net.stationList) for (const f of s.facts || []) out.push({ text: f, type: "station", id: s.id, label: s.name });
  for (const t of net.trains) for (const f of t.facts || []) out.push({ text: f, type: "train", id: t.id, label: t.name });
  return out;
}

export function search(net, query, limit = 8) {
  const q = norm(query).trim();
  if (!q) return [];
  const score = (hay, name) => {
    const n = norm(name);
    if (n === q) return 0;
    if (n.startsWith(q)) return 1;
    if (hay.includes(q)) return 2;
    return -1;
  };
  const results = [];
  for (const l of net.lines) {
    const sc = score(l._search, l.name);
    if (sc >= 0 || norm(l.code) === q) results.push({ type: "line", item: l, sc: norm(l.code) === q ? -1 : sc });
  }
  for (const s of net.stationList) {
    const sc = Math.min(...[s.name, s.ja].map((n) => score(s._search, n)).filter((x) => x >= 0), 9);
    if (sc < 9) results.push({ type: "station", item: s, sc: sc - s.lines.length * 0.01 });
  }
  for (const t of net.trains) {
    const sc = score(t._search, t.name);
    if (sc >= 0) results.push({ type: "train", item: t, sc: sc + 0.5 });
  }
  return results.sort((a, b) => a.sc - b.sc).slice(0, limit);
}

export function networkStats(net) {
  const km = net.lines.reduce((a, l) => a + (l.length_km || l.drawn_km || 0), 0);
  const oldest = net.lines.reduce((a, l) => (l.opened < a.opened ? l : a));
  const busiest = net.stationList.reduce((a, s) => (s.lines.length > a.lines.length ? s : a));
  return { lines: net.lines.length, stations: net.stationList.length, km: Math.round(km), oldest, busiest };
}
