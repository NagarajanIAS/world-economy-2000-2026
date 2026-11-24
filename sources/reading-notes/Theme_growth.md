# Reading notes: theme chapter "Growth and convergence, 2000–2026" (read 22 Nov 2026)

Method: IMF issue pages fetched from imf.org with plain `curl` (default user-agent, no custom headers), starting from the listing page
https://www.imf.org/en/Publications/WEO. That listing does not reach back to every 2000s and 2010s issue. For older issues I followed the
"http://www.imf.org/external/pubs/ft/weo/YYYY/NN/index.htm" table-of-contents link printed on the new-style issue page, and took the chapter
PDF links from those pages. World Bank documents came from worldbank.org and openknowledge.worldbank.org, again with plain `curl`. Downloads
are in `/private/tmp/growth_dl/` (IMF in `pdf/`, World Bank in `wb/`). PDFs were converted with `pdftotext` (plain and `-layout`). Each
quote was checked by script against the plain-text conversion. The check normalises case, spaces, curly quotes and line-end hyphens. Quotes
are verbatim and under 15 words, at most one per bullet; everything else is paraphrase.

Page numbers are the printed numbers ("International Monetary Fund | Month Year N" in the 2015–2025 IMF chapters; bare footers in the 2003
chapter and in the World Bank books). Offsets: WEO Apr 2003 Ch III p. = PDF + 94; WEO Oct 2015 Ch 2 p. = PDF + 64; WEO Apr 2017 full text
p. = PDF − 18; WEO Apr 2024 Ch 3 p. = PDF + 64; WEO Oct 2025 Ch 2 p. = PDF + 50; *Growth Report* p. = PDF − 15; *Falling Long-Term Growth
Prospects* Overview p. = PDF − 30.

India: the Economic Survey extracts in `Econ Subject/sources/text/es<YEAR>.txt`. Pages are cited as in `India_ES_2024-2026.md`: "p." is the
printed page and "st." is the stitched page (form feeds + 1). Offsets used here, taken from the existing India notes and checked on the pages
cited: ES 2007-08 Ch 2 p. = st. − 1; ES 2013-14 p. = st.; ES 2015-16 Vol 1 p. = st.; ES 2022-23 p. = st. − 43; ES 2024-25 p. = st. − 45;
ES 2025-26 p. = st. − 51.

Item labels: GR-IMF-n, GR-WB-n, GR-IN-n. Growth rates are annual percent unless stated. Indian years are fiscal years (FY25 = 2024-25).

---

## IMF

### GR-IMF-1. WEO April 2003, Chapter III "Growth and Institutions"
Issue page title: "World Economic Outlook, April 2003: Growth and Institutions". Issue page:
https://www.imf.org/en/publications/weo/issues/2016/12/30/world-economic-outlook-april-2003-growth-and-institutions-16369 (its
bibliographic block says "Published: September 24, 2002", which cannot be right for an April 2003 issue; the date is the issue's
label, April 2003). Contents page: http://www.imf.org/external/pubs/ft/weo/2003/01/index.htm. Chapter PDF:
https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2003/01/pdf/_chapter3pdf.pdf (34 pages,
pp. 95–128). Main authors named on p. 95: Maitland MacFarlan (lead), Hali Edison and Nicola Spatafora. Read: pp. 95–97 (introduction),
pp. 105–113 (empirical results; "Institutional Reform in Practice").
- p. 95: gaps in GDP per capita are huge. Incomes run from about $100 a year (Ethiopia) to over $43,000 (Switzerland). Few countries sit at
  an "intermediate" $6,000–16,000, and most of sub-Saharan Africa is well under $1,000. Better macro policies may have helped end the
  stagnation that began in the early 1980s, but developing economies still face large, persistent income gaps (Figure 3.1).
- p. 96 (Table 3.1): in 1995 dollars, China and India both sit in Group 2 ($281–769) of six income groups.
- pp. 105–106: the aggregate governance measure alone explains nearly three-quarters of cross-country variation in income per head. Raising
  institutional quality by one standard deviation (Cameroon to the sample average) would raise income per head, "income would increase
  almost five-fold (by 462 percent)", from $600 to $2,760.
- p. 106: if sub-Saharan Africa's institutions improved to developing Asia's mean, its per capita income would rise 80% (about $800 to over
  $1,400). p. 107: developing Asia's income roughly doubles if its institutions reach the all-country average.
