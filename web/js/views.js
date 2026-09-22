// Vistas del panel lateral. Cada función devuelve HTML (texto siempre escapado con esc).
import { esc, textOn, neighbours, networkStats, groupOf, trainRegion } from "./data.js";

const fmtKm = (n) => `${String(n).replace(".", ",")}<small> km</small>`;

/** Icono de tren (SVG en línea, usa currentColor). */
export const trainIcon = (size = 20) =>
  `<svg class="train-svg" width="${size}" height="${size}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 10h14M9 21l-2 -3M15 21l2 -3"/><circle cx="9" cy="14" r=".6" fill="currentColor"/><circle cx="15" cy="14" r=".6" fill="currentColor"/></svg>`;

export const badge = (line, text = line.code) =>
  `<span class="badge" style="--c:${line.color};--t:${textOn(line.color)}">${esc(text)}</span>`;

/** Cartel de numeración de estación al estilo japonés: letra(s) de línea + número. */
export const stationCode = (line, code) => {
  const m = /^([A-Z]+)(\d+)$/.exec(code || "");
  return m
    ? `<span class="stn-code" style="--c:${line.color}" title="${esc(line.name)}"><b>${esc(m[1])}</b>${esc(m[2])}</span>`
    : badge(line);
};

const link = (type, id, html, cls = "") => `<a href="#/${type}/${encodeURIComponent(id)}" class="${cls}">${html}</a>`;

const back = `<a href="#/" class="back" aria-label="Volver al inicio">← Inicio</a>`;

const factList = (facts) =>
  facts?.length ? `<h3>Datos curiosos</h3><ul class="facts">${facts.map((f) => `<li>${esc(f)}</li>`).join("")}</ul>` : "";

// ------------------------------------------------------------------ inicio
export function homeView(net, { tab, hidden, fact }) {
  const st = networkStats(net);
  const tabs = [["lines", "Líneas"], ["stations", "Estaciones"], ["trains", "Trenes"]];

  let body = "";
  if (tab === "stations") body = stationsTab(net);
  else if (tab === "trains") body = trainsTab(net);
  else body = linesTab(net, hidden);

  return `
    <section class="intro">
      <h1>Los trenes de Japón</h1>
      <p>La red Shinkansen y, con todo detalle, el tren y el metro de Tokio y Kioto. Toca una línea en el mapa o elige una de la lista.</p>
      <dl class="stats">
        <div><dt>Líneas</dt><dd>${st.lines}</dd></div>
        <div><dt>Estaciones</dt><dd>${st.stations}</dd></div>
        <div><dt>Km de red</dt><dd>${st.km}</dd></div>
      </dl>
    </section>

    ${fact ? factCard(fact) : ""}

    <nav class="tabs" role="tablist">
      ${tabs.map(([id, label]) => `<a role="tab" href="#/${id === "lines" ? "" : id}" aria-selected="${tab === id}" class="tab">${label}</a>`).join("")}
    </nav>
    ${body}`;
}

function factCard(f) {
  return `
    <aside class="fact-card">
      <div class="fact-head"><span>¿Sabías que…?</span><button type="button" class="ghost" data-action="next-fact">Otro dato ↻</button></div>
      <p>${esc(f.text)}</p>
      ${link(f.type, f.id, `${esc(f.label)} →`, "fact-link")}
    </aside>`;
}

function linesTab(net, hidden) {
  const chips = net.groups.map((g) => `
      <button type="button" class="chip" data-action="toggle-group" data-group="${esc(g.id)}" aria-pressed="${!hidden.has(g.id)}">${esc(g.name)}</button>`).join("");
  const lineRow = (l) => `
          <li>${link("line", l.id, `
            ${badge(l)}
            <span class="ll-name">${esc(l.name)}<span class="ja">${esc(l.ja)}</span></span>
            <span class="ll-meta">${l.stations.length} est. · ${fmtKm(l.length_km ?? l.drawn_km)}</span>`, "line-row")}</li>`;
  const groups = net.groups.map((g) => {
    const lines = net.lines.filter((l) => groupOf(l) === g.id);
    const ops = [...new Set(lines.map((l) => l.operator))];
    // Shinkansen: una sola lista; ciudades: subgrupos por operador
    const body = g.id === "japan"
      ? `<ul class="line-list">${lines.map(lineRow).join("")}</ul>`
      : ops.map((op) => `
        <h3 class="op-title">${esc(net.operators[op]?.name || op)} <span class="ja">${esc(net.operators[op]?.ja || "")}</span></h3>
        <ul class="line-list">${lines.filter((l) => l.operator === op).map(lineRow).join("")}</ul>`).join("");
    return `
      <section class="group ${hidden.has(g.id) ? "is-hidden" : ""}" data-group="${esc(g.id)}">
        <h2 class="region-title">${esc(g.name)} <span class="ja">${esc(g.ja || "")}</span></h2>
        ${body}
      </section>`;
  }).join("");
  return `<div class="chips" aria-label="Mostrar u ocultar regiones">${chips}</div>${groups}`;
}

