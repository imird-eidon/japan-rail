// Punto de entrada: carga datos, crea el mapa y enruta por el hash de la URL.
//   #/                 inicio (líneas)      #/stations  #/trains
//   #/line/<id>        #/station/<id>       #/train/<id>
import { loadNetwork, allFacts, search, esc } from "./data.js";
import { createMap } from "./map.js";
import { homeView, lineView, stationView, trainView, notFoundView, badge, trainIcon } from "./views.js";

const panel = document.getElementById("panel");
const input = document.getElementById("search");
const results = document.getElementById("search-results");

const HIDDEN_KEY = "jre.hiddenRegions";
const ui = {
  hidden: new Set(readStored(HIDDEN_KEY, [])),
  facts: [],
  factIndex: 0,
};

function readStored(key, fallback) {
  try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; }
}
function store(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* sin almacenamiento: no pasa nada */ }
}

const go = (hash) => { if (location.hash !== hash) location.hash = hash; else route(); };

let net, map;
const scrollMemory = new Map();   // hash → posición de scroll del panel
let lastHash = null;

async function main() {
  try {
    net = await loadNetwork();
  } catch (err) {
    panel.innerHTML = `<p class="empty">No se pudieron cargar los datos: ${esc(err.message)}</p>`;
    console.error(err);
    return;
  }
  ui.facts = shuffle(allFacts(net));
  map = createMap(document.getElementById("map"), net, {
    onLine: (id) => go(id ? `#/line/${id}` : "#/"),
    onStation: (id) => go(`#/station/${id}`),
  });
  map.setHidden(ui.hidden);
  window.addEventListener("hashchange", route);
  route({ initial: true });
}

// ------------------------------------------------------------------ router
function route({ initial = false } = {}) {
  const [, type, rawId] = location.hash.split("/");
  const id = rawId && decodeURIComponent(rawId);
  let html;

  if (type === "line") {
    const line = net.lineById.get(id);
    html = line ? lineView(net, line) : notFoundView("esa línea");
    if (line) { map.focusLine(line.id, { animate: !initial }); document.title = `${line.name} · Japan Rail Explorer`; }
  } else if (type === "station") {
    const st = net.stations[id];
    html = st ? stationView(net, st) : notFoundView("esa estación");
    if (st) { map.focusStation(st.id, { animate: !initial }); document.title = `${st.name} ${st.ja} · Japan Rail Explorer`; }
  } else if (type === "train") {
    const t = net.trainById.get(id);
    html = t ? trainView(net, t) : notFoundView("ese tren");
    if (t) { map.focusLines(t.lines.length ? t.lines : (t.history || []).map((h) => h.line), { animate: !initial }); document.title = `${t.name} · Japan Rail Explorer`; }
  } else {
    const tab = ["stations", "trains"].includes(type) ? type : "lines";
    html = homeView(net, { tab, hidden: ui.hidden, fact: ui.facts[ui.factIndex % ui.facts.length] });
    map.overview({ fit: initial });
    document.title = "Japan Rail Explorer";
  }

  if (lastHash !== null) scrollMemory.set(lastHash, panel.scrollTop);
  lastHash = location.hash;
  panel.innerHTML = `<div class="view">${html}</div>`;
  // al volver a una vista ya visitada se recupera la posición; a una nueva, se empieza arriba
  panel.scrollTop = scrollMemory.get(lastHash) ?? 0;
  if (!initial) panel.focus({ preventScroll: true });
}

// ------------------------------------------------------------------ acciones del panel
panel.addEventListener("click", (e) => {
  const btn = e.target.closest("[data-action]");
  if (!btn) return;
  if (btn.dataset.action === "next-fact") {
    ui.factIndex++;
    const card = panel.querySelector(".fact-card");
    const tmp = document.createElement("div");
    tmp.innerHTML = homeView(net, { tab: "lines", hidden: ui.hidden, fact: ui.facts[ui.factIndex % ui.facts.length] });
    card?.replaceWith(tmp.querySelector(".fact-card"));
  } else if (btn.dataset.action === "toggle-group") {
    const g = btn.dataset.group;
    if (ui.hidden.has(g)) ui.hidden.delete(g); else ui.hidden.add(g);
    store(HIDDEN_KEY, [...ui.hidden]);
    map.setHidden(ui.hidden);
    btn.setAttribute("aria-pressed", String(!ui.hidden.has(g)));
    panel.querySelector(`.group[data-group="${CSS.escape(g)}"]`)?.classList.toggle("is-hidden", ui.hidden.has(g));
  }
});

// ------------------------------------------------------------------ buscador
let current = [];
let active = -1;

function renderResults() {
  const open = current.length > 0;
  results.hidden = !open;
  input.setAttribute("aria-expanded", String(open));
  results.innerHTML = current.map((r, i) => {
    const { type, item } = r;
    const label = { line: "Línea", station: "Estación", train: "Tren" }[type];
    const lead = type === "line" ? badge(item)
      : type === "station" ? item.lines.slice(0, 4).map((x) => `<span class="dot" style="--c:${net.lineById.get(x.line).color}"></span>`).join("")
      : `<span class="tr-ico">${trainIcon(18)}</span>`;
    return `<li role="option" id="sr-${i}" aria-selected="${i === active}" data-href="#/${type}/${encodeURIComponent(item.id)}">
      <span class="sr-lead">${lead}</span>
      <span class="sr-name">${esc(item.name)} ${item.ja ? `<span class="ja">${esc(item.ja)}</span>` : ""}</span>
      <span class="sr-type">${label}</span></li>`;
  }).join("");
}

function closeResults() { current = []; active = -1; renderResults(); }

input.addEventListener("input", () => {
  if (!net) return;
  current = search(net, input.value);
  active = current.length ? 0 : -1;
  renderResults();
});
input.addEventListener("keydown", (e) => {
  if (e.key === "ArrowDown" || e.key === "ArrowUp") {
    if (!current.length) return;
    e.preventDefault();
    active = (active + (e.key === "ArrowDown" ? 1 : -1) + current.length) % current.length;
    renderResults();
  } else if (e.key === "Enter" && active >= 0) {
    e.preventDefault();
    const r = current[active];
    go(`#/${r.type}/${r.item.id}`);
    input.value = "";
    closeResults();
    input.blur();
  } else if (e.key === "Escape") {
    input.value = "";
    closeResults();
  }
});
results.addEventListener("mousedown", (e) => {
  const li = e.target.closest("li[data-href]");
  if (!li) return;
  e.preventDefault();
  go(li.dataset.href);
  input.value = "";
  closeResults();
});
input.addEventListener("blur", () => setTimeout(closeResults, 120));
document.addEventListener("keydown", (e) => {
  if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
});

function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

main();