- p. 107 (Table 3.3): a one-standard-deviation gain in institutional quality adds 1.4 points a year to growth of GDP per capita (1960–98
  regressions), and 1.7 points in sub-Saharan Africa if it adopted average institutions. The same gain cuts the volatility of growth by 1.2
  points (p. 108: by over a quarter).
- p. 109: once institutions are controlled for, most policy variables lose significance for the level of income. The chapter reports the
  literature's finding that "institutions are the dominant factor, with little if any independent influence of policies", and notes Sachs's
  objection. Financial development still adds growth (0.5 point a year for sub-Saharan Africa at the sample average).
- pp. 110–111: the weak policy result partly reflects method (cross-sections; institutions and policies are highly correlated). The bottom
  line is not that policies are unimportant.
- p. 112: the analysis finds "catch-up" or convergence effects: the growth payoff from better institutions is largest for countries
  starting lowest.
- p. 113: there is no single recipe. Fast growers such as China, Botswana and Mauritius did well "under substantially different institutional
  arrangements".

### GR-IMF-2. WEO October 2015, Chapter 2 "Where Are Commodity Exporters Headed? Output Growth in the Aftermath of the Commodity Boom"
Issue page title: "World Economic Outlook, October 2015: Adjusting to Lower Commodity Prices". Published October 6, 2015 (issue page).
Issue page: https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/World-Economic-Outlook-October-2015-Adjusting-to-Lower-Commodity-Prices-43229.
Contents page: http://www.imf.org/external/pubs/ft/weo/2015/02/index.htm. Chapter PDF:
https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2015/02/pdf/_c2pdf.pdf. Team leader: Oya Celasun
(p. 65). Read: summary and introduction pp. 65–67; Australia/Canada/Chile case studies p. 84; conclusions pp. 84–85.
- p. 65: after almost a decade of rises, energy and metal prices have fallen sharply since 2011. Many analysts link the upswing to strong
  emerging-market growth, especially in east Asia, and the downswing to softer growth there and more supply. Footnote 1 cites work on
  China's rising share of commodity imports in the 2000s.
- p. 65 (summary): actual and potential output both move with the commodity terms of trade, but "actual output comoves twice as strongly as
  potential output".
- p. 66: commodity exporters' growth slowed far more than other EMDEs'. Their medium-term prospects were also cut: "almost 1 percentage point
  has been shaved off" the average five-year-ahead forecast since 2012. Other EMDEs' medium-term forecasts were broadly unchanged.
- p. 67: in past long terms-of-trade booms, actual growth ran 1.0–1.5 points higher in upswings than in downswings, potential growth only
  0.3–0.5 point higher. Investment is the main channel to potential output; employment and TFP contribute little.
- p. 67: growth swings harder in energy and metal exporters, in countries with shallow finance, rigid exchange rates and procyclical fiscal
  spending.
- p. 84: in Australia, Canada and Chile, economy-wide TFP growth slowed during the 2000–10 boom, with weak TFP in the extractive sector a
  common contributor.
- p. 85: the weak price outlook is projected to cut commodity exporters' growth by about 1 point a year in 2015–17 relative to 2012–14 (about
  2¼ points for energy exporters). The drag on potential growth is about ⅓ point (⅔ for energy exporters).
- p. 85: post-boom slowdowns mostly reflect output cooling to a potential that is itself growing more slowly, so policymakers should not
  overestimate output gaps. The chapter concludes that "declining growth of potential output exacerbates the postboom slowdowns".