function stationsTab(net) {
  const hubs = [...net.stationList].sort((a, b) => b.lines.length - a.lines.length || a.name.localeCompare(b.name)).slice(0, 12);
  const all = [...net.stationList].sort((a, b) => a.name.localeCompare(b.name));
  const row = (s) => link("station", s.id, `
      <span class="st-name">${esc(s.name)} <span class="ja">${esc(s.ja)}</span></span>
      <span class="st-lines">${s.lines.map((x) => dot(net.lineById.get(x.line))).join("")}</span>`, "station-row");
  return `
    <h2 class="group-title">Grandes nudos</h2>
    <ul class="station-list">${hubs.map((s) => `<li>${row(s)}</li>`).join("")}</ul>
    <h2 class="group-title">Todas las estaciones (${all.length})</h2>
    <ul class="station-list">${all.map((s) => `<li>${row(s)}</li>`).join("")}</ul>`;
}

/** Miniatura de la foto del tren o, si no hay, el icono. */
const trainThumb = (t, cls = "thumb") =>
  t.photo ? `<img class="${cls}" src="${esc(t.photo.thumb || t.photo.src)}" alt="" loading="lazy" decoding="async">`
          : `<span class="${cls} no-photo">${trainIcon(cls === "thumb" ? 18 : 28)}</span>`;

/** Años en una línea: «1963–1988», «hasta 1986», «desde 1954» (cuando solo se conoce uno). */
const yearsText = ([a, b] = []) => (a && b ? `${a}–${b}` : b ? `hasta ${b}` : a ? `desde ${a}` : "");
/** Años de servicio de un tren en su conjunto (1963–1988, o «desde 2015»). */
const serviceText = (t) => (t.retired ? `${t.introduced}–${t.retired}` : t.introduced ? `desde ${t.introduced}` : "en servicio");

/**
 * Tarjetas de trenes (foto + nombre).
 * meta(t) permite cambiar el texto de debajo (p. ej. los años en una línea concreta).
 */
function trainCards(net, ids, { meta, historic = false } = {}) {
  const trains = ids.map((id) => net.trainById.get(id)).filter(Boolean);
  if (!trains.length) return "";
  return `<ul class="train-cards ${historic ? "is-historic" : ""}">${trains.map((t) => `<li>${link("train", t.id, `
      ${trainThumb(t, "card-img")}
      <span class="card-name">${esc(t.name)}</span>
      <span class="card-meta">${meta ? meta(t) : `${esc(net.operators[t.operator]?.name || "")} · ${serviceText(t)}`}</span>`, "train-card")}</li>`).join("")}</ul>`;
}

/** Trenes que circularon por una línea, del más antiguo al más reciente, con sus años. */
function historicOnLine(net, lineId) {
  const rows = net.trains
    .map((t) => ({ t, h: (t.history || []).find((h) => h.line === lineId) }))
    .filter((x) => x.h)
    .sort((a, b) => (a.h.years[0] || a.t.introduced) - (b.h.years[0] || b.t.introduced));
  return trainCards(net, rows.map((x) => x.t.id), {
    historic: true,
    meta: (t) => yearsText(rows.find((x) => x.t === t).h.years),
  });
}

const dot = (l) => `<span class="dot" style="--c:${l.color}" title="${esc(l.name)}"></span>`;

function trainsTab(net) {
  const row = (t) => `
    <li>${link("train", t.id, `
      ${trainThumb(t)}
      <span class="tr-name">${esc(t.name)}<span class="tr-meta">${esc(net.operators[t.operator]?.name || "")} · ${serviceText(t)}</span></span>
      <span class="tr-lines">${(t.lines.length ? t.lines : (t.history || []).map((h) => h.line))
        .map((id) => badge(net.lineById.get(id))).join("")}</span>`, "train-row")}</li>`;
  const current = net.trains.filter((t) => t.lines.length);
  const retired = net.trains.filter((t) => !t.lines.length).sort((a, b) => (a.introduced || 0) - (b.introduced || 0));
  const sections = net.groups.map((g) => {
    const list = current.filter((t) => trainRegion(net, t) === g.id);
    if (!list.length) return "";
    const title = g.id === "japan" ? "Shinkansen" : `Tren y metro de ${g.name}`;
    return `<h2 class="group-title">${esc(title)} <span class="ja">${esc(g.ja || "")}</span></h2>
      <ul class="train-list">${list.map(row).join("")}</ul>`;
  }).join("");
  return `${sections}
    <h2 class="group-title">Históricos <span class="ja">引退車両</span></h2>
    <p class="muted group-note">Series que ya no circulan por estas líneas (algunas siguen en otras partes de Japón o del mundo).</p>
    <ul class="train-list">${retired.map(row).join("")}</ul>`;
}

