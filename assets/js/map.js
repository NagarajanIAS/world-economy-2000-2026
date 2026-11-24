/* World map: one indicator, one year, every country shaded.
   Indicators come from data/js/meta/catalogue.js (the same list as the explorer).
   Classes are fixed for each indicator across all years from 1990, so colours can be
   compared as the year changes. The selection is kept in the address (#i=<id>&y=<year>). */
(function () {
  const WE = window.WE;
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const dark = () => { const t = document.documentElement.getAttribute("data-theme"); return t ? t === "dark" : matchMedia("(prefers-color-scheme: dark)").matches; };
  // Natural Earth code -> code used by each source, where they differ
  const ALIAS = { weo: { PSE: "WBG" }, wdi: { KOS: "XKX" } };
  // Sequential: the blue ramp, light to dark (reversed on a dark page so "more" is always more contrast)
  const SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#104281"];
  // Diverging: red arm (below zero), grey midpoint, blue arm (above zero)
  const DIV_L = ["#b9302f", "#e34948", "#f2a09f", "#f0efec", "#9ec5f4", "#3987e5", "#184f95"];
  const DIV_D = ["#e66767", "#a83636", "#5e2b2a", "#383835", "#1f3f66", "#2a78d6", "#86b6ef"];

  let cat, item, src, data, year, years, classes, chart, geoReady = false, timer = null, picked = null, names;

  function readHash() {
    const h = new URLSearchParams(location.hash.slice(1));
    return { i: h.get("i"), y: h.get("y") ? +h.get("y") : null };
  }
  function writeHash() {
    const h = `#i=${item.id}&y=${year}`;
    if (location.hash !== h) history.replaceState(null, "", h);
    document.getElementById("mp-ex").href = `explorer.html#i=${item.id}${picked ? `&c=${code(picked)}` : ""}`;
  }
  const code = (ne) => (ALIAS[src][ne] || ne);
  const scaled = (v) => (v == null ? null : v * item.scale);
  const isAgg = (c) => (src === "weo" ? /^G\d|^GX/.test(c) : !!(WE.DATA["meta/wdi_countries"][c] || {}).aggregate);
  const fmt = (v) => WE.fmt(v, item.dec);

  function valueAt(c, y) {
    const row = data[c]; if (!row) return null;
    const p = row.find((r) => +r[0] === y);
    return p && p[1] != null ? scaled(p[1]) : null;
  }
  function nice(x) {
    if (!isFinite(x) || x === 0) return 0;
    const s = Math.sign(x), a = Math.abs(x), m = Math.pow(10, Math.floor(Math.log10(a)) - 1);
    const r = Math.round(a / m) * m;
    return s * (r >= 10 ? Math.round(r) : +r.toPrecision(2));
  }
  function quant(sorted, q) { const i = (sorted.length - 1) * q, lo = Math.floor(i); return sorted[lo] + (sorted[Math.min(lo + 1, sorted.length - 1)] - sorted[lo]) * (i - lo); }

  // fixed class breaks for this indicator, from every country-year since 1990
  function makeClasses() {
    const vals = [];
    Object.keys(data).filter((c) => !isAgg(c)).forEach((c) => data[c].forEach(([y, v]) => { if (+y >= 1990 && v != null) vals.push(scaled(v)); }));
    vals.sort((a, b) => a - b);
    if (item.map === "div") {
      const abs = vals.map(Math.abs).sort((a, b) => a - b);
      const b0 = nice(quant(abs, 0.12)), b1 = nice(quant(abs, 0.45)), b2 = nice(quant(abs, 0.8));
      const cuts = [-b2, -b1, -b0, b0, b1, b2];
      const pal = dark() ? DIV_D : DIV_L;
      return { cuts, colours: pal, labels: labelsFor(cuts) };
    }
    const cuts = [1, 2, 3, 4, 5].map((k) => nice(quant(vals, k / 6)));
    for (let i = 1; i < cuts.length; i++) if (cuts[i] <= cuts[i - 1]) cuts[i] = nice(cuts[i - 1] * 1.5 || 1);
    return { cuts, colours: dark() ? [...SEQ].reverse() : SEQ, labels: labelsFor(cuts) };
  }
  function labelsFor(cuts) {
    const f = (v) => WE.fmt(v, Math.abs(v) < 10 && v % 1 ? 1 : 0);
    return [`below ${f(cuts[0])}`, ...cuts.slice(1).map((c, i) => `${f(cuts[i])} to ${f(c)}`), `${f(cuts[cuts.length - 1])} and above`];
  }
  const classOf = (v) => { let k = 0; while (k < classes.cuts.length && v >= classes.cuts[k]) k++; return k; };

  function projected(c, y) {
    if (src !== "weo") return false;
    const la = WE.DATA[item.id].last_actual || {};
    return y > (la[c] ?? item.last_actual_default);
  }

  function rows() {
    return (WE_WORLD_GEO.features).map((f) => f.properties.name)
      .map((ne) => ({ ne, c: code(ne), name: names(ne), v: valueAt(code(ne), year) }));
  }

  function draw() {
    const rs = rows();
    // no data: page colour with a diagonal hatch and an outline, so it cannot be mistaken for the grey "near zero" class
    const noData = css("--surface"), border = css("--surface"), outline = css("--axis");
    const hatch = { symbol: "rect", symbolSize: 1, color: outline, dashArrayX: [1, 0], dashArrayY: [1, 4], rotation: Math.PI / 4 };
    chart.setOption({
      animation: false,
      tooltip: { trigger: "item", confine: true, backgroundColor: css("--surface"), borderColor: css("--border"), textStyle: { color: css("--ink"), fontSize: 12 },
        formatter: (p) => { const r = rs.find((x) => x.ne === p.name); if (!r) return ""; return `<strong>${esc(r.name)}</strong><br>${year}: ${r.v == null ? "no data" : `${fmt(r.v)} ${esc(item.unit)}${projected(r.c, year) ? " (IMF estimate or projection)" : ""}`}`; } },
      series: [{ type: "map", map: "world", roam: false, nameProperty: "name", selectedMode: false, left: 0, right: 0, top: 4, bottom: 4,
        label: { show: false }, emphasis: { label: { show: false }, itemStyle: { areaColor: css("--accent") } },
        itemStyle: { borderColor: border, borderWidth: 0.5 },
        data: rs.map((r) => ({ name: r.ne, value: r.v, itemStyle: { areaColor: r.v == null ? noData : classes.colours[classOf(r.v)], decal: r.v == null ? hatch : undefined, borderColor: r.ne === picked ? css("--ink") : r.v == null ? outline : border, borderWidth: r.ne === picked ? 1.5 : 0.5 } })) }],
    }, true);
    // legend
    document.getElementById("mp-legend").innerHTML = classes.labels.map((l, i) => `<span class="lg"><span class="lg-sw" style="background:${classes.colours[i]}"></span>${esc(l)}</span>`).join("") +
      `<span class="lg"><span class="lg-sw" style="background:repeating-linear-gradient(135deg, ${outline} 0 1px, ${noData} 1px 4px);border-color:${outline}"></span>no data</span>` + `<span class="lg-unit">${esc(item.unit)}</span>`;
    // readout, rankings, source
    const have = rs.filter((r) => r.v != null).sort((a, b) => b.v - a.v);
    const proj = src === "weo" && year > item.last_actual_default;
    document.getElementById("mp-year").textContent = year;
    document.getElementById("mp-read").textContent = `${item.name}, ${year}: ${have.length} economies with data.${proj ? " Values for this year are IMF estimates or projections for most economies." : ""}`;
    const li = (r, i) => `<li value="${i}"><button type="button" data-ne="${r.ne}">${esc(r.name)}</button> <span class="v">${fmt(r.v)}</span>${projected(r.c, year) ? " <span class=\"muted\">(p)</span>" : ""}</li>`;
    document.getElementById("mp-top").innerHTML = have.slice(0, 10).map((r, i) => li(r, i + 1)).join("");
    document.getElementById("mp-bottom").innerHTML = have.slice(-10).map((r, i) => li(r, have.length - Math.min(10, have.length) + i + 1)).join("");
    document.getElementById("mp-top-h").textContent = `Highest in ${year}`;
    document.getElementById("mp-bottom-h").textContent = `Lowest in ${year}`;
    const full = document.getElementById("mp-table");
    if (!full.hidden) full.innerHTML = tableHTML(have);
    document.querySelectorAll("#mp-rank button[data-ne]").forEach((b) => b.onclick = () => pick(b.dataset.ne));
    const m = WE.DATA[item.id];
    document.getElementById("mp-source").innerHTML = `<strong>Source:</strong> ${esc(m.source)}, series ${esc(m.code)}${m.vintage ? ` (${esc(m.vintage)})` : ""}. Boundaries: Natural Earth, 1:110m countries (public domain); shown as drawn there. ` +
      `<br><strong>Notes:</strong> Colour classes are fixed for this indicator across all years from 1990, set at the ${item.map === "div" ? "12th, 45th and 80th percentiles of the size of all country-year values, either side of zero" : "sixths of all country-year values"}, rounded. Groups of countries are not shown. Small states may be too small to see; the lists below include them.${src === "weo" ? " (p): IMF estimate or projection." : " World Bank series end in different years for different countries."}`;
    showPicked(rs);
    writeHash();
  }

  function tableHTML(have) {
    return `<div class="table-wrap"><table><caption>${esc(item.name)}, ${year} (${esc(item.unit)})</caption><thead><tr><th scope="col">Rank</th><th scope="col">Economy</th><th scope="col">Value</th></tr></thead><tbody>${
      have.map((r, i) => `<tr><td>${i + 1}</td><th scope="row">${esc(r.name)}</th><td>${fmt(r.v)}${projected(r.c, year) ? " (p)" : ""}</td></tr>`).join("")}</tbody></table></div>`;
  }

  function pick(ne) { picked = ne; draw(); document.getElementById("mp-picked").focus(); }
  function showPicked(rs) {
    const box = document.getElementById("mp-picked");
    if (!picked) { box.innerHTML = `<span class="muted">Click or tap a country to see its value and rank.</span>`; return; }
    const r = rs.find((x) => x.ne === picked);
    const have = rs.filter((x) => x.v != null).sort((a, b) => b.v - a.v);
    const rank = have.findIndex((x) => x.ne === picked) + 1;
    box.innerHTML = `<strong>${esc(r.name)}</strong>, ${year}: ${r.v == null ? "no data" : `${fmt(r.v)} ${esc(item.unit)}${projected(r.c, year) ? " (IMF estimate or projection)" : ""}; ranks ${ordinal(rank)} of ${have.length}, counting from the highest`}. ` +
      `<a href="explorer.html#i=${item.id}&c=${code(picked)}">See ${esc(r.name)} over time</a>`;
  }
  const ordinal = (n) => n + (n % 100 >= 11 && n % 100 <= 13 ? "th" : ["th", "st", "nd", "rd"][n % 10] || "th");

  async function show(id, y) {
    stop();
    item = cat.items.find((x) => x.id === id) || cat.items[0];
    src = item.id.split("/")[0];
    await WE.load([item.id, "meta/wdi_countries", "meta/weo_countries"]);
    data = WE.DATA[item.id].data;
    const wb = WE.DATA["meta/wdi_countries"], imf = WE.DATA["meta/weo_countries"].countries;
    const label = Object.fromEntries(WE_WORLD_GEO.features.map((f) => [f.properties.name, f.properties.label]));
    names = (ne) => (wb[code(ne)] ? wb[code(ne)].name.trim() : imf[code(ne)]) || label[ne] || ne;
    classes = makeClasses();
    // years with data for at least a third of countries
    const count = {};
    Object.keys(data).filter((c) => !isAgg(c)).forEach((c) => data[c].forEach(([yy, v]) => { if (v != null) count[yy] = (count[yy] || 0) + 1; }));
    const maxN = Math.max(...Object.values(count));
    years = Object.keys(count).map(Number).filter((yy) => yy >= 1990 && count[yy] >= maxN / 3).sort((a, b) => a - b);
    const def = src === "weo" ? item.last_actual_default : years.filter((yy) => count[yy] >= maxN * 0.6).pop();
    year = y && years.includes(y) ? y : (years.includes(def) ? def : years[years.length - 1]);
    const sl = document.getElementById("mp-slider");
    sl.min = years[0]; sl.max = years[years.length - 1]; sl.value = year;
    document.getElementById("mp-min").textContent = years[0];
    document.getElementById("mp-max").textContent = years[years.length - 1];
    document.getElementById("mp-ind").value = item.id;
    document.getElementById("mp-title").textContent = item.name;
    document.getElementById("mp-desc").innerHTML = `<strong>${esc(item.source)}</strong>, series <code>${esc(item.id.split("/")[1])}</code>: “${esc(item.label)}”.`;
    draw();
  }

  function setYear(y) {
    const yy = Math.max(years[0], Math.min(years[years.length - 1], y));
    if (!years.includes(yy)) return;
    year = yy; document.getElementById("mp-slider").value = yy; draw();
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; const b = document.getElementById("mp-play"); b.textContent = "Play"; b.setAttribute("aria-pressed", "false"); } }
  function play() {
    if (timer) return stop();
    if (year >= years[years.length - 1]) setYear(years[0]);
    const b = document.getElementById("mp-play"); b.textContent = "Pause"; b.setAttribute("aria-pressed", "true");
    timer = setInterval(() => { const i = years.indexOf(year); if (i >= years.length - 1) return stop(); setYear(years[i + 1]); }, 700);
  }

  async function init() {
    // Antarctica is left off: no indicator here covers it, and it takes a third of the frame
    WE_WORLD_GEO.features = WE_WORLD_GEO.features.filter((f) => f.properties.name !== "ATA");
    echarts.registerMap("world", WE_WORLD_GEO);
    await WE.load(["meta/catalogue"]);
    cat = WE.DATA["meta/catalogue"];
    const sel = document.getElementById("mp-ind");
    const groups = [...new Set(cat.items.map((x) => x.group))];
    sel.innerHTML = groups.map((g) => `<optgroup label="${esc(g)}">${cat.items.filter((x) => x.group === g)
      .map((x) => `<option value="${x.id}">${esc(x.name)} (${x.source === "IMF WEO" ? "IMF" : "World Bank"})</option>`).join("")}</optgroup>`).join("");
    sel.onchange = () => show(sel.value, year);
    chart = echarts.init(document.getElementById("mp-canvas"), null, { renderer: "svg" });
    chart.on("click", (p) => { if (p.name) pick(p.name); });
    const sl = document.getElementById("mp-slider");
    sl.oninput = () => { stop(); setYear(+sl.value); };
    document.getElementById("mp-play").onclick = play;
    document.getElementById("mp-prev").onclick = () => { stop(); setYear(year - 1); };
    document.getElementById("mp-next").onclick = () => { stop(); setYear(year + 1); };
    document.getElementById("mp-full").onclick = (e) => {
      const t = document.getElementById("mp-table"); t.hidden = !t.hidden; e.target.setAttribute("aria-expanded", String(!t.hidden));
      e.target.textContent = t.hidden ? "Show all economies" : "Hide the full list"; draw();
    };
    const h = readHash();
    await show(h.i || "weo/NGDP_RPCH", h.y);
    window.addEventListener("resize", () => chart.resize());
    window.addEventListener("hashchange", () => { const k = readHash(); if (k.i && (k.i !== item.id || (k.y && k.y !== year))) show(k.i, k.y); });
    document.addEventListener("we-theme", () => { classes = makeClasses(); draw(); });
  }
  document.addEventListener("DOMContentLoaded", init);
})();
