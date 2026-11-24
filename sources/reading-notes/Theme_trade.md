# Reading notes: theme chapter "Trade, 2000–2026" (read 22 Nov 2026)

Method: every document was fetched with plain `curl` (default user-agent, no custom headers). IMF chapters came from imf.org: for older
issues the old contents page "http://www.imf.org/external/pubs/ft/weo/YYYY/NN/index.htm" (which now redirects to the new-style issue page)
gave the chapter PDF links; for newer issues the chapter PDFs are linked from the issue page. WTO documents came from wto.org, the World
Bank report from worldbank.org / openknowledge.worldbank.org, and Indian government documents from the sites named in each entry. Downloads
are in `/private/tmp/trade_dl/` (subfolders `imf/`, `wto/`, `wb/`, `in/`). PDFs were converted with `pdftotext` (plain and `-layout`). Each
quote was checked by script (`/private/tmp/trade_scripts/qc.py`) against the plain-text conversion; the check normalises case, spaces,
curly quotes and line-end hyphens. Quotes are verbatim and under 15 words, at most one per bullet; everything else is paraphrase. The
2025–26 tariff episode is taken from the existing notes `IMF_2024-2025.md` and `IMF_2026.md`, cited by their item labels, not re-read.

Page numbers are printed numbers, with the PDF-to-printed offset given in each entry.

India: the Economic Survey extracts in `Econ Subject/sources/text/es<YEAR>.txt`. Pages are cited as in `India_ES_2024-2026.md`: "p." is the
printed page and "st." is the stitched page (form feeds + 1).

Item labels: TR-IMF-n, TR-WTO-n, TR-WB-n, TR-IN-n. Growth rates are annual percent unless stated. Indian years are fiscal years
(FY25 = 2024-25).

---

## IMF

### TR-IMF-1. WEO October 2016, Chapter 2 "Global Trade: What's Behind the Slowdown?"
Issue page title: "IMF World Economic Outlook (WEO), October 2016: Subdued Demand: Symptoms and Remedies". Published October 4, 2016 (issue
page). Contents page http://www.imf.org/external/pubs/ft/weo/2016/02/index.htm redirects to the issue page
https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/Subdued-Demand-Symptoms-and-Remedies. Chapter PDF:
https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2016/02/pdf/_c2pdf.pdf (58 PDF pages, pp. 63–120).
Offset: p. = PDF + 62. Main authors (p. 63): Aqib Aslam, Emine Boz and Petia Topalova (co-team leaders), Eugenio Cerutti, Marcos
Poplawski-Ribeiro. Read: pp. 63–69 (summary, findings, distribution, key patterns), pp. 80–81 (trade costs, GVCs), pp. 85–87 (summary and
policy implications), Box 2.1 pp. 88–90.
- p. 63: since 2012 the volume of world trade in goods and services has grown just over 3% a year, under half the pace of the previous three
  decades. In 1985–2007, "real world trade grew on average twice as fast as global GDP"; in the past four years it barely kept pace with GDP.
- p. 63 (summary): weak activity, especially investment, explains up to three-quarters of the slowdown. Slower liberalisation and the uptick
  in protectionism hold trade back but with limited measured effect so far; slower GVC growth also "played an important part".
- p. 64: China is rebalancing from investment towards consumption, and investment is more trade-intensive than consumption. Footnote 3
  (citing Constantinescu, Mattoo and Ruta) says growth of supply chains involving China had weakened even before the global financial crisis.
- p. 65 (findings): the slowdown was broad: few countries were spared, trade fell for 85% of product lines, sharpest in capital and
  intermediate goods. Up to three-quarters of the fall in goods import growth between 2003–07 and 2012–15 traces to weaker activity; a
  general equilibrium model attributes about 60% of the slowdown in the imports-to-GDP ratio to the composition of demand. Factors beyond
  demand cut about 1¾ points off annual global real import growth since 2012.
- p. 67: trade's gains are unevenly spread. The chapter cites Autor, Dorn and Hanson (2013): rising imports from China led to higher
  unemployment, lower participation and lower wages in US local labour markets with import-competing manufacturing. Footnote 13 notes similar
  effects in Europe. Adjustment costs "should not be underestimated".
- p. 67: in nominal dollars, trade collapsed after mid-2014. The value of goods and services trade fell 10½% in 2015, driven by a 13% drop in
  the import deflator (oil and the strong dollar); volumes kept growing at just over 3%.
- p. 69: compared with 2003–07, import growth in 2012–15 slowed in 143 of 171 countries (116 relative to GDP growth). Services trade was more
  resilient: services and goods volumes grew about 9½% and 9% a year in 2003–07, but in 2012–15 services slowed to 5½% and goods to just under
  3%.
- p. 80: transport and logistics costs kept falling after 2006, so they probably did not cause the slowdown.
- pp. 80–81 (Figure 2.12): GVC participation rose in advanced and emerging economies until the global financial crisis; China's peaked in the
  second half of the 2000s. On p. 81, "since 2011, participation seems to have leveled off". Whether this is maturation or policy is hard to say.
- p. 85: in 2003–07, trade in country-pair sectors in the top quartile of GVC participation grew about 1¼ points faster than the rest; in
  2012–14 there was no significant difference.
- pp. 85–86 (summary): the pace of new liberalisation has slowed, and the post-crisis uptick in protectionism is "not innocuous"; it could
  weigh heavily on trade if it spreads. A slower fall in trade costs explains about a quarter of the slowdown in
  nominal imports relative to GDP.
- pp. 86–87: slow trade growth will likely persist; even when growth picks up, trade is unlikely to regain pre-crisis rates, when investment in
  China and other EMDEs was unusually high and GVCs were spreading fast. Policy: fix the growth constraints (especially investment), and lower
  trade barriers while helping those who bear adjustment costs.
- p. 90 (Box 2.1, Ahn and Duval): trade raises productivity through imports, imported inputs and exports; a 1-point rise in China's import
  penetration in a sector is associated with a 1.5% higher sector TFP level in 18 OECD economies (1995–2007).

(TR-IMF-2 and TR-IMF-3, the April 2022 and April 2023 WEO chapters, follow below the WTO entries; imf.org returned HTTP 429 on the first
attempt and they were fetched later.)

## WTO