// ------------------------------------------------------------------ línea
export function lineView(net, line) {
  const op = net.operators[line.operator];
  const codeOf = (st) => st.lines.find((x) => x.line === line.id)?.code;
  const stops = line.stations.map((id) => net.stations[id]).map((s) => {
    const others = s.lines.filter((x) => x.line !== line.id).map((x) => net.lineById.get(x.line));
    return `
      <li>
        ${link("station", s.id, `
          <span class="rs-code">${codeOf(s) ? stationCode(line, codeOf(s)) : ""}</span>
          <span class="rs-name">${esc(s.name)} <span class="ja">${esc(s.ja)}</span></span>
          <span class="rs-xfer">${others.map((o) => badge(o)).join("")}</span>`, "route-stop")}
      </li>`;
  }).join("");

  const trains = net.trains.filter((t) => t.lines.includes(line.id));
  let hist;
  return `
    ${back}
    <header class="entity-head" style="--c:${line.color}">
      ${badge(line)}
      <div>
        <h1>${esc(line.name)}</h1>
        <p class="sub"><span class="ja">${esc(line.ja)}</span> · ${esc(op?.name || "")} · ${esc(net.types[line.type] || line.type)}</p>
      </div>
    </header>
    ${line.summary ? `<p class="summary">${esc(line.summary)}</p>` : ""}
    <dl class="stats">
      <div><dt>Longitud</dt><dd>${fmtKm(line.length_km ?? line.drawn_km)}</dd></div>
      <div><dt>Estaciones</dt><dd>${line.stations.length}</dd></div>
      <div><dt>Desde</dt><dd>${line.opened ?? "—"}</dd></div>
    </dl>
    ${factList(line.facts)}
    ${trains.length ? `<h3>Trenes actuales</h3>${trainCards(net, trains.map((t) => t.id))}` : ""}
    ${(hist = historicOnLine(net, line.id)) ? `<h3>Trenes históricos</h3>${hist}` : ""}
    <h3>Recorrido${line.loop ? " (circular ↻)" : ""}</h3>
    <ol class="route ${line.loop ? "is-loop" : ""}" style="--c:${line.color}">${stops}</ol>
    <p class="source">Trazado: ${line.osm.map((id) => `<a href="https://www.openstreetmap.org/relation/${id}" target="_blank" rel="noopener">OSM ${id}</a>`).join(", ")}</p>`;
}

// ------------------------------------------------------------------ estación
export function stationView(net, st) {
  // un cartel por código (las líneas JR Kyōto y JR Kōbe comparten «A47» en Ōsaka, por ejemplo)
  const seen = new Set();
  const codes = st.lines.filter((x) => !x.code || !seen.has(x.code) && seen.add(x.code))
    .map((x) => stationCode(net.lineById.get(x.line), x.code)).join("");
  const rows = st.lines.map((x) => {
    const line = net.lineById.get(x.line);
    const { prev, next } = neighbours(line, st.id);
    const nb = (id, arrow) => (id ? link("station", id, arrow === "←" ? `← ${esc(net.stations[id].name)}` : `${esc(net.stations[id].name)} →`, "nb") : `<span class="nb end">fin de línea</span>`);
    return `
      <li class="serving">
        ${link("line", line.id, `${badge(line)} <span>${esc(line.name)}</span>`, "serving-line")}
        <div class="nbs">${nb(prev, "←")}${nb(next, "→")}</div>
      </li>`;
  }).join("");
  const near = (st.nearby || []).map((n) => {
    const o = net.stations[n.station];
    return `<li>${link("station", o.id, `<span>${esc(o.name)} <span class="ja">${esc(o.ja)}</span></span><span class="muted">${n.m} m a pie · ${o.lines.map((x) => dot(net.lineById.get(x.line))).join("")}</span>`, "station-row")}</li>`;
  }).join("");

  return `
    ${back}
    <header class="entity-head station">
      <div class="codes">${codes}</div>
      <div>
        <h1>${esc(st.name)}</h1>
        <p class="sub"><span class="ja big">${esc(st.ja)}</span></p>
      </div>
    </header>
    ${st.summary ? `<p class="summary">${esc(st.summary)}</p>` : ""}
    <h3>${st.lines.length === 1 ? "Línea" : `${st.lines.length} líneas`}</h3>
    <ul class="serving-list">${rows}</ul>
    ${st.trains?.length ? `<h3>Trenes que pasan por aquí</h3>${trainCards(net, st.trains)}` : ""}
    ${st.past_trains?.length ? `<details class="more"><summary>Trenes históricos de sus líneas (${st.past_trains.length})</summary>
      ${trainCards(net, [...st.past_trains].sort((a, b) => net.trainById.get(a).introduced - net.trainById.get(b).introduced), { historic: true })}</details>` : ""}
    ${factList(st.facts)}
    ${near ? `<h3>Transbordo a pie</h3><ul class="station-list">${near}</ul>` : ""}
    <p class="source"><a href="https://www.openstreetmap.org/?mlat=${st.lat}&mlon=${st.lon}#map=17/${st.lat}/${st.lon}" target="_blank" rel="noopener">Ver en OpenStreetMap ↗</a></p>`;
}

