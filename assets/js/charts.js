/* WE.chart — the single chart wrapper used by every page.
   Adds: phase bands, recession shading, projection marking, hover values,
   series toggles (legend), optional country picker, keyboard-accessible year
   range, data table, CSV download, and an auto-generated source line.
   Data arrive as data/js/<folder>/<id>.js files calling WE.register(). */
(function () {
  const WE = (window.WE = window.WE || {});
  WE.DATA = WE.DATA || {};
  const pending = {};
  const ROOT = (function () {
    const s = document.currentScript && document.currentScript.src;
    return s ? s.replace(/assets\/js\/charts\.js.*$/, "") : "";
  })();
  WE.ROOT = ROOT;

  WE.register = function (id, obj) {
    WE.DATA[id] = obj;
    (pending[id] || []).forEach((f) => f());
    delete pending[id];
  };
  WE.load = function (ids) {
    return Promise.all(ids.map((id) => new Promise((res, rej) => {
      if (WE.DATA[id]) return res(WE.DATA[id]);
      (pending[id] = pending[id] || []).push(() => res(WE.DATA[id]));
      if (pending[id].length > 1) return;
      const s = document.createElement("script");
      s.src = ROOT + "data/js/" + id + ".js";
      s.onerror = () => rej(new Error("Could not load data file " + id));
      document.head.appendChild(s);
    })));
  };

  // ---------- helpers
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const isAnnual = (p) => typeof p === "number" || /^\d{4}$/.test(String(p));
  function toDate(p, annualMid = true) {
    if (isAnnual(p)) return Date.UTC(+p, annualMid ? 6 : 0, 1);
    const [y, m] = String(p).split("-").map(Number);
    return Date.UTC(y, m - 1, 15);
  }
  const monthStart = (p) => { const [y, m] = p.split("-").map(Number); return Date.UTC(y, m - 1, 1); };
  const monthEnd = (p) => { const [y, m] = p.split("-").map(Number); return Date.UTC(y, m, 0, 23); };
  WE.fmt = function (v, d = 1) {
    if (v == null || isNaN(v)) return "–";
    return Number(v).toLocaleString("en-GB", { minimumFractionDigits: d, maximumFractionDigits: d });
  };
  function periodLabel(t, freq) {
    const d = new Date(t);
    if (freq === "A") return String(d.getUTCFullYear());
    if (freq === "Q") return d.getUTCFullYear() + " Q" + (Math.floor(d.getUTCMonth() / 3) + 1);
    return d.toLocaleString("en-GB", { month: "short", year: "numeric", timeZone: "UTC" });
  }
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // transforms applied to [[t, v]] arrays (t = ms)
  function transform(pts, tr, raw) {
    if (!tr) return pts;
    if (typeof tr === "function") return tr(pts, raw);
    const [kind, arg] = tr.split(":");
    if (kind === "index") {          // index to 100 at period arg (YYYY or YYYY-MM)
      const t0 = toDate(arg); const b = pts.find((p) => p[0] >= t0);
      return b ? pts.map(([t, v]) => [t, (v / b[1]) * 100]) : pts;
    }
    if (kind === "fromPeak") {       // % below running max of year arg
      const y = +arg; const inYr = pts.filter(([t]) => new Date(t).getUTCFullYear() === y);
      const m = Math.max(...inYr.map((p) => p[1]));
      return pts.map(([t, v]) => [t, (v / m) * 100]);
    }
    if (kind === "yoy") {            // % change on the same period a year earlier (monthly: 12 back; quarterly: 4)
      const m = new Map(pts.map(([t, v]) => [t, v]));
      return pts.map(([t, v]) => { const d = new Date(t); d.setUTCFullYear(d.getUTCFullYear() - 1); const p = m.get(d.getTime()); return p ? [t, (v / p - 1) * 100] : null; }).filter(Boolean);
    }
    if (kind === "scale") return pts.map(([t, v]) => [t, v * +arg]);
    if (kind === "minus") {          // subtract another series (same dates), e.g. "minus:ecb/Y10_DE"
      const m = WE.DATA[arg]; if (!m) return pts;
      const ref = new Map(m.data[Object.keys(m.data)[0]].map(([p, v]) => [toDate(p), v]));
      return pts.filter(([t]) => ref.get(t) != null).map(([t, v]) => [t, v - ref.get(t)]);
    }
    if (kind === "ratio") {          // % of another series (same dates), e.g. "ratio:fred/A255RC1Q027SBEA" or "ratio:weo/PPPPC@USA"
      const [rid, rarea] = arg.split("@"); const m = WE.DATA[rid]; if (!m) return pts;
      const rk = rarea && m.data[rarea] ? rarea : Object.keys(m.data)[0];
      const ref = new Map(m.data[rk].map(([p, v]) => [toDate(p), v]));
      return pts.filter(([t]) => ref.get(t)).map(([t, v]) => [t, (v / ref.get(t)) * 100]);
    }
    return pts;
  }

  // ---------- shading (phases + recessions)
  function shadingAreas(kind, freq, cat) {
    const areas = [];
    const ink = css("--muted") || "#898781";
    (WE.PHASES || []).forEach((p, i) => {
      const a = cat ? String(p.from.slice(0, 4)) : monthStart(p.from);
      const b = cat ? String(p.to.slice(0, 4)) : monthEnd(p.to);
      areas.push([{ name: String(p.n), xAxis: a, itemStyle: { color: i % 2 ? css("--band-b") : css("--band-a") },
        label: { show: true, position: "insideTop", color: ink, fontSize: 10, formatter: String(p.n) } }, { xAxis: b }]);
    });
    const R = WE.DATA["meta/recessions"];
    if (R && kind && kind !== "none") {
      const list = kind === "us" ? R.data.us : R.data.world;
      list.forEach(([f, t]) => {
        const a = cat ? f.slice(0, 4) : monthStart(f), b = cat ? t.slice(0, 4) : monthEnd(t);
        areas.push([{ name: "recession", xAxis: a, itemStyle: { color: css("--recession") }, label: { show: false } }, { xAxis: b }]);
      });
    }
    return areas;
  }

  // ---------- main
  const REG = [];
  WE.chart = async function (target, spec) {
    const fig = typeof target === "string" ? document.querySelector(target) : target;
    if (!fig) return;
    // a figure redrawn with a new spec (the explorer) replaces its old state
    const old = REG.findIndex((s) => s.fig === fig);
    if (old >= 0) { if (REG[old].chart) REG[old].chart.dispose(); REG.splice(old, 1); }
    const state = { spec, fig, picked: spec.picker ? [...spec.picker.default] : null, shading: true, table: false };
    const needs = new Set(["meta/recessions"]);
    if (spec.categories) (spec.series || []).forEach((s) => { s.data = s.data || "__inline"; });
    (spec.series || []).forEach((s) => { needs.add(s.data); if (typeof s.transform === "string" && /^(minus|ratio):/.test(s.transform)) needs.add(s.transform.split(":")[1].split("@")[0]); });
    if (spec.picker) { needs.add(spec.picker.data); if (typeof spec.picker.transform === "string" && /^(minus|ratio):/.test(spec.picker.transform)) needs.add(spec.picker.transform.split(":")[1].split("@")[0]); needs.add(spec.picker.names || "meta/weo_countries"); }
    try { await WE.load([...needs]); }
    catch (e) { fig.innerHTML = `<p class="chart-error">Chart data could not be loaded (${esc(e.message)}).</p>`; console.error(e); return; }
    build(state);
    REG.push(state);
  };

  function seriesList(state) {
    const { spec } = state;
    if (spec.picker) {
      const names = WE.DATA[spec.picker.names || "meta/weo_countries"];
      const nm = (c) => (spec.picker.labels && spec.picker.labels[c]) || (names.countries ? names.countries[c] : names[c] && names[c].name) || c;
      const st = spec.picker.autoStyle ? WE.assign(state.picked) : null;
      return state.picked.map((c) => ({ data: spec.picker.data, area: c, key: c, name: nm(c), transform: spec.picker.transform, hue: st ? st[c][0] : undefined, dash: st ? st[c][1] : undefined }));
    }
    return spec.series || [];
  }

  function build(state) {
    const { spec, fig } = state;
    const list = seriesList(state);
    const cat = !!spec.categories;
    // assemble series data
    const rows = list.map((s, i) => {
      const meta = WE.DATA[s.data] || {};
      const raw = (meta.data && meta.data[s.area || Object.keys(meta.data)[0]]) || [];
      let pts = raw.map(([p, v]) => [toDate(p), v]).filter((p) => p[1] != null);
      pts = transform(pts, s.transform, raw);
      const last = meta.last_actual ? (meta.last_actual[s.area] || meta.last_actual_default) : (meta.last_actual_default || null);
      return { ...s, i, meta, pts, last, freq: meta.freq || "A", key: s.key || s.area || "S" + i };
    });
    const freq = spec.freq || (rows[0] ? rows[0].freq : "A");
    const hasProj = rows.some((r) => r.last);
    const projFrom = hasProj ? Math.min(...rows.filter((r) => r.last).map((r) => r.last)) + 1 : null;

    // time extent
    const allT = rows.flatMap((r) => r.pts.map((p) => p[0]));
    const tMin = Math.min(...allT), tMax = Math.max(...allT);
    const from = spec.from ? toDate(spec.from, false) : tMin;
    const to = spec.to ? (isAnnual(spec.to) ? Date.UTC(+spec.to, 11, 31) : monthEnd(spec.to)) : tMax;

    const alt = typeof spec.alt === "function" ? spec.alt(state.picked) : spec.alt;
    fig.classList.add("chart");
    fig.innerHTML = `
      <figcaption><h3 class="chart-title">${esc(spec.title)}</h3>${spec.subtitle ? `<p class="chart-sub">${esc(spec.subtitle)}</p>` : ""}</figcaption>
      <div class="chart-controls" role="group" aria-label="Chart controls">
        ${spec.picker ? `<div class="picker" aria-label="Economies shown"></div>` : ""}
        <span class="ctl-group">
          ${cat ? "" : `<label>From <select class="yr-from" aria-label="Start year"></select></label>
          <label>to <select class="yr-to" aria-label="End year"></select></label>`}
          ${cat ? "" : `<label class="chk"><input type="checkbox" class="shade" checked> Phases &amp; recessions</label>`}
          <button type="button" class="btn tbl" aria-expanded="false">Data table</button>
          <button type="button" class="btn csv">CSV</button>
        </span>
      </div>
      <div class="chart-canvas" role="img" aria-label="${esc(alt)}"></div>
      <p class="sr-only">${esc(alt)}</p>
      <div class="chart-table" hidden></div>
      <footer class="chart-source"></footer>`;

    // source line
    const srcs = [];
    if (spec.source) srcs.push(spec.source);
    const seen = new Set();
    // spec.ownSource: the chart's own source and notes replace the per-series ones (for series whose metadata is long)
    if (!spec.ownSource) rows.forEach((r) => {
      const k = r.meta.source + "|" + r.meta.code;
      if (seen.has(k) || !r.meta.source) return; seen.add(k);
      const code = spec.picker ? r.meta.code : r.meta.code;
      srcs.push(`${r.meta.source}, series ${code}${r.meta.vintage ? ` (${r.meta.vintage})` : ""}.`);
    });
    const notes = [];
    const projMeta = (rows.find((r) => r.last) || {}).meta || {};
    if (hasProj) notes.push(projMeta.proj_note ? projMeta.proj_note.replace("{from}", projFrom) : `Values from ${projFrom} onward (shaded) are IMF staff estimates or projections.`);
    if (!spec.ownSource) rows.forEach((r) => { if (r.meta.notes && !/projections/.test(r.meta.notes) && !notes.includes(r.meta.notes)) notes.push(r.meta.notes); });
    if (!cat) notes.push(spec.shading === "none" ? "Numbered bands are the book's nine phases." : `Numbered bands are the book's nine phases; grey bands are ${spec.shading === "us" ? "US recessions (NBER dates, FRED USREC)" : "years in which world real GDP per capita fell (computed from WDI NY.GDP.PCAP.KD, World)"}.`);
    if (spec.notes) notes.push(spec.notes);
    fig.querySelector(".chart-source").innerHTML =
      `<strong>Source:</strong> ${srcs.map(esc).join(" ")} ${notes.length ? `<br><strong>Notes:</strong> ${notes.map(esc).join(" ")}` : ""}`;

    // controls
    if (!cat) {
      const yrs = []; for (let y = new Date(tMin).getUTCFullYear(); y <= new Date(tMax).getUTCFullYear(); y++) yrs.push(y);
      const sf = fig.querySelector(".yr-from"), st = fig.querySelector(".yr-to");
      sf.innerHTML = st.innerHTML = yrs.map((y) => `<option>${y}</option>`).join("");
      sf.value = new Date(from).getUTCFullYear(); st.value = new Date(to).getUTCFullYear();
      const apply = () => {
        let a = +sf.value, b = +st.value; if (a > b) [a, b] = [b, a];
        state.chart.dispatchAction({ type: "dataZoom", startValue: Date.UTC(a, 0, 1), endValue: Date.UTC(b, 11, 31) });
      };
      sf.onchange = st.onchange = apply;
      fig.querySelector(".shade").onchange = (e) => { state.shading = e.target.checked; state.chart.setOption({ series: [{ id: "__shade", markArea: { data: state.shading ? shadingAreas(spec.shading || "world", freq, cat) : [] } }] }); };
    }
    if (spec.picker) renderPicker(state);
    if (spec.onPick) spec.onPick(state.picked);
    const tbtn = fig.querySelector(".tbl");
    tbtn.onclick = () => { const el = fig.querySelector(".chart-table"); el.hidden = !el.hidden; tbtn.setAttribute("aria-expanded", String(!el.hidden)); if (!el.hidden) el.innerHTML = tableHTML(state); };
    fig.querySelector(".csv").onclick = () => downloadCSV(state);

    // ECharts option
    const ink = css("--ink"), ink2 = css("--ink-2"), muted = css("--muted"), grid = css("--grid"), axis = css("--axis");
    const unit = spec.unit || (rows[0] && rows[0].meta.unit) || "";
    const dec = spec.decimals ?? 1;
    // room for direct end labels and for a legend that wraps onto several rows
    const endRoom = Math.min(170, 24 + 6.4 * Math.max(0, ...rows.map((r) => String(r.name).length)));
    const figW = (fig.clientWidth || 700) - 40;
    // direct end labels only when they leave the plot most of the width (the legend always names the lines)
    const direct = rows.length <= 4 && endRoom <= 0.3 * figW;
    let legendRows = 1, lineW = 0;
    rows.forEach((r) => { const w = 30 + 7 * String(r.name).length; if (lineW + w > figW) { legendRows++; lineW = w; } else lineW += w; });
    const series = [];
    if (cat) {
      rows.forEach((r) => series.push({ name: r.name, type: "bar", barMaxWidth: 28, itemStyle: { color: r.hue ? WE.hue(r.hue) : WE.colour(r.key, r.i), borderRadius: [4, 4, 0, 0] },
        label: { show: !!spec.barLabels, position: "outside", color: ink2, formatter: (p) => WE.fmt(p.value, dec) },
        data: r.values.map((v) => ({ value: v, itemStyle: { borderRadius: v < 0 ? [0, 0, 4, 4] : [4, 4, 0, 0] }, label: { position: v < 0 ? "bottom" : "top" } })) }));
    } else {
      rows.forEach((r) => {
        const col = r.hue ? WE.hue(r.hue) : WE.colour(r.key, r.i), dash = r.dash || WE.dash(r.key, r.i);
        const projT = r.last ? Date.UTC(r.last, 11, 31) : Infinity;
        const act = r.pts.filter((p) => p[0] <= projT);
        const lastAct = act.length ? act[act.length - 1][0] : -Infinity;
        const proj = r.last ? r.pts.filter((p) => p[0] >= lastAct) : [];
        const base = { name: r.name, type: spec.type === "bar" ? "bar" : "line", showSymbol: false, symbolSize: 8, sampling: "lttb",
          emphasis: { focus: "series" }, itemStyle: { color: col }, labelLayout: { moveOverlap: "shiftY" } };
        series.push({ ...base, data: act, lineStyle: { width: 2, type: dash, color: col },
          endLabel: { show: direct && !r.last, formatter: "{a}", color: ink2, fontSize: 11 } });
        if (r.last && proj.length > 1) series.push({ ...base, data: proj, lineStyle: { width: 2, type: [2, 3], color: col, opacity: 0.85 }, tooltip: { show: true },
          endLabel: { show: direct, formatter: "{a}", color: ink2, fontSize: 11 }, __proj: true });
      });
      // shading helper
      const projArea = projFrom ? [[{ name: "proj", xAxis: Date.UTC(projFrom, 0, 1), itemStyle: { color: css("--proj") }, label: { show: true, position: "insideTopRight", color: muted, fontSize: 10, formatter: projMeta.proj_label || "IMF projections", offset: [0, 14] } }, { xAxis: tMax + 2e10 }]] : [];
      series.push({ id: "__shade", name: "__shade", type: "line", data: [], silent: true, markArea: { silent: true, data: shadingAreas(spec.shading || "world", freq, cat) } });
      series.push({ id: "__proj", name: "__proj", type: "line", data: [], silent: true, markArea: { silent: true, data: projArea } });
      if (spec.markLines) series.push({ id: "__ml", name: "__ml", type: "line", data: [], silent: true,
        markLine: { symbol: "none", silent: true, lineStyle: { color: muted, type: "dashed", width: 1 }, label: { color: ink2, fontSize: 10, formatter: "{b}" },
          data: spec.markLines.map((m) => ({ name: m.label, xAxis: toDate(m.at) })) } });
    }

    const opt = {
      animation: false,
      textStyle: { fontFamily: css("--font-ui"), color: ink },
      grid: { left: 52, right: direct && !cat ? endRoom : 24, top: 30 + legendRows * 20, bottom: cat ? 52 : 64, containLabel: false },
      legend: { show: rows.length > 1, top: 0, left: 0, icon: "roundRect", itemWidth: 14, itemHeight: 3, textStyle: { color: ink2, fontSize: 12 },
        data: [...new Set(rows.map((r) => r.name))] },
      tooltip: { trigger: "axis", confine: true, backgroundColor: css("--surface"), borderColor: grid, textStyle: { color: ink, fontSize: 12 },
        axisPointer: { type: cat ? "shadow" : "line", lineStyle: { color: axis } },
        formatter: (ps) => tooltip(ps, rows, freq, unit, dec, cat) },
      xAxis: cat ? { type: "category", data: spec.categories, axisLine: { lineStyle: { color: axis } }, axisLabel: { color: muted, interval: 0, fontSize: 11, formatter: (v) => (Math.max(...spec.categories.map((c) => String(c).length)) * 6.5 > 0.9 * (figW - 36) / spec.categories.length ? String(v).replace("–", "–\n") : v) }, axisTick: { show: false } }
        : { type: "time", min: tMin, max: tMax, axisLine: { lineStyle: { color: axis } }, axisLabel: { color: muted, hideOverlap: true, formatter: (tMax - tMin > 3 * 365.25 * 864e5) ? (v) => { const d = new Date(v); return d.getMonth() === 0 && d.getDate() === 1 ? String(d.getFullYear()) : ""; } : undefined }, splitLine: { show: false } },
      yAxis: { type: "value", name: unit, nameTextStyle: { color: muted, align: "left", padding: [0, 0, 0, -40] }, min: spec.yMin, max: spec.yMax,
        axisLabel: { color: muted, formatter: (v) => WE.fmt(v, spec.axisDecimals ?? (Number.isInteger(v) ? 0 : Math.abs(v * 10 - Math.round(v * 10)) < 1e-9 ? 1 : 2)) }, splitLine: { lineStyle: { color: grid } }, axisLine: { show: false } },
      dataZoom: cat ? [] : [
        { type: "slider", startValue: from, endValue: to, height: 18, bottom: 8, borderColor: grid, fillerColor: css("--zoom"),
          handleStyle: { color: css("--surface"), borderColor: axis }, textStyle: { color: muted }, dataBackground: { lineStyle: { color: axis }, areaStyle: { color: grid } },
          labelFormatter: (v) => new Date(v).getUTCFullYear() },
        { type: "inside", zoomOnMouseWheel: "shift" }],
      series,
    };
    if (cat) { opt.legend.data = rows.map((r) => r.name); rows.forEach((r) => { r.values = r.values; }); }

    const el = fig.querySelector(".chart-canvas");
    if (state.chart) state.chart.dispose();
    state.chart = echarts.init(el, null, { renderer: "svg" });
    state.chart.setOption(opt);
    state.rows = rows; state.freq = freq; state.unit = unit; state.dec = dec; state.cat = cat;
    state.chart.on("datazoom", () => {
      if (cat) return;
      const o = state.chart.getOption().dataZoom[0];
      const sf = fig.querySelector(".yr-from"), st = fig.querySelector(".yr-to");
      if (o.startValue != null && sf) { sf.value = new Date(o.startValue).getUTCFullYear(); st.value = new Date(o.endValue).getUTCFullYear(); }
    });
  }

  function tooltip(ps, rows, freq, unit, dec, cat) {
    if (!ps.length) return "";
    const head = cat ? ps[0].axisValueLabel : periodLabel(ps[0].axisValue, freq);
    const seenNames = new Set();
    const lines = ps.filter((p) => !String(p.seriesName).startsWith("__")).filter((p) => {
      if (seenNames.has(p.seriesName)) return false; seenNames.add(p.seriesName); return true;
    }).map((p) => {
      const v = Array.isArray(p.value) ? p.value[1] : p.value;
      const r = rows.find((x) => x.name === p.seriesName);
      const yr = Array.isArray(p.value) ? new Date(p.value[0]).getUTCFullYear() : null;
      const proj = r && r.last && yr > r.last ? ` <em class="tt-proj">projection</em>` : "";
      return `<div class="tt-row"><span class="tt-dot" style="background:${p.color}"></span><span class="tt-name">${esc(p.seriesName)}</span><span class="tt-val">${WE.fmt(v, dec)}${proj}</span></div>`;
    });
    return `<div class="tt"><div class="tt-head">${esc(head)}${unit ? ` · ${esc(unit)}` : ""}</div>${lines.join("")}</div>`;
  }

  function renderPicker(state) {
    const { spec, fig } = state;
    const box = fig.querySelector(".picker");
    const names = WE.DATA[spec.picker.names || "meta/weo_countries"];
    const all = names.countries || Object.fromEntries(Object.entries(names).map(([k, v]) => [k, v.name]));
    const avail = Object.keys(WE.DATA[spec.picker.data].data).filter((c) => all[c]);
    const label = (c) => (spec.picker.labels && spec.picker.labels[c]) || all[c] || c;
    const max = spec.picker.max || 8;
    const st = spec.picker.autoStyle ? WE.assign(state.picked) : null;
    box.innerHTML = state.picked.map((c, i) => `<span class="chip"><span class="sw" style="${st && st[c][1] !== "solid" ? `background:none;height:0;border-top:3px ${st[c][1]} ${WE.hue(st[c][0])}` : `background:${st ? WE.hue(st[c][0]) : WE.colour(c, i)}`}"></span>${esc(label(c))}<button type="button" aria-label="Remove ${esc(label(c))}" data-c="${c}">×</button></span>`).join("") +
      (state.picked.length < max ? `<label class="add">Add <select aria-label="Add an economy"><option value="">choose…</option>${
        avail.filter((c) => !state.picked.includes(c)).sort((a, b) => label(a).localeCompare(label(b))).map((c) => `<option value="${c}">${esc(label(c))}</option>`).join("")}</select></label>` : `<span class="muted">(max ${max})</span>`);
    box.querySelectorAll("button[data-c]").forEach((b) => b.onclick = () => { state.picked = state.picked.filter((x) => x !== b.dataset.c); build(state); });
    const sel = box.querySelector("select");
    if (sel) sel.onchange = () => { if (sel.value) { state.picked.push(sel.value); build(state); fig.querySelector(".picker select")?.focus(); } };
  }

  function visibleRange(state) {
    if (state.cat) return [-Infinity, Infinity];
    const o = state.chart.getOption().dataZoom[0];
    return [o.startValue ?? -Infinity, o.endValue ?? Infinity];
  }
  function matrix(state) {
    const { rows, freq, cat } = state;
    if (cat) return { head: ["", ...rows.map((r) => r.name)], body: state.spec.categories.map((c, i) => [c, ...rows.map((r) => r.values[i])]) };
    const [a, b] = visibleRange(state);
    const keys = new Map();
    rows.forEach((r, j) => r.pts.forEach(([t, v]) => { if (t >= a - 2e9 && t <= b + 2e9) { if (!keys.has(t)) keys.set(t, Array(rows.length).fill(null)); keys.get(t)[j] = v; } }));
    const body = [...keys.entries()].sort((x, y) => x[0] - y[0]).map(([t, vs]) => [periodLabel(t, freq), ...vs]);
    return { head: ["Period", ...rows.map((r) => r.name)], body };
  }
  function tableHTML(state) {
    const m = matrix(state);
    return `<div class="table-wrap"><table><caption>${esc(state.spec.title)} (${esc(state.unit)})</caption><thead><tr>${m.head.map((h) => `<th scope="col">${esc(h)}</th>`).join("")}</tr></thead><tbody>${
      m.body.map((r) => `<tr><th scope="row">${esc(r[0])}</th>${r.slice(1).map((v) => `<td>${WE.fmt(v && typeof v === "object" ? v.value : v, state.dec)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
  }
  function downloadCSV(state) {
    const m = matrix(state);
    const q = (s) => `"${String(s ?? "").replace(/"/g, '""')}"`;
    const src = state.fig.querySelector(".chart-source").innerText.replace(/\s+/g, " ");
    const lines = [`# ${state.spec.title} (${state.unit})`, `# ${src}`, m.head.map(q).join(","), ...m.body.map((r) => [q(r[0]), ...r.slice(1).map((v) => (v == null ? "" : typeof v === "object" ? v.value : v))].join(","))];
    const blob = new Blob([lines.join("\n")], { type: "text/csv" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = (state.fig.id || "chart") + ".csv";
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  // categorical (hand-entered) data: spec.categories + spec.series[{name,key,values}]
  WE.DATA["__inline"] = { data: { x: [] }, freq: "A" };

  window.addEventListener("resize", () => REG.forEach((s) => s.chart && s.chart.resize()));
  document.addEventListener("we-theme", () => REG.forEach((s) => build(s)));
  WE.rebuildCharts = () => REG.forEach((s) => build(s));
})();