### TR-WTO-1. World Trade Report 2019, "The future of services trade"
Landing page: https://www.wto.org/english/res_e/publications_e/wtr19_e.htm. PDFs: front matter, foreword, key facts and executive summary
https://www.wto.org/english/res_e/booksp_e/01_wtr19_0_e.pdf (13 PDF pages; offset p. = PDF − 2); section B "Services trade in numbers"
https://www.wto.org/english/res_e/booksp_e/03_wtr19_2_e.pdf (offset p. = PDF + 19). Full report (not downloaded):
https://www.wto.org/english/res_e/booksp_e/00_wtr19_e.pdf. Foreword signed by Roberto Azevêdo, Director-General. Read: pp. 4–11 (foreword,
key facts and findings, executive summary); in section B, pp. 28 and 32–33 (IT services, leading developing-economy traders).
- p. 4 (foreword; also p. 7): counting services sold through foreign affiliates (GATS "mode 3", commercial presence), services trade was worth
  US$13.3 trillion in 2017. That puts services' share of world trade 20 points higher than traditional estimates.
- p. 4 / p. 6: services trade grew 5.4% a year on average in 2005–17, faster than goods trade (4.6%).
- p. 6 (key facts): commercial presence is almost 60% of services trade (58.9% in 2017, p. 7); cross-border supply close to 30% (p. 7).
  Distribution and financial services are each almost one-fifth of services trade.
- p. 6: "Services value-added accounts for close to half of the value" of international trade in goods and services, i.e. in value-added
  terms services are about half of world trade.
- p. 6: "Trade costs in services are almost double those in goods", but they fell 9% in 2000–17 (digital technology, lower policy barriers,
  infrastructure).
- p. 6 / p. 7: developing economies' share of world services trade rose more than 10 points after 2005, to 25% of services exports and 34.4%
  of services imports in 2017, but is concentrated in five economies. LDCs had 0.3% of world services exports.
- p. 7 (executive summary): "Services have become the backbone of the global economy" and trade in services has grown faster than goods trade
  since 2011. Services are about three-quarters of GDP in developed economies, up from 40% in 1950.
- p. 10: WTO Global Trade Model simulations (lower digital trade costs, less need for face-to-face contact, lower policy barriers) project the
  services share of world trade growing by 50% by 2040; developing countries' share of services trade could rise about 15% if they adopt
  digital technologies.
- pp. 10–11: services barriers are regulatory rather than tariffs and remain higher than in goods; cooperation through trade agreements has
  been hard to advance.
- p. 28 (section B): world IT services exports were about US$438 billion in 2017, mostly cross-border, with the EU first and India second;
  "India has become a prominent exporter of IT services". India's IT exports exceeded US$52 billion in 2017, about 13% through IT
  professionals abroad (mode 4). Global ICT services trade grew about 11% a year over the decade.
- p. 32: in 2017 the leading developing-economy services traders were China, Hong Kong (China), Korea, Singapore and India; together 56.7% of
  developing economies' services exports.
- p. 33: in India cross-border trade is still the dominant mode; only 20% of its services exports go through foreign-controlled affiliates
  (up 12 points since 2005), against up to two-thirds in China and Korea.

### TR-WTO-2. World Trade Report 2023, "Re-globalization for a secure, inclusive and sustainable future"
Landing page: https://www.wto.org/english/res_e/publications_e/wtr23_e.htm. PDFs: executive summary
https://www.wto.org/english/res_e/booksp_e/wtr23_e/wtr23_ch0c_e.pdf (8 PDF pages, pp. 8–15; offset p. = PDF + 7); chapter A "Introduction"
https://www.wto.org/english/res_e/booksp_e/wtr23_e/wtr23_ch1_e.pdf (offset p. = PDF + 15). Read: pp. 8–15 in full; p. 21.
- p. 8: the WTO's founding vision of interdependence for peace and prosperity is being questioned. The pandemic and the war in Ukraine have fed
  a "trade-sceptic narrative", and policymakers now stress economic independence. The report's alternative to fragmentation is
  re-globalization: extending integration to more people, economies and issues.
- p. 8: trade tensions are surging in WTO committees. Concerns raised in the Market Access Committee rose fourfold in 2015–22, and in the
  Council for Trade in Goods ninefold; countervailing measures against subsidies rose sharply.
- p. 9: the stagnation of the world trade-to-GDP ratio since 2008–09 does not seem to be driven by trade tensions, since trade costs kept
  falling. It reflects slower production unbundling, as more components could be sourced within countries.
- p. 9: US–China bilateral trade hit a record in 2022, but its composition shifted in line with tariffs (sharp slowdowns in, for example,
  semiconductors).
- p. 9: "trade is gradually becoming reoriented along geopolitical lines". Since the Ukraine war (February 2022), trade between hypothetical
  blocs (based on foreign-policy similarity) has grown 4–6% more slowly than trade within blocs.
- p. 9: yet "claims of de-globalization are still greatly exaggerated". Trade recovered quickly from COVID-19 and adapted to the war;
  digitally delivered services, environmental goods and GVC participation (Cambodia, Romania, Viet Nam) grew.
- p. 9: trade costs in developing economies are still almost 30% higher than in high-income economies; agriculture's are 50% higher than
  manufacturing's.
- p. 12 (Figure 6): trade has helped cut extreme poverty by three-quarters since the 1990s; East Asia and Eastern Europe did well with
  export-led growth, sub-Saharan Africa less so.
- pp. 12–13: "fragmentation presents a major risk to the progress achieved" on poverty. In a full geopolitical rivalry scenario, developing
  economies would diverge from the developed world, with the GDP gap widening by 3.5%.
- p. 13: non-tariff measures are about 14% of total trade costs.
- p. 21 (chapter A): the WTO estimates that splitting the world trading system into separate blocs would cost about 5% of global real
  income, with double-digit losses for some developing economies.

## IMF (continued)

### TR-IMF-2. WEO April 2022, Chapter 4 "Global Trade and Value Chains during the Pandemic"
Issue page title: "World Economic Outlook, April 2022: War Sets Back The Global Recovery". Published April 19, 2022. Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2022/04/19/world-economic-outlook-april-2022. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2022/april/english/ch4.pdf (21 PDF pages, pp. 87–107; offset p. = PDF + 86; first
download attempt returned HTTP 429, retry worked). Prepared by Ting Lan, Davide Malacrino, Adil Mohommad (lead), Andrea Presbitero and
Galen Sher, under Shekhar Aiyar (p. 87). Footnote 1 (p. 87): analysis concluded early 2022, before the war in Ukraine. Read: pp. 87–89,
pp. 91–92, pp. 96–99.
- p. 87 (summary): COVID-19 was expected to collapse trade, but while services stayed sluggish, "trade in goods bounced back surprisingly
  quickly". Pandemic-specific factors rotated trade from services to goods beyond what demand explains.
