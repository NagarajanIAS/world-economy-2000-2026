# Reading notes: lens 'Sub-Saharan Africa' — part A (region, debt, poverty, trade) (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL -o file -w '%{http_code}' URL` (default user-agent, no custom headers, no
cookies), with `--max-time 120` and a 3-second pause after each request; every request and its HTTP status is logged in the scratchpad
file `ssa_a_scripts/fetchlog.txt`. Listing pages used: the IMF REO landing page https://www.imf.org/en/Publications/REO (200), which links
the SSA issue pages for May 2005, Oct 2005, Fall 2006, Apr 2007, Oct 2014, May 2017, Jun 2020 and every edition from Oct 2020 to Apr 2026
(the SSA listing https://www.imf.org/en/Publications/REO/SSA itself returned 404 "Blob not found", also as `index.md`/`index.json` and in
lower case); the issue pages (200) gave the PDF links. Editions not linked there (Oct 2009, Oct 2013, Oct 2026) come from GUESSED URLs built
on the IMF file-naming patterns, each confirmed from the cover/title page; failed guesses are under Not obtained. World Bank: the Documents &
Reports search API (search.worldbank.org/api/v2/wds, JSON, 200) and the Open Knowledge Repository (OKR) DSpace API
(openknowledge.worldbank.org/server/api/discover/search/objects and /core/items/{uuid}/bundles, 200), which gave the bitstream links;
the World Bank Poverty and Inequality Platform API (api.worldbank.org/pip/v1, 200). AfCFTA: the AU treaty page and its signature/ratification
list (au.int, 200) and the AfCFTA Secretariat "About" page (au-afcfta.org, 200; URL GUESSED). Downloads are in the scratchpad folder
`lens_ssa_dl/a/` with subfolders `imf/` (listing and issue pages), `imf/pdf/` (REOs), `imf/fs/` (factsheet, FAQ, G20 statement), `wb/`,
`au/`, `oth/` (failed Paris Club and G20 Information Centre attempts). PDFs were converted with `pdftotext` (plain and `-layout`) into
`lens_ssa_dl/a_txt/`; HTML was stripped of tags and read as text. Python that read downloads was run with `python3 -I` from scripts kept in
the scratchpad folder `ssa_a_scripts/`. Quotes are verbatim and under 15 words; the script `ssa_a_scripts/q.py` checked all 15 against the
converted text (whitespace-, quote-, dash- and line-end-hyphen-normalised): 15 of 15 matched. Everything else is paraphrase. The April 2007
REO was obtained only in its French translation and is paraphrased in English (no quotes from it). Shares, differences and forecast-vs-outturn
gaps are marked "own arithmetic". Outturns come from `data/clean/weo/NGDP_RPCH.json` (WEO October 2026 vintage, published 13 Oct 2026; series
G603 = Sub-Saharan Africa; `last_actual_default` = 2025, so 2026–27 are IMF projections).

Printed-page offsets (printed = PDF − n; roman-numbered front matter is cited with its roman number or as "PDF p."):
REO Apr 2007 (French): −8. REO Oct 2009: −8. REO Oct 2013: −11. REO Oct 2014: −11. REO Apr 2017: −10. REO Oct 2020: −7 (Executive
Summary p. v = PDF 6). REO Apr 2023: −9. REO Apr 2026: −9. REO Update Oct 2026: printed = PDF (pp. 1–9). Africa's Pulse Oct 2014 (vol. 10):
printed = PDF. Africa's Pulse No. 22 (Oct 2020): −10. Africa's Pulse No. 31 (Apr 2025): −8. Global Findex 2025: −38 for the main text
(p. 100 = PDF 138); Executive Summary p. xxiii = PDF 25. G20 statement of 13 Nov 2020: printed = PDF (pp. 1–5).

Item labels:
- SA-REO-n: IMF Regional Economic Outlook: Sub-Saharan Africa (nine editions, 2007–2026).
- SA-IMF-n: other IMF documents (HIPC factsheet; sovereign-debt Q&A; G20 Common Framework statement hosted by the IMF).
- SA-WB-n: World Bank (Africa's Pulse ×3; HIPC brief; Global Findex 2025; PIP poverty data).
- SA-AU-n: African Union / AfCFTA Secretariat.
- SA-OTH-n: none obtained (Paris Club and G20 Information Centre refused or returned 404; see Not obtained).

Abbreviations: AfCFTA = African Continental Free Trade Area; CEMAC = Central African Economic and Monetary Community; CF = G20 Common
Framework for Debt Treatments beyond the DSSI; DSA = debt sustainability analysis; DSSI = Debt Service Suspension Initiative; FCS = fragile
and conflict-affected situations; HIPC = Heavily Indebted Poor Countries; LIC = low-income country; LIC DSF = IMF–World Bank Low-Income
Country Debt Sustainability Framework; MDRI = Multilateral Debt Relief Initiative; ODA = official development assistance; PIP = Poverty and
Inequality Platform; PPG = public and publicly guaranteed; REO = Regional Economic Outlook; SSA = Sub-Saharan Africa; WAEMU = West African
Economic and Monetary Union.

Note on regional definitions: the IMF's SSA (WEO group G603, 45 countries) excludes Mauritania, Somalia and Sudan, which the IMF puts in
the Middle East and Central Asia; the World Bank's SSA includes them. Some REOs report an "African Department" aggregate and a "WEO
definition" aggregate side by side (SA-REO-1, SA-REO-2), and SA-REO-3 gives a total with and without South Sudan. Africa's Pulse growth
figures use World Bank definitions and weights, so they are not strictly comparable with G603 outturns.

---

## IMF Regional Economic Outlook: Sub-Saharan Africa

### SA-REO-1. IMF, *Perspectives économiques régionales: Afrique subsaharienne*, April 2007 (French translation of *Regional Economic Outlook: Sub-Saharan Africa*, April 2007), World Economic and Financial Surveys
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2017/01/07/regional-economic-outlook-april-2007-sub-saharan-african-20257
(200; "Published: April 12, 2007"; the page links only the French PDF). PDF:
https://www.imf.org/-/media/websites/imf/imported-publications/external/pubs/ft/reo/2007/afr/fra/_afrf.pdf (200; 138 pp.; cataloguing page
says "French translation of: Regional Economic Outlook: Sub-Saharan Africa", ISBN 978-1-58906-639-7). Accessed 23 Nov 2026. Data as of
29 March 2007 (Preface, PDF p. 7). Read in French; paraphrased only.
- p. 1 (Overview, "Vue d'ensemble"): a third year in a row of growth of about 5–6 percent; growth above 5 percent in 2006 and expected at
  6–7 percent in 2007, mainly from higher output in oil producers; over half of non-oil countries grew 5 percent or more in 2006. Trend
  growth is slowly approaching the 7 percent seen as needed for the MDG income-poverty goal. Governments raised poverty-reducing spending,
  partly with resources freed by debt relief. Commodity producers saved much of their windfall, unlike in earlier booms.
