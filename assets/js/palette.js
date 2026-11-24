/* Fixed colour assignments: the same economy is the same colour on every chart.
   Hues are the validated reference categorical palette (light / dark steps).
   Colour never carries identity alone: every chart has a legend, direct labels
   for <= 4 series, and a dash pattern per entity as a second channel. */
(function () {
  const H = {
    blue:    ["#2a78d6", "#3987e5"],
    orange:  ["#eb6834", "#d95926"],
    aqua:    ["#1baf7a", "#199e70"],
    yellow:  ["#eda100", "#c98500"],
    magenta: ["#e87ba4", "#d55181"],
    green:   ["#008300", "#0ca30c"],
    violet:  ["#6250d6", "#9085e9"],
    red:     ["#e34948", "#e66767"],
    ink:     ["#52514e", "#c3c2b7"],   // World / totals: neutral ink, not a hue
    navy:    ["#184f95", "#86b6ef"],   // blue ramp steps 600 / 250
  };
  // entity key -> [hue, dash]; dash: "solid" | "dashed" | "dotted"
  const ENTITY = {
    WLD: ["ink", "solid"],     G001: ["ink", "solid"],
    USA: ["blue", "solid"],    US: ["blue", "solid"],
    EA: ["orange", "solid"],   G163: ["orange", "solid"], XM: ["orange", "solid"], EMU: ["orange", "solid"],
    CHN: ["red", "solid"],     CN: ["red", "solid"],
    JPN: ["violet", "solid"],  JP: ["violet", "solid"],
    IND: ["aqua", "solid"],    IN: ["aqua", "solid"],
    GBR: ["magenta", "solid"], GB: ["magenta", "solid"],
    DEU: ["yellow", "solid"],  DE: ["yellow", "solid"],
    BRA: ["green", "solid"],   BR: ["green", "solid"],
    G110: ["navy", "dashed"],                      // Advanced economies
    G200: ["green", "dashed"], EMDE: ["green", "dashed"],  // Emerging market & developing economies
    G201: ["yellow", "dashed"],                    // Low-income developing countries
    G603: ["magenta", "dashed"], SSF: ["magenta", "dashed"], // Sub-Saharan Africa
    ITA: ["green", "dotted"],  IT: ["green", "dotted"],
    ESP: ["red", "dotted"],    ES: ["red", "dotted"],
    GRC: ["aqua", "dotted"],   GR: ["aqua", "dotted"],
    PRT: ["violet", "dotted"], PT: ["violet", "dotted"],
    IRL: ["yellow", "dotted"], IE: ["yellow", "dotted"],
    FRA: ["navy", "dotted"],   FR: ["navy", "dotted"],
    RUS: ["violet", "dashed"], MEX: ["aqua", "dashed"], IDN: ["orange", "dashed"],
    TUR: ["red", "dashed"],    ZAF: ["blue", "dashed"], KOR: ["blue", "dotted"],
    SAU: ["yellow", "solid"],  NGA: ["green", "dotted"],
    ETH: ["orange", "dotted"], KEN: ["navy", "solid"], GHA: ["magenta", "dotted"],
    AGO: ["ink", "dashed"],    ZMB: ["red", "dotted"],  CIV: ["violet", "dotted"],
  };
  const FALLBACK = ["blue", "orange", "aqua", "yellow", "magenta", "green", "violet", "red"];
  const DASHES = ["solid", "dashed", "dotted"];

  function dark() {
    const t = document.documentElement.getAttribute("data-theme");
    if (t) return t === "dark";
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  function hash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; }

  window.WE = window.WE || {};
  WE.colour = function (key, i) {
    const e = ENTITY[key];
    const hue = e ? e[0] : FALLBACK[(i ?? hash(key)) % 8];
    return H[hue][dark() ? 1 : 0];
  };
  WE.dash = function (key, i) {
    const e = ENTITY[key];
    return e ? e[1] : DASHES[Math.floor((i ?? hash(key)) / 8) % 3];
  };
  // For pickers that can show any economy (the explorer): economies with a fixed style keep it;
  // the others take, in the order picked, the first hue-and-dash pair not already on the chart.
  WE.assign = function (keys) {
    const used = new Set(), out = {};
    keys.forEach((k) => { if (ENTITY[k]) { out[k] = ENTITY[k]; used.add(ENTITY[k].join()); } });
    keys.forEach((k) => {
      if (out[k]) return;
      const pair = DASHES.flatMap((d) => FALLBACK.map((h) => [h, d])).find((p) => !used.has(p.join()));
      out[k] = pair || ["ink", "dotted"]; used.add(out[k].join());
    });
    return out;
  };
  WE.hue = (name) => H[name][dark() ? 1 : 0];
  WE.isDark = dark;
})();