- p. 87: at the trough (2020:Q2) goods trade volume was 12.2% below 2019:Q4 and services trade 21.4% below. Goods trade was back to
  pre-pandemic levels by October 2021, much faster than after the global financial crisis. Services lagged because of travel.
- p. 87: exports of GVC-intensive goods fell 30% between January and April 2020, against about 18% for other goods (p. 88), but recovered
  faster too. Autos were hit by semiconductor shortages.
- p. 89 (findings): lockdowns in trading partners accounted for up to 60% of the fall in imports in the first half of 2020, with bigger
  spillovers in GVC-intensive industries. These spillovers were short-lived, smaller where telework was possible, and shrank in later waves:
  evidence of GVC adaptability and resilience.
- p. 87 (summary): given that resilience, "policies such as reshoring are likely misguided". Resilience is better built by diversifying away
  from domestic sourcing and by making inputs easier to switch between countries.
- p. 96: firms in the Western Hemisphere source 82% of intermediates domestically against a benchmark of 31%, a large home bias; "This is a
  simple argument against reshoring", since reshoring would raise concentration risk.
- p. 97: in a model shock (a 25% labour-supply contraction in a large supplier calibrated to China), the average economy's GDP falls 0.8%;
  higher diversification cuts the loss by almost half. Diversification gives little protection against highly correlated shocks such as the
  first months of COVID-19 (p. 98).
- p. 98: greater substitutability cuts non-source countries' GDP losses by about four-fifths. Tariffs are already low globally, so the scope
  is in non-tariff barriers, especially in emerging and low-income economies.
- p. 98: domestic-sourcing policies may tilt firms against diversifying; the chapter names Made in China 2025, Make in India and the US
  Innovation and Competition Act of 2021.
- p. 99: the shift of demand from services to goods may not last; services trade should recover as travel restrictions lift.

### TR-IMF-3. WEO April 2023, Chapter 4 "Geoeconomic Fragmentation and Foreign Direct Investment"
Issue page title: "World Economic Outlook, April 2023: A Rocky Recovery". Published April 11, 2023. Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2023/04/11/world-economic-outlook-april-2023. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2023/april/english/ch4.pdf (24 PDF pages, pp. 91–114; offset p. = PDF + 90; first
attempt HTTP 429, retry worked). Authors: JaeBin Ahn, Benjamin Carton, Ashique Habib, Davide Malacrino, Dirk Muir, Andrea Presbitero, under
Shekhar Aiyar (p. 91). Read: pp. 91–94 (summary, introduction, findings), p. 99 (vulnerability), pp. 104–105 (scenarios, conclusions).
- p. 91: rising geopolitical tensions and the uneven spread of globalisation's gains have fed scepticism of multilateralism. Brexit, US–China
  trade tensions and Russia's invasion of Ukraine could lead to a policy-driven reversal of integration, "geoeconomic fragmentation".
- p. 91: *slowbalization* dates for most countries to the aftermath of the global financial crisis. Global FDI fell "from 3.3 percent of GDP
  in the 2000s to 1.3 percent" in 2018–22.
- p. 92: firms' earnings calls show a sharp spike in interest in reshoring and friend-shoring, as geopolitical distance between countries
  rose. The chapter cites US Treasury Secretary Yellen's friend-shoring call, the CHIPS and Science Act, the Inflation Reduction Act and the
  European Chips Act, and Chinese moves to replace imported technology.
- p. 93: FDI is about 12% of the domestic capital stock globally, and brings technology transfer.
- pp. 93–94 (findings): FDI flows, especially in strategic sectors such as semiconductors, are increasingly concentrated among geopolitically
  aligned countries, and alignment has mattered more since 2018 with the resurgence of US–China trade tensions. Emerging and developing
  economies are more vulnerable to FDI relocation than advanced economies.
- p. 94: model scenarios (a permanent rise in cross-bloc barriers to investment inputs) cut global output by about 2% in the long term, with
  losses uneven and largest for emerging economies cut off from advanced-economy FDI.
- p. 99: the most vulnerable cluster includes large emerging markets "such as Brazil, China, and India".
- p. 104 (Figure 4.15): "Fragmentation could lower global output by up to 2 percent"; the baseline puts India and Indonesia, and Latin
  America, as nonaligned. Nonaligned regions may gain some bargaining power, but uncertainty can hurt investment; footnote 19 cites US support
  for investment in India by the largest US solar manufacturer.
- p. 105 (conclusions): "a fragmented global economy is likely to be a poorer one". The costs give a rationale for a robust defence of
  global integration; diversifying sourcing away from domestic suppliers builds resilience (citing TR-IMF-2).

### TR-IMF-4. The 2025–26 tariff episode, from the existing notes `IMF_2024-2025.md` and `IMF_2026.md` (not re-read)
These bullets restate what those notes record, with their page citations; the source PDFs were not re-fetched for this chapter. Check
against those notes before quoting.
- WEO April 2024, Ch. 1 p. 3 (`IMF_2024-2025.md`): world trade expected to recover to about 3¼% a year in 2024–25 after quasi-stagnation in
  2023; cross-border trade restrictions had surged, hurting trade between geopolitically distant blocs.
- WEO April 2025, Ch. 1 p. 11: tariff chronology from the 1 February 2025 executive orders on Canada, China and Mexico to the 2 April Fair
  and Reciprocal Plan (10% minimum tariff, country rates up to 50% for about 60 countries) and China's 34% response.
- WEO April 2025, Ch. 1 p. 14: after the 9 April pause, the US effective tariff rate on the world was about 25% on 14 April, up from under 3%
  in January 2025; the US rate on Chinese goods was 115% and China's on US goods 146%. Executive Summary p. xv: effective tariff rates at
  levels not seen in a century. Foreword p. xiii: world trade growth cut by 1½ points for 2025.
- WEO July 2025 Update, p. 3: US effective tariff rate in the projections 17.3% (24.4% in the April reference forecast).
- WEO October 2025, Foreword p. xii: the global hit was at the modest end of April's range (front-loading, rerouting, deals, limited
  retaliation), but the US effective rate stayed at about 19%. Ch. 1 p. 1: US rates settling mostly between 10% and 20%. Ch. 1 p. 15: a higher
  US effective tariff on Indian goods since July 2025.
- WEO January 2026 Update, p. 2 and p. 3 (`IMF_2026.md`): a US–China truce cut bilateral tariffs until November 2026 and paused export
  controls (semiconductors, rare earths); US effective rate in the projections 18.5%.
