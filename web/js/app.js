// Punto de entrada: carga datos, crea el mapa y enruta por el hash de la URL.
//   #/                 inicio (líneas)      #/stations  #/trains  #/fotos
//   #/line/<id>        #/station/<id>       #/train/<id>
import { loadNetwork, allFacts, search, esc } from "./data.js";
import { createMap } from "./map.js";
import { homeView, lineView, stationView, trainView, notFoundView, badge, trainIcon, allStations, stationRows,
         galleryView, galleryGrid, galleryCount, filterPhotos, photoLightbox } from "./views.js";

const panel = document.getElementById("panel");
const input = document.getElementById("search");
const results = document.getElementById("search-results");

const HIDDEN_KEY = "jre.hiddenRegions";
const ui = {
  hidden: new Set(readStored(HIDDEN_KEY, [])),
  facts: [],
  factIndex: 0,
  gallery: { q: "", region: null },   // filtros de la galería de fotos
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
let mapFocused = false;           // ¿el mapa está centrado en una línea/estación/tren?

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
    if (line) { mapFocused = true; map.focusLine(line.id, { animate: !initial }); document.title = `${line.name} · Japan Rail Explorer`; }
  } else if (type === "station") {
    const st = net.stations[id];
    html = st ? stationView(net, st) : notFoundView("esa estación");
    if (st) { mapFocused = true; map.focusStation(st.id, { animate: !initial }); document.title = `${st.name} ${st.ja} · Japan Rail Explorer`; }
  } else if (type === "train") {
    const t = net.trainById.get(id);
    html = t ? trainView(net, t) : notFoundView("ese tren");
    if (t) { mapFocused = true; map.focusLines(t.lines.length ? t.lines : (t.history || []).map((h) => h.line), { animate: !initial }); document.title = `${t.name} · Japan Rail Explorer`; }
  } else {
    const tab = ["stations", "trains"].includes(type) ? type : "lines";
    html = homeView(net, { tab, hidden: ui.hidden, fact: ui.facts[ui.factIndex % ui.facts.length] });
    if (initial || mapFocused) map.overview({ fit: initial });   // entre pestañas el mapa no cambia
    mapFocused = false;
    document.title = "Japan Rail Explorer";
  }

  // la galería es una capa aparte: se abre encima de todo y al salir devuelve la vista de antes
  if (type === "fotos") abrirGaleria(); else cerrarGaleria();

  if (type === "fotos" && panel.querySelector(".intro")) return;   // el panel ya está en la portada

  if (lastHash !== null) scrollMemory.set(lastHash, panel.scrollTop);
  lastHash = location.hash;
  panel.innerHTML = `<div class="view">${html}</div>`;
  lazyImages();
  // al volver a una vista ya visitada se recupera la posición; a una nueva, se empieza arriba
  panel.scrollTop = scrollMemory.get(lastHash) ?? 0;
  if (!initial) panel.focus({ preventScroll: true });
}

// Las fotos se piden solo cuando se acercan al hueco visible: la lista de trenes tiene
// casi doscientas miniaturas y cargarlas de golpe bloqueaba la pestaña.
const watchers = new WeakMap();   // contenedor con scroll → su observador

function watcherFor(root) {
  if (!("IntersectionObserver" in window)) return null;
  let obs = watchers.get(root);
  if (!obs) {
    obs = new IntersectionObserver((entries, o) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        const img = e.target;
        img.src = img.dataset.src;
        img.removeAttribute("data-src");
        o.unobserve(img);
      }
    }, { root, rootMargin: "400px 0px" });
    watchers.set(root, obs);
  }
  return obs;
}

function lazyImages(box = panel, root = panel) {
  const pending = box.querySelectorAll("img[data-src]");
  const obs = watcherFor(root);
  if (!obs) {   // navegador sin soporte: se cargan todas, como antes
    for (const img of pending) { img.src = img.dataset.src; img.removeAttribute("data-src"); }
    return;
  }
  for (const img of pending) obs.observe(img);
}

// La lista completa de estaciones (más de cuatro mil filas) solo se pinta si se pide:
// crearlas cuesta, pero sobre todo cuesta destruirlas al cambiar de pestaña.
function verTodasLasEstaciones(btn) {
  const ul = panel.querySelector("#all-stations");
  if (!ul) return;
  const list = allStations(net);
  let from = Number(btn.dataset.from) || 0;
  btn.remove();
  const idle = window.requestIdleCallback || ((fn) => setTimeout(fn, 16));
  const step = () => {
    if (!ul.isConnected || from >= list.length) return;
    ul.insertAdjacentHTML("beforeend", stationRows(net, list, from, 500));
    from += 500;
    lazyImages();
    idle(step);
  };
  idle(step);
}

