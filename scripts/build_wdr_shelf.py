"""Build wdr-shelf.html: one card per World Development Report, 1999/2000 to 2026.

Titles: the World Bank's WDR archive page (bibliography key wdr-archive).
Summaries: paraphrased from each report's own abstract in the World Bank Documents
and Reports API (raw JSON saved in sources/reports/wdr_wds/, fetched 24 Nov 2026 with
plain curl). The WDR 2017 abstract is a list of topics, so its card paraphrases that list.
Groupings ("strand") are this book's, not the World Bank's.

Run: .venv/bin/python scripts/build_wdr_shelf.py
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(ROOT, *p)
E = html.escape

STRANDS = {
    "poverty": "Poverty and equity",
    "inst": "Institutions and governance",
    "people": "People: health, schooling, work",
    "growth": "Growth, trade and finance",
    "planet": "Environment and risk",
    "tech": "Technology and data",
}

# key, label, title, strands, summary (paraphrase of the abstract), chapters that cite it
WDR = [
    ("1999", "1999/2000", "Entering the 21st Century", ["growth", "inst"],
     "Two forces would shape development in the new century: the integration of the world economy and growing demands for self-government. The report called them globalisation and localisation, and argued that states would have to strike a balance between international and local partners.", []),
    ("2000", "2000/01", "Attacking Poverty", ["poverty"],
     "Poverty is more than low income: it also means powerlessness, having no voice, vulnerability and fear. The report proposed attacking it on three fronts — opportunity, empowerment and security — through action at global, national and local levels.", ["theme-development"]),
    ("2002", "2002", "Building Institutions for Markets", ["inst", "growth"],
     "Markets need institutions that carry information, enforce property rights and contracts, and keep competition alive. These should suit local conditions and be built by experiment, helped by open trade and open flows of information.", []),
    ("2003", "2003", "Sustainable Development in a Dynamic World", ["planet", "poverty"],
     "With three billion more people expected over fifty years, social and environmental strains could derail development unless policies and institutions improved. Many good policies were already known but went unused because of who would win and who would lose from them.", []),
    ("2004", "2004", "Making Services Work for Poor People", ["people", "inst"],
     "Health, schooling, water, sanitation and electricity too often fail poor people, both in access and in quality. The answer is stronger accountability — changing how services are delivered, how the public sector works and how aid is given — not only more money.", []),
    ("2005", "2005", "A Better Investment Climate for Everyone", ["growth", "inst"],
     "Firms of every size drive growth, jobs and tax revenue, and how much they invest depends on the climate governments create: property rights, regulation and tax, infrastructure, finance and labour markets, and corruption. Improving it should be a top priority.", []),
    ("2006", "2006", "Equity and Development", ["poverty"],
     "Unequal opportunities reinforce one another in “inequality traps” and waste talent. Levelling the political and economic playing field, at home and in global markets, supports long-run development and the fight against poverty.", ["theme-development"]),
    ("2007", "2007", "Development and the Next Generation", ["people"],
     "The 1.3 billion people aged 12 to 24 were the largest youth cohort in history, and healthier and better educated than any before. Countries should invest in five transitions — learning, working, health, forming families and citizenship — before population ageing closes the window.", ["theme-demography"]),
    ("2008", "2008", "Agriculture for Development", ["poverty", "growth"],
     "Three in four poor people in developing countries lived in rural areas. Farming was a vital tool for halving poverty and hunger: through smallholder productivity in Africa, rural jobs in Asia, and better care of land and water everywhere.", []),
    ("2009", "2009", "Reshaping Economic Geography", ["growth"],
     "As economies grow, production crowds into cities, coasts and well-connected countries. Growth will be unbalanced, but living standards can still converge, and the way to get both is economic integration.", []),
    ("2010", "2010", "Development and Climate Change", ["planet"],
     "Growth and poverty reduction remained the priority, but climate change makes both harder. Rich countries must cut their emissions; developing countries need more energy, transport and cities without the old carbon intensity, and must adapt to warming that is unlikely to be held below 2°C.", ["theme-energy"]),
    ("2011", "2011", "Conflict, Security, and Development", ["inst"],
     "Violence becomes more likely when institutions fail to protect citizens, curb corruption, give access to justice or create jobs. Legitimate institutions are the key to stability, and outside partners must act faster and stay longer.", []),
    ("2012", "2012", "Gender Equality and Development", ["people", "poverty"],
     "Gender equality is a goal in its own right and also “smart economics”. Growth alone does not close every gap, so policy should target female mortality and education, economic opportunity, women's voice, and the passing of inequality from one generation to the next.", ["theme-demography"]),
    ("2013", "2013", "Jobs", ["people", "growth"],
     "Jobs are the cornerstone of development: they cut poverty, raise productivity and hold societies together. Governments should get the fundamentals right, design labour policy well, and find and unblock the jobs that would do most for development in their country.", ["theme-demography"]),
    ("2014", "2014", "Risk and Opportunity", ["planet", "growth"],
     "After financial crises, disasters and epidemics, the report urged people and institutions to stop fighting crises and start managing risk in advance. Many developing countries came through the 2008 crisis well because of reforms made before it.", []),
    ("2015", "2015", "Mind, Society, and Behavior", ["people", "inst"],
     "People decide by intuition, through the lens of their culture and under social pressure, not as textbook optimisers. Policies built on how people actually choose — defaults, social rewards, framing — can be cheap and effective, and poverty itself shapes decisions.", []),
    ("2016", "2016", "Digital Dividends", ["tech"],
     "Internet access and mobile phones were spreading fast, even among the poorest households, but the wider benefits lagged. They would come only with competition in telecoms, a good business climate, education and health, and good governance.", ["theme-technology"]),
    ("2017", "2017", "Governance and the Law", ["inst"],
     "Why do sound policies so often fail? Their success depends on commitment, coordination and cooperation, which imbalances of power can undermine, and laws on paper differ from how they are applied. Bad governance can persist, but change is possible.", []),
    ("2018", "2018", "Learning to Realize Education's Promise", ["people"],
     "Getting children into school is not enough: in many countries they learn little there, and the disadvantaged learn least. The causes lie in whole education systems, not only in classrooms.", ["theme-development"]),
    ("2019", "2019", "The Changing Nature of Work", ["tech", "people"],
     "Fears that robots would take people's jobs looked, on balance, unfounded. Technology changes the skills employers want and the terms on which people work, so governments should invest in people and extend social protection to all workers, paid for with broader taxes.", ["theme-technology"]),
    ("2020", "2020", "Trading for Development in the Age of Global Value Chains", ["growth"],
     "Global value chains powered the trade boom after 1990, made up almost half of world trade and helped poor countries catch up, but stalled after 2008. They can still lift growth if developing countries reform, rich countries stay open and multilateral cooperation revives.", ["theme-trade"]),
    ("2021", "2021", "Data for Better Lives", ["tech", "inst"],
     "Data can improve poor people's lives but can also harm them. The report called for a new social contract on data: using and reusing data to create value, sharing that value fairly, and building trust that data will not be misused.", []),
    ("2022", "2022", "Finance for an Equitable Recovery", ["growth"],
     "After COVID-19, hidden financial risks — bad loans and unsustainable debts — threatened the recovery as support was withdrawn. The report urged transparent handling of bad loans, insolvency reform, new ways of lending, and better management of government debt.", []),
    ("2023", "2023", "Migrants, Refugees, and Societies", ["people"],
     "About 184 million people live outside their country of nationality. The report's “Match and Motive Matrix” sorts movements by how well migrants' skills fit the destination's needs and why they moved, so policy can differ for each kind.", ["theme-demography", "lens-ssa"]),
    ("2024", "2024", "The Middle-Income Trap", ["growth"],
     "Since the 1970s, income per person in the median middle-income country has stayed below a tenth of the US level. To escape, countries need two shifts: from investment to absorbing technology from abroad (“infusion”), and then to innovation.", ["theme-development"]),
    ("2025", "2025", "Standards for Development", ["inst", "growth"],
     "Standards for measurement, compatibility and quality are invisible infrastructure for trade and technology. Countries should adapt, align and then author standards as they develop, build the institutions that test and certify, and avoid overregulation.", []),
    ("2026", "2026", "The Promise of Artificial Intelligence", ["tech"],
     "Few developing countries can push the AI frontier soon, but adapting available AI to local problems — health, farming, small firms, public services — could achieve in a decade what might otherwise take a century. That needs electricity, connectivity, skills, computing and local-language data, and neither hype nor hysteria.", ["theme-development", "theme-technology"]),
]

SHORT = {"poverty": "Poverty, equity", "inst": "Institutions", "people": "People", "growth": "Growth, trade", "planet": "Environment", "tech": "Technology"}

CH = {"theme-development": "Development", "theme-demography": "Demography and labour", "theme-energy": "Energy, commodities and climate",
      "theme-technology": "Technology and productivity", "theme-trade": "Trade", "lens-ssa": "Sub-Saharan Africa"}


def detail(url):
    """The API gives documents.worldbank.org/curated/en/<id>, which answered 403 on 24 Nov 2026;
    the documentdetail form of the same id answered 200."""
    return "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/" + url.rstrip("/").split("/")[-1]


def wds(key):
    """URL of the English full report (not the overview) in the World Bank Documents and Reports API."""
    files = [key + ".json"] + (["2017b.json"] if key == "2017" else [])
    yr = {"1999": "1999/2000", "2000": "2000/2001"}.get(key, key)
    for f in reversed(files):
        d = json.load(open(J("sources", "reports", "wdr_wds", f)))
        docs = [v for k, v in d["documents"].items() if k != "facets"]
        good = [v for v in docs if "world development report" in v["display_title"].lower() and yr.split("/")[0] in v["display_title"]
                and not re.search(r"overview|summary|concept", v["display_title"], re.I)
                and (key != "2017" or "governance and the law" in v["display_title"].lower())]
        if good:
            return detail(good[0]["url"])
    # WDR 2009: the database holds only the English overview volume (Vol. 2 of 2)
    for v in docs:
        if "world development report " + yr in v["display_title"].lower() and "overview" in v["display_title"].lower():
            return detail(v["url"])
    raise SystemExit("no WDS record for " + key)


cards = []
for key, label, title, strands, text, chs in WDR:
    url = wds(key)
    tags = "".join(f'<span class="wdr-tag" data-s="{s}">{E(STRANDS[s])}</span>' for s in strands)
    cited = (" · ".join(f'<a href="chapters/{c}.html">{E(CH[c])}</a>' for c in chs)) if chs else ""
    cards.append(f'''<article class="wdr-card{' wdr-pre' if key == '1999' else ''}" id="wdr-{key}" data-strands="{' '.join(strands)}">
<p class="wdr-year">WDR {E(label)}</p>
<h3 class="wdr-title"><cite>{E(title)}</cite></h3>
<p class="wdr-text">{E(text)}</p>
<p class="wdr-tags">{tags}</p>
<p class="wdr-links"><a href="{E(url)}">Report record (World Bank)</a>{f' · In this book: {cited}' if cited else ''}</p>
</article>''')

counts = {s: sum(1 for w in WDR[1:] if s in w[3]) for s in STRANDS}
chips = '<button type="button" class="chip-btn" aria-pressed="true" data-s="all">All</button>' + "".join(
    f'<button type="button" class="chip-btn" aria-pressed="false" data-s="{s}">{E(n)}</button>' for s, n in STRANDS.items())

# strip: one cell per report, by strand, so the drift in subjects shows at a glance
strip_rows = "".join(
    f'<tr><th scope="row" title="{E(n)}">{E(SHORT[s])}</th>' + "".join(
        f'<td class="{"on" if s in w[3] else ""}" title="WDR {E(w[1])}: {E(w[2])}">{"●" if s in w[3] else ""}</td>' for w in WDR[1:]) + "</tr>"
    for s, n in STRANDS.items())
strip_head = "".join(f'<th scope="col"><a href="#wdr-{w[0]}" aria-label="WDR {E(w[1])}">{"00/01" if w[0] == "2000" else w[0][2:]}</a></th>' for w in WDR[1:])

page = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WDR shelf · The World Economy 2000–2026</title>
<meta name="description" content="The World Bank's World Development Reports from 1999/2000 to 2026: what each one argued, in brief, with links to the reports and to the chapters that use them.">
<link rel="stylesheet" href="assets/css/book.css">
<link rel="stylesheet" href="assets/css/print.css">
</head>
<body data-root="." data-page="wdr-shelf.html">
<div class="layout">
<nav id="sidebar" class="sidebar"></nav>
<main id="main">
<article class="prose">
<p class="kicker">Tools</p>
<h1>WDR shelf</h1>
<p class="dek">The World Development Report is the World Bank's annual report on one big question of development; the 2008 edition was the thirtieth. Here are the twenty-six from 2000/01 to 2026, with the 1999/2000 edition for context.</p>

<p>Each card gives the report's main argument in a few sentences, paraphrased from the summary the World Bank publishes with it, and links to the report's record in the World Bank's document library and to any chapter of this book that draws on it. Titles are as listed on the World Bank's WDR archive page.<sup class="fn"><a href="#fn1" id="r1">1</a></sup></p>

<h2 id="drift">How the subjects moved</h2>
<p>The grid sorts the reports into six broad strands. The sorting is this book's, not the World Bank's, and most reports fit more than one. Read across a row to see when a subject was in favour: poverty and equity early in the period, people and jobs through the middle, technology and data from 2016.</p>
<div class="table-wrap wdr-strip-wrap wide"><table class="wdr-strip"><caption>World Development Reports by strand, 2000/01–2026 (● = the report's main subject falls in this strand)</caption>
<thead><tr><th scope="col">Strand</th>{strip_head}</tr></thead><tbody>{strip_rows}</tbody></table></div>

<h2 id="shelf">The reports</h2>
<div class="wdr-filter" role="group" aria-label="Show reports by strand">{chips}</div>
<p class="sr-only" id="wdr-count" aria-live="polite"></p>
<div class="wdr-grid wide">
{chr(10).join(cards)}
</div>

<section class="footnotes" aria-label="Notes">
<h2>Notes</h2>
<ol>
<li id="fn1">Titles: World Bank, “WDR Reports” (archive page), accessed 23 November 2026, <a href="https://www.worldbank.org/en/publication/wdr/wdr-archive">worldbank.org</a>. The edition count is from the WDR 2008 abstract, which calls it “the 30th in the series”. Summaries: paraphrased from the abstracts in the World Bank Documents and Reports database (search.worldbank.org/api/v3/wds), retrieved 24 November 2026; the WDR 2017 abstract is a list of the report's topics, and its card paraphrases those. The full reports and overviews cited in the chapters are listed on the <a href="sources.html">sources page</a>. <a href="#r1">↩</a></li>
</ol>
</section>
</article>
</main>
</div>
<script src="assets/js/book-data.js"></script>
<script src="assets/js/glossary-data.js"></script>
<script src="assets/js/book.js"></script>
<script>
(function () {{
  const btns = document.querySelectorAll(".wdr-filter .chip-btn"), cards = document.querySelectorAll(".wdr-card");
  btns.forEach((b) => b.onclick = () => {{
    btns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    let n = 0;
    cards.forEach((c) => {{ const show = b.dataset.s === "all" || c.dataset.strands.split(" ").includes(b.dataset.s); c.hidden = !show; if (show) n++; }});
    document.getElementById("wdr-count").textContent = n + " reports shown";
  }});
}})();
</script>
</body>
</html>
'''
open(J("wdr-shelf.html"), "w").write(page)
print(len(WDR), "cards;", counts)