- WEO April 2026, Ch. 1 pp. 1, 5, 11: after court rulings and executive actions the US effective statutory rate in the projections was 13.5%;
  the additional US tariff on Indian goods fell from 50% to 10%. Box 1.1 p. 21: the actual collected US tariff rate in December 2025 was about
  half the announced rate. Ch. 1 p. 13: world trade volume 5.1% (2025), 2.8% (2026).
- WEO October 2026, Ch. 1 pp. 13–14: world trade 5.0% (2025), 4.6% (2026), 4.7% (2027). `IMF_2026.md` hindsight table: the 2026 trade
  forecast rose from 2.6% (January) to 4.6% (October), lifted by tech-related (AI-hardware) trade; Ch. 1 p. 6: Taiwan Province of China and
  Korea supply 62% of net AI-hardware trade. Foreword p. xii: reshoring not viable for most countries; diversify trade instead.

### TR-WTO-3. WTO, "Global Trade Outlook and Statistics – Update: October 2026" (released 8 October 2026)
The wto.org news listing pages are built by JavaScript; the item was found in the news data file
https://www.wto.org/library/news/news_2026_e.js (entry dated 2026.10.08, subject tag TFORE). News item: "AI boom and trade resilience to
Middle East crisis lift outlook, but gains to be uneven", https://www.wto.org/english/news_e/news26_e/stat_08oct26_510_e.htm. Report PDF:
https://www.wto.org/english/res_e/booksp_e/gtos1026_e.pdf (52 PDF pages; offset p. = PDF − 2). Read: news item in full; report pp. 1–6
(key messages, Table 1), pp. 22–23 (fragmentation), Appendix Tables 1 and 3 (pp. 40, 42). The October 2026 update replaces the March 2026
baseline; no April 2026 issue was looked for separately.
- p. 6 (Table 1): world merchandise trade volume (average of exports and imports) grew 2.4% (2022), −0.9% (2023), 2.7% (2024) and 4.2% in
  2025. The forecast for 2026 is 3.9% (March 2026 baseline: 1.9%) and 4.1% for 2027. World GDP at market exchange rates: 3.0% (2025), 2.6%
  (2026), 2.9% (2027). So in 2025–26 goods trade grew faster than world output again, about 1.4–1.5 times.
- p. 6 (Table 1): 2025 export volume growth was 9.6% for Asia, 2.8% for North America and −0.5% for Europe. Excluding intra-EU trade, world
  trade grew 5.1% in 2025.
- News item: commercial services trade volume is forecast at 3.3% in 2026 (March: 4.8%) and 6.4% in 2027; transport and travel were hit by
  the Middle East conflict, while computer services exports rose 18% year on year in Q1 2026. DG Ngozi Okonjo-Iweala: "The numbers reflect
  trade resilience in action."
- News item / p. 2: merchandise trade volume grew 3.5% in the first half of 2026. AI-enabling goods (semiconductors, servers) accounted for
  47% of world merchandise trade growth in H1 2026 and rose 67% year on year.
- p. 3 (key messages): AI-enabling goods trade grew 16% in 2024, 31% in 2025 and 67% in H1 2026 (value terms); its share of world merchandise
  trade rose to 14.8% in H1 2026 from 7–8% in 2016–23. The top 10 traders had about 85% of world exports of these goods in 2025.
- p. 3: the gap between intra-bloc and inter-bloc trade narrowed through 2025 and into 2026; bloc-based fragmentation "has not continued to
  intensify", but US–China decoupling has accelerated since 2025 and is now the main driver of bloc divergence.
- p. 23: "US imports from China fell by 29% in 2025", cutting China's share of US imports from 13.8% to 9.3% (more than 20% before 2018).
  Trade of both with connecting economies grew faster than with the rest of the world; decoupling is strongest in complex products.
- p. 40 (Appendix Table 1, merchandise 2025, US$ billion): China first exporter, 3,771 (14.4% of world exports); United States second, 2,180
  (8.3%); India 19th, 445 (1.7%). The US is first importer, 3,505 (13.2%); India 9th importer, 755 (2.8%). World exports 26,275.
- p. 42 (Appendix Table 3, commercial services 2025, US$ billion): United States first exporter, 1,212 (12.6%); UK second (7.4%); China fifth
  (5.3%); India eighth, 412 (4.3%, up 10%). India ninth importer (3.2%). World services exports 9,594.

## World Bank

### TR-WB-1. World Development Report 2020, "Trading for Development in the Age of Global Value Chains" (overview and Chapter 1)
Landing page: https://www.worldbank.org/en/publication/wdr2020 (page title as above). The openknowledge "bitstream/handle" links on that
page return an HTML app shell, so the files were taken through the repository's API (item handle 10986/32437, found via
https://openknowledge.worldbank.org/server/api/pid/find?id=hdl:10986/32437). Overview booklet ("211457ov.pdf"):
https://openknowledge.worldbank.org/server/api/core/bitstreams/3df67ad2-367c-5718-ba97-edd213723bb3/content (19 PDF pages; overview pp.
1–10 = PDF 7–16; offset p. = PDF − 6; back cover unnumbered). Chapter 1 ("9781464814570_Ch01.pdf"):
https://openknowledge.worldbank.org/server/api/core/bitstreams/07eb7f0e-03b1-5a5d-924e-c0d40f95e678/content (22 PDF pages from p. 14;
offset p. = PDF + 13). © 2020 IBRD/World Bank, CC BY 3.0 IGO. Read: overview pp. 1–7; back cover; Chapter 1 pp. 14 and 19.
- p. 1: trade expanded rapidly after 1990 on the rise of GVCs, enabling an unprecedented convergence of poor countries on rich ones; productivity and incomes rose in
  countries that became integral to GVCs (Bangladesh, China, Vietnam). But "it can no longer be taken for granted that trade will remain a
  force" for prosperity: since 2008 trade growth has been sluggish and GVC expansion has slowed. Nothing in the last decade matched the
  1990s integration of China and Eastern Europe or the Uruguay Round and NAFTA.
- p. 1: two threats to labour-intensive, trade-led growth: labour-saving technology (automation, 3D printing) and trade conflict among large
  countries.
- p. 2 (Figure O.1, titled to say GVC trade grew fast in the 1990s and stagnated after 2008): GVC share of global trade
  on a 30–55% axis, 1970–2015 (Eora26; Borin–Mancini method); the line values are not legible in the text conversion. Back cover: GVCs "now
  account for almost half of all trade".