### GR-IMF-3. WEO April 2017, Chapter 2 "Roads Less Traveled: Growth in Emerging Market and Developing Economies in a Complicated External Environment"
Issue page title: "World Economic Outlook, April 2017 : Gaining Momentum?" (spacing as on the page). Published April 18, 2017. Issue page:
https://www.imf.org/en/publications/weo/issues/2019/08/30/world-economic-outlook-april-2017-gaining-momentum-44510. PDF (full volume, the
only PDF on the page): https://www.imf.org/-/media/files/publications/weo/2017/april/pdf/text.pdf. Authors: Bertrand Gruss, Malhar Nabar
(team leader), Marcos Poplawski-Ribeiro (p. 65). Read: pp. 65–69 (summary, growth performance, convergence record), pp. 87–88 ("Taking
Stock" and Conclusion), Box 2.1 p. 89.
- p. 65: EMDEs now account for more than 75% of global growth in output and consumption, almost double their share two decades earlier.
  External conditions (terms of trade, external demand and especially external finance) have become more important for their medium-term
  growth.
- p. 65: the income gaps leave room for catch-up, but "steady catch-up growth has not been automatic in the past". Growth comes in
  accelerations and reversals.
- p. 66: the contribution of external financial conditions to EMDE medium-term growth rose by about ½ point between 1995–2004 and 2005–14,
  about a third of the rise in per capita growth. Demand from other EMDEs has become a more powerful force.
- p. 67: EMDEs supplied 70% of global growth in 2000–08 (PPP terms), nearly double their 1980s share. In 90% of EMDEs, real income per capita
  is still less than half the US level (85% for income per worker).
- p. 68 (Figure 2.3): of the EMDEs in the bottom three quintiles in the 1970s, the best performers rose from about 11% to about 21% of US
  income. For the group as a whole, "the median relative income level for that group has in fact declined".
- p. 69 (Figure 2.4): the median income gap held steady in the 1970s and widened in the 1980s and 1990s (Latin America's lost decade; Asian
  and Latin American crises). It then narrowed in the 2000s and 2010s, helped by the commodity boom and other tailwinds. This was not
  "convergence from above": except in the crisis, US income per head did not fall.
- p. 87: advanced-economy potential growth projections were cut from close to 2% (October 2014 WEO) to just over 1½% (October 2016 WEO),
  which means weaker external demand for EMDEs. External demand in 2017–22 is expected to be weaker than in the past (Figure 2.20).
- p. 88 (Conclusion): EMDEs can get more from a weaker external impulse by strengthening institutions, protecting trade integration, letting
  exchange rates move and containing current-account, external-debt and public-debt vulnerabilities. Terms-of-trade windfalls matter most for
  commodity exporters.
- p. 89 (Box 2.1): the BRICS' income gap with the US narrowed markedly in 2002–14. China's per capita income rose by about 13 points as a
  share of the US level, Russia's by about 26 points. Within India, the richest state's income is about 10 times the poorest's.

### GR-IMF-4. WEO April 2024, Chapter 3 "Slowdown in Global Medium-Term Growth: What Will It Take to Turn the Tide?"
Issue page title: "World Economic Outlook, April 2024: Steady but Slow: Resilience amid Divergence". Published April 16, 2024. Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2024/04/16/world-economic-outlook-april-2024. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2024/april/english/ch3.pdf (pp. 65–85). Co-leads: Nan Li and Diaa Noureldin (p. 65).
Read: pp. 65–68 (summary, findings, forecasts, growth accounting), pp. 77–78 (scenarios, conclusions), Box 3.2 p. 80.
- p. 65: "its medium-term growth prospects have consistently been revised downward" since the 2008–09 crisis. The slowdown started in the
  early 2000s in advanced economies and after the crisis in EMDEs. A broad TFP slowdown accounts for more than half of the decline. Without
  policy action or new technology, global growth will be only 2.8% by the end of the decade, 1 point below its 2000–19 average.
- p. 66 (Figure 3.1; findings): five-year-ahead world growth forecasts from both the WEO and Consensus Economics trend down over 2000–29.
  The downgrade is "reflecting secular forces rather than forecaster pessimism", and is largest in emerging market economies.
- p. 66: in EMDEs, TFP growth rose before the crisis and then fell, "mirroring the globalization cycle". Rising misallocation of capital and
  labour across firms subtracted 0.6 point a year from TFP growth, so TFP growth could have been 50% higher.
- p. 67: returning to the 2000–19 average of 3.8% would need reforms; by 2030 global labour-supply growth is projected at only 0.3%.
- p. 67 (Figure 3.2): since 2008 five-year-ahead forecasts have fallen for nearly 82% of economies. Brazil, China, India, Indonesia and Russia
  account for about 0.8 point of the 1.8-point drop in projected global growth; the downshift is largest in East Asia and the Pacific.
- p. 67: no pessimism bias is found; the cuts may partly correct earlier optimism, especially since 2012.
- p. 68: the catch-up of EMDEs can "explain only about a quarter of the projected global growth decline since 2008". Box 3.2 suggests convergence is
  slowing or may reverse.
- p. 68: TFP growth in advanced economies fell from 1.3% (1995–2000) to 0.2% after the pandemic. In emerging markets it fell from 2.5% and in
  low-income countries from 2% (2001–07) to 0.7% and nearly zero. Capital formation also slowed: after 2008 in advanced economies and since
  2013 in emerging markets.
- p. 77: of the scenarios, structural reforms closing 15% of the policy gap with the US could add 1.2 points to global growth. AI could add
  0.1–0.8 point; fragmentation could subtract 0.1–0.8 point.
- pp. 77–78 (Conclusions): the headwinds are persistent; the chapter's policy list covers competition, trade openness, finance, labour
  flexibility, migration, female participation and AI, and warns that poorly designed industrial policy may hinder reallocation.
- p. 80 (Box 3.2): between-country convergence held up in 2008–19 and was fastest in 2008–12. The rate turned positive (no convergence) after
  the pandemic: "Current projections point to no convergence over the medium term." Global inequality fell from the mid-2000s, mainly through
  convergence between countries, but most of it now stems from differences within countries.

### GR-IMF-5 (context only). WEO October 2025, Chapter 2 "Emerging Market Resilience: Good Luck or Good Policies?"
Issue page title: "World Economic Outlook, October 2025: Global Economy in Flux, Prospects Remain Dim". Published October 14, 2025. Issue
page: https://www.imf.org/en/publications/weo/issues/2025/10/14/world-economic-outlook-october-2025. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2025/october/english/ch2.pdf (pp. 51–73). Co-leads: Francesco Grigoli and Andrea
Presbitero (p. 51). Read: pp. 51–52, pp. 66–67. This is a chapter on shocks, not trend growth; it is here for the 2020s explanation of why EM
economies held up.
- p. 51: EMs have been resilient to risk-off shocks. Good luck helped, but better monetary, macroprudential and fiscal frameworks
  played a critical role.
- p. 51: EMs also benefited from spillovers from China's sustained growth and integration.
- p. 66: "attributing recent resilience solely to good luck does not tell the whole story". Comparing typical post-GFC and pre-GFC risk-off
  episodes, better frameworks gave 0.5 point higher growth and 0.6 point lower inflation; favourable external conditions added 0.5 point of
  growth.
- p. 67: no complacency: external conditions may not stay favourable, and fiscal buffers have eroded in some cases.

---

## World Bank

### GR-WB-1. Commission on Growth and Development, *The Growth Report: Strategies for Sustained Growth and Inclusive Development* (2008)
Title as on the Open Knowledge Repository page ("The Growth Report : Strategies for Sustained Growth and Inclusive Development"; citation
date 2008). Page: https://openknowledge.worldbank.org/handle/10986/6507. PDF:
https://openknowledge.worldbank.org/bitstreams/df194a38-cb6f-5553-8fd8-e48a8a7c9574/download (© 2008 IBRD/World Bank on behalf of the
Commission). The Commission had 19 leaders, mostly from developing countries, plus two academics (Preface); members include Montek Singh
Ahluwalia (PDF p. 5). Read: Overview p. 1; Part 1 pp. 19–22; "Middle-Income Countries" pp. 82–83.
- p. 1: since 1950, 13 economies have grown at 7% a year or more for 25 years or longer, roughly doubling every decade. "Unlike miracles,
  sustained, high growth can be explained and, we hope, repeated."
