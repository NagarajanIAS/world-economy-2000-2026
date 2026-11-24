/* Page shell: top bar, sidebar contents, reading progress, theme, footnote and
   glossary popovers, search, keyboard shortcuts. Every page includes this file. */
(function () {
  const WE = (window.WE = window.WE || {});
  const body = document.body;
  const ROOT = body.dataset.root || ".";            // "." on root pages, ".." in chapters/
  const here = body.dataset.page || "";              // e.g. "chapters/phase-3.html"
  const url = (p) => (ROOT === "." ? p : ROOT + "/" + p);
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
                  set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };

  // ---------- theme (set early)
  const saved = store.get("we-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  function toggleTheme() {
    const cur = document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next); store.set("we-theme", next);
    themeBtn.textContent = next === "dark" ? "Light mode" : "Dark mode";
    document.dispatchEvent(new Event("we-theme"));
  }

  // ---------- top bar
  const bar = document.createElement("header");
  bar.className = "topbar";
  bar.innerHTML = `<a class="skip" href="#main">Skip to content</a>
    <button class="iconbtn menu-btn" type="button" aria-controls="sidebar" aria-expanded="false">Contents</button>
    <a class="brand" href="${url("index.html")}">The World Economy <span>2000–2026</span></a>
    <span class="spacer"></span>
    <button class="iconbtn search-btn" type="button" aria-haspopup="dialog" title="Search (/)">Search <kbd>/</kbd></button>
    <button class="iconbtn theme-btn" type="button"></button>`;
  body.prepend(bar);
  const prog = document.createElement("div"); prog.className = "progress"; prog.setAttribute("aria-hidden", "true"); bar.after(prog);
  const themeBtn = bar.querySelector(".theme-btn");
  const isDarkNow = () => (document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")) === "dark";
  themeBtn.textContent = isDarkNow() ? "Light mode" : "Dark mode";
  themeBtn.onclick = toggleTheme;
  const menuBtn = bar.querySelector(".menu-btn");
  menuBtn.onclick = () => { const o = body.classList.toggle("nav-open"); menuBtn.setAttribute("aria-expanded", String(o)); };

  // ---------- sidebar
  const side = document.getElementById("sidebar");
  if (side && WE.BOOK) {
    side.setAttribute("aria-label", "Book contents");
    side.innerHTML = WE.BOOK.map((g) => `<h2>${g.part}</h2><ol>${g.items.map((it) => {
      const cur = it.href === here;
      const inner = it.ready ? `<a href="${url(it.href)}"${cur ? ' aria-current="page"' : ""}>${it.label}${it.sub ? `<span class="sub">${it.sub}</span>` : ""}</a>`
                             : `<span class="todo">${it.label}${it.sub ? `<span class="sub">${it.sub}</span>` : ""}</span>`;
      return `<li>${inner}${cur ? '<ol class="onpage"></ol>' : ""}</li>`;
    }).join("")}</ol>`).join("");
    const onpage = side.querySelector(".onpage");
    const heads = [...document.querySelectorAll("main h2[id]")];
    if (onpage) {
      onpage.innerHTML = heads.map((h) => `<li><a href="#${h.id}">${h.textContent}</a></li>`).join("");
      const links = [...onpage.querySelectorAll("a")];
      const spy = () => {
        let idx = 0; heads.forEach((h, i) => { if (h.getBoundingClientRect().top < 120) idx = i; });
        links.forEach((a, i) => a.classList.toggle("active", i === idx));
      };
      addEventListener("scroll", spy, { passive: true }); spy();
    }
    side.addEventListener("click", (e) => { if (e.target.closest("a")) body.classList.remove("nav-open"); });
  }

  // ---------- reading progress
  const onScroll = () => {
    const h = document.documentElement; const max = h.scrollHeight - h.clientHeight;
    prog.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + "%";
  };
  addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // ---------- popovers (footnotes + glossary)
  let pop = null;
  function showPop(anchor, html) {
    hidePop();
    pop = document.createElement("div"); pop.className = "pop"; pop.setAttribute("role", "tooltip"); pop.innerHTML = html;
    document.body.appendChild(pop);
    const r = anchor.getBoundingClientRect();
    const left = Math.min(scrollX + r.left, scrollX + innerWidth - pop.offsetWidth - 12);
    pop.style.left = Math.max(8, left) + "px";
    pop.style.top = (scrollY + r.bottom + 6) + "px";
  }
  function hidePop() { if (pop) { pop.remove(); pop = null; } }
  document.querySelectorAll("sup.fn a").forEach((a) => {
    const id = a.getAttribute("href").slice(1);
    const show = () => { const li = document.getElementById(id); if (li) showPop(a, li.innerHTML.replace(/<a[^>]*class="back"[^>]*>.*?<\/a>/, "")); };
    a.addEventListener("mouseenter", show); a.addEventListener("focus", show);
    a.addEventListener("mouseleave", hidePop); a.addEventListener("blur", hidePop);
  });
  document.querySelectorAll(".term").forEach((t) => {
    const key = t.dataset.term; const g = (WE.GLOSSARY || {})[key];
    if (!g) { console.warn("Glossary term missing:", key); return; }
    t.setAttribute("tabindex", "0"); t.setAttribute("aria-describedby", "");
    const show = () => showPop(t, `<strong>${g.term}</strong>${g.def} <a href="${url("glossary.html#" + key)}">Glossary</a>`);
    t.addEventListener("mouseenter", show); t.addEventListener("focus", show);
    t.addEventListener("mouseleave", () => setTimeout(() => { if (pop && !pop.matches(":hover")) hidePop(); }, 200));
    t.addEventListener("blur", () => setTimeout(() => { if (pop && !pop.contains(document.activeElement)) hidePop(); }, 150));
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hidePop(); });

  // ---------- search
  const dlg = document.createElement("dialog");
  dlg.className = "search-dialog"; dlg.setAttribute("aria-label", "Search the book");
  dlg.innerHTML = `<input type="search" placeholder="Search the book…" aria-label="Search terms"><ul class="search-results" role="list"></ul><p class="search-hint">Press Esc to close. Results cover the chapters, the glossary, the WDR shelf and the tool pages.</p>`;
  document.body.appendChild(dlg);
  let ms = null;
  function ensureIndex() {
    return new Promise((res) => {
      if (ms) return res();
      const go = () => {
        ms = new MiniSearch({ fields: ["title", "text"], storeFields: ["title", "href", "section"], searchOptions: { boost: { title: 3 }, prefix: true, fuzzy: 0.15 } });
        ms.addAll(WE.SEARCH || []); res();
      };
      const need = [];
      if (!window.MiniSearch) need.push("assets/vendor/minisearch.min.js");
      if (!WE.SEARCH) need.push("assets/js/search-index.js");
      if (!need.length) return go();
      let n = need.length;
      need.forEach((p) => { const s = document.createElement("script"); s.src = url(p); s.onload = () => { if (--n === 0) go(); }; document.head.appendChild(s); });
    });
  }
  const input = dlg.querySelector("input"), out = dlg.querySelector(".search-results");
  input.addEventListener("input", () => {
    const q = input.value.trim();
    if (!q || !ms) { out.innerHTML = ""; return; }
    out.innerHTML = ms.search(q).slice(0, 12).map((r) => `<li><a href="${url(r.href)}">${r.title}<small>${r.section || ""}</small></a></li>`).join("") || `<li class="search-hint">No matches.</li>`;
  });
  // Esc inside a search box only clears it in some browsers, so close explicitly; a click on the backdrop closes too
  dlg.addEventListener("keydown", (e) => { if (e.key === "Escape") { e.preventDefault(); dlg.close(); } });
  dlg.addEventListener("click", (e) => { if (e.target === dlg) dlg.close(); });
  function openSearch() { ensureIndex().then(() => { dlg.showModal(); input.focus(); }); }
  bar.querySelector(".search-btn").onclick = openSearch;

  // ---------- prev / next and keyboard
  const ready = (WE.BOOK || []).flatMap((g) => g.items).filter((i) => i.ready && i.href.startsWith("chapters/"));
  const idx = ready.findIndex((i) => i.href === here);
  const pager = document.querySelector(".pager");
  if (pager && idx >= 0) {
    const p = ready[idx - 1], n = ready[idx + 1];
    pager.innerHTML = `<span>${p ? `<a href="${url(p.href)}" rel="prev"><small>Previous</small>${p.label}</a>` : ""}</span><span style="text-align:right">${n ? `<a href="${url(n.href)}" rel="next"><small>Next</small>${n.label}</a>` : `<a href="${url("index.html")}"><small>Back to</small>Home and timeline</a>`}</span>`;
  }
  document.addEventListener("keydown", (e) => {
    if (e.target.matches("input, textarea, select") || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === "/") { e.preventDefault(); openSearch(); }
    if (e.key === "[" && idx > 0) location.href = url(ready[idx - 1].href);
    if (e.key === "]" && idx >= 0 && idx < ready.length - 1) location.href = url(ready[idx + 1].href);
  });
})();