- p. 2: GVCs grew fastest in 1990–2007, concentrated in machinery, electronics and transport equipment and in East Asia, North America and
  Western Europe. Reasons for the slowdown: slower growth and investment, slower or reversed trade reform, maturing fragmentation; China is
  producing more at home; US shale cut oil imports by a quarter in 2010–15. Unless policy predictability is restored, "any expansion of GVCs
  is likely to remain on hold".
- p. 3: in Ethiopia GVC firms are more than twice as productive as similar firms in standard trade. A 1% rise in GVC participation is
  estimated to raise per capita income by more than 1%, against 0.2% from standard trade; the biggest spurt comes on moving from commodities
  to basic manufactures (Bangladesh, Cambodia).
- p. 3: gains are unequal: lead firms' markups rise while developing-country producers' markups fall, as in garment firms in the United States
  versus India.
- p. 4: in 2017, 65% of trade was in product categories that did not exist in 1992; automation in industrial countries has raised their
  imports of inputs from developing countries; evidence of reshoring is limited.
- p. 6: for many GVC goods a day's delay equals a tariff of more than 1%.
- p. 7: the US–China trade conflict is beginning to disrupt GVCs; if it worsens, more than 30 million people could fall into poverty
  (below $5.50 a day) and global income could fall by up to $1.4 trillion. Tariff escalation in large markets inhibits processing in
  developing countries; liberalisation is overdue in agriculture and services.
- p. 19 (Ch. 1): the GVC share of world trade grew in the 1990s and early 2000s but "it appears to have stagnated or even declined in the
  last 10 years"; about half of world trade still appears GVC-related. Since 2008 trade has grown only marginally faster than output; trade
  in parts and components fell in 2011–14. The share of intermediate imports in China's goods exports fell from about 50% in the 1990s to a
  little over 30% in 2015. No new liberalisation wave: the Doha Round stalled.

## India

### TR-IN-1. Economic Survey 2019-20, Vol 1 Ch 5 "Creating Jobs and Growth by Specializing to Exports in Network Products"
`es2019-20.txt`, st. 112–137 (pp. 100–125). Offset (from `India_ES_2015-2020.md`, checked on these pages): Vol 1 p. = st. − 12. Survey
dated January 2020. Read: pp. 100–102, p. 112, pp. 121–125.
- p. 100 (chapter summary): the trade environment gives India an unprecedented opportunity to follow a China-like, labour-intensive
  export path. Integrating "Assemble in India for the world" into Make in India could create 4 crore well-paid jobs by 2025 and 8 crore by
  2030. World exports of network products are expected to reach $7 trillion in 2025.
- p. 100: "India that harbours misplaced insecurity on the trade front" will miss this chance; trade policy must be an enabler.
- p. 100 (paras 5.1–5.2): in 2001–06 alone China's labour-intensive exports created 70 million jobs for workers with primary education. The
  US–China trade war is causing major GVC adjustments as firms look for alternatives; China's image as a low-cost assembly base was already
  fading with labour shortages and rising wages.
- p. 101 (para 5.3): after the 1991 reforms India's merchandise exports grew 13.2% a year and its share of world exports rose from 0.6%
  (1991) to 1.7% (2018), but "India’s world market share remains paltry compared to 12.8 per cent for China". Merchandise imports grew faster
  (14.9% a year, 1993–2018), widening trade deficits; services exports generally grew faster than imports and cushioned the current account.
- pp. 101–102: network products are computers, electronic and electrical equipment, telecom equipment, road vehicles and the like, made in
  MNE-run production networks. Target: India's export market share at about 3.5% by 2025 and 6% by 2030; NP exports of $248 billion in 2025
  would supply about a quarter of the value added needed for a $5 trillion economy.
- p. 102 (Figure 2, 2000–2015): the China–India gap in world manufactured-export share is almost entirely a specialization effect; India is
  well diversified but spreads exports thinly over many products and partners.
- p. 112: Asia's share of world network-product exports rose from about 37% in 2000 to 51% in 2018, mostly East Asia; South, Central and
  West Asia together supplied just 3% of Asian NP exports.
- pp. 121–122 (paras 5.34–5.37, on the RCEP debate): the Survey rejects the "mercantilist" view that India's FTAs failed because deficits
  with partners widened. Gravity regressions (1993–2018, 14 agreements) find FTAs raised India's exports to partners by 13.4% (manufactures)
  and 10.9% (total merchandise), imports by 12.7% and 8.6%: a 0.7% a year rise in the trade surplus for manufactures and 2.3% for total
  merchandise. Manufactured exports gained from 8 of 14 agreements; the Korea and Japan agreements had a negative effect on them.
- pp. 124–125 (Way forward): the targets would create about 38.5 million extra jobs by 2025 and 82 million by 2030. On fears that GVC
  participation traps low-wage countries at the bottom, India's auto sector shows "such apprehensions are unwarranted" (para 5.40). Assembly needs zero or negligible tariffs on intermediate inputs (para 5.41), flexible labour rules and a pro-active FDI policy.

### TR-IN-2. Economic Survey 2016-17, Vol 1: Box 2 "Political Carrying Capacity of the West for Openness and Impact on India" (Ch 1) and Ch 2 openness section
`es2016-17.txt`. Offset (from `India_ES_2015-2020.md`, checked here): Vol 1 p. = st. − 16; the "Eight Interesting Facts" pages carry roman
numerals. Survey dated January 2017. Read: p. xiii (st. 15), pp. 7–8 (st. 23–24), pp. 39–40 (st. 55–56).
- p. xiii (Eight facts): by 2011 India's openness, trade in goods and services relative to GDP, had far overtaken China's.
- pp. 39–40 (paras 2.4–2.6): large countries usually trade less, but India now trades far more than its size predicts, a sharp turnaround
  from the pre-1991 years when it under-traded (the two-column text extract breaks the sentence, so it is paraphrased here). India's trade-to-GDP ratio doubled in the decade to 2012, to 53%, and now surpasses
  China's. FDI was running at about $75 billion a year.
- p. 7 (para 1.26): the world's political carrying capacity for globalisation may have changed after recent events (Brexit, US election);
  a strong dollar could feed protectionism, on top of stagnant or falling world trade.
- p. 7 (Box 2): "the world cannot bear too much globalisation either". The world trade-to-GDP ratio since 1870 is split into two
  globalisations, inter-war deglobalisation and hyperglobalisation in 1985–2008.