- p. 19: China and then India reformed closed, regulated economies, partly following international example, which helps explain why global
  growth rose. About 65% of the world's roughly 6 billion people live in high-income or high-growth economies, up from under a fifth 30 years
  ago; the remaining 2 billion live where incomes stagnate or fall.
- p. 19: the 13 are Botswana, Brazil, China, Hong Kong (China), Indonesia, Japan, Korea, Malaysia, Malta, Oman, Singapore, Taiwan (China) and
  Thailand; "India and Vietnam, may be on their way to joining this group".
- p. 20 (Table 1): six reached high income. Others lost momentum early; Brazil's fast growth (1950–80) faded around the second oil shock and
  had not resumed. China's per capita income went from 105 to 1,400 (constant 2000 US$) over 1961–2005.
- p. 21: five common traits: they fully exploited the world economy, kept macro stability, saved and invested a lot, let markets allocate
  resources, and had committed, credible, capable governments. Openness is the most important.
- p. 22: catch-up works because learning is easier than inventing; the high-growth countries "imported what the rest of the world knew, and
  exported what it wanted."
- pp. 82–83: only six of the 13 reached advanced-economy incomes. Elsewhere, including much of Latin America, "growth has slowed markedly at
  the middle-income level" (p. 83). As surplus labour runs out, wages rise and labour-intensive exports fade, and policy must move to skills,
  technology and markets. China is cited as having both stages at once.

