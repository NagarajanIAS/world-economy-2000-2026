/* Compare countries: one indicator, up to eight economies, drawn with WE.chart.
   The indicator list is data/js/meta/catalogue.js (built by scripts/build_catalogue.py).
   The selection is kept in the address (#i=<id>&c=USA,CHN) so a view can be bookmarked. */
(function () {
  const WE = window.WE;
  // IMF and World Bank codes for the same aggregate, so a selection survives a change of source
  const SAME = { G001: "WLD", G163: "EMU", G603: "SSF" };
  const BACK = Object.fromEntries(Object.entries(SAME).map(([a, b]) => [b, a]));
  const LENSES = { weo: ["USA", "CHN", "G163", "JPN", "IND", "G603"], wdi: ["USA", "CHN", "EMU", "JPN", "IND", "SSF"] };
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  let cat, picked = null, current = null;

  function readHash() {
    const h = new URLSearchParams(location.hash.slice(1));
    return { i: h.get("i"), c: h.get("c") ? h.get("c").split(",").filter(Boolean) : null };
  }
  function writeHash() {
    if (!current) return;
    const h = `#i=${current.id}&c=${(picked || []).join(",")}`;
    if (location.hash !== h) history.replaceState(null, "", h);
    const link = document.getElementById("ex-map");
    if (link) link.href = `map.html#i=${current.id}`;
  }

  function convert(codes, src) {
    return codes.map((c) => (src === "wdi" ? SAME[c] || c : BACK[c] || c));
  }

  async function show(id, codes) {
    const item = cat.items.find((x) => x.id === id) || cat.items[0];
    const src = item.id.split("/")[0];
    await WE.load([item.id, item.names, "meta/wdi_countries"]);
    const data = WE.DATA[item.id].data;
    const want = convert(codes || picked || LENSES[src], src).filter((c) => data[c] && data[c].length);
    picked = want.length ? want.slice(0, 8) : LENSES[src].filter((c) => data[c]);
    current = item;
    document.getElementById("ex-ind").value = item.id;
    const desc = document.getElementById("ex-desc");
    desc.innerHTML = `<strong>${esc(item.source)}</strong>, series <code>${esc(item.id.split("/")[1])}</code>: “${esc(item.label)}”. ` +
      `${item.n} economies and groups, ${item.first}–${item.last}.` +
      (src === "weo" ? ` Years after each economy's last actual year are IMF estimates or projections.` : "");
    // shorter World Bank names for countries ("China" rather than "China, People's Republic of")
    const wb = WE.DATA["meta/wdi_countries"], imf = WE.DATA["meta/weo_countries"];
    const nm = (c) => (wb[c] ? wb[c].name.trim() : imf && imf.countries[c]) || c;
    const labels = Object.fromEntries(Object.keys(data).map((c) => [c, nm(c)]));
    WE.chart("#ex-chart", {
      title: item.name,
      subtitle: item.unit,
      unit: item.unit,
      decimals: item.dec,
      from: Math.max(item.first, 1990),
      picker: { data: item.id, names: item.names, default: picked, max: 8, labels, autoStyle: true, transform: item.scale !== 1 ? `scale:${item.scale}` : undefined },
      alt: (p) => `Line chart of ${item.name.toLowerCase()} (${item.unit}) for ${p.map(nm).join(", ") || "no economies"}, by year.`,
      onPick: (p) => { picked = [...p]; writeHash(); },
    });
  }

  async function init() {
    await WE.load(["meta/catalogue"]);
    cat = WE.DATA["meta/catalogue"];
    const sel = document.getElementById("ex-ind");
    const groups = [...new Set(cat.items.map((x) => x.group))];
    sel.innerHTML = groups.map((g) => `<optgroup label="${esc(g)}">${cat.items.filter((x) => x.group === g)
      .map((x) => `<option value="${x.id}">${esc(x.name)} (${x.source === "IMF WEO" ? "IMF" : "World Bank"})</option>`).join("")}</optgroup>`).join("");
    sel.onchange = () => show(sel.value);
    document.getElementById("ex-lenses").onclick = () => { picked = null; show(current.id, LENSES[current.id.split("/")[0]]); };
    document.getElementById("ex-count").textContent = cat.items.length;
    const h = readHash();
    await show(h.i || "weo/NGDP_RPCH", h.c);
    window.addEventListener("hashchange", () => { const k = readHash(); if (k.i && (k.i !== current.id || (k.c || []).join() !== picked.join())) show(k.i, k.c); });
  }
  document.addEventListener("DOMContentLoaded", init);
})();