- p. 8 (Box 2): in 2003–11 India grew 8.2% a year on average and its exports 20–25% a year in real dollar terms. If India grows 8% with 15%
  export growth while the world grows 3%, India alone would lift the world export-to-GDP ratio (about 21% for goods, 27.3% for goods and
  services) by about 1.3 points in ten years, and China at 7% export growth another 1.4 points. So "India’s export growth will run up
  against the world’s carrying capacity". The world services exports-to-GDP ratio is about 6.1%; Indian services growth would add about 0.5
  point and could meet curbs on labour mobility or outsourcing. Capacity may be larger for India's services than for China's goods, since
  China's expansion was imbalanced (big surpluses, displaced rich-country manufacturing).

### TR-IN-3. Economic Survey 2017-18, Vol 1 Ch 2 "A New, Exciting Bird's-Eye View of the Indian Economy Through the GST" (exports sections)
`es2017-18.txt`, pp. 37–39 (st. 55–57). Offset (from `India_ES_2015-2020.md`, checked here): Vol 1 p. = st. − 18. Survey dated January 2018.
(ES 2017-18 has no stand-alone trade chapter; this is its main new evidence on exports. Ch 5 "Late Converger Stall", p. 71, also discusses
backlash against globalisation; not read in full.)
- p. 37 (paras 2.24–2.25): for the first time, GST returns give state-wise international exports of goods and services. Five states,
  Maharashtra (22.3%), Gujarat (17.2%), Karnataka (12.7%), Tamil Nadu (11.5%) and Telangana (6.4%), account for 70% of exports (Table 5;
  non-GST exports such as petroleum excluded). States' GSDP per capita is highly correlated with their export share in GSDP (0.70).
- p. 37 (para 2.26): India's internal trade in goods and services is about 60% of GDP, above the previous year's 30–50% estimate for goods.
- p. 39 (paras 2.30–2.31, section *Trading superstars: Indian export egalitarian exceptionalism*): the top 1% of exporting firms account for 72%, 68%,
  67% and 55% of exports in Brazil, Germany, Mexico and the US but "only 38 percent in the case of India"; the top 25% account for 82% in
  India against 93–99% elsewhere.

### TR-IN-4. Economic Survey 2024-25 (January 2025), Ch 3 "External Sector" and Ch 8 (services); partly from `India_ES_2024-2026.md`
`es2024-25.txt`. Offset: p. = st. − 45 (from `India_ES_2024-2026.md`, checked on st. 129 = p. 84 and st. 265 = p. 220). Items marked
(ES24-n) restate `India_ES_2024-2026.md`; pp. 84–85 and p. 220 were re-read here.
- p. 84 (para 3.12): regional trade agreements in force rose from 22 in 1990 to 369 by August 2024. Between 2000 and 2024 India's average
  tariff on dutiable items fell from 48.9% to 17.3%; China's from 16.4% to 8.3%.
- p. 85 (Box III.1, "Tariffs and successful industrial policy design"): tariffs are presented as a standard industrial-policy tool to be
  used in a calibrated way; the box cites Klein and Pettis and Robert Allen on Europe and North America catching up with Britain behind high
  external tariffs. This is the Survey's tariff stance in the year before the US tariffs.
- p. 220 (para 8.3): in 2023 the US led world services exports with 13%, then the UK (7.4%) and Germany (5.5%); "India ranks seventh
  globally, representing a 4.3 per cent share". Services have offset the swings in India's share of merchandise exports.
- (ES24-9) pp. 10–11, 28: trade policy uncertainty rose sharply but was below 2018-19 levels; G20 import-restrictive measures covered 12.7%
  of G20 imports, over three times the 2015 level; the "evolving trade stance of a few major economies could affect key Indian export
  sectors" (para 1.59) such as chemicals, machinery, textiles and electronics. Ch 3 also flags friend-shoring and the EU's CBAM from 2026.
- (ES24-10) pp. 26–27: April–December 2024 merchandise exports +1.6% (non-oil +7.1%), imports +5.2%; services exports +11.6%; CAD 1.2% of
  GDP in Q2 FY25.
- (ES24-14) pp. 140–141: UNIDO projects China at 45% of world manufacturing by 2030; the globalisation-era model of outsourcing
  manufacturing to China is being reset.

### TR-IN-5. Economic Survey 2025-26 (January 2026), Ch 1 and Ch 4 "External Sector"; partly from `India_ES_2024-2026.md`
`es2025-26.txt`. Offset: p. = st. − 51 (from `India_ES_2024-2026.md`, checked on st. 203 = p. 152). Preface dated 29 January 2026. Items
marked (ES25-n) restate `India_ES_2024-2026.md` (stitched pages confirmed here: st. 13, 53, 210, 220); pp. 27, 152–153 and 260 were read
here.
- (ES25-6) p. 2 (para 1.1): "The most disruptive amongst these disturbances was the imposition of tariffs by the USA". The Survey tracks
  the IMF's 2025 world growth forecast: 3.3% (January 2025), 2.8% (April), 3.2% (October), 3.3% (January 2026).
- (ES25-7) p. 159 (para 4.40): India faces an "effective export tariff rate of 50 per cent on goods exported to the US". Table IV.1
  (April–November 2025, year on year): gems and jewellery exports to the US −44.3% (US share 33.7% → 18.7%) while exports to the world rose
  0.6%; marine products −5.7% to the US but +16.1% to the world; pharma +0.8% to the US. The main text gives no reason for the extra 25%
  (footnote 26 cites the 6 August 2025 Executive Order, which refers to the Russian Federation).
- p. 27 (para 1.35): total exports (goods and services) were a record US$825.3 billion in FY25. Despite US tariffs, merchandise exports grew
  2.4% and services exports 6.5% in April–December 2025; merchandise imports +5.9%; CAD 0.8% of GDP in H1 FY26.
- p. 152 (para 4.18): between 2005 and 2024 India's share of world merchandise exports rose from 1% to 1.8%, and of world commercial services
  exports from 2% to 4.3% (citing WTO). p. 152–153 (para 4.20): FY25 total exports US$825.3 billion (+6.1%), led by services (+13.6%); total
  imports US$919.9 billion; overall trade deficit US$94.7 billion.
- p. 152 (para 4.19): UNCTAD ranks India third in the Global South (after China and the UAE) on diversity of trade partners.
- p. 260: "India is the world’s seventh-largest exporter of services", its share more than doubling from 2% (2005) to 4.3% (2024).
- (ES25-9) p. 30, p. 169: the tariff shock was used to push GST rationalisation and deregulation; relief included a five-year Export
  Promotion Mission and RBI relief for exporters (export credit up to 450 days; realisation period 9 → 15 months).