### GR-WB-2. M. Ayhan Kose and Franziska Ohnsorge (eds.), *Falling Long-Term Growth Prospects: Trends, Expectations, and Policies* (World Bank)
Page title: "Falling Long-Term Growth Prospects". Page: https://www.worldbank.org/en/research/publication/long-term-growth-prospects.
"Full report" link: https://openknowledge.worldbank.org/server/api/core/bitstreams/3e4fc06d-db25-447d-8797-a032e6dd9688/content (562
PDF pages). The copyright page reads "© 2024"; no release date was found on the page as fetched. Read: Overview pp. 1–4, 9, 11, 14, 22–28.
- p. 1: "a structural growth slowdown is under way". On current trends, global potential growth will fall to a three-decade low over the rest
  of the 2020s. Nearly all forces behind growth since the early 1990s have weakened: investment and TFP growth, labour-force growth, and
  trade.
- p. 1: the authors' 2015 study asked whether the EMDE slowdown was a rough patch; their answer now is a prolonged period of weakness.
- p. 2: global growth fell from 4.5% in 2010 to a projected 1.7% in 2023. Growth in 2011–21 was lower than in 2000–10 in 80% of advanced
  economies and 75% of EMDEs.
- p. 2 (convergence): EMDE per capita incomes grew 2.0 points a year faster than advanced economies' in 2011–21, against 3.4 points in
  2000–10. Middle-income per capita growth fell from 4.9% to 3.5%, low-income from 2.9% to 1.7%.
- p. 4: trade grew only as fast as GDP in 2010–19, against twice as fast in 1990–2011. Factor reallocation and education and health gains
  have also faded; EMDE investment growth is projected at 3.5% a year, about half its 2000–21 average.
- p. 9: global potential growth fell from 3.5% (2000–10) to 2.6% (2011–21); EMDE potential growth from 6.0% to 5.0%. Recessions leave lasting
  damage: potential growth 1.4 points lower even five years later.
- p. 11: global potential growth is projected at 2.2% a year in 2022–30, "the slowest pace since 2000", about half of the slowdown due to
  ageing and falling participation.
- p. 14: policies that raise investment, human capital and labour supply could add 0.7 point a year in 2022–30, offsetting the projected
  0.4-point global decline.
- p. 26 (Figure O.8): EAP is expected to show the sharpest decline in 2022–30, mainly from slower capital accumulation in China. Potential
  growth in South Asia stayed broadly unchanged between 2000–10 and 2011–21 (p. 9).
- p. 28: investment weakness in the 2010s reflects slower credit, worse terms of trade for commodity exporters, slowing reform, and China's
  move away from fixed-investment-led growth.
- p. 2: restoring the previous decade's growth would need "a herculean collective policy effort".

---

## India: Economic Surveys

### GR-IN-1. Economic Survey 2007-08, Ch 2 "Challenges, Policy Response and Medium Term Prospects"
`es2007-08.txt`, p. 18 (st. 19).
- p. 18: the economy has moved to a higher growth path as the 1990s reforms work through. The Survey identifies two statistically significant
  breaks: the early 1980s (out of the "Hindu growth rate" of about 3.5–5.5%) and the mid-1990s. Growth stepped up to 6.5% in the late 1990s
  and 7.8% in the Tenth Plan (2002-07), with the last three years above 9%.
- p. 18: if the trend persists, the Eleventh Plan (2007-08 to 2011-12) would average over 8.9%. The slightly lower 2007-08 growth is on the moving-average trend and
  is not read as a shift to a lower growth trend.
- p. 18: about a dozen medium/large economies have averaged 9% or more for a decade; fewer than half kept it up for two decades. Meeting the
  Plan target and then growing 9.5% would put India among them, alongside China, Singapore, Japan, Taiwan, Thailand, Korea, Portugal, Greece
  and Hong Kong. The binding constraints are infrastructure and institutional and implementation weaknesses.