// ------------------------------------------------------------------ acciones del panel
panel.addEventListener("click", (e) => {
  const btn = e.target.closest("[data-action]");
  if (!btn) return;
  if (btn.dataset.action === "ver-todas") {
    verTodasLasEstaciones(btn);
  } else if (btn.dataset.action === "next-fact") {
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

// ------------------------------------------------------------------ galería de fotos
// Capa a pantalla completa por encima del mapa y del panel. Se abre con #/fotos.
let galeria = null, lightbox = null, fotos = [], fotoIndex = 0;

function abrirGaleria() {
  if (!galeria) {
    galeria = document.createElement("div");
    galeria.className = "gal";
    galeria.setAttribute("role", "dialog");
    galeria.setAttribute("aria-modal", "true");
    galeria.setAttribute("aria-label", "Galería de fotos");
    galeria.addEventListener("click", clicGaleria);
    galeria.addEventListener("input", (e) => {
      if (!e.target.matches(".gal-q")) return;
      ui.gallery.q = e.target.value;
      clearTimeout(galeria._timer);
      galeria._timer = setTimeout(repintarMosaico, 120);   // esperar a que pare de escribir
    });
    document.body.appendChild(galeria);
  }
  galeria.innerHTML = galleryView(net, ui.gallery);
  document.body.classList.add("con-galeria");
  const scroll = galeria.querySelector(".gal-scroll");
  lazyImages(galeria, scroll);
  if (!matchMedia("(max-width: 820px)").matches) galeria.querySelector(".gal-q")?.focus();
  document.title = "Galería · Japan Rail Explorer";
}

function cerrarGaleria() {
  if (!galeria) return;
  cerrarFoto();
  galeria.remove();
  galeria = null;
  document.body.classList.remove("con-galeria");
}

function clicGaleria(e) {
  const btn = e.target.closest("[data-photo], [data-gallery-region]");
  if (!btn) return;
  if (btn.dataset.photo !== undefined) {
    abrirFoto(Number(btn.dataset.photo));
  } else {
    ui.gallery.region = btn.dataset.galleryRegion || null;
    for (const c of galeria.querySelectorAll("[data-gallery-region]"))
      c.setAttribute("aria-pressed", String((c.dataset.galleryRegion || null) === ui.gallery.region));
    repintarMosaico();
  }
}

/** Solo se repinta el mosaico: la cabecera se queda, y con ella el foco del buscador. */
function repintarMosaico() {
  if (!galeria) return;
  const scroll = galeria.querySelector(".gal-scroll");
  scroll.innerHTML = galleryGrid(net, ui.gallery);
  scroll.scrollTop = 0;
  galeria.querySelector(".gal-count").textContent = galleryCount(net, ui.gallery);
  lazyImages(scroll, scroll);
}

// ------------------------------------------------------------------ foto a tamaño grande
function abrirFoto(i) {
  fotos = filterPhotos(net, ui.gallery);
  if (!fotos.length) return;
  fotoIndex = Math.max(0, Math.min(i, fotos.length - 1));
  if (!lightbox) {
    lightbox = document.createElement("div");
    lightbox.className = "lightbox";
    lightbox.addEventListener("click", (e) => {
      const b = e.target.closest("[data-lb]");
      if (!b) { if (e.target === lightbox) cerrarFoto(); return; }
      if (b.dataset.lb === "prev") moverFoto(-1);
      else if (b.dataset.lb === "next") moverFoto(1);
      else cerrarFoto();   // cerrar, o irse a la ficha
    });
    document.body.appendChild(lightbox);
  }
  pintarFoto();
}

function pintarFoto() {
  lightbox.innerHTML = photoLightbox(fotos[fotoIndex], fotoIndex + 1, fotos.length);
  lightbox.querySelector(".lb-close")?.focus();
}

function moverFoto(paso) {
  fotoIndex = (fotoIndex + paso + fotos.length) % fotos.length;
  pintarFoto();
}

function cerrarFoto() {
  lightbox?.remove();
  lightbox = null;
}

document.addEventListener("keydown", (e) => {
  if (lightbox) {
    if (e.key === "Escape") cerrarFoto();
    else if (e.key === "ArrowLeft") moverFoto(-1);
    else if (e.key === "ArrowRight") moverFoto(1);
    return;
  }
  if (galeria && e.key === "Escape") go("#/");
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