- p. 1–2: pressure to spend more on roads and power has grown with promised extra aid (not yet delivered) and HIPC and MDRI debt relief;
  public financial management must improve. Trade with Asia, especially China, has grown dramatically, though the US and EU still take
  two and a half times Asia's share of the region's exports; exports remain undiversified (oil and commodities); AGOA helped garment exports.
- p. 2: governments are turning more to domestic debt markets to fund deficits.
- p. 3 (ch. II): growth was 5.4 percent in 2006 after 6 percent in 2004 and 2005; investment and productivity contributed more.
- p. 4 (Table 2.1): Africa Department aggregate real GDP 2002–07: 3.5, 4.0, 6.0, 6.0, 5.4 (est.), **6.7 (projection 2007)**; oil exporters
  11.6 in 2007; reserves 6.8 months of imports in 2007. Memo line "Sub-Saharan Africa (WEO definition)": 3.7, 4.2, 6.0, 6.0, 5.7, **6.8**.
  Fiscal balance incl. grants +4.1 percent of GDP in 2006 (oil windfall).

### SA-REO-2. IMF, *Regional Economic Outlook: Sub-Saharan Africa — Weathering the Storm*, October 2009, World Economic and Financial Surveys
URL: https://www.imf.org/external/pubs/ft/reo/2009/afr/eng/sreo1009.pdf (GUESSED; cover reads "Regional Economic Outlook Sub-Saharan Africa
Weathering the Storm OCT 09"; ISBN 978-1-58906-857-5). HTTP 200. 102 pp. Accessed 23 Nov 2026. Data as of 17 September 2009 (Table 1.1 note).
- p. 1 (Main Messages): after nearly a decade of strong performance, growth expected to slow to about 1 percent in 2009; exports slashed,
  capital flows disrupted; oil exporters and middle-income countries hit hardest. Prudent policies in the upswing gave room to absorb the
  shock; protectionism largely avoided. Recovery to 4 percent in 2010 and more than 5 percent later expected.
- p. 3: output grew about 6½ percent a year in 2002–07, "the highest rate in more than 30 years"; per capita income to fall about 1 percent
  in 2009, the first drop in a decade. The fiscal balance incl. grants swung from a surplus of 1¼ percent of GDP (2008) to an expected
  deficit of 4¾ percent (2009). Median-country growth falls only from 4¾ (2002–07) to 2½ percent (2009).
- p. 4 (Table 1.1, AFR aggregate excl. Zimbabwe): real GDP 2005–10: 6.2, 6.4, 6.9, 5.5, 1.1 (proj.), **4.1 (proj. 2010)**; WEO definition
  6.2, 6.6, 7.0, 5.5, 1.3, **4.1**. Oil price assumption $61.5 (2009), $76.5 (2010).
- p. 5: growth projected at ½ point lower in 2009 and ¼ higher in 2010 than in the April 2009 REO. Past global recoveries (after 1975,
  1982, 1991) left Africa behind; this time more shock absorbers and no trade restrictions.
- p. 40 (ch. 2): HIPC and MDRI relief: US$73 billion (2008 present value) committed to 28 of the 30 HIPC-eligible SSA countries;
  post-completion-point debt cut by as much as 95 percent (excluding traditional relief). In DSAs mostly from 2008, 61 percent of SSA
  countries were at low or moderate risk of debt distress, the rest at high risk or in distress. p. 34 (PDF 42): high-growth non-oil
  exporters were the main beneficiaries of debt forgiveness, especially after the MDRI began in 2006.

### SA-REO-3. IMF, *Regional Economic Outlook: Sub-Saharan Africa — Keeping the Pace*, October 2013, World Economic and Financial Surveys
URL: https://www.imf.org/-/media/websites/imf/imported-full-text-pdf/external/pubs/ft/reo/2013/afr/eng/_sreo1013.pdf (GUESSED on the pattern of
the October 2014 link; cover reads "Regional Economic Outlook Sub-Saharan Africa Keeping the Pace OCT 13"; ISBN 978-1-47555-341-3). HTTP 200.
127 pp. Accessed 23 Nov 2026.
- p. viii (In Brief): output projected to grow 5 percent in 2013 and 6 percent in 2014, led by investment; softer 2013 from higher financing
  costs, slower emerging markets and weaker commodity prices. Wider current-account deficits since 2008 mostly reflect investment and are
  largely FDI-financed. External debt, cut sharply in LICs by debt forgiveness, "remains low by historical standards in most countries".
- p. 1: revisions against the May 2013 REO are modest (−0.7 point in 2013, −0.1 in 2014).
- p. 3 (Table 1.1): SSA (total) 2004–08 average 6.5; 2009 2.6; 2010 5.6; 2011 5.5; 2012 4.9; 2013 5.0; **2014 6.0**; excluding South Sudan:
  2012 5.1, 2013 4.8, **2014 5.7**. South Africa 2.0 (2013), 2.9 (2014).
- p. 6 (Table 1.2, debt risk index from DSAs): SSA total 17 countries at low risk, 19 moderate, 6 high, 2 in debt distress; public debt 33.0
  percent of GDP (2012).
- ix (In Brief, ch. 3) and p. 55 (PDF 66): frontier markets became more integrated; many countries issued sovereign bonds, many for the
  first time (the April 2013 REO had a chapter on international sovereign bond issuance — not read). p. 72 (PDF 83): Ghana sold a $1 billion
  10-year bond in August 2013 at 8 percent; its first 10-year Eurobond (2007) was four times oversubscribed. p. 73 (PDF 84): Zambia issued
  its first sovereign Eurobond in September 2012 ($750 million, 10-year).

### SA-REO-4. IMF, *Regional Economic Outlook: Sub-Saharan Africa — Staying the Course*, October 2014, World Economic and Financial Surveys
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2015/10/20/regional-economic-outlook-october-2014-staying-the-course-41855 (200;
datePublished 2014-10-20). PDF: https://www.imf.org/-/media/websites/imf/imported-full-text-pdf/external/pubs/ft/reo/2014/afr/eng/_sreo1014.pdf
(200; 112 pp.; ISBN 978-1-49838-645-6). Accessed 23 Nov 2026.
- Executive Summary (PDF p. 10) and p. 1: growth about 5 percent in 2014 and **5¾ percent in 2015**; low-income countries 6½–6¾ percent in
  2014–15; Nigeria 7–7¼ percent; Nigeria's national-accounts rebasing almost doubled the services share. The Ebola outbreak in Guinea,
  Liberia and Sierra Leone overshadows the picture; Ghana and (until recently) Zambia face large imbalances. Risks: fiscal vulnerabilities
  in some frontier economies (recurrent spending), slower emerging markets, tighter global finance.