### GR-IN-2. Economic Survey 2013-14, Ch 1 and Ch 2 "Issues and Priorities"
`es2013-14.txt`, p. 3 (st. 3), p. 29 (st. 29). The text dates reserves to 20 June 2014 (p. 3).
- p. 3: growth fell from an average of 8.3% a year in 2004-05 to 2011-12 to 4.6% in 2012-13 and 2013-14. EMDEs including China slowed from
  6.8% to 4.9%, so India's slowdown is "broadly in sync with trends in other emerging economies, but relatively deeper". Manufacturing
  averaged 0.2%.
- p. 29: "The key to reviving investment in India lies in reviving the trend growth rate". The three fronts are low and stable inflation
  (fiscal consolidation, a monetary framework, food markets), sustainable public finances (GST, DTC, a new FRBM Act) and legal and regulatory
  frameworks for a market economy.

### GR-IN-3. Economic Survey 2015-16, Vol 1 Ch 1, Box 1.1 "What is India's Potential GDP Growth?"
`es2015-16.txt`, pp. 5–7 (st. 5–7).
- p. 5: "India is oozing potential." The box sets aside filter-based and production-function estimates and uses a deep
  determinants-cum-convergence framework (institutions as the root of long-run growth: North; Acemoglu and Robinson).
- p. 6: India and China are opposite outliers to the institutions–income line. India is not rich enough for its political institutions;
  China is "too rich given its weak democratic institutions". China should normalise through slower growth, India through faster growth.
- p. 6: India's 2015 gap with the US is about 2.2 log points. A normal convergence rate is about 2% a year, but India, having under-achieved,
  should converge faster.
- p. 7 (table, 2015-30): at convergence speeds of 2/2.5/3/3.5%, potential growth is 3.3/4.1/5.0/5.9% for China and 6.2/7.6/9.0/10.4% for
  India. Conclusion: "India’s medium term growth potential is somewhere between 8 and 10 percent". Hard choices and a cooperative external
  environment are needed.

### GR-IN-4. Economic Survey 2022-23, Ch 2 "India's Medium-Term Growth Outlook: With Optimism and Hope"
`es2022-23.txt`, pp. 24–25 (st. 67–68), p. 40 (st. 83).
- p. 24 (chapter summary): the 1998-2002 reforms paid off from 2003, once temporary shocks faded. By analogy, the post-2014 reforms should
  pay off once the pandemic and the 2022 commodity spike fade.
- p. 25: the 2010s were held back by over-leveraged financial and corporate balance sheets and then by one-off global shocks. The chances of
  India growing at its potential, and of that potential rising, are higher than in the last two decades.
- p. 40: the Survey expects "an average of 6.5 per cent real GDP growth in the medium term". If further reforms are pursued, potential growth
  can rise to 7-8% a year.

### GR-IN-5. Economic Survey 2024-25, Ch 5 "Medium Term Outlook: Deregulation Drives Growth"
`es2024-25.txt`, p. 133 (st. 178), p. 147 (st. 192), p. 150 (st. 195). Preface dated 31 January 2025 (see `India_ES_2024-2026.md`).
- p. 133: to become Viksit Bharat by the centenary of independence, India needs "a growth rate of around 8 per cent at constant prices" on
  average for a decade or two. The setting is geoeconomic fragmentation replacing globalisation and China's rise as a manufacturing
  powerhouse.
- p. 147: Viksit Bharat@2047 means close to 8% growth a year for at least a decade. This needs an investment rate of about 35% of GDP (from
  31%), 78.5 lakh new non-farm jobs a year to 2030, universal literacy and better infrastructure.
- p. 150: East Asia (Japan to China) raised investment rates to grow, but the context has changed. External savings are less available, so
  "efficiency of investment matters more for economic growth than raising the investment rate". Deregulation is the main lever.

### GR-IN-6. Economic Survey 2025-26, Ch 1, Box I.4 "Reassessing India's Medium-Term Potential Growth"
`es2025-26.txt`, pp. 31–34 (st. 82–85). Preface dated 29 January 2026 (see `India_ES_2024-2026.md`).
- p. 31: reforms appear to have lifted medium-term potential closer to 7%. FY27 growth is projected at 6.8–7.2%.
- p. 31 (Box I.4): ES 2022-23 put potential at around 6.5%, possibly 7–8% with reforms. The Box argues for an upgrade: "India’s potential
  growth has risen to around 7 per cent over the medium term". The case rests on PLI, FDI and logistics reforms; effective capex of 4% of
  GDP; and cleaner balance sheets (gross NPAs from 11.2% in March 2018 to 2.2% in September 2025).