// ------------------------------------------------------------------ tren
export function trainView(net, t) {
  const op = net.operators[t.operator];
  const p = t.photo;
  const runs = (t.runs || []).map((r) => {
    const l = net.lineById.get(r.line);
    const span = r.from ? `${esc(net.stations[r.from].name)} – ${esc(net.stations[r.to].name)}` : "toda la línea";
    return `<li>${link("line", l.id, `${badge(l)}<span class="ll-name">${esc(l.name)}<span class="ja">${span}</span></span>`, "line-row")}</li>`;
  }).join("");
  const nStations = net.stationList.filter((s) => s.trains?.includes(t.id)).length;
  const past = (t.history || []).map((h) => {
    const l = net.lineById.get(h.line);
    const span = h.from ? ` · ${esc(net.stations[h.from].name)} – ${esc(net.stations[h.to].name)}` : "";
    return `<li>${link("line", l.id, `${badge(l)}<span class="ll-name">${esc(l.name)}<span class="ja">${yearsText(h.years)}${span}</span></span>`, "line-row")}</li>`;
  }).join("");
  return `
    ${back}
    ${p ? `
    <figure class="photo">
      <img src="${esc(p.src)}" alt="${esc(t.name)}" decoding="async">
      <figcaption>Foto: ${esc(p.author)} ·
        ${p.license_url ? `<a href="${esc(p.license_url)}" target="_blank" rel="noopener">${esc(p.license)}</a>` : esc(p.license)} ·
        <a href="${esc(p.source)}" target="_blank" rel="noopener">Wikimedia Commons</a></figcaption>
    </figure>` : ""}
    <header class="entity-head">
      ${p ? "" : `<span class="train-icon">${trainIcon(34)}</span>`}
      <div>
        <h1>${esc(t.name)}</h1>
        <p class="sub">${esc(op?.name || "")}${t.retired ? ` · <span class="tag">Retirado en ${t.retired}</span>` : !t.lines.length ? ` · <span class="tag">Histórico</span>` : ""}</p>
      </div>
    </header>
    ${t.summary ? `<p class="summary">${esc(t.summary)}</p>` : ""}
    <dl class="stats">
      ${t.introduced ? `<div><dt>${t.retired ? "En servicio" : "Desde"}</dt><dd>${t.retired ? `${t.introduced}<small>–${t.retired}</small>` : t.introduced}</dd></div>` : ""}
      ${t.cars ? `<div><dt>Coches</dt><dd>${t.cars}</dd></div>` : ""}
      ${nStations ? `<div><dt>Estaciones</dt><dd>${nStations}</dd></div>` : ""}
      ${t.builder ? `<div class="wide"><dt>Fabricante</dt><dd class="small">${esc(t.builder)}</dd></div>` : ""}
    </dl>
    ${factList(t.facts)}
    ${runs ? `<h3>Circula por</h3><ul class="line-list">${runs}</ul>` : ""}
    ${past ? `<h3>Circuló por</h3><ul class="line-list">${past}</ul>` : ""}`;
}

export function notFoundView(what) {
  return `${back}<p class="empty">No encuentro ${esc(what)}. Puede que el enlace sea antiguo.</p>`;
}