- p. 4: "Sovereign spreads have reverted to postglobal crisis lows across the board", Ghana excepted.
- p. 5: Eurobond issuance included maiden issues by Côte d'Ivoire and Kenya; total issuance incl. South Africa nearly $7 billion so far
  in 2014, above the record $6.5 billion of 2013. p. 3: goods exports close to 30 percent of regional GDP, about 10 points more than in the
  mid-1990s, the rise mostly from trade with China and India.
- p. 17 (Box 1.1): Ghana's 2007 Eurobond projected to cost about 60 percent more in NPV terms than an equivalent domestic bond once
  depreciation is counted; Zambia's 2012 10-year Eurobond ($750 million at 5.6 percent) compares with a 15.7 percent domestic yield.

### SA-REO-5. IMF, *Regional Economic Outlook: Sub-Saharan Africa — Restarting the Growth Engine*, April 2017 (issue page dated 9 May 2017; cover "APR 17"), World Economic and Financial Surveys
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2017/05/03/sreo0517 (200). PDF:
https://www.imf.org/-/media/files/publications/reo/afr/2017/may/pdf/sreo0517.pdf (200; 122 pp.; ISBN 978-1-47557-446-3). Accessed 23 Nov 2026.
(No 2016 edition obtained; this issue gives the account of the 2016 slump.)
- Executive Summary (PDF p. 9): in 2016 growth slowed in about two-thirds of countries (83 percent of regional GDP) to about 1½ percent,
  the worst in more than two decades; modest rebound to 2½ percent in 2017, driven by one-offs in Nigeria, Angola and South Africa.
- p. 1: growth averaged 1.4 percent in 2016, "the lowest in two decades"; **2.6 percent expected in 2017**; growth will barely exceed
  population growth. Oil exporters (Angola, Nigeria, CEMAC) slow to adjust; Ghana, Zambia, Zimbabwe have wider deficits; in Côte d'Ivoire,
  Kenya and Senegal debt is rising and arrears emerging.
- p. 9: debt at around or above 50 percent of GDP in many non-resource-intensive countries; oil exporters' debt service rose from 8 percent
  of revenue (2013) to 57 percent (2016) — Nigeria 66, Angola 60; the risk of debt distress has risen in a number of countries since 2013.

### SA-REO-6. IMF, *Regional Economic Outlook: Sub-Saharan Africa — A Difficult Road to Recovery*, October 2020, World Economic and Financial Surveys
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2020/10/22/regional-economic-outlook-sub-saharan-africa (200). PDF:
https://www.imf.org/-/media/files/publications/reo/afr/2020/october/english/text.pdf (429 at first attempt, 200 on retry; 32 pp.; ISBN
978-1-5135-5760-1). Accessed 23 Nov 2026.
- p. v (Executive Summary): activity in 2020 projected to contract 3.0 percent, "still the worst outcome on record"; real per capita income
  down 5.3 percent, back to 2013 levels; **2021 growth 3.1 percent**. Financing gap of about $290 billion if private inflows stay below
  pre-crisis levels.
- p. 1: many countries will not regain 2019 output until 2022–24. p. 2 (PDF 9): SSA borrowers had yet to return to the Eurobond market.
- p. 6: the region entered COVID with less fiscal space than at the start of the global financial crisis: 16 countries at high risk of or
  in debt distress in 2019 (Figure 1.9, PRGT-eligible LICs).
- p. 16 (Box 1.2): after HIPC and MDRI, debt fell until the late 2000s, then rose from about 35 percent of GDP (early 2010s) to about 55
  percent (mid-2010s); projected 65 percent by end-2020. Debt service to revenue about 27 percent vs 22 percent pre-COVID projection.
  Per the latest LIC DSAs, 11 SSA countries at high risk of debt distress and 6 in distress. The DSSI deferred payments without cutting
  their net present value; Paris Club/non-Paris Club cooperation should be widened into a platform to resolve debt problems.
- p. 17 (Box 1.3): external financing needs about $890 billion in 2020–23 (about 55 percent of 2020 GDP); gap $130–410 billion, central
  estimate $290 billion; almost $130 billion for PRGT-eligible countries.

### SA-REO-7. IMF, *Regional Economic Outlook: Sub-Saharan Africa — The Big Funding Squeeze*, April 2023, World Economic and Financial Surveys
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2023/04/14/regional-economic-outlook-for-sub-saharan-africa-april-2023 (200).
PDF: https://www.imf.org/-/media/files/publications/reo/afr/2023/april/english/text.pdf (200; 29 pp.; ISBN 979-8-4002-3564-1). Accessed 23 Nov 2026.
- p. 1 (Executive Summary): borrowing costs up and exchange rates under pressure; "no country has been able to issue a Eurobond since spring
  2022". Public debt and inflation at levels not seen in decades; double-digit inflation in half the countries; 132 million acutely
  food-insecure in 2022. Growth to fall to 3.6 percent in 2023.
- p. 2: growth 3.6 percent in 2023, **4.2 percent in 2024**.
- p. 3: spreads rose to three times the emerging-market average; Eurobond issuance fell from $14 billion (2021) to $6 billion in Q1 2022;
  interest payments 11 percent of revenue (excl. grants) for the median country in 2022, about triple the median advanced economy, after
  doubling over a decade; aid decline pushed countries to costlier market finance; China inflows fell.
- p. 4: public debt 56 percent of GDP in 2022, levels last seen in the early 2000s; 19 of the region's 35 LICs in or at high risk of debt
  distress in 2022; about 40 percent of debt external (2021). p. 5: 35 percent of the population below $2.15 a day (2019).
- p. 8: Eurobond repayments of about $6 billion due in 2024 and $7 billion in 2025 (Figure 7); interest bills above 50 percent of revenue in
  a few cases. p. 9: four SSA countries seeking or in Common Framework restructuring — Chad, Ethiopia, Zambia and, most recently, Ghana;
  creditor coordination has been hard and slower than expected.

### SA-REO-8. IMF, *Regional Economic Outlook: Sub-Saharan Africa — Hard-Won Gains Under Pressure*, April 2026
Issue page: https://www.imf.org/en/publications/reo/ssa/issues/2026/04/16/regional-economic-outlook-for-sub-saharan-africa-april-2026 (200).
PDF: https://www.imf.org/-/media/files/publications/reo/afr/2026/april/english/text.pdf (200; 52 pp.; ISBN 979-8-2290-4217-8 paper). Accessed
23 Nov 2026. Team led by Saad Quayyum (p. v).
- p. 1: 2025 growth about 4.5 percent, "the fastest in a decade"; war in the Middle East has raised oil, gas, fertilizer and shipping
  costs; 2026 growth cut 0.3 point from pre-war projections to 4.3 percent.
- p. 2: growth 4.5 percent in 2025 from 4.2 in 2024; above 6 percent in 10 economies; median inflation 3.4 percent end-2025 (4.8 end-2024);
  median deficit 3.0 percent of GDP and median public debt down from 57.2 (2024) to 53.1 percent (2025); Ethiopia, Ghana and Zambia made
  significant progress on debt restructuring; rating upgrades for Ghana, South Africa and Zambia.