- p. 32: capital stock grew about 8.6% a year in the FY03–FY12 investment boom and about 7.6% in FY13–FY20, when stressed balance sheets
  held it back.
- p. 34 (Table I.7): pre-pandemic (FY13–FY20) capital 7.6%, labour input 2.3%, trend TFP 1.9%. For FY26–FY30 the assumptions are capital
  7.6%, labour 2.6%, TFP 1.9% and capital share 0.49, giving output growth of 7.0%. TFP is assumed only to return to its pre-pandemic
  average.
- p. 34: step-ups in potential are most credible when reforms persist and macro stability holds, as in East Asia in the 1990s and Eastern
  Europe after EU accession.

### How the Survey's view of India's trend growth moved
| Survey | View of trend/potential growth | Item |
|---|---|---|
| 2007-08 | New higher path; Eleventh Plan to average over 8.9%; 9% for a decade within reach | GR-IN-1 |
| 2013-14 | Growth down to 4.6%; the trend rate itself must be revived | GR-IN-2 |
| 2015-16 | Potential 8–10% (convergence framework) | GR-IN-3 |
| 2022-23 | 6.5% medium term; 7–8% with reforms | GR-IN-4 |
| 2024-25 | About 8% needed for a decade or two to reach 2047 goal | GR-IN-5 |
| 2025-26 | Potential raised from 6.5% to about 7% | GR-IN-6 |

---

## Useful for the chapter (15 items)

1. **Catch-up did happen after 2000, then slowed.** EMDE per capita income grew 3.4 points a year faster than advanced economies' in 2000–10
   but only 2.0 points faster in 2011–21 (GR-WB-2, p. 2). The IMF's April 2017 decade chart shows gaps widening in the 1980s–90s and
   narrowing in the 2000s–10s (GR-IMF-3, p. 69).
2. **Convergence has stopped in the IMF's projections.** The convergence rate turned positive after the pandemic, and no convergence is
   projected over the medium term (GR-IMF-4, Box 3.2, p. 80).
3. **Long-run forecasts fell steadily.** Five-year-ahead world growth forecasts have been cut since 2008 for nearly 82% of economies. The
   IMF finds no pessimism bias, but possibly a correction of earlier optimism (GR-IMF-4, pp. 66–67).