- (ES25-10) Preface p. xii, p. 28, p. 168: trade agreements: UK CETA concluded; Oman CEPA signed 18 December 2025; New Zealand concluded
  December 2025; EFTA TEPA with a US$100 billion investment commitment; the EU FTA concluded "after three years of negotiations" (Preface),
  pending ratification; talks continuing with the US, Chile and Peru.

### TR-IN-6. India in 2026: tariff cut and unsettled US trade relations, from `India_2026.md` (not re-read)
Restated from `India_2026.md` with its citations; the underlying Ministry of Finance Monthly Economic Reviews (MER) were not re-fetched.
- (IN26-38) MER April 2026, abstract, PDF p. 7: the IMF's April 2026 WEO raised India's 2026 growth to 6.5%, crediting domestic demand and the
  cut in US tariffs on Indian goods from 50% to 10% (matches TR-IMF-4, WEO April 2026 Ch. 1 p. 11).
- (IN26-40) MER September 2026, abstract, PDF p. 4: reports a US Graham Bill allowing tariffs of up to 100% on countries buying Russian
  crude; trade relations with the US "remain unsettled". Single source; `India_2026.md` flags it for verification.
- `India_2026.md` (lines on March 2026 trade): with the West Asia war, March 2026 merchandise exports fell 7.4% year on year; exports to
  the UAE fell 61.93% and to Saudi Arabia 45.67%.

### TR-IN-7. India and RCEP, November 2019 (PIB, Ministry of Commerce & Industry)
PIB release IDs were found with a web search restricted to pib.gov.in and mea.gov.in; the pages were then fetched with plain `curl`. The
PIB page headings did not come through in the HTML, so releases are cited by ID and date. No MEA briefing text on the decision itself
was fetched (see Not read).
- PIB Release ID 1606300, 13 March 2020 (written reply in the Rajya Sabha by Commerce Minister Piyush Goyal),
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=1606300: at the 3rd RCEP Leaders' Summit in Bangkok on 4 November 2019, India said the
  current structure of RCEP did not reflect the RCEP Guiding Principles or address India's outstanding issues and concerns; since it did not
  adequately meet the ambition and concerns of India's stakeholders, "India did not join RCEP in its current form".
- PIB Release ID 1596654, 16 December 2019, Year End Review 2019 of the Ministry of Commerce & Industry,
  https://www.pib.gov.in/PressReleasePage.aspx?PRID=1596654: "India’s key concerns were not addressed"; the decision is presented as
  protecting farmers, the dairy sector and small manufacturers from RCEP rules. The same review reports agreement to review the
  ASEAN–India FTA, the first two bilateral safeguard cases by DGTR, and a Steel Import Monitoring System from 1 November 2019.
- Contrast with TR-IN-1 (Survey published January 2020): the Survey's regressions found India's FTAs had on balance raised its trade
  surplus, and it criticised the "mercantilist" reading of FTA deficits that the government's RCEP stance relied on.

### TR-IN-8. Foreign Trade Policy 2023 (DGFT) and its launch release
FTP page https://www.dgft.gov.in/CP/?opt=ft-policy (lists chapter PDFs, current version "v1.2.2", Chapter 4 revised 2026). Chapter 1
"Legal Framework and Trade Facilitation": https://content.dgft.gov.in/Website/Chapter_1_Revised_FTP_v1.2.2.pdf (8 pages; printed page =
PDF page). Launch release: PIB Release ID 1912572, 31 March 2023, https://www.pib.gov.in/PressReleasePage.aspx?PRID=1912572.
- FTP Ch 1, p. 2 (para 1.01): FTP 2023 came into force on 1 April 2023 and runs "unless otherwise specified or amended", with no fixed end
  date. Para 1.06 (p. 3): India ratified the WTO Trade Facilitation Agreement in April 2016.
- PIB 1912572: the policy aims to take exports to US$2 trillion by 2030; "FTP seeks to take India's exports to 2 trillion dollars by 2030"
  (sub-heading attributed to Goyal). Total exports had crossed US$760 billion (2022-23).
- PIB 1912572: four pillars: incentive to remission; export promotion through collaboration (exporters, states, districts, missions); ease
  of doing business; emerging areas (e-commerce, Districts as Export Hubs, SCOMET dual-use items). The policy is described as "moving away
  from an incentive regime to a regime which is facilitating". E-commerce export potential estimated at US$200–300 billion by 2030; a
  one-time amnesty for defaults on export obligations.

---

## Synthesis: how the view of trade moved, 2000–2026

1. **1985–2008: trade ran ahead of output.** Real world trade grew about twice as fast as world GDP in 1985–2007 (TR-IMF-1, p. 63). GVCs
   drove the surge after 1990, including the integration of China and Eastern Europe (TR-WB-1, pp. 1–2). The Indian Survey calls 1985–2008
   hyperglobalisation (TR-IN-2, p. 7). India's trade-to-GDP ratio doubled in the decade to 2012, to 53%, passing China's (TR-IN-2, p. 40).
2. **China shock.** The 2016 WEO cites Autor–Dorn–Hanson on US local labour-market losses from Chinese imports, and says adjustment costs
   "should not be underestimated" (TR-IMF-1, p. 67). Box 2.1 shows Chinese import competition also raised sector TFP in OECD economies (p. 90).
   The 2017 Survey says China's export expansion was imbalanced and created few jobs in rich countries (TR-IN-2, p. 8).
3. **Post-2011 slowdown: a cyclical or structural cause?** The IMF (2016) blames mainly weak demand and investment, up to three-quarters of
   it, plus policy and the GVC plateau, about 1¾ points (TR-IMF-1, p. 65). The World Bank (2020) stresses the maturing of fragmentation, China
   making more at home (its imported-input share fell from about 50% to just over 30%) and the end of new liberalisation (TR-WB-1, p. 19). The
   WTO (2023) says the flat trade-to-GDP ratio after 2008 was not caused by trade tensions, because trade costs kept falling (TR-WTO-2, p. 9).
   These views are compatible but weight things differently: IMF on demand, WB and WTO on structure.
4. **Services rose.** Services trade grew faster than goods: 5.4% against 4.6% a year in 2005–17, and it was more resilient in 2012–15
   (TR-WTO-1, p. 6; TR-IMF-1, p. 69). Services are close to half of world trade in value-added terms (TR-WTO-1, p. 6). India's share of world
   services exports rose from 2% (2005) to 4.3% (2023–24), seventh in the world (TR-IN-4, p. 220; TR-IN-5, p. 152). The WTO's 2025 table puts
   India eighth at 4.3% (TR-WTO-3, p. 42). **Disagreement on rank: seventh (Survey) vs eighth (WTO 2025 table).** The year differs, and the
   Survey may count only commercial services. Compare TR-WTO-1 (2017): India was second in IT services exports.