- p. 3: Eurobond issuance $14 billion in 2025 and $5.5 billion in Jan–Feb 2026. p. 4: **4.3 percent in 2026, 4.4 percent in 2027**.
- p. 5: medium-term per capita growth 2.3 percent vs 3.6 percent in other EMDEs (1.8 percent in resource-intensive economies).
- p. 7: more than one-third of the region at high risk of, or already in, debt distress; in 21 countries deficits exceed the
  debt-stabilising level; higher interest rates and lower ODA raise interest/revenue; in WAEMU government debt is 43 percent of bank assets.
- pp. 17–19 (ch. 2, aid cuts): ODA nearly 3 percent of regional GDP in 2024, more than twice the next region; 6.4 percent of GDP in LICs;
  grants fell from 97 percent of ODA (2010) to 68 percent (2024); 2025 bilateral aid to Africa down an estimated 16–28 percent ($4–7
  billion); Chinese lending to Africa has turned net negative.

### SA-REO-9. IMF, *Regional Economic Outlook Update: Sub-Saharan Africa — Resilient Growth, Clouded Outlook*, October 2026
URL: https://www.imf.org/-/media/files/publications/reo/afr/2026/october/english/text.pdf (GUESSED on the April 2026 pattern; page 1 reads
"REGIONAL ECONOMIC OUTLOOK UPDATE SUB-SAHARAN AFRICA OCTOBER 2026 Resilient Growth, Clouded Outlook"; no issue page found on the REO landing
page). HTTP 200. 9 pp. Accessed 23 Nov 2026. Prepared under Mlachila, Slavov and Sy (p. 9, endnote 1).
- p. 1: growth **4.5 percent in both 2026 and 2027** (0.2 point above April for 2026), after 4.5 in 2025; oil exporters 4.1, other
  resource-intensive 3.8, non-resource-intensive 6.0 percent in 2026; median inflation 3.4 (2025) → 4.3 (2026) → 5.0 percent (2027).
  "Risks remain decidedly tilted to the downside". Oil $96 a barrel (2026), $87 (2027); fertilizer prices +26 percent in 2026.
- p. 2: Ethiopia, Ghana and Zambia have progressed with debt restructuring; median deficit 4.6 (2020) → 3.1 percent of GDP (2025); median
  public debt 56.3 (2024) → 53.0 (2025) → 51.7 percent (2026 proj.). About $12 billion of Eurobonds issued in 2026; bilateral aid fell by
  roughly a quarter in 2025 and is projected (OECD) to fall a further 12 percent in 2026.
- p. 3: interest absorbs a median of about 12 percent of government revenue (2025–27); banks' growing sovereign holdings crowd out private
  credit. p. 5: generalised fuel-price smoothing could cost about 4 percent of GDP vs at most 0.5 percent for targeted transfers.
- p. 6: faster, more predictable debt resolution needed for countries with unsustainable debt; little direct support from the AI boom.
- p. 8 (Box 1): a strong El Niño could cut median growth 0.5 point and add 2.6 points to median inflation in 2027.

## IMF: debt relief and debt resolution