4. **The five big EMs drove much of the downgrade.** Brazil, China, India, Indonesia and Russia account for about 0.8 point of the 1.8-point
   cut (GR-IMF-4, p. 67). Pair with GR-WB-2 p. 26 (China's slower capital accumulation drags EAP).
5. **Productivity is the main story.** TFP accounts for more than half the growth decline. TFP in emerging markets went from 2.5% (2001–07)
   to 0.7% (GR-IMF-4, pp. 65, 68), and misallocation costs 0.6 point a year (p. 66).
6. **Potential growth numbers.** Global potential fell from 3.5% (2000–10) to 2.6% (2011–21), EMDEs from 6.0% to 5.0% (GR-WB-2, p. 9), with
   2.2% projected for 2022–30 (p. 11). IMF: 2.8% by decade-end against 3.8% in 2000–19 (GR-IMF-4, pp. 65, 67).
7. **The 2000s were partly tailwinds.** The narrowing in the 2000s owed much to exceptional external tailwinds, not only to domestic reform.
   External finance's contribution rose by about ½ point (GR-IMF-3, pp. 66, 69).
8. **Commodity exporters rode the boom and paid after it.** Their five-year forecasts were cut almost 1 point since 2012, and the 2015–17 drag
   was about 1 point (2¼ for energy exporters). Potential growth moves about half as much as actual growth (GR-IMF-2, pp. 65–67, 85).
9. **China was cause and casualty.** Its demand drove the commodity upswing (GR-IMF-2, p. 65) and its rebalancing removed a tailwind
   (GR-IMF-3, p. 65). The Indian Survey saw its slowdown as normalisation (GR-IN-3, p. 6), and the World Bank expects its slower capital
   accumulation to lead the EAP decline (GR-WB-2, p. 26).
10. **2003: institutions explain income gaps.** Governance alone explains nearly three-quarters of cross-country income differences, and the
    growth payoff is biggest for the poorest (GR-IMF-1, pp. 105–112). Contrast with 2017's emphasis on external conditions and 2024's on
    misallocation and demography.
11. **2008: the Growth Report's optimism.** Thirteen economies grew 7% or more for 25 years, with India and Vietnam possibly next. Its
    warning about the middle-income slowdown and Brazil (GR-WB-1, pp. 19–20, 83) foreshadows later concerns.
12. **The global downshift in advanced economies starts early.** AE growth and TFP slowing began in the early 2000s (GR-IMF-4, pp. 65, 68),
    and AE potential forecasts were cut from close to 2% to just over 1½% between 2014 and 2016 (GR-IMF-3, p. 87).
13. **India's Survey swung between 9% hopes and 6.5% realism.** Over 8.9% expected in 2007-08 (GR-IN-1) and 8–10% potential in 2015-16
    (GR-IN-3), then 6.5% in 2022-23 (GR-IN-4) and about 7% in 2025-26 (GR-IN-6). See the table above. India was the main large EM still
    projected at around 6%+ (GR-IMF-4, Figure 3.2, p. 67).
14. **2047 arithmetic.** About 8% for a decade or two with investment at about 35% of GDP (GR-IN-5, pp. 133, 147). Set against the IMF and
    World Bank finding that the global slowdown is broad-based (GR-IMF-4; GR-WB-2), and against the Survey's own 7% potential estimate
    (GR-IN-6).
15. **2020s policy consensus.** Both institutions call for reforms on reallocation, labour participation, investment and trade, and for
    harnessing AI (GR-IMF-4, pp. 77–78; GR-WB-2, p. 14). The 2025 IMF credits better EM policy frameworks with resilience (GR-IMF-5, p. 66).
    The Indian Survey's equivalent is deregulation and investment efficiency (GR-IN-5, p. 150).

---

## Not read / not found

- **WEO April 2015, Ch 3 "Where Are We Headed? Perspectives on Potential Output".** Title confirmed on the old contents page
  http://www.imf.org/external/pubs/ft/weo/2015/01/index.htm (page title "IMF World Economic Outlook (WEO), April 2015: Uneven Growth: Short-
  and Long-Term Factors"). Every PDF link on that page tried (`_c3pdf.pdf`, `_text.pdf`, `_textpdf.pdf`, `_3sumpdf.pdf` under
  /-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2015/01/pdf/) returned HTTP 404 "Blob not found". A guessed new-style
  issue URL also returned 404, and the issue is not on the current WEO listing page. The eLibrary returned 403 and was not pursued. Its
  findings are known here only through the cross-reference in GR-IMF-2 (p. 66 fn 2; p. 67 fn 6).
- **WEO September 2006, Ch 3 "Asia Rising: Patterns of Economic Development and Growth".** Title confirmed on
  http://www.imf.org/external/pubs/ft/weo/2006/02/index.htm; `_c3pdf.pdf`, `_c3sumpdf.pdf` and the full volume `_weo0906pdf.pdf` all returned
  404 "Blob not found".
- **WEO October 2015 full text** (`/-/media/websites/imf/imported-full-text-pdf/.../2015/02/pdf/_text.pdf`, linked from the issue page)
  returned 404. The Ch 2 PDF from the old contents page worked and was used.
- **WEO September 2005 "Building Institutions"**: contents page fetched (http://www.imf.org/external/pubs/ft/weo/2005/02/index.htm) but the
  chapter was not downloaded; GR-IMF-1 covers the institutions theme for the 2000s.
- **Rate limits:** imf.org returned HTTP 429 ("Rate limit is exceeded") several times on HTML pages (the WEO listing, the October 2024 and
  October 2025 issue pages). Each worked on a later plain retry. The first download of the October 2025 Ch 2 PDF stalled and was truncated;
  a second plain download was complete (24 pages).
- **World Bank Global Economic Prospects chapters** on convergence were not read. The two World Bank books above cover the ground, and the
  GEP listing page was only scanned for links.
- **Economic Surveys not used:** ES 2016-17 and 2017-18 have long passages on convergence *among Indian states*. They are not about India's
  catch-up with rich countries, so they were left out; they are worth a look if the chapter treats regional divergence (compare GR-IMF-3,
  Box 2.1).
