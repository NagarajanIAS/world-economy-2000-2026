/* Master timeline on the home page.
   Lower panel: world real GDP growth (IMF WEO, NGDP_RPCH, G001), with the nine
   phase bands and the years in which world GDP per person fell (WDI).
   Upper lane: dated events from WE.EVENTS, one row per theme.
   A year slider ("scrubber") moves a cursor and fills the panel below with the
   phase, the year's growth figure and that year's events. Clicking a phase band,
   or the phase name in the panel, opens its chapter when it is written. */
(function () {
  const WE = window.WE;
  const el = document.getElementById("timeline-chart");
  if (!el) return;
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const ms = (p) => { const [y, m, d] = p.split("-").map(Number); return Date.UTC(y, (m || 1) - 1, d || 1); };
  const monthEnd = (p) => { const [y, m] = p.split("-").map(Number); return Date.UTC(y, m, 0, 23); };
  const THEMES = [["finance", "Finance"], ["money", "Central banks"], ["fiscal", "Fiscal"], ["trade", "Trade"]];
  const slider = document.getElementById("tl-range"), yearOut = document.getElementById("tl-year"), panel = document.getElementById("tl-panel");
  const ready = new Set(WE.BOOK[0].items.filter((i) => i.ready).map((i) => i.href));
  const href = (p) => `chapters/${p.slug}.html`;
  let chart, growth, recess, year = +slider.value;

  WE.load(["weo/NGDP_RPCH", "meta/recessions"]).then(([g, r]) => {
    growth = { pts: g.data.G001, last: (g.last_actual && g.last_actual.G001) || g.last_actual_default, meta: g };
    recess = r.data.world;
    draw(); update();
    document.addEventListener("we-theme", draw);
    addEventListener("resize", () => chart && chart.resize());
  }).catch((e) => { el.innerHTML = `<p class="chart-error">Timeline data could not be loaded (${e.message}).</p>`; });

  function draw() {
    if (chart) chart.dispose();
    chart = echarts.init(el, null, { renderer: "svg" });
    const ink = css("--ink"), ink2 = css("--ink-2"), muted = css("--muted"), grid = css("--grid"), axis = css("--axis");
    const xMin = Date.UTC(2000, 0, 1), xMax = Date.UTC(2027, 11, 31);
    const bands = WE.PHASES.map((p, i) => [{
      name: p.slug, xAxis: ms(p.from), itemStyle: { color: css(i % 2 ? "--band-b" : "--band-a") },
      label: { show: true, position: "insideTop", formatter: String(p.n), color: muted, fontSize: 11, fontWeight: 600 },
      emphasis: { itemStyle: { color: css("--zoom") } },
    }, { xAxis: monthEnd(p.to) }]);
    const recAreas = recess.filter(([f]) => +f.slice(0, 4) >= 2000).map(([f, t]) => [{ name: "recession", xAxis: ms(f), itemStyle: { color: css("--recession") }, label: { show: false }, silent: true }, { xAxis: monthEnd(t) }]);
    const bars = growth.pts.filter(([y]) => y >= 2000 && y <= 2027).map(([y, v]) => ({
      value: [Date.UTC(y, 6, 1), v], proj: y > growth.last,
      itemStyle: { color: y > growth.last ? css("--proj-bar") || WE.hue("ink") : WE.hue("ink"), opacity: y > growth.last ? 0.45 : 0.9,
                   borderRadius: v < 0 ? [0, 0, 3, 3] : [3, 3, 0, 0] },
    }));
    const ev = WE.EVENTS.map((e) => ({ value: [ms(e.d), THEMES.findIndex((t) => t[0] === e.theme)], e }));
    const lanes = THEMES.map((t) => t[1]);
    chart.setOption({
      animation: false, textStyle: { fontFamily: css("--font-ui") },
      grid: [{ left: 96, right: 18, top: 8, height: 92 }, { left: 96, right: 18, top: 130, bottom: 34 }],
      xAxis: [
        { gridIndex: 0, type: "time", min: xMin, max: xMax, axisLabel: { show: false }, axisTick: { show: false }, axisLine: { show: false }, splitLine: { show: false } },
        { gridIndex: 1, type: "time", min: xMin, max: xMax, axisLine: { lineStyle: { color: axis } }, axisLabel: { color: muted }, splitLine: { show: false } },
      ],
      yAxis: [
        { gridIndex: 0, type: "category", data: lanes, inverse: true, axisLine: { show: false }, axisTick: { show: false }, axisLabel: { color: ink2, fontSize: 11 }, splitLine: { show: true, lineStyle: { color: grid } } },
        { gridIndex: 1, type: "value", name: "World GDP growth, %", nameLocation: "middle", nameGap: 36, nameTextStyle: { color: muted }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: grid } } },
      ],
      tooltip: { trigger: "item", confine: true, backgroundColor: css("--surface"), borderColor: grid, textStyle: { color: ink, fontSize: 12 },
        formatter: (p) => {
          if (p.componentType === "series" && p.seriesId === "events") return `<div class="tt-head">${p.data.e.d}</div>${p.data.e.t}<br><span class="tt-proj">${p.data.e.src}</span>`;
          if (p.componentType === "series" && p.seriesId === "growth") { const y = new Date(p.value[0]).getUTCFullYear(); return `<div class="tt-head">${y}</div>World real GDP growth <b>${WE.fmt(p.value[1], 1)}%</b>${p.data.proj ? '<span class="tt-proj">IMF projection</span>' : ""}`; }
          if (p.componentType === "markArea" && p.name !== "recession") { const ph = WE.PHASES.find((x) => x.slug === p.name); return ph ? `<div class="tt-head">Phase ${ph.n} · ${ph.years}</div>${ph.title}<br><span class="tt-proj">${ready.has(href(ph)) ? "Click to open the chapter" : "Chapter in preparation"}</span>` : ""; }
          return "";
        } },
      series: [
        { id: "bandsTop", type: "line", xAxisIndex: 0, yAxisIndex: 0, data: [], silent: false,
          markArea: { data: WE.PHASES.map((p, i) => [{ name: p.slug, xAxis: ms(p.from), itemStyle: { color: css(i % 2 ? "--band-b" : "--band-a") }, label: { show: false } }, { xAxis: monthEnd(p.to) }]) } },
        { id: "events", type: "scatter", xAxisIndex: 0, yAxisIndex: 0, data: ev, symbolSize: 10,
          itemStyle: { color: WE.hue("blue"), borderColor: css("--surface"), borderWidth: 2 } },
        { id: "growth", type: "bar", xAxisIndex: 1, yAxisIndex: 1, data: bars, barWidth: "55%",
          markArea: { data: [...bands, ...recAreas] },
          markLine: { id: "cursor", symbol: "none", silent: true, animation: false, label: { show: false }, lineStyle: { color: css("--accent"), width: 2, type: "solid" },
                      data: [{ xAxis: Date.UTC(year, 6, 1) }] } },
      ],
    });
    chart.on("click", (p) => {
      if (p.componentType === "markArea" && p.name && p.name !== "recession") openPhase(p.name);
      else if (p.componentType === "series" && p.seriesId === "growth") setYear(new Date(p.value[0]).getUTCFullYear());
      else if (p.componentType === "series" && p.seriesId === "events") setYear(+p.data.e.d.slice(0, 4));
    });
  }

  function openPhase(slug) {
    const ph = WE.PHASES.find((x) => x.slug === slug); if (!ph) return;
    if (ready.has(href(ph))) location.href = href(ph);
    else { setYear(+ph.from.slice(0, 4)); panel.querySelector(".tl-phase")?.focus(); }
  }
  function setYear(y) { slider.value = y; year = y; update(); }

  function update() {
    yearOut.textContent = year;
    if (chart) chart.setOption({ series: [{ id: "growth", markLine: { data: [{ xAxis: Date.UTC(year, 6, 1) }] } }] });
    const phases = WE.PHASES.filter((p) => +p.from.slice(0, 4) <= year && +p.to.slice(0, 4) >= year);
    const g = growth && growth.pts.find(([y]) => y === year);
    const proj = g && year > growth.last;
    const evs = WE.EVENTS.filter((e) => +e.d.slice(0, 4) === year);
    const rec = recess && recess.some(([f]) => +f.slice(0, 4) === year);
    panel.innerHTML = `<div>
        <h3>${phases.length > 1 ? "Phases" : "Phase"}</h3>
        ${phases.map((p) => ready.has(href(p))
          ? `<p><a class="tl-phase" href="${href(p)}"><strong>${p.n}. ${p.title}</strong></a><br><span class="src">${p.years}</span></p>`
          : `<p class="tl-phase" tabindex="-1"><strong>${p.n}. ${p.title}</strong><br><span class="src">${p.years} · chapter in preparation</span></p>`).join("")}
        <h3>World real GDP growth</h3>
        <p>${g ? `<strong>${WE.fmt(g[1], 1)}%</strong>${proj ? ' <span class="unverified" title="IMF staff projection, not an outturn">IMF projection</span>' : ""}` : "–"}${rec ? '<br><span class="src">World GDP per person fell this year (WDI).</span>' : ""}</p>
        <p class="src">IMF WEO database, ${growth ? growth.meta.vintage : ""}, NGDP_RPCH, World.</p>
      </div>
      <div>
        <h3>Events in ${year}</h3>
        ${evs.length ? `<ul>${evs.map((e) => `<li><time datetime="${e.d}">${e.d.slice(5)}</time>${e.t} <a class="src" href="${e.url}">${e.src}</a></li>`).join("")}</ul>`
                     : `<p class="src">No events recorded for this year yet. Events are added as each phase chapter is written.</p>`}
      </div>`;
  }

  slider.addEventListener("input", () => { year = +slider.value; update(); });
  document.getElementById("tl-prev").onclick = () => setYear(Math.max(+slider.min, year - 1));
  document.getElementById("tl-next").onclick = () => setYear(Math.min(+slider.max, year + 1));
  let timer = null;
  const play = document.getElementById("tl-play");
  play.onclick = () => {
    if (timer) { clearInterval(timer); timer = null; play.textContent = "Play"; return; }
    if (year >= +slider.max) setYear(+slider.min);
    play.textContent = "Pause";
    timer = setInterval(() => { if (year >= +slider.max) { clearInterval(timer); timer = null; play.textContent = "Play"; return; } setYear(year + 1); }, 900);
  };
})();