### SA-IMF-1. IMF, "Debt Relief Under the Heavily Indebted Poor Countries Initiative" (factsheet), published 3 February 2023 ("facts current as of February 2023"; page modified 29 Sep 2026)
URL: https://www.imf.org/en/About/Factsheets/Sheets/2023/Debt-relief-under-the-heavily-indebted-poor-countries-initiative-HIPC (GUESSED; page
headline confirms). HTTP 200 (HTML). Accessed 23 Nov 2026. The IMF factsheet listing (https://www.imf.org/en/About/Factsheets) returned 404.
- The IMF and World Bank launched HIPC in 1996 "to ensure that no poor country faces an unmanageable debt burden". In 2005 the MDRI
  supplemented it: 100 percent relief on eligible debts to the IMF, World Bank and African Development Fund for countries completing HIPC.
- Of 39 eligible or potentially eligible countries, 36 have reached completion point. Before HIPC, eligible countries spent slightly more
  on debt service than on health and education combined; since, about five times more on social spending than on debt service. For the 36,
  debt service fell about 1.5 points of GDP between 2001 and 2015.
- Somalia and Sudan had reached decision point (financing plans approved December 2019 and May 2021); Eritrea eligible but owes nothing to the
  IMF. (The World Bank brief, SA-WB-4, records Somalia's completion point in December 2023 — after this factsheet's date.)

### SA-IMF-2. IMF, "Questions and Answers on Sovereign Debt Issues" (web page, modified 1 Oct 2026)
URL: https://www.imf.org/en/About/FAQ/sovereign-debt (GUESSED; title confirms). HTTP 200 (HTML). Accessed 23 Nov 2026. HTML, no page numbers.
- The Common Framework is an agreement of the G20 and Paris Club to coordinate debt treatments for up to 73 DSSI-eligible LICs; a country
  needs an IMF-supported programme; it requires the debtor to seek comparable treatment from private creditors (the DSSI only encouraged it).
  Requests from Chad, Ethiopia and Zambia are noted.
- DSSI: 43 countries estimated to have benefited from $5.7 billion of suspension in 2020; final extension to end-December 2021 (agreed 7
  April 2021). An IMF paper (Feb 2020) found half of LICs (36 of 70) at high risk of or in debt distress.
- MDRI adopted by the IMF Board in November 2005, effective 5 January 2006; IMF MDRI relief SDR 2.3 billion to 30 countries.

### SA-IMF-3. G20, "Statement, Extraordinary G20 Finance Ministers and Central Bank Governors' Meeting, November 13, 2020 [Virtual]", with Annex I "Common Framework for Debt Treatments beyond the DSSI" (PDF hosted by the IMF)
URL: https://www.imf.org/-/media/files/news/news-articles/english-extraordinary-g20-fmcbg-statement-november-13.pdf (linked from SA-IMF-2). HTTP 200.
5 pp. Accessed 23 Nov 2026.
- p. 1: the G20 endorses the Common Framework (Annex I), "also endorsed by the Paris Club", and agrees an extended DSSI term-sheet addendum.
- p. 2: process starts at the debtor's request; envelope based on an IMF–WBG DSA; covers PPG debt with original maturity over one year;
  cut-off date 24 March 2020. Key parameters: change in nominal debt service over the programme period, NPV reduction where applicable, and
  maturity extension. In principle "debt treatments will not be conducted in the form of debt write-off or cancellation".
- p. 3: parameters recorded in a non-binding MoU; private-creditor treatment at least as favourable as official bilateral creditors'.

## World Bank

### SA-WB-1. World Bank, *Africa's Pulse: An analysis of issues shaping Africa's economic future*, Volume 10, October 2014 (report no. 91207)
URL: http://documents.worldbank.org/curated/en/179091468009576085/pdf/912070REVISED00ct20140vol100v120web.pdf (from the WDS API). HTTP 200.
48 pp. Accessed 23 Nov 2026. Team leads Punam Chuhan-Pole and Francisco H. G. Ferreira.
- p. 2 (Summary): growth moderate; Ebola risk; on the MDGs "the region has achieved only a third of the poverty target" of halving
  $1.25-a-day poverty, which the world has already met. Growth in agriculture and services cut poverty more than growth in industry.
- p. 3 and p. 9: regional growth 4.6 percent in 2014 (same as 2013), **5.2 percent a year on average in 2015–16**, 5.3 percent in 2017.
- p. 5: FDI about $29 billion in 2014 (nearly $32 billion in 2013); fiscal deficit 3.6 percent of GDP (3.1 in 2013).
- p. 7: Eurobond issuance $6.9 billion year-to-date, above the $6.5 billion of 2013; maiden issue by Kenya (orders $8 billion); Zambia $1.0
  billion (April), Côte d'Ivoire $750 million and Senegal $500 million (July), Ghana $1.0 billion (September). p. 8 (Box 1): Senegal's
  sukuk (US$208 million), South Africa's $500 million sukuk.

### SA-WB-2. World Bank (Albert G. Zeufack, Cesar Calderon et al.), *Africa's Pulse, No. 22, October 2020: Charting the Road to Recovery* (doi 10.1596/978-1-4648-1568-3; WDS report no. 153598)
OKR item https://openknowledge.worldbank.org/handle/10986/34587 (issue date 7 Oct 2020); PDF bitstream
https://openknowledge.worldbank.org/server/api/core/bitstreams/a59f7b00-82f7-5a05-99bf-46a342d8f743/content (200; 150 pp.). Accessed 23 Nov 2026.
- p. 1: activity to contract 3.3 percent in 2020, the region's first recession in a quarter-century, "putting a decade of hard-won economic
  progress at risk"; per capita GDP back to its 2008 level by end-2021; up to 40 million more Africans in extreme poverty.
- p. 2: growth **2.1 percent in 2021** (below 2019's 2.4 percent and population growth), 3.2 percent in 2022; downside 1.2 percent in 2021.
- p. 3: deficits widen 3.5 points of GDP in 2020; "the risk of debt default has started to materialize for one country" (country not named
  in the passage read). AfCFTA must be fully leveraged.
- p. 4: 25 percent of firms in SSA accelerated their use of digital technologies at the height of the lockdown. p. 5: Togo's Novissi
  programme paid via mobile money accounts; 46 countries had put in place 166 social protection measures by mid-September.
- p. 6: the AfCFTA is the largest free trade area by membership: 1.3 billion people, US$3.4 trillion; DSSI potential savings for
  participating African countries only US$5.2 billion.

### SA-WB-3. World Bank (Andrew L. Dabalen, Cesar Calderon et al.), *Africa's Pulse, No. 31, April 2025: Improving Governance and Delivering for People in Africa*
OKR item https://openknowledge.worldbank.org/handle/10986/42886 (issue date 23 Apr 2025); PDF bitstream
https://openknowledge.worldbank.org/server/api/core/bitstreams/3bbc4659-de1e-472c-9d23-d67eb8364f1d/content (200; 100 pp.). Accessed 23 Nov 2026.
This is the latest edition indexed in the WDS (latest: No. 30, Oct 2024) or OKR (No. 31); later editions not found (see Not obtained).
- p. 1: growth 3.3 percent (2024) → **3.5 percent (2025)** → 4.3 percent (2026–27 average); excluding Angola, Nigeria and South Africa 4.6
  (2025) and 5.7 percent. Real income per capita in 2025 about 2 percent below its 2015 peak. Poverty at $2.15 (2017 PPP) peaks at 43.9
  percent in 2025, then 43.2 percent in 2027.
- p. 2: median inflation 7.1 (2023) → 4.5 percent (2024); interest payments 3.4 percent of GDP a year in 2025–27; 20 of 48 countries
  "paid more in debt service than for healthcare and education combined" in 2024; public debt service rose from 16 percent of revenue
  (2012) to 39 percent (2019) and about 50 percent (2024).
- p. 3: about US$20 billion of interest on PPG external debt in 2025, nearly three-quarters to private creditors and Chinese lenders; net
  external debt flows fell from $37.7 billion a year (2016–19) to $18.4 billion (2023); multilaterals 80 percent of inflows since the pandemic.
- p. 7: **4.2 percent in 2026** (section 1 figure; the Executive Summary's 4.3 is the 2026–27 average).
- p. 33: Ghana downgraded to "in debt distress" in May 2023 and Ethiopia in July 2024; Ghana reclassified "high" in the November 2024 DSA.
- p. 39 (Figure 1.38, LIC DSF data to end-2024): share of SSA countries in or at high risk of debt distress 25 percent (2012) → 50 percent
  (2019) → peak 61 percent (2021, 39 percent at high risk); 53 percent in 2022–24; none at low risk since 2021; December 2024: 18 percent in
  distress, 34 high, 47 moderate. Chad, Ghana and Zambia have completed or almost completed Common Framework restructurings; Ghana and Zambia
  concluded Eurobond exchanges and bilateral MoUs; Ethiopia reportedly reached agreement in principle with official creditors (mid-March
  2025) on $8.4 billion, giving $2.5 billion of relief in 2023–28.

### SA-WB-4. World Bank, "Heavily Indebted Poor Countries (HIPC) Initiative" (brief, dated 9 May 2024; modified 3 Aug 2026)
URL: https://www.worldbank.org/en/topic/debt/brief/hipc (GUESSED; resolves to https://www.worldbank.org/en/brief/2024/05/09/hipc). HTTP 200
(HTML). Accessed 23 Nov 2026. No page numbers.
- HIPC and MDRI have relieved 37 countries of more than $100 billion in debt; 37 countries, 31 of them in Africa, have received the relief
  for which they were eligible. Somalia reached completion point in December 2023 ($4.5 billion of debt-service savings); Eritrea and Sudan
  are potentially eligible but have not started.
- Own count from the brief's country list: the 31 African countries include Mauritania and Somalia, which the IMF does not count in SSA, so
  29 are in the IMF's SSA group (own arithmetic). Note the IMF factsheet (SA-IMF-1, Feb 2023) gives 36 completion-point countries; the
  difference is Somalia (Dec 2023).

### SA-WB-5. Leora Klapper, Dorothe Singer, Laura Starita and Alexandra Norris, *The Global Findex Database 2025: Connectivity and Financial Inclusion in the Digital Economy*, World Bank, 2025
OKR item https://openknowledge.worldbank.org/handle/10986/43438 (issue date 16 Jul 2025); PDF bitstream
https://openknowledge.worldbank.org/server/api/core/bitstreams/795d71b1-9df7-4c04-a11d-75d1d8bbcf2f/content (200; 342 pp.; ISBN
978-1-4648-2204-9). Accessed 23 Nov 2026. Survey year 2024.
- p. xxiii (Executive Summary): 40 percent of adults in SSA had a mobile money account in 2024, up from 27 percent in 2021 (Latin America
  and the Caribbean 37 percent, from 22). Telecom companies in SSA catalysed the mobile money revolution, starting in East Africa; mobile
  money is "a Sub-Saharan African success story". Worldwide 86 percent of adults own a mobile phone.
- p. 100: in SSA 20 percent of all adults have only a mobile money account. Contents (PDF 10): SSA remains the region with the largest
  share of adults with only mobile money accounts (Figure 2.1.5, p. 93); about 40 percent across its four subregions (Figure 2.1.7, p. 95).
- p. 158 (PDF 196): only 7 percent of SSA adults borrowed from their mobile money provider (unchanged from 2021).

### SA-WB-6. World Bank, Poverty and Inequality Platform API, regional aggregates (`pip-grp`, `group_by=wb`, poverty line $3.00 a day, 2021 PPP)
URL: https://api.worldbank.org/pip/v1/pip-grp?country=all&year=all&povline=3&group_by=wb&format=json (constructed from the API's documented
parameters, GUESSED). HTTP 200 (JSON). Accessed 23 Nov 2026. The request named no version; the versions endpoint
(https://api.worldbank.org/pip/v1/versions, 200) lists 20260922_2021_01_02_PROD first, so this is presumably the September 2026 release.
- Share of the world's extreme poor ($3.00 a day) living in SSA (own arithmetic from `pop_in_poverty`): 1990 13.9 percent (321 of 2,301
  million); 2000 19.1 (425 of 2,231); 2010 30.1 (442 of 1,469); 2015 46.6 (465 of 999); 2019 59.7 (500 of 837); 2022 64.5 (561 of 869);
  **2024 70.4 percent (581 of 824 million; flagged "actual")**; 2025 71.5 and 2026 72.3 percent (nowcasts).
- SSA headcount rate: 62.4 percent (2000), 45.0 (2024), 43.3 (2026 nowcast); world 36.2 (2000), 10.1 (2024), 9.8 (2026).
- For the book: the 2024 "about seven in ten" figure is consistent with DV-WB-3's "two thirds" (2022 reference year, June 2025 vintage).

## African Union / AfCFTA

### SA-AU-1. African Union, "Agreement Establishing the African Continental Free Trade Area" (treaty page) and "List of countries which have signed, ratified/acceded to the Agreement Establishing the African Continental Free Trade Area" (status list dated 22/05/2026)
Treaty page: https://au.int/en/treaties/agreement-establishing-african-continental-free-trade-area (GUESSED; title confirms; 200). Status list:
https://au.int/sites/default/files/treaties/36437-sl-AGREEMENT_ESTABLISHING_THE_AFRICAN_CONTINENTAL_FREE_TRADE_AREA_1.pdf (linked from the
treaty page; 200; 2 pp.). Accessed 23 Nov 2026.
- Treaty page: date of adoption 21 March 2018; date of last signature 5 June 2026; "Date entry into force" shown as 22 May 2019.
- Status list p. 2: adopted by the 10th Extraordinary Session of the Assembly in Kigali on 21 March 2018; entered into force on 30 May 2019;
  as of 22 May 2026, of 55 countries, 54 had signed and 49 had ratified and deposited. (The treaty page's 22 May 2019 conflicts with the
  list's 30 May 2019; the AfCFTA Secretariat also gives 30 May — use 30 May 2019 and note the discrepancy.)

### SA-AU-2. AfCFTA Secretariat, "About" page (page dated 17 Jun 2022, modified 2 May 2025)
URL: https://au-afcfta.org/about/ (GUESSED; 200, HTML). Accessed 23 Nov 2026.
- Entered into force on 30 May 2019 "after 24 Member States deposited" ratifications; the timeline on the same page says it entered into
  force after the 22nd deposit (by the Saharawi Republic, 29 April 2019) — internal inconsistency (the Agreement's own threshold was not read).
- Timeline: January 2012 AU decision to fast-track; June 2015 negotiations launched (Johannesburg); March 2018 Kigali: 44 of 55 AU members
  signed; July 2019 Niamey: operational phase launched; 10 February 2020 Wamkele Mene elected first Secretary-General; Secretariat in
  Accra (handover 17 August 2020). "The commencement of trading under the AfCFTA was in January 1, 2021". Self-description: largest free
  trade area in the world by number of participating countries.

---

## Forecast vs outturn pairs (own arithmetic; outturn = WEO Oct 2026, G603)

Caveat: outturns have been revised since each forecast (e.g. Nigeria's GDP rebasing, SA-REO-4 p. 1), and Africa's Pulse uses World Bank
aggregates, so gaps mix forecast error and revisions. 2026–27 "outturns" are themselves WEO Oct 2026 projections.

| Report (label) | Published | Year forecast | Forecast | Outturn (WEO Oct 2026) | Gap (outturn − forecast) |
|---|---|---|---|---|---|
| REO Apr 2007 (SA-REO-1, p. 4, WEO definition) | Apr 2007 | 2007 | 6.8 | 6.6 | −0.2 |
| REO Oct 2009 (SA-REO-2, p. 4) | Oct 2009 | 2009 (current year) | 1.3 (WEO def.; AFR 1.1) | 4.1 | +2.8 |
| REO Oct 2009 (SA-REO-2, p. 4) | Oct 2009 | 2010 | 4.1 | 7.4 | +3.3 |
| REO Oct 2013 (SA-REO-3, p. 3) | Oct 2013 | 2014 | 6.0 (5.7 excl. South Sudan) | 5.1 | −0.9 (−0.6) |
| REO Oct 2014 (SA-REO-4, p. 1) | Oct 2014 | 2015 | 5¾ | 3.2 | −2.6 |
| Africa's Pulse Oct 2014 (SA-WB-1, p. 3) | Oct 2014 | 2015–16 average | 5.2 | 2.2 (avg of 3.2 and 1.2) | −3.0 |
| REO Apr 2017 (SA-REO-5, p. 1) | Apr/May 2017 | 2017 | 2.6 | 2.9 | +0.3 |
| REO Oct 2020 (SA-REO-6, p. v) | Oct 2020 | 2020 (current year) | −3.0 | −3.1 | −0.1 |
| REO Oct 2020 (SA-REO-6, p. v) | Oct 2020 | 2021 | 3.1 | 3.9 | +0.8 |
| Africa's Pulse Oct 2020 (SA-WB-2, p. 2) | Oct 2020 | 2021 | 2.1 | 3.9 | +1.8 |
| REO Apr 2023 (SA-REO-7, p. 2) | Apr 2023 | 2023 / 2024 | 3.6 / 4.2 | 3.8 / 4.2 | +0.2 / 0.0 |
| Africa's Pulse Apr 2025 (SA-WB-3, pp. 1, 7) | Apr 2025 | 2025 / 2026 | 3.5 / 4.2 | 4.5 / 4.5 (proj.) | +1.0 / +0.3 |
| REO Apr 2026 (SA-REO-8, p. 4) | Apr 2026 | 2026 / 2027 | 4.3 / 4.4 | 4.5 / 4.5 (both proj.) | +0.2 / +0.1 |
| REO Update Oct 2026 (SA-REO-9, p. 1) | Oct 2026 | 2026 / 2027 | 4.5 / 4.5 | same vintage | — |

Other outturns for context: average 2002–07 6.3 percent (REO Oct 2009 said about 6½); 2016 1.2 (REO Apr 2017 estimate 1.4); 2025 4.5.
Pattern: big misses at turning points — too gloomy in 2009 (the 2010 rebound was far stronger), too rosy in 2014 (the 2015–16 commodity
slump); recent forecasts within about half a point.

## Already in the book (not refetched)

- IMF_2003-2006.md, WEO September 2003, Ch. 1 p. 17: per capita growth below 1 percent in SSA.
- IMF_2003-2006.md, WEO April 2006, Foreword p. xi: SSA heading for its best growth in over 30 years.
- IMF_2020-2021.md, WEO Update January 2021, p. 1: calls for debt treatment under the G20 Common Framework.
- IMF_2022-2023.md, WEO October 2022, Ch. 1 p. 7: food about 40 percent of the SSA consumption basket.
- IMF_2026.md, WEO April 2026, Ch. 1 p. 14: balance-of-payments distress and unrest risks in commodity importers, especially SSA; WEO Update
  July 2026, p. 8: food-insecurity risk in low-income South Asia and SSA.
- Theme_debt.md, DF-IMF-6 (WEO April 2023 ch. 3), pp. 70–71: HIPC and MDRI as large coordinated restructurings; p. 71: Common Framework
  needs more predictability.
- Theme_debt.md, DF-WB-1 (Global Waves of Debt), pp. 1–2: first wave incl. low-income Africa; HIPC/MDRI relief from the mid-1990s.
- Theme_debt.md, DF-WB-2 (International Debt Report 2026), pp. 44–45: Common Framework MoUs for Ghana (Dec 2023) and Zambia (June 2024), bondholder
  deals in 2024, MoU with Ethiopia; Common Framework created 2020; p. 26: high-yield issuers shut out in 2022–23, back in 2025.
- Theme_debt.md, DF-WB-3 (DSSI brief, 10 March 2022): DSSI established May 2020; 48 of 73 eligible took part; $12.9 billion suspended.
- Theme_development.md, DV-WB-1 (PPP 2026), p. xv fact 2: by 2030, 87 percent of the extreme poor in SSA, FCS or both.
- Theme_development.md, DV-WB-2 (PPP 2024), p. 6: SSA's extreme poor rose from 282 million (1990) to 464 million (2024); p. 7: share of
  extreme poor in SSA or FCS a quarter (2000), half (2014), three-quarters (2024); SSA GDP per capita growth 0.7 percent a year 1990–2022.
- Theme_development.md, DV-WB-3 (PIP June 2025 update), pp. 2–3: SSA "home to two thirds of the global extreme poor"; 45.5 percent (2022).
- Theme_development.md, DV-WB-4 (PIP March 2026 update), p. 2: SSA 46.2 (2021) → 45.1 (2024) → 43.3 percent (2026).
- Theme_development.md, DV-UN-2 (SDG Report 2026), PDF 10: SSA extreme poverty regained pre-pandemic levels only in 2025.
- Theme_development.md, DV-UN-3 (Millennium Declaration), para. 15: enhanced HIPC debt relief.
- Theme_technology.md, TE-OTH-10 (ITU Facts and Figures 2026): Africa 42 percent online.
- Theme_trade.md, TR-WTO-2 (World Trade Report 2023), p. 12: trade helped cut poverty, SSA less so.
- Theme_markets.md, MK-IMF-6 (GFSR April 2007): portfolio flows to SSA among reversal risks.
- Theme_demography.md, Synthesis / DL-WB-4, DL-WB-5: SSA youth bulge; over 330 million of 1.2 billion new working-age people by 2035 in SSA.
- Theme_growth.md, GR-IMF-1 (WEO April 2003 ch. III), p. 106: SSA institutions and income.
- No existing items on AfCFTA, M-Pesa/mobile money, Eurobonds or the REO SSA series; timeline_events.md has no Africa entries.

## Not obtained

- IMF SSA REO listing: https://www.imf.org/en/Publications/REO/SSA (404, "Blob not found"); `/index.md`, `/index.json` (404);
  https://www.imf.org/en/publications/reo/ssa (404); https://www.imf.org/en/Publications/REO/Issues?Region=Sub-Saharan%20Africa (404).
- REO April 2007 in English: the issue page links only the French PDF; GUESSED English URLs
  https://www.imf.org/external/pubs/ft/reo/2007/afr/eng/sreo0407.pdf, .../-/media/websites/imf/imported-publications/external/pubs/ft/reo/2007/afr/eng/sreo0407.pdf
  and .../imported-full-text-pdf/external/pubs/ft/reo/2007/afr/eng/_sreo0407.pdf (all 404).
- Fall 2006 Supplement: issue page (200) carries no PDF link.
- REO 2008, 2012, 2013 (May), 2016 (Apr/Oct) — GUESSED URLs, 404 unless stated: external/pubs/ft/reo/2013/afr/eng/sreo0513.pdf (404, later
  429); 2016/afr/eng/pdf/sreo1016.pdf; 2016/afr/eng/sreo1016.pdf; 2016/afr/eng/sreo0416.pdf; 2012/afr/eng/sreo1012.pdf; 2012/afr/eng/sreo0412.pdf;
  2014/afr/eng/sreo0414.pdf; 2013/afr/eng/sreo1013.pdf; 2008/afr/eng/sreo0408.pdf (429); 2007/afr/eng/sreo1007.pdf (429; not retried);
  imported-publications 2012/2013/2016 variants (404); imported-full-text-pdf 2008 _sreo0408, 2007 _sreo1007, 2016 _sreo1016, 2016
  pdf/_sreo1016, pdf/_sreo0416 (404). **No 2016 edition (the "multispeed" year) was read**; the 2016 slump is taken from SA-REO-5.
- IMF factsheet listing https://www.imf.org/en/About/Factsheets (404).
- IMF–World Bank LIC DSA list: https://www.imf.org/external/Pubs/ft/dsa/DSAlist.pdf and .../dsalist.pdf both returned 200 but an empty
  HTML page (392 bytes), not the list. Country risk ratings therefore come only from the REO and Pulse summaries above.
- Paris Club: https://clubdeparis.org/sites/default/files/annex_common_framework_for_debt_treatments_beyond_the_dssi.pdf (GUESSED, 400) and
  https://clubdeparis.org/en (400 Bad Request) — treated as a block.
- G20 Information Centre (Toronto): http://www.g20.utoronto.ca/2020/2020-g20-statement-1113.html (404), http://www.g20.utoronto.ca/2020/index.html
  (404), https://g20.utoronto.ca/2020/2020-g20-statement-1113.html (404), https://g20.utoronto.ca/2020/ (403). The G20 text was read from the
  IMF-hosted copy (SA-IMF-3).
- World Bank Africa's Pulse page https://www.worldbank.org/en/region/afr/publication/africas-pulse (GUESSED, 404). Africa's Pulse editions
  after No. 31 (April 2025) — e.g. October 2025, April and October 2026 — were not found in the WDS API (latest indexed: No. 30, October
  2024) or the OKR API (latest: No. 31).
- Primary documents on the Zambia (2020), Ghana (2022) and Ethiopia (2023) defaults themselves were not fetched (country detail is part B);
  the restructuring status here comes from SA-REO-7, SA-REO-8, SA-REO-9 and SA-WB-3.

## Bibliography rows

| Suggested key | Title | Publisher | Year | Edition / report no. | URL |
|---|---|---|---|---|---|
| imf_reo_ssa_2007apr | Perspectives économiques régionales: Afrique subsaharienne (French ed. of REO SSA) | IMF | 2007 | April 2007; ISBN 978-1-58906-639-7 | https://www.imf.org/-/media/websites/imf/imported-publications/external/pubs/ft/reo/2007/afr/fra/_afrf.pdf |
| imf_reo_ssa_2009oct | Regional Economic Outlook: Sub-Saharan Africa — Weathering the Storm | IMF | 2009 | October 2009; ISBN 978-1-58906-857-5 | https://www.imf.org/external/pubs/ft/reo/2009/afr/eng/sreo1009.pdf |
| imf_reo_ssa_2013oct | Regional Economic Outlook: Sub-Saharan Africa — Keeping the Pace | IMF | 2013 | October 2013; ISBN 978-1-47555-341-3 | https://www.imf.org/-/media/websites/imf/imported-full-text-pdf/external/pubs/ft/reo/2013/afr/eng/_sreo1013.pdf |
| imf_reo_ssa_2014oct | Regional Economic Outlook: Sub-Saharan Africa — Staying the Course | IMF | 2014 | October 2014; ISBN 978-1-49838-645-6 | https://www.imf.org/-/media/websites/imf/imported-full-text-pdf/external/pubs/ft/reo/2014/afr/eng/_sreo1014.pdf |
| imf_reo_ssa_2017apr | Regional Economic Outlook: Sub-Saharan Africa — Restarting the Growth Engine | IMF | 2017 | April 2017; ISBN 978-1-47557-446-3 | https://www.imf.org/-/media/files/publications/reo/afr/2017/may/pdf/sreo0517.pdf |
| imf_reo_ssa_2020oct | Regional Economic Outlook: Sub-Saharan Africa — A Difficult Road to Recovery | IMF | 2020 | October 2020; ISBN 978-1-5135-5760-1 | https://www.imf.org/-/media/files/publications/reo/afr/2020/october/english/text.pdf |
| imf_reo_ssa_2023apr | Regional Economic Outlook: Sub-Saharan Africa — The Big Funding Squeeze | IMF | 2023 | April 2023; ISBN 979-8-4002-3564-1 | https://www.imf.org/-/media/files/publications/reo/afr/2023/april/english/text.pdf |
| imf_reo_ssa_2026apr | Regional Economic Outlook: Sub-Saharan Africa — Hard-Won Gains Under Pressure | IMF | 2026 | April 2026 | https://www.imf.org/-/media/files/publications/reo/afr/2026/april/english/text.pdf |
| imf_reo_ssa_2026oct | Regional Economic Outlook Update: Sub-Saharan Africa — Resilient Growth, Clouded Outlook | IMF | 2026 | October 2026 (update) | https://www.imf.org/-/media/files/publications/reo/afr/2026/october/english/text.pdf |
| imf_fs_hipc_2023 | Debt Relief Under the Heavily Indebted Poor Countries Initiative (factsheet) | IMF | 2023 | 3 February 2023 | https://www.imf.org/en/About/Factsheets/Sheets/2023/Debt-relief-under-the-heavily-indebted-poor-countries-initiative-HIPC |
| imf_faq_sovdebt | Questions and Answers on Sovereign Debt Issues | IMF | 2026 | web page (modified 1 Oct 2026) | https://www.imf.org/en/About/FAQ/sovereign-debt |
| g20_cf_2020 | Statement, Extraordinary G20 FMCBG Meeting, Annex I: Common Framework for Debt Treatments beyond the DSSI | G20 (hosted by IMF) | 2020 | 13 November 2020 | https://www.imf.org/-/media/files/news/news-articles/english-extraordinary-g20-fmcbg-statement-november-13.pdf |
| wb_pulse_2014oct | Africa's Pulse, Volume 10 | World Bank | 2014 | October 2014; report no. 91207 | http://documents.worldbank.org/curated/en/179091468009576085/pdf/912070REVISED00ct20140vol100v120web.pdf |
| wb_pulse_22 | Africa's Pulse, No. 22: Charting the Road to Recovery | World Bank | 2020 | October 2020; doi 10.1596/978-1-4648-1568-3 | https://openknowledge.worldbank.org/handle/10986/34587 |
| wb_pulse_31 | Africa's Pulse, No. 31: Improving Governance and Delivering for People in Africa | World Bank | 2025 | April 2025 | https://openknowledge.worldbank.org/handle/10986/42886 |
| wb_hipc_brief | Heavily Indebted Poor Countries (HIPC) Initiative (brief) | World Bank | 2024 | 9 May 2024 | https://www.worldbank.org/en/brief/2024/05/09/hipc |
| wb_findex_2025 | The Global Findex Database 2025: Connectivity and Financial Inclusion in the Digital Economy | World Bank | 2025 | ISBN 978-1-4648-2204-9 | https://openknowledge.worldbank.org/handle/10986/43438 |
| wb_pip_2026 | Poverty and Inequality Platform, regional aggregates ($3.00/day, 2021 PPP) | World Bank | 2026 | release 20260922 (presumed) | https://api.worldbank.org/pip/v1/pip-grp?country=all&year=all&povline=3&group_by=wb&format=json |
| au_afcfta_treaty | Agreement Establishing the African Continental Free Trade Area (treaty page and status list) | African Union | 2018 / 2026 | adopted 21 Mar 2018; status list 22 May 2026 | https://au.int/en/treaties/agreement-establishing-african-continental-free-trade-area |
| afcfta_about | About the AfCFTA | AfCFTA Secretariat | 2022 / 2025 | web page | https://au-afcfta.org/about/ |