5. **GVC share.** "Almost half" of world trade (TR-WB-1, back cover and p. 19). Participation plateaued from 2011 (TR-IMF-1, p. 81). The WTO
   (2023) notes GVCs spreading to new economies such as Viet Nam and Cambodia (TR-WTO-2, p. 9).
6. **2018–19 tariff war.** The World Bank warned that escalation could push 30 million people into poverty and cut global income by up to
   $1.4 trillion (TR-WB-1, p. 7). The Indian Survey saw the war as an opening for "Assemble in India" in network products (TR-IN-1, p. 100).
   India stayed out of RCEP in November 2019 (TR-IN-7). In the same weeks, the Survey argued that India's FTAs had helped its trade balance
   (TR-IN-1, pp. 121–122). This is a policy tension worth noting.
7. **Pandemic.** Goods trade dropped 12.2% and services 21.4% at the trough, but goods recovered by October 2021. The IMF called reshoring
   "misguided" and recommended diversification instead (TR-IMF-2, pp. 87, 96).
8. **Fragmentation, 2022–23.** FDI fell from 3.3% of GDP in the 2000s to 1.3% in 2018–22, and FDI fragmentation could cost about 2% of world
   output (TR-IMF-3, pp. 91, 94). Splitting into trade blocs could cost about 5% of global real income (TR-WTO-2, p. 21). Since 2022,
   between-bloc trade has grown 4–6% more slowly than within-bloc trade (TR-WTO-2, p. 9). By 2026 the WTO finds the bloc gap has narrowed;
   what remains is mostly US–China decoupling (TR-WTO-3, p. 3).
9. **2025–26 tariffs.** The US effective tariff went from under 3% in January 2025 to about 25% in April 2025, then about 19% (October 2025)
   and 13.5% in the April 2026 projections (TR-IMF-4). India faced an effective 50% in late 2025 (TR-IN-5, p. 159), cut to 10% by April 2026
   (TR-IMF-4; TR-IN-6). Trade did not collapse. Merchandise volume grew 4.2% in 2025 (WTO) or 5.0–5.1% for goods and services (IMF), helped by
   front-loading and AI hardware (TR-WTO-3, p. 6; TR-IMF-4). **Disagreement on 2025 trade growth: 4.2% (WTO, goods only) vs 5.0–5.1% (IMF,
   goods and services).** US imports from China fell 29% in 2025 (TR-WTO-3, p. 23).
10. **India's place.** India had 1.7% of world goods exports in 2018 against China's 12.8% (TR-IN-1, p. 101). It had 1.8% in 2024 (TR-IN-5,
    p. 152) and 1.7% (19th) in 2025, against China's 14.4% (TR-WTO-3, p. 40). India's average tariff on dutiable items fell from 48.9% (2000)
    to 17.3% (2024), while the 2025 Survey also defends calibrated tariffs as industrial policy (TR-IN-4, pp. 84–85). The FTP 2023 target is
    US$2 trillion of exports by 2030 (TR-IN-8), against US$825 billion in FY25 (TR-IN-5).

---

## Not read / not found

- **WEO October 2016 full volume** (`/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2016/02/pdf/_text.pdf`) was not
  tried. The Ch 2 PDF (TR-IMF-1) was enough. Box 2.2 (adjustment policies) and the annexes were not read.
- **imf.org rate limits:** the first downloads of the April 2022 and April 2023 Ch 4 PDFs returned HTTP 429 (167-byte JSON body). Both
  worked on a plain retry a few minutes later.
- **WEO April 2025, October 2025 and the 2026 issues** were not re-fetched. TR-IMF-4 relies on `IMF_2024-2025.md` and `IMF_2026.md`, as
  instructed. No IMF chapter on the 2025 tariffs themselves was read (for example, October 2025 Ch 3 on industrial policy, listed as not read
  in `IMF_2024-2025.md`).
- **WTO World Trade Report 2019 full report** (`00_wtr19_e.pdf`) and sections C–F were not downloaded. Only the front matter, the
  executive summary and section B were read.
- **WTO World Trade Report 2023 chapters B–E** were not read beyond the executive summary and chapter A.
- **WTO Global Trade Outlook, March 2026** (the baseline that TR-WTO-3 revises) was not fetched. Its 1.9% and 4.8% figures come from the
  October 2026 update. A guessed landing page `https://www.wto.org/english/res_e/publications_e/trade_outlook26_e.htm` redirected to
  WTO's 404 page. Guessed PDFs `trade_outlook26_e.pdf`, `trade_outlook25oct_e.pdf` and `trade_outlook25_oct_e.pdf` returned HTTP 302 to
  HTML (not found). The wto.org news listing (`news_e.htm`, `archive_e/tfore_arc_e.htm`) is built by JavaScript, so
  `/library/news/news_2026_e.js` was used to find the October 2026 release.
- **World Bank WDR 2020:** the "bitstream/handle/10986/32437/211457ov.pdf" link on the landing page returned HTTP 200 with an HTML app
  shell, not a PDF. The repository API worked (see TR-WB-1). Chapters 2–9 were not read. The Figure O.1 line values could not be read from
  the text conversion. The ~50% GVC share is stated in words on p. 19 and on the back cover.
- **MEA briefings on RCEP:** the web search found a 31 October/2 November 2019 pre-visit briefing by Secretary (East) and a 7 November
  2019 weekly briefing (Hindi page). Neither was fetched, so no MEA wording on the 4 November decision is used. TR-IN-7 uses PIB only.
- **Foreign Trade Policy 2023:** only Chapter 1 of the current revised text (v1.2.2) was read. The 2026 revision of Chapter 4 was not
  checked, and the original March 2023 FTP PDF was not fetched. The $2 trillion target comes from the PIB launch release, not the FTP text.
  Grep of Ch 1 found no target.
- **Economic Survey 2017-18 Ch 5 ("Late Converger Stall")**: its globalisation-backlash passage (p. 71, st. 89) was only skimmed.
- **ES 2024-25 and 2025-26 external-sector chapters** were not re-read in full. TR-IN-4 and TR-IN-5 re-read only the pages listed and rely
  on `India_ES_2024-2026.md` for the rest.
- **China's WTO accession (December 2001):** none of the documents read gives the accession date or terms directly. The IMF and WB
  documents refer to China's integration in the 1990s–2000s (TR-WB-1, p. 1; TR-IMF-1, p. 64). A WTO accession page was not fetched. Do not
  supply the date or terms from memory without a source.
