# Reading notes: theme chapter "Demography and labour, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies). URLs were taken from publisher
listing or issue pages where possible (openknowledge.worldbank.org via its search and item/bundle APIs; the imf.org WEO listing page and WEO
issue pages; the population.un.org WPP site's own file list; unfpa.org and worldmigrationreport.iom.int report pages; ilo.org report pages;
the economy-finance.ec.europa.eu Ageing Report page; the stats.gov.cn English press-release listing; fred.stlouisfed.org); every guessed URL
is flagged. Downloads are in the session scratchpad folder `demog_dl/` (subfolders `wb/`, `imf/`, `oth/`, `in/`, one new folder per batch).
PDFs were converted with `pdftotext` (plain and `-layout`) and read in the text; HTML pages were stripped of tags and read as text; Python
that read downloads was run with `python3 -I`, with scripts kept outside the download folders. Economic Survey texts were not refetched: they
were read from the Econ Subject folder (`sources/text/es*.txt`; text page = PDF page) and the printed page number was taken from the running
header or footer on that page. Quotes are verbatim, under 15 words, and were checked by a script against the converted text (for two-column
PDFs against the plain, reading-order conversion); everything else is paraphrase. Page numbers are printed page numbers unless stated
("PDF p." where only the PDF page could be given). US labour-market levels and dates (DL-OTH-9) are my own reading of the FRED copies of BLS
series and are marked "own reading".

Item labels: DL-WB-n (World Bank), DL-IMF-n (IMF), DL-OTH-n (UN DESA, UNFPA, IOM, ILO, European Commission, China NBS, BLS/FRED), DL-IN-n
(India). Indian years are fiscal or survey years (2017-18, FY26). WDR = World Development Report; WEO = World Economic Outlook; WPP = World
Population Prospects; PLFS = Periodic Labour Force Survey; LFPR = labour force participation rate; FLFPR = female LFPR; WPR = worker-population
ratio; UR = unemployment rate; TFR = total fertility rate; EMDE = emerging market and developing economy; AE = advanced economy; NEET = not in
employment, education or training. Indian "lakh" = 100,000; "crore" = 10 million.

Note on definitions: migrant totals differ by source. WDR 2023 counts about 184 million migrants and excludes naturalized foreign-born citizens
(DL-WB-3 p. 2, notes a–b); the IMF (April 2025) and IOM (2026) both give 304 million, or 3.7 percent of world population, for 2024 (DL-IMF-4,
DL-OTH-4). India's LFPR figures in the Surveys are PLFS "usual status", ages 15+, July–June years, unless the Survey says "current weekly
status" (CWS); the monthly PLFS bulletins from April 2025 use CWS and are not comparable with the annual usual-status series.

---

## World Bank

### DL-WB-1. World Bank, *World Development Report 2013: Jobs*, Overview "Moving jobs center stage", October 2012 (OKR item dated 2012-10)
Listing: OKR item https://hdl.handle.net/10986/11843 (found via the OKR search API
https://openknowledge.worldbank.org/server/api/discover/search/objects?query=World%20Development%20Report%202013%20Jobs). Overview PDF
("9780821395752_overview.pdf"): https://openknowledge.worldbank.org/bitstreams/96f0f5f7-8518-5ae4-82c9-9f3c17b186d1/download (46 PDF pages;
printed = PDF + 1). Read: overview pp. 2–7.
- p. 2: opening claim that jobs are the cornerstone of development: "development happens through jobs".
- p. 3: more than 3 billion people work worldwide, some 1.65 billion of them for a regular wage or salary; nearly half of the people at work in
  developing countries are farmers or self-employed, outside the labour market.
- p. 4 (infographic): women's labour force participation 77% in Vietnam against 28% in Pakistan; 600 million jobs needed over 15 years to keep
  employment rates constant; 248 million youth neither working nor studying; 90 million people working abroad; international migrants 3% of
  world population; 10 million labour-force entrants a year in Sub-Saharan Africa.
- p. 5: another 1.5 billion work in farming, household enterprises or casual labour; 200 million unemployed, disproportionately youth; almost
  2 billion working-age adults, most of them women, neither working nor looking for work.
- p. 6: fewer than half of women have jobs against almost four-fifths of men (Pakistan: 28% of women, over 82% of men); youth unemployment above
  40% in South Africa since early 2008 and above 50% in Spain in early 2012; about 600 million more jobs needed in 2020 than in 2005, mostly in
  Asia and Sub-Saharan Africa; nearly 8 million new labour-force entrants a year in China since the mid-1990s and 7 million in India, while
  Ukraine's labour force falls by about 160,000 a year.

### DL-WB-2. World Bank, *World Development Report 2012: Gender Equality and Development*, Overview (OKR item dated 2012)
Listing: OKR item https://hdl.handle.net/10986/4391 (OKR search API, query "World Development Report 2012" gender). Overview PDF
("9780821388105_overview.pdf"): https://openknowledge.worldbank.org/bitstreams/c3fd75a7-4636-541a-a18c-92463daf69e3/download (44 PDF pages;
printed = PDF + 1). Read: pp. 3, 7–10, 15–16.
- p. 3: women are more than 40 percent of the global labour force, 43 percent of the agricultural workforce and more than half of the world's
  university students; misallocating women's skills has a high and rising economic cost.
- pp. 9–10: women's labour force participation grew as economic opportunities drew women into the market; between 1980 and 2008 the gender
  gap in participation narrowed from 32 to 26 percentage points; by 2008 women were over 40 percent of the global labour force. Female
  participation was lowest in the Middle East and North Africa (26 percent) and South Asia (35 percent), highest in East Asia and Pacific (64)
  and Sub-Saharan Africa (61). A figure on p. 9 compares how many years countries (India and the United States among them) took for the
  total fertility rate to fall from more than 6 to less than 3.
- p. 15, Table 1 "Almost 4 million missing women each year" (excess female deaths, thousands): India, all ages under 60, 1,255 (1990) and 856
  (2008), of which girls at birth 265 and 257; China 1,470 and 1,254, of which girls at birth 890 and 1,092.
- p. 16: in almost all countries women in manufacturing earn less than men; women farmers have lower yields.

### DL-WB-3. World Bank, *World Development Report 2023: Migrants, Refugees, and Societies*, Overview, 25 April 2023 (OKR issue date)
Listing: OKR item https://openknowledge.worldbank.org/handle/10986/39696 (OKR search API). Overview PDF ("Overview.pdf"):
https://openknowledge.worldbank.org/bitstreams/95ff039b-394f-4dc6-9ad9-b85da5a0b0d3/download (20 PDF pages; printed = PDF). Read: pp. 1–4, 9.
- pp. 1–2 (Box O.1): about 184 million migrants, about 2.3 percent of world population, 37 million of them refugees. About 40 percent (64 million
  economic migrants, 10 million refugees) live in OECD high-income countries; about 17 percent (31 million) in the Gulf states, where they are
  about half the population; about 43 percent (52 million migrants, 27 million refugees) in low- and middle-income countries. The share has been
  stable since 1960, but migration grew three times faster than population in high-income countries.
- p. 2: in 2020 about 84 percent of migrants lived in a country richer than their own. Italy (59 million) projected to shrink almost by half, to
  32 million, by 2100, with the 65+ share rising from 24 to 38 percent; Mexico's fertility has dropped to barely replacement; Nigeria projected
  to grow from 213 million to 791 million and become the second most populous country after India by century's end. Rich countries will need
  foreign workers; many middle-income countries will soon have to compete for them. About 3.5 billion people (40 percent) live in places highly
  exposed to climate change.
- p. 3: the number of refugees more than doubled over the last decade. p. 4: children are 41 percent of refugees.
- p. 9: remittances are a stable income source for families; lowering their cost would amplify benefits; Silicon Valley expatriates helped
  nurture India's IT sector.

### DL-WB-4. World Bank, *World Development Report 2007: Development and the Next Generation*, Overview (OKR item dated 2006)
Listing: OKR item https://hdl.handle.net/10986/5989 (OKR search API, query "World Development Report 2007"). Full English PDF ("WDR 2007 -
English.pdf"): https://openknowledge.worldbank.org/bitstreams/515dd9ae-dad1-5964-b8a0-57d758010541/download (340 PDF pages; printed = PDF − 20).
Read: overview pp. 2–4; ch. 1 pp. 33–35 (grepped).
- p. 4: 1.5 billion people aged 12–24 worldwide, 1.3 billion in developing countries, "the most ever in history"; the number is near a plateau
  as birth rates fall. Falling dependency opens a "window of opportunity" (the demographic dividend) only if countries invest in young people's
  human capital. In most developing countries the number of young people is peaking or will peak within 10 years; all of Sub-Saharan Africa,
  Afghanistan, Iraq, West Bank and Gaza and Yemen will not peak for 20 years.
- p. 33: on current projections, 12–24-year-olds reach a maximum of 1.5 billion in 2035 and decline only gradually thereafter.
- p. 35: the literature on the pathways of the dividend is "not conclusive" (paraphrase), but East Asia absorbed its large cohorts of entrants.

### DL-WB-5. World Bank, *The Global Jobs Challenge*, Executive Summary, 16 June 2026 (OKR issue date)
Listing: OKR item https://hdl.handle.net/10986/43758 (OKR search API, query "population aging labor force", sorted by date). Executive summary
PDF ("Global-jobs-challenge-executive-summary.pdf"): https://openknowledge.worldbank.org/bitstreams/04b7275f-041a-47ae-9a71-42afb13e0ebd/download
(4 PDF pages; printed = PDF). Full report also downloaded (bitstream 021e6eaf-4067-4494-b82a-fe1e86dd99fe, 252 PDF pages) but not read. Read:
executive summary pp. 1–3.
- p. 1: over the decade to 2035 around 1.2 billion young people in EMDEs reach working age, "the largest youth cohort the world will likely
  ever see"; an illustrative extrapolation has just over 400 million of them employed in 2035 and about 300 million NEET. In 2035 over 330
  million young people will live in Sub-Saharan Africa, almost 2.5 times as many as in 2000.
- p. 2 (fig. ES.1): global potential growth one-third lower in the 2020s than in the 2000s; in most countries of the four regions with the
  largest incoming cohorts, recent job creation has not matched projected working-age growth.
- p. 3: East Asia and Pacific had almost 350 million young people entering working age in the decade to 1988, its largest cohort, which fuelled
  its growth; more than a fifth of the coming 1.2 billion live in fragile and conflict-affected situations.

### DL-WB-6. Elina Pradhan, Syud Amer Ahmed, Lynn Hu, Jumana Alaref, Zoe Xie, Omoniyi Alimi, Miglena Abels and Margaret Triyana, *Demographic Change in South Asia: From Tailwinds to Headwinds for Development* (South Asia Development Matters), World Bank, © 2026 (OKR issue date 2 November 2026)
Listing: OKR item https://hdl.handle.net/10986/45714 (OKR search API, sorted by date). Executive summary PDF ("33985.pdf"):
https://openknowledge.worldbank.org/bitstreams/3dae5e4c-a779-4a4d-a600-fe73b7004720/download (24 PDF pages; summary p. 1 = PDF 9, printed =
PDF − 8). Full report ("Demographic Change in South Asia.pdf"): https://openknowledge.worldbank.org/bitstreams/04d9003c-6ebf-4355-b34a-f05b34a7a527/download
(204 PDF pages; ch. 1 p. 5 = PDF 35, printed = PDF − 30). Read: executive summary pp. 1–5; full report ch. 1 pp. 5–6 (grepped).
- Exec. summary p. 1: South Asia's working-age share peaks in 2034; by 2049 the 65+ share doubles to 14 percent ("aged"), seven years faster
  than the EMDE average and two decades faster than advanced economies. The region has 1.66 billion people (24 percent of the world) and 1.17
  billion of working age (22 percent); one in five of the world's workers. Demographics added about 0.4 point a year to the region's GDP growth
  since 2000 (0.5 for India). Working-age growth, 2.2 percent a year in 1960–2023, falls to 0.6 percent in 2024–50, and the demographic
  contribution to growth shrinks by three-quarters, to about 0.1 point. India, Bhutan and Maldives have less than a decade before their
  working-age shares peak; Sri Lanka's peaked in 2005.
- p. 2 (fig. ES.1 note): India's transition from "aging" (65+ at 7 percent) to "aged" (14 percent) runs 2024–49.
- p. 3: an average EMDE takes 32 years to go from aging to aged, France took 126 and the US 72; South Asia will take 25 ("Growing old before
  growing rich"). Only 60 percent of the working-age population is employed (69 percent in other EMDEs); 34 percent in non-farm work (51
  elsewhere); 88 percent of the employed are informal. Formal firms grow employment 2.7 percent a year, against 5.4 percent in EMDEs; in
  India the most productive 10 percent of firms cut jobs.
- p. 4: since late 2022, postings for highly AI-exposed occupations fell about a fifth; South Asia's FLFPR, 35 percent, is among the lowest
  of EMDE regions.
- p. 5: moderate human-capital gains plus rising female participation could raise India's GDP per capita in 2050 by 10 percent over the
  baseline; scenarios that fully close the gender gap in participation raise the gain to 19 percent.
- Full report ch. 1 p. 5: a South Asian woman had 6.3 children on average in 1960 and 1.9 in 2023, below replacement.

### DL-WB-7. World Bank, "Remittances & Migration" brief (web page, content date 28 September 2026)
Listing: linked from the KNOMAD publications page https://www.knomad.org/publications (200). Page:
https://www.worldbank.org/en/brief/2024/09/18/remittances-knomad (200). Read: whole page.
- KNOMAD, the Global Knowledge Partnership on Migration and Development, "was active from 2013 until 2024" (page description; paraphrase
  otherwise). In 2023 remittances to home countries totalled about $656 billion, "equivalent to the GDP of Belgium"; in more than 60 countries
  remittances are 3 percent of GDP or more. Repeats the WDR 2023 figure of 184 million migrants.
- Consequence for the chapter: no 2025 or 2026 Migration and Development Brief was found (see Not obtained); 2024 remittance figures come from
  IOM (DL-OTH-4) and India's from the Economic Survey (DL-IN-9).

---

## IMF

### DL-IMF-1. IMF, *World Economic Outlook, April 2017: Gaining Momentum?*, Chapter 3 "Understanding the Downward Trend in Labor Income Shares" (Mai Chi Dao, Mitali Das (team leader), Zsoka Koczan, Weicheng Lian)
Listing: WEO listing https://www.imf.org/en/Publications/WEO → issue page
https://www.imf.org/en/publications/weo/issues/2019/08/30/world-economic-outlook-april-2017-gaining-momentum-44510 (200). PDF:
https://www.imf.org/-/media/files/publications/weo/2017/april/pdf/text.pdf (258 PDF pages; ch. 3 p. 121 = PDF 139, printed = PDF − 18). Read:
pp. 121, 123, 125, 135–136, 140.
- p. 121: the labour share is the share of national income paid to workers in wages and benefits. In advanced economies labour shares
  "began trending down in the 1980s", reached their lowest level in half a century just before the 2008–09 crisis and have not recovered; in
  more than half of EMDEs, especially the larger ones, they have also declined since the early 1990s. Technology (the falling relative price
  of investment goods) together with exposure to routine occupations explains about half the decline in advanced economies, with larger
  losses for middle-skilled workers; in emerging markets the main force is global integration, especially global value chains.
- p. 123: the relative price of investment fell steeply in advanced economies, much less in emerging markets (rising in some).
- pp. 125, 136: about half of the decline in advanced-economy labour shares traced to technology; global integration contributed about half as
  much as technology. p. 140: policy should help displaced workers move to new jobs and spread the gains.

### DL-IMF-2. IMF, *World Economic Outlook, April 2018: Cyclical Upswing, Structural Change*, Chapter 2 "Labor Force Participation in Advanced Economies: Drivers and Prospects" (Francesco Grigoli, Zsóka Kóczán, Petia Topalova (lead))
Listing: issue page https://www.imf.org/en/publications/weo/issues/2019/08/31/world-economic-outlook-april-2018-cyclical-upswing-structural-change-45570
(200, title confirmed; the page carries no PDF link). PDF: https://www.imf.org/-/media/files/publications/weo/2018/april/c2.pdf (GUESSED URL,
returned 200; 58 PDF pages; the chapter file is paginated from 1, printed = PDF). Read: pp. 1, 4, grepped the rest.
- p. 1: by mid-century the UN projects total population shrinking in almost half of advanced economies, and today's working-age people will
  support close to double the number of elderly. Since the crisis, aggregate participation actually rose in half of advanced economies; it has
  risen among prime-age women and older workers but fallen among the young and prime-age men. Ageing and the crisis explain much of the fall
  for men; policies, structural change and education explain most of the rise for women and older workers; automation weighed moderately.
  Demographic shifts could overwhelm policy, which "underscores the need to rethink migration policies to boost labor supply".
- p. 4: net migration accounts for roughly half of population growth in advanced economies over the past three decades.

### DL-IMF-3. IMF, *World Economic Outlook, April 2025: A Critical Juncture amid Policy Shifts*, Chapter 2 "The Rise of the Silver Economy: Global Implications of Population Aging" (Bertrand Gruss (co-lead), Eric Huang, Andresa Lagerborg, Diaa Noureldin (co-lead), Galip Kemal Ozhan)
Listing: WEO listing → issue page https://www.imf.org/en/publications/weo/issues/2025/04/22/world-economic-outlook-april-2025 (200). PDF:
https://www.imf.org/-/media/files/publications/weo/2025/april/english/ch2.pdf (chapter file paginated from 1). Read: pp. 1–2, grepped p. 5.
- p. 1: world population growth slows from 1.1 percent a year before COVID-19 to basically zero in 2080–2100; the average age of the world's
  population rises by 11 years between 2020 and the end of the century. Life expectancy rose about 4½ years over two decades, with healthy life
  expectancy rising at a similar pace.
- p. 2: ageing is no longer confined to advanced economies; the window for demographic dividends in younger low-income countries is closing.
  In 41 economies, a 70-year-old in 2022 had the cognitive ability of a 53-year-old in 2000 ("the 70s are the new 50s"); a decade of such
  improvement goes with about 20 points higher likelihood of being in the labour force. Healthy ageing adds about 0.4 point a year to world GDP
  growth in 2025–50, yet world growth is projected 1.1 points lower than the 2016–18 average, almost three-quarters of the fall due to
  demographics; many countries will need large efforts to stabilise debt.

### DL-IMF-4. IMF, *World Economic Outlook, April 2025*, Chapter 3 "Journeys and Junctions: Spillovers from Migration and Refugee Policies" (Paula Beltran Saavedra, Nicolas Fernandez-Arias, Shushanik Hakobyan, Samuel Mann, Neil Meads, Carolina Osorio Buitron, under the guidance of Aqib Aslam)
Listing: same issue page. PDF: https://www.imf.org/-/media/files/publications/weo/2025/april/english/ch3.pdf (chapter file paginated from 1).
Read: pp. 1–2.
- p. 1: as of 2024 the global stock of legal migrants and refugees reached 304 million, 3.7 percent of world population, almost double 1995;
  about one in six are refugees or asylum seekers; about 40 percent of migrants and 75 percent of refugees live in EMDEs. Migrant flows as a
  share of world population rose from the late 1990s until the global financial crisis. Tighter policies elsewhere can raise inflows to a
  given economy by 10 percent over five years, raising its output by about 0.2 percent.
- p. 2 (fig. 3.2 and text): acceptance of migrants has been deteriorating in several major destinations (index change 2016–23); media
  coverage of migration spiked with Iraq (2002), Syria (2014), Venezuela (2015) and Ukraine (2022).

### DL-IMF-5. IMF, *World Economic Outlook, April 2024*, Chapter 3 "Slowdown in Global Medium-Term Growth: What Will It Take to Turn the Tide?" (Nan Li (co-lead), Chiara Maggi, Diaa Noureldin (co-lead), Cedric Okou, Alexandre B. Sollaci, Robert Zymek)
Listing: issue page https://www.imf.org/en/publications/weo/issues/2024/04/16/world-economic-outlook-april-2024 (200). PDF:
https://www.imf.org/-/media/files/publications/weo/2024/april/english/ch3.pdf (22 PDF pages; chapter file paginated from 1). Read: p. 1; fig.
3.5–3.6 on p. 5.
- p. 1: without policy action or new technology, global growth will be only 2.8 percent by the end of the decade, about 1 point below the
  2000–19 average; slower working-age population growth in major economies and declining labour force participation hold back labour inputs.
- p. 5 (figs. 3.5–3.6): compare working-age population growth in 2008 and 2021 by country and break the 2008–21 change in participation
  into an ageing effect and within-group changes by sex (chart values not legible in the text conversion; not used).

---

## UN DESA, UNFPA, IOM, ILO, European Commission, China NBS, BLS/FRED

### DL-OTH-1. UN DESA Population Division, *World Population Prospects 2024: Summary of Results*, July 2024
Listing: the WPP site https://population.un.org/wpp/ (200) is a script application; its own script file
https://population.un.org/wpp/main-JDJAGSLT.js (200) lists the downloadable files, including the 2024 Summary of Results and Key Messages, and
no 2026 revision (the newest files are WPP2024). PDF: https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf (80 PDF
pages; printed = PDF − 14 from chapter I). Read: executive summary PDF pp. 9–12; pp. 3, 16, 18, 20, 37–38.
- Executive summary (PDF p. 9): in nine countries, including Angola, the Central African Republic, DR Congo, Niger and Somalia, populations
  are likely to double between 2024 and 2054. PDF p. 10: nearly a fifth of countries, including China, Italy, the Republic of Korea and Spain,
  have "ultra-low" fertility (under 1.4 births per woman); for 24 such countries whose populations have peaked, a return to 2.1 within 30
  years is highly unlikely (probability 0.1 percent). PDF p. 12: in 14 ultra-low-fertility countries emigration is a major driver of
  population loss to 2054.
- p. 3: the projected world population is lower than a decade ago partly because fertility in China came in lower than expected and fell
  slightly faster in parts of Sub-Saharan Africa.
- p. 16: China will have the largest absolute population loss between 2024 and 2054 (204 million), followed by Japan (21 million) and Russia
  (10 million); by 2100 China loses 786 million, more than half its population, returning to its late-1950s size.
- p. 18: among countries whose populations have peaked, fertility averages 1.0 births per woman in Eastern and South-Eastern Asia; Hong Kong
  SAR and the Republic of Korea are below 0.75 in 2024; the probability of a return to 2.1 within 30 years is 0.1 percent or less for China
  and Korea.
- p. 37: India, "expected to remain the world's largest throughout the century", peaks in the early 2060s at about 1.7 billion and then
  declines by about 12 percent.

### DL-OTH-2. UN DESA Population Division, *World Population Prospects 2024: Ten key messages*, July 2024
Listing: as DL-OTH-1. PDF: https://population.un.org/wpp/assets/Files/WPP2024_Key-Messages.pdf (2 PDF pages). Read: both pages.
- World population (8.2 billion in 2024) peaks at about 10.3 billion in the mid-2080s and falls to 10.2 billion by 2100; an 80 percent chance
  of a peak this century, against about 30 percent a decade ago.
- 63 countries and areas, with 28 percent of world population, had peaked before 2024; 48 more (10 percent) peak in 2025–54.
- Global fertility is 2.3 births per woman, down from 3.3 in 1990; over half of countries are below 2.1. Life expectancy 73.3 years in 2024.
- In about 100 countries the working-age population (20–64) grows through 2054, the window of the demographic dividend.
- By the late 2070s people aged 65+ (2.2 billion) outnumber children under 18; by the mid-2030s those aged 80+ (265 million) outnumber infants.
- In 50 countries immigration is projected to soften population decline.

### DL-OTH-3. UNFPA, *State of World Population 2023* (English PDF; dated 29 March 2023 in the file name), Demographic indicators table
Listing: report page https://www.unfpa.org/swp2023 (200). PDF: https://www.unfpa.org/sites/default/files/swop23/SWOP2023-ENGLISH-230329-web.pdf
(192 PDF pages). Read: demographic indicators table, PDF pp. 166–168 (the subtitle and narrative chapters were not read).
- Table (2023 estimates): India 1,428.6 million, China 1,425.7 million; TFR India 2.0, China 1.2; population aged 65+ India 7 percent, China 14
  percent; aged 15–64 India 68, China 69 percent; world 8,045 million, TFR 2.3. (So the UN's 2023 figures put India ahead of China; the UN DESA
  policy brief announcing it could not be fetched; see Not obtained.)

### DL-OTH-4. IOM, *World Migration Report 2026*: press release "IOM Report: Migration Drives Economies and Development, but Gains Are at Risk" (Geneva/New York, 5 May 2026) and chapter 2 web section "International remittances"
Listing: WMR site https://worldmigrationreport.iom.int/ (200) → news page
https://worldmigrationreport.iom.int/news/iom-report-migration-drives-economies-and-development-gains-are-risk (200); WMR 2026 contents page
https://worldmigrationreport.iom.int/what-we-do/world-migration-report-2026/foreword/foreword (200) → chapter 2 section
https://worldmigrationreport.iom.int/what-we-do/wmr-2026/chapter-2/international-remittances (200). Read: both pages (HTML, no page numbers).
- Press release: by mid-2024 there were about 304 million international migrants, about 3.7 percent of world population; migrant workers rose by
  more than 30 million in 2013–2022; remittances in 2024 were expected to reach about USD 905 billion, including USD 685 billion to low- and
  middle-income countries, more than ODA and FDI combined; over 120 million people displaced at end-2024. The report argues that "restricting
  these pathways does not stop migration" but pushes it into irregular routes.
- Remittances section and Table 2: in 2024 the top recipients were India, Mexico, the Philippines, France and Pakistan; India received more than
  USD 137 billion and was the only country above USD 100 billion. India's receipts: USD 53.48 billion (2010), 68.91 (2015), 83.15 (2020),
  137.67 (2024); Mexico 67.64 in 2024. The United States was the top sender (USD 103.18 billion in 2024), then Saudi Arabia (46.56).

### DL-OTH-5. ILO, *World Employment and Social Outlook: Trends 2025*, January 2025
Listing: report page https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-trends-2025 (200). PDF:
https://www.ilo.org/sites/default/files/2025-01/WESO25_Trends_EN_WEB5.pdf (84 PDF pages; p. xi = PDF 13). Read: executive summary pp. xi–xii;
contents. (The 2026 edition was not found; see Not obtained.)
- p. xi: global unemployment steady at 5 percent in 2024, similar to 2023; youth unemployment around 12.6 percent; informality and working
  poverty back at pre-pandemic levels, so "the job recovery has lost much of its ability to generate further improvements"; world growth 3.2
  percent in 2024; demographic shifts in advanced and some large emerging economies; labour shortages have eased but not disappeared; labour
  hoarding high in Europe.
- p. xii: in most countries real wages have not recouped losses from the pandemic and the inflation that followed; labour market power has
  shifted towards employers. Participation fell slightly worldwide; in high-income countries it rose by almost 1 point over ten years thanks
  to older workers and women; gender gaps narrowed mostly because young men's participation fell; young men's NEET rate in low-income
  countries is almost 4 points above its historical average.

### DL-OTH-6. ILO, *Global Wage Report 2024–25*, Executive Summary, November 2024 (subtitle not checked; the page slug reads "wage-inequality-decreasing-globally")
Listing: report page https://www.ilo.org/publications/flagship-reports/global-wage-report-2024-25-wage-inequality-decreasing-globally (GUESSED
URL, returned 200). PDF: https://www.ilo.org/sites/default/files/2024-11/GWR2024_English_ExecutiveSummary_WEB.pdf (10 PDF pages). Read: pp. 3–4.
- p. 3: global real wage growth was −0.9 percent in 2022, +1.8 percent in 2023 and an estimated 2.7 percent in 2024 (first two quarters), "the
  largest gain in more than 15 years"; excluding China, −1.5, 1.3 and 2.3 percent. Advanced G20 real wages fell 2.8 percent (2022) and 0.5
  percent (2023) and rose 0.9 percent in 2024; emerging G20 rose 1.8, 6.0 and 5.9 percent.
- p. 4: in high-income countries labour productivity rose 29 percent and real wages 15 percent over 1999–2024, most of the gap opening in
  1999–2006.

### DL-OTH-7. National Bureau of Statistics of China, "National Economy Pushed Forward with Innovation-led and High-quality Development and Ex..." (title cut off in the listing; full title not recorded), press release, 19 January 2026
Listing: NBS English press releases https://www.stats.gov.cn/english/PressRelease/ (200), listing page index_11 → release
https://www.stats.gov.cn/english/PressRelease/202601/t20260119_1962328.html (200). Read: section 10 and the labour paragraphs (HTML).
- Section 10, "Total Population Went down and Urbanization Rate Continued to Grow.": population at end-2025 was 1,404.89 million, 3.39
  million fewer than at end-2024. Births 7.92 million (birth rate 5.63 per thousand), deaths 11.31 million (8.04 per thousand), natural growth
  −2.41 per thousand. Aged 16–59: 851.36 million (60.6 percent); 60+: 323.38 million (23.0 percent); 65+: 223.65 million (15.9 percent).
  Urban residents 953.80 million.
- Labour: surveyed urban unemployment in 31 major cities 5.1 percent; rural migrant workers 301.15 million in 2025.
- The 2026 statistical communiqué on 2025 is also on the listing (https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html)
  but the fetch failed (connection reset). The releases for 2022–2024 (first declines) could not be reached (see Not obtained).

### DL-OTH-8. European Commission (DG ECFIN) and Economic Policy Committee, *2024 Ageing Report: Economic and budgetary projections for the EU Member States (2022-2070)*, Institutional Paper 279 (title from PDF metadata)
Listing: report page https://economy-finance.ec.europa.eu/publications/2024-ageing-report-economic-and-budgetary-projections-eu-member-states-2022-2070_en
(200). PDF: https://economy-finance.ec.europa.eu/document/download/971dd209-41c2-425d-94f8-e3c3c3459af9_en?filename=ip279_en.pdf (358 PDF
pages; executive summary p. 3 = PDF 13). Read: executive summary pp. 3–4.
- p. 3: EU population rises from 449 million (2022) to a peak of 453 million in 2026, then falls to 432 million in 2070. The old-age dependency
  ratio, about 29 percent in 2010 and 36 percent in 2022, rises to 59 percent by 2070, most of the rise by 2045; from nearly three people aged
  20–64 per person over 65 to fewer than two by 2045. Fertility rises only from 1.50 to 1.62; life expectancy at birth rises from 78.4 to 86.1
  (men) and from 84.0 to 90.4 (women); net migration averages 0.3 percent of population a year.
- p. 4: participation of 20–64-year-olds rises from 79.4 to 82.7 percent by 2070, and of 55–64-year-olds from 65.4 to 75.5 percent, but not enough
  to offset the shrinking working-age population; total hours worked fall 9 percent; the economic old-age dependency ratio rises from 46 to
  70 percent.

### DL-OTH-9. US Bureau of Labor Statistics series via FRED: quits rate (JTSQUR), job openings (JTSJOL), unemployment rate (UNRATE), prime-age (25–54) participation rate (LNS11300060), monthly
Listing: FRED series pages; data from https://fred.stlouisfed.org/graph/fredgraph.csv?id=JTSQUR (and id=JTSJOL, UNRATE, LNS11300060), all 200.
Read: whole series; figures below are my own reading.
- Unemployment rate: 10.0 percent in October 2009 (post-crisis peak); 3.5 percent in February 2020; 14.8 percent in April 2020 (series high
  since 1948); back to 3.5 percent by July 2022; low of 3.4 percent in April 2023; 4.5 percent in November 2025; 4.1 percent in October 2026
  (latest).
- "Great Resignation": quits rate peaked at 3.0 percent in November 2021 (2.3–2.4 percent in 2019; low of 1.2 percent in August 2009); job
  openings peaked at 12.301 million in March 2022 (7.5 million in January 2019); quits back to 2.1 percent in September 2026.
- Prime-age participation: 83.0 percent in December 2019, 79.8 percent in April 2020, 84.0 percent in July 2024 (just below the January 1999
  record of 84.6), 83.7 percent in October 2026.

---

## India

### DL-IN-1. Government of India, Ministry of Finance, *Economic Survey 2006-07*, Chapter 1 (on disk; not refetched)
Files: `sources/text/es2006-07.txt` (pp. 10, 14 = PDF 10, 14). Read: paras 1.33–1.39, 1.48–1.51.
- p. 10: the working-age (15–64) share of the population rises steadily from 62.9 percent in 2006 to 68.4 percent in 2026, so the demographic
  dividend in the form of a high savings rate is likely to continue.
- p. 14 (para 1.48): India will keep benefiting from the demographic dividend until 2045 (paraphrase); para 1.51: higher growth together with
  the dividend makes the current growth phase sustainable.

### DL-IN-2. *Economic Survey 2010-11* (on disk)
Files: `sources/text/es2010-11.txt` (pp. 21, 308 = PDF 21, 308). Read: grepped passages.
- p. 21: growth expected to stay high partly because India's demographic dividend has not yet peaked and the working-age savings rate is
  rising (paraphrase).
- p. 308: India will see a sharp decline in its dependency ratio over the next 30 years, a major demographic dividend, but only if
  supplemented by skilling the young.

### DL-IN-3. *Economic Survey 2012-13*, Chapter 2 "Seizing the Demographic Dividend" (on disk)
Files: `sources/text/es2012-13.txt` (pp. 26–28 = PDF 26–28). Read: pp. 26–28.
- p. 26: "The central long-run question facing India is where will good jobs come from?"; more than half the population depends on
  agriculture; industry creates too many low-productivity, unorganised jobs; services jobs grow slowly; "a good job is the best form of
  inclusion".
- p. 26: the dependency ratio will fall sharply in coming decades; fertility decline may raise female participation (Bailey 2006).
- p. 27: high-growth states (Tamil Nadu, Karnataka, Gujarat) had dependency ratios 8.7 points lower than low-growth states (Bihar, Madhya
  Pradesh, Uttar Pradesh) in 1991–2001 and grew 4.3 points faster (Aiyar and Mody 2011); nearly half the additions to India's labour force in
  2011–30 will be aged 30–49, while China, Korea and the US shrink that group. Pessimists: a larger workforce means more workers only if there
  are productive jobs.

### DL-IN-4. *Economic Survey 2017-18*, Vol. 1, Chapter 7 "Gender and Son Meta-Preference: Is Development Itself an Antidote?" (on disk)
Files: `sources/text/es2017-18.txt` (pp. 102–105 = PDF 120–123; p. 116 = PDF 134). Read: pp. 102–105, 116.
- p. 102: India improved on 14 of 17 indicators of women's agency, attitudes and outcomes over 10–15 years, but on employment, reversible
  contraception and son preference "development has not proved to be an antidote"; a meta-preference for sons shows up in fertility-stopping
  rules and notionally creates about 21 million "unwanted" girls.
- p. 103: IMF research cited by Christine Lagarde: raising women's workforce participation to men's level could boost India's economy by 27
  percent.
- pp. 105, 116: the skewed sex ratio implies about 63 million "missing" women.

### DL-IN-5. *Economic Survey 2018-19*, Vol. 1, Chapter 7 "India's Demography at 2040: Planning Public Good Provision for the 21st Century" (on disk)
Files: `sources/text/es2018-19.txt` (p. 128 = PDF 140, printed = PDF − 12). Read: pp. 128–129.
- p. 128: population growth slowed from 2.5 percent a year (1971–81) to about 1.3 percent (2011–16); the 0–19 population "has already peaked";
  the southern states and several others are well below replacement fertility; the national TFR is expected to fall below replacement by 2021
  (and may already be there, adjusted for the sex ratio); the working-age population grows by about 9.7 million a year in 2021–31 and 4.2
  million a year in 2031–41; some states start ageing by the 2030s; plan for a phased rise in the retirement age.

### DL-IN-6. *Economic Survey 2021-22*, Vol. 2, Chapter 8 (Social Infrastructure) (on disk)
Files: `sources/text/es2021-22.txt` (pp. 344, 378 = PDF 370, 404). Read: the NFHS-5 passages.
- p. 344: NFHS-5 shows the TFR falling from 2.2 (2015-16) to 2 (2019-21).
- p. 378, Table 11: TFR 3.4 (NFHS-1, 1992-93), 2.9 (NFHS-2), 2.7 (NFHS-3, 2005-06), 2.2 (NFHS-4, 2015-16), 2.0 (NFHS-5, 2019-21); sex ratio
  at birth (females per 1,000 males) 914, 919 and 929 in NFHS-3 to NFHS-5.

### DL-IN-7. *Economic Survey 2023-24*, Chapters 1, 5 and 8 (employment) (on disk)
Files: `sources/text/es2023-24.txt` (pp. 32, 158, 272, 276 = PDF 79, 205, 319, 323). Read: those pages.
- p. 32: FLFPR rose for six years, from 23.3 percent (2017-18) to 37 percent (2022-23), driven mainly by rural women.
- p. 158: working-age population (15–59) grows until 2044; the economy needs to generate "nearly 78.51 lakh jobs annually in the non-farm
  sector" (about 7.85 million).
- p. 272: quarterly urban UR (CWS, 15+) 6.7 percent in the quarter to March 2024, from 6.8 a year earlier.
- p. 276: youth (15–29) UR fell from 17.8 percent (2017-18) to 10 percent (2022-23).

### DL-IN-8. *Economic Survey 2024-25*, Chapter 1 and Chapter 12 "Employment and Skill Development" (on disk)
Files: `sources/text/es2024-25.txt` (p. 31 = PDF 76; ch. 12 printed = PDF − 45). Read: p. 31; pp. 363–371.
- p. 31: per the annual PLFS 2023-24, UR (15+) fell steadily from 6 percent (2017-18) to 3.2 percent (2023-24), with LFPR and WPR rising.
- p. 363: need for 78.5 lakh non-farm jobs a year until 2030 (repeating ES 2023-24).
- p. 364: urban UR 6.6 percent (Q2 FY24) to 6.4 percent (Q2 FY25); urban LFPR 49.3 to 50.4 percent.
- p. 365, Chart XII.4 (usual status, 15+; values read from chart labels): LFPR 49.8 (2017-18), 50.2, 53.5, 54.9, 55.2, 57.9, 60.1 (2023-24);
  WPR 46.8 to 58.2; UR 6.0, 5.8, 4.8, 4.2, 4.1, 3.2, 3.2.
- p. 367: self-employed share of workers rose from 52.2 percent (2017-18) to 58.4 percent (2023-24); regular wage/salaried fell from 22.8 to
  21.7; casual labour fell from 24.9 to 19.8. Rural women in regular wage jobs fell from 10.5 to 7.8 percent of rural women workers; among rural
  women "own account workers/employers" rose from 19 to 31.2 percent and unpaid "helpers in household enterprises" from 38.7 to 42.3 percent.
- p. 370: FLFPR rose for seven years, from 23.3 percent (2017-18) to 41.7 percent (2023-24), "driven mainly by the rising participation of
  rural women"; rural women's agricultural share rose from 73.2 to 76.9 percent. p. 371: rural FLFPR 24.6 to 47.6 percent.

### DL-IN-9. *Economic Survey 2025-26*, Chapter 1, Chapter 4 (External Sector) and Chapter 12 "Employment and Skill Development: Getting Skilling Right" (on disk)
Files: `sources/text/es2025-26.txt` (printed = PDF − 51; pp. 28–29 = PDF 79–80, p. 173 = PDF 224, pp. 467–469 = PDF 518–520, p. 474 = PDF 525,
p. 485 = PDF 536). Read: those pages.
- p. 28: immigration controls in countries favoured by Indian emigrants may cap the growth of remittances.
- p. 29 (Chart I.26, from the PLFS Monthly Bulletin): monthly CWS estimates for April–December FY26 show LFPR around 55–56 percent and UR
  around 5 percent, with quarterly averages showing a falling UR; 29 central laws consolidated into four Labour Codes.
- p. 173: remittances USD 73 billion in H1 FY26 against USD 64.7 billion a year earlier; inflows rose from USD 55.6 billion (FY11) to USD 135.4
  billion (FY25, provisional), about 3.5 percent of GDP, consistent with "India's longer-term position as the world's largest recipient of
  remittances" (quote uses curly apostrophes in the source).
- p. 467: "India's workforce of over 56 crore holds tremendous potential"; the working-age population (15–59) will exceed 98 crore within 10
  years. p. 468: the demographic dividend peaks around 2030, when nearly 65 percent of the population will be aged 15–59; the TFR has fallen
  below replacement and the population is ageing. p. 469: MoSPI issued the first monthly bulletin of the revised PLFS in April 2025; 56.2
  crore people (15+) were employed in July–September 2025, 8.7 lakh more than in April–June.
- p. 474 (Box XII.2): FLFPR rose from 23.3 to 41.7 percent between 2017-18 and 2023-24, with UR falling from 5.6 to 3.2 percent (note: ES
  2024-25 p. 31 gives 6 percent for 2017-18; the two Surveys differ).
- p. 485: the four Labour Codes (the passage names, among others, the Industrial Relations Code 2020 and the Occupational Safety, Health and
  Working Conditions Code 2020) consolidate 29 central laws; "The implementation of these Codes was notified on 21 November 2025."

---

## Synthesis

1. **The demographic transition went global and faster than expected.** World fertility fell from 3.3 births per woman in 1990 to 2.3, and over
   half of countries are below replacement (DL-OTH-2). The UN now gives an 80 percent chance that world population peaks this century, at about
   10.3 billion in the mid-2080s; a decade earlier the chance was about 30 percent (DL-OTH-2). Lower-than-expected Chinese fertility is one
   reason for the downward revision (DL-OTH-1 p. 3).
2. **East Asia and Europe are shrinking.** Ultra-low fertility (under 1.4) covers China, Italy, Korea and Spain; Korea and Hong Kong are below
   0.75 (DL-OTH-1 PDF 10, p. 18). China loses 204 million people by 2054 and Japan 21 million (DL-OTH-1 p. 16). China's population fell to
   1,404.89 million at end-2025, down 3.39 million in a year, with 7.92 million births against 11.31 million deaths and 15.9 percent aged 65+
   (DL-OTH-7). The EU peaks at 453 million in 2026, and its old-age dependency ratio rises from 36 to 59 percent by 2070 (DL-OTH-8).
3. **Africa and South Asia hold the young.** In 2006 the World Bank counted 1.5 billion people aged 12–24, "the most ever in history", with
   Sub-Saharan Africa 20 years from its peak (DL-WB-4 p. 4). In 2026 it counts 1.2 billion young people reaching working age in EMDEs by 2035.
   Over 330 million of them are in Sub-Saharan Africa, and only about 400 million of the 1.2 billion are projected to have jobs (DL-WB-5 p. 1).
   Nigeria could reach 791 million by 2100 (DL-WB-3 p. 2).
4. **Ageing hits growth, but healthy ageing softens the blow.** The IMF projects world growth 1.1 points lower in 2025–50 than in 2016–18, mostly
   from demographics. Healthier older workers add back about 0.4 point a year ("the 70s are the new 50s") (DL-IMF-3 p. 2). In advanced
   economies, participation by women and older workers rose while young and prime-age men's fell (DL-IMF-2 p. 1). The EU expects its 55–64
   participation rate to rise from 65.4 to 75.5 percent (DL-OTH-8 p. 4).
5. **Women's work: slow convergence.** By 2008 women were over 40 percent of the world labour force, and the participation gap had narrowed from
   32 to 26 points since 1980. South Asia stood at 35 percent (DL-WB-2 pp. 9–10) and still does in 2026 (DL-WB-6 p. 4). In 2012 fewer than half of women worldwide
   had jobs against four-fifths of men (DL-WB-1 p. 6). The ILO notes that gender gaps have narrowed partly because young men dropped out
   (DL-OTH-5 p. xii).
6. **Unemployment after 2008 and 2020: two very different recoveries.** US unemployment peaked at 10.0 percent in October 2009 and took years to
   fall. After hitting 14.8 percent in April 2020 it was back to 3.5 percent by July 2022, when quits (3.0 percent, November 2021) and job
   openings (12.3 million, March 2022) were at record highs, the "Great Resignation" (DL-OTH-9). World unemployment was a steady 5 percent in
   2024 (DL-OTH-5 p. xi). Youth unemployment had exceeded 50 percent in Spain in 2012 (DL-WB-1 p. 6).
7. **Wages and the labour share.** In advanced economies labour shares fell from the 1980s to a half-century low before 2008 and did not recover.
   About half of the fall is attributed to technology (DL-IMF-1 pp. 121, 125). In high-income countries productivity rose 29 percent against 15
   percent for real wages in 1999–2024. After real wages fell in 2022, global real wages grew 2.7 percent in 2024 (DL-OTH-6 pp. 3–4), but most
   countries had not recouped their pandemic-era losses (DL-OTH-5 p. xii).
8. **Migration and remittances grew to new records.** Migrants and refugees numbered 304 million in 2024 (3.7 percent of world population), almost
   double 1995. About 40 percent of migrants and 75 percent of refugees live in EMDEs (DL-IMF-4 p. 1). Remittances reached an estimated USD 905
   billion in 2024 (USD 685 billion to developing countries), more than ODA and FDI combined (DL-OTH-4). Acceptance of migrants fell in major
   destinations from 2016 to 2023 (DL-IMF-4 p. 2), and the IMF had argued in 2018 that rich countries need migration to sustain labour supply
   (DL-IMF-2 p. 1).
9. **India, part 1: the dividend, now closing.** The Survey of 2006-07 promised a dividend until 2045 (DL-IN-1 p. 14). In 2012-13 the Survey asked
   where good jobs would come from (DL-IN-3 p. 26). In 2018-19 it said the 0–19 population had already peaked and the TFR would fall below
   replacement by 2021 (DL-IN-5 p. 128). NFHS-5 (2019-21) put the TFR at 2.0 (DL-IN-6 p. 378), and UNFPA's 2023 figures put India at 1,428.6
   million, ahead of China (DL-OTH-3). The World Bank says India's working-age share peaks within a decade (DL-WB-6 p. 1). ES 2025-26 puts the
   peak around 2030 (DL-IN-9 p. 468). India needs about 7.85 million non-farm jobs a year (DL-IN-7 p. 158).
10. **India, part 2: more work, but what kind; and the remittance cushion.** PLFS unemployment fell from 6.0 to 3.2 percent and LFPR rose from 49.8
    to 60.1 percent between 2017-18 and 2023-24 (DL-IN-8 pp. 31, 365). FLFPR rose from 23.3 to 41.7 percent (DL-IN-8 p. 370). But the self-employed
    share rose from 52.2 to 58.4 percent, and unpaid helpers rose to 42.3 percent of rural women workers (DL-IN-8 p. 367). The World Bank finds
    88 percent of South Asian workers informal (DL-WB-6 p. 3). The Labour Codes took effect by notification on 21 November 2025 (DL-IN-9 p.
    485). India is the world's largest remittance recipient, with USD 137.67 billion in 2024 (DL-OTH-4) and USD 135.4 billion in FY25, about 3.5
    percent of GDP (DL-IN-9 p. 173).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2006 | WDR 2007 (DL-WB-4) | 12–24-year-olds at a record 1.5 bn, to peak in 2035; Sub-Saharan Africa 20 years from its youth peak | 2026: 1.2 bn young people reach working age in EMDEs by 2035, the largest cohort ever, increasingly in Sub-Saharan Africa (DL-WB-5 p. 1) |
| 2007 | ES 2006-07 (DL-IN-1) | India benefits from the demographic dividend until 2045; working-age share rises to 68.4% by 2026 | World Bank 2026: India's working-age share peaks within a decade (DL-WB-6 p. 1); ES 2025-26: dividend peaks around 2030 (DL-IN-9 p. 468) |
| 2011 | WDR 2012 (DL-WB-2) | South Asia's female participation 35%, among the lowest | Still 35% in 2026 (DL-WB-6 p. 4) |
| 2012 | WDR 2013 (DL-WB-1) | 600 mn more jobs needed between 2005 and 2020 | 2026: only ~400 mn of 1.2 bn young people projected to be employed in 2035 (DL-WB-5 p. 1) |
| 2013 | ES 2012-13 (DL-IN-3) | The central question: where will good jobs come from? | Self-employed share rose from 52.2% to 58.4% and regular wage jobs fell from 22.8% to 21.7% (2017-18 to 2023-24) (DL-IN-8 p. 367); 88% informal (DL-WB-6 p. 3) |
| 2017 | WEO Apr 2017 (DL-IMF-1) | AE labour shares at a half-century low and not recovering | 1999–2024: productivity +29% vs real wages +15% in high-income countries (DL-OTH-6 p. 4) |
| 2018 | WEO Apr 2018 (DL-IMF-2) | Ageing will depress participation; migration needed for labour supply | US prime-age LFPR reached 84.0% in Jul 2024 (DL-OTH-9); migrant stock 304 mn by 2024 (DL-IMF-4); EU expects participation to keep rising (DL-OTH-8) |
| 2018 | ES 2017-18 (DL-IN-4) | Women's employment lagging; development no antidote | FLFPR rose from 23.3% to 41.7% by 2023-24, mainly rural and much of it self-employed or unpaid helpers (DL-IN-8 pp. 367, 370) |
| 2019 | ES 2018-19 (DL-IN-5) | TFR below replacement by 2021 | NFHS-5 (2019-21): TFR 2.0 (DL-IN-6 p. 378); UNFPA 2023: 2.0 (DL-OTH-3) |
| 2019 | ES 2018-19 (DL-IN-5) | Working-age population +9.7 mn a year in 2021–31 | ES 2023-24: 7.85 mn non-farm jobs needed every year (DL-IN-7 p. 158) |
| 2023 | WDR 2023 (DL-WB-3) | ~184 mn migrants, 2.3% of world population | 304 mn migrants and refugees (3.7%) in 2024 on IMF/IOM counts (DL-IMF-4, DL-OTH-4); definitions differ |
| 2023 | UNFPA SWOP 2023 (DL-OTH-3) | India 1,428.6 mn vs China 1,425.7 mn | China 1,404.89 mn at end-2025 and falling (DL-OTH-7); WPP: India the largest country to 2100 (DL-OTH-1 p. 37) |
| 2024 | WPP 2024 (DL-OTH-1) | China to lose 204 mn by 2054 | End-2025: −3.39 mn in one year; births 7.92 mn, deaths 11.31 mn (DL-OTH-7) |
| 2024 | World Bank brief (DL-WB-7) | Remittances ~$656 bn in 2023 | ~$905 bn in 2024; India $137.67 bn (DL-OTH-4) |
| 2025 (Jan) | ILO WESO 2025 (DL-OTH-5) | Unemployment steady at 5%; labour shortages eased but not gone | US quits back to 2.1% (Sep 2026) from 3.0%; US UR 4.1% in Oct 2026 (DL-OTH-9) |
| 2025-26 | ES 2025-26 (DL-IN-9) | Immigration controls may cap remittances | Remittances still rose to $73 bn in H1 FY26 from $64.7 bn (DL-IN-9 p. 173) |

Candidate quotes (all verified by script against the converted text, under 15 words):
- "development happens through jobs" (WDR 2013, DL-WB-1 p. 2)
- "Worldwide, fewer than half of women have jobs, compared with almost four-fifths of men" (WDR 2013, DL-WB-1 p. 6)
- "By 2008, women represented more than 40 percent of the global labor force" (WDR 2012, DL-WB-2 p. 10)
- "wealthy countries will need foreign workers to sustain their economies" (WDR 2023, DL-WB-3 p. 2)
- "the most ever in history" (WDR 2007, DL-WB-4 p. 4)
- "the largest youth cohort the world will likely ever see" (The Global Jobs Challenge, DL-WB-5 p. 1)
- "In less than a decade, in 2034, South Asia’s working-age population share will peak" (DL-WB-6 p. 1)
- "Growing old before growing rich." (DL-WB-6 p. 3)
- "labor income shares began trending down in the 1980s" (WEO April 2017, DL-IMF-1 p. 121)
- "underscores the need to rethink migration policies to boost labor supply" (WEO April 2018, DL-IMF-2 p. 1)
- "the 70s are the new 50s" (WEO April 2025 ch. 2, DL-IMF-3 p. 2)
- "the global stock of legal migrants and refugees had reached 304 million" (WEO April 2025 ch. 3, DL-IMF-4 p. 1)
- "The world’s population is likely to peak within the current century." (WPP 2024 key messages, DL-OTH-2)
- "China is projected to have lost more than half of its current population" (WPP 2024, DL-OTH-1 p. 16)
- "expected to remain the world’s largest throughout the century" (WPP 2024 on India, DL-OTH-1 p. 37)
- "restricting these pathways does not stop migration" (IOM press release, DL-OTH-4)
- "India, however, continued to be well above the rest" (IOM WMR 2026 remittances section, DL-OTH-4)
- "the job recovery has lost much of its ability to generate further improvements" (ILO WESO 2025, DL-OTH-5 p. xi)
- "the largest gain in more than 15 years" (ILO Global Wage Report 2024–25, DL-OTH-6 p. 3)
- "Total Population Went down and Urbanization Rate Continued to Grow." (NBS, DL-OTH-7)
- "the old-age dependency ratio will rise sharply in all Member States" (EU 2024 Ageing Report, DL-OTH-8 p. 3)
- "where will good jobs come from?" (ES 2012-13, DL-IN-3 p. 26)
- "a good job is the best form of inclusion" (ES 2012-13, DL-IN-3 p. 26)
- "development has not proved to be an antidote" (ES 2017-18, DL-IN-4 p. 102)
- "population in the 0-19 age bracket has already peaked" (ES 2018-19, DL-IN-5 p. 128)
- "nearly 78.51 lakh jobs annually in the non-farm sector" (ES 2023-24, DL-IN-7 p. 158)
- "driven mainly by the rising participation of rural women" (ES 2024-25, DL-IN-8 p. 370)
- "India's workforce of over 56 crore holds tremendous potential" (ES 2025-26, DL-IN-9 p. 467)
- "India’s longer-term position as the world’s largest recipient of remittances" (ES 2025-26, DL-IN-9 p. 173)
- "The implementation of these Codes was notified on 21 November 2025." (ES 2025-26, DL-IN-9 p. 485)

## Not obtained

- IMF *WEO September 2004*, Chapter 3 "How Will Demographic Change Affect the Global Economy?" (the chapter exists: its title and sections are
  on the index page https://www.imf.org/external/pubs/ft/weo/2004/02/index.htm, 200, and the issue page
  https://www.imf.org/en/publications/weo/issues/2016/12/31/the-global-demographic-transition, 200). Chapter PDF linked from the index:
  https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2004/02/pdf/_chapter3pdf.pdf — 404; other PDFs on
  the same page (_chapter1pdf.pdf, _frontmpdf.pdf, chp3pdf/_box31pdf.pdf) — 404; guessed
  https://www.imf.org/external/pubs/ft/weo/2004/02/pdf/chapter3.pdf — 404. The issue page's machine-written index.md (200) was not used. No
  2004 IMF view is cited.
- IMF *WEO October 2017*, Chapter 2 on wage dynamics: issue page
  https://www.imf.org/en/publications/weo/issues/2019/08/31/world-economic-outlook-october-2017-seeking-sustainable-growth-short-term-recovery-long-term-45123
  (200) has no PDF link, and its bundle-manifest.json (200) lists only the landing-page files. Guessed URLs under
  https://www.imf.org/-/media/files/publications/weo/2017/october/ — pdf/text.pdf, pdf/main-chapter/text.ashx, english/text.pdf, c2.pdf,
  ch2.pdf, pdf/c2.pdf, pdf/ch2.pdf, text.pdf — all 404. Guessed .../weo/2018/april/pdf/text.pdf and .../2018/april/english/text.pdf — 404
  (the April 2018 chapter came from the guessed c2.pdf, DL-IMF-2).
- IMF 2024 work on immigration to the US and Europe: not located on the issue pages read; WEO October 2024 ch. 3 (structural reforms,
  https://www.imf.org/-/media/files/publications/weo/2024/october/english/ch03.pdf, 200) was downloaded but is off topic and not used.
- World Bank Migration and Development Brief / KNOMAD brief for 2025 or 2026: the OKR search API (200) returns Brief No. 20 (2013) and
  "Migration and Remittances" (2018) as the latest; the KNOMAD publications page (200) points to the documents.worldbank.org list, whose API
  https://search.worldbank.org/api/v3/wds?format=json&qterm=%22Migration%20and%20Development%20Brief%22&... — 503 (rate-limit message). The
  World Bank brief page says KNOMAD was active until 2024 (DL-WB-7), so no 2025/2026 brief may exist; not confirmed.
- World Bank GEP chapter on ageing or labour supply: none found by OKR search; the South Asia report (DL-WB-6) and Global Jobs Challenge
  (DL-WB-5) were used instead.
- UN DESA pages on un.org (CloudFront "Request blocked"): https://www.un.org/development/desa/pd/publications — 403;
  https://www.un.org/development/desa/pd/ — 403; https://www.un.org/en/desa/world-population-prospects-2024 (guessed) — 403; WPP 2022 summary
  https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/wpp2022_summary_of_results.pdf (from the WPP script) — 403;
  UN DESA Policy Brief No. 153 on India overtaking China
  https://www.un.org/development/desa/dpad/publication/un-desa-policy-brief-no-153-india-overtakes-china-as-the-worlds-most-populous-country/
  (guessed) — 403; International Migrant Stock 2024 page https://www.un.org/development/desa/pd/content/international-migrant-stock (guessed)
  — 403. https://population.un.org/wpp/publications — 404. No 2026 WPP revision appears in the WPP site's file list.
- ILO *WESO Trends 2026*: https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-trends-2026 (guessed) — 404;
  ...-trends-2026-0 (guessed) — 404; ...world-employment-and-social-outlook-may-2026-update (guessed) — 404; ILO search
  https://www.ilo.org/search?search_api_fulltext=World%20Employment%20and%20Social%20Outlook%20Trends%202026 — 403; listing pages
  https://www.ilo.org/publications/flagship-reports, https://www.ilo.org/research-and-publications/flagship-reports and
  https://www.ilo.org/research-and-publications/publications — 404. The WESO May 2025 update page (guessed, 200) was not read.
- China NBS: the communiqués and January releases for 2022, 2023 and 2024 (first population declines): listing pages
  https://www.stats.gov.cn/english/PressRelease/index_40.html and index_46.html — 404 (the listing ends before early 2024); index_24, 38, 39, 41,
  44, 48, 50, 52 — connection reset (curl error 35 / HTTP 000) after many requests; the 2026 communiqué
  https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html — connection reset. Official announcements of the two-child
  (2015) and three-child (2021) policies: not attempted (no listing page found within the call budget); nothing on them is in these notes.
- US CBO *The Demographic Outlook*: https://www.cbo.gov/topics/demographics — 403. No CBO figures on the immigration surge.
- OECD *Employment Outlook 2025*: https://www.oecd.org/en/publications/oecd-employment-outlook-2025_194a947b-en.html (guessed) — 403.
- BLS JOLTS page https://www.bls.gov/jlt/ — 403; the same BLS series were read from FRED (DL-OTH-9). No Federal Reserve paper on the
  Great Resignation was read.
- MoSPI PLFS annual reports (2017-18, 2023-24, 2024) and monthly bulletins: https://www.mospi.gov.in/periodic-labour-force-survey-plfs — 200 but a
  2.6 KB script shell; https://www.mospi.gov.in/download-reports?main_cat=NzI2&cat=All&sub_category=All — same; the site script
  (https://www.mospi.gov.in/assets/index-C8jWYmQX.js, 200) exposes no report file list. PLFS figures in these notes come from the Economic
  Surveys (DL-IN-7 to IN-9), which cite the annual and monthly reports; unemployment by age and sex and rural/urban breakdowns beyond those
  quoted were not obtained.
- NFHS-5 India fact sheet: https://rchiips.org/nfhs/factsheet_NFHS-5.shtml — connection failed (HTTP 000). The NFHS TFR series is taken from ES
  2021-22 (DL-IN-6).
- Sample Registration System statistical report: https://censusindia.gov.in/census.website/data/SRSSTAT — 200 but a script-driven catalogue
  with no report links in the page; guessed catalogue API
  https://censusindia.gov.in/nada/index.php/api/catalog/search?sk=SRS%20Statistical%20Report&ps=10&sort_by=year&sort_order=desc — connection
  failed (HTTP 000). No SRS TFR is in these notes.
- PIB releases on the Labour Codes coming into force (November 2025) and on Census 2027: not attempted (no PIB listing or search used). The
  21 November 2025 notification date comes from ES 2025-26 (DL-IN-9 p. 485); nothing on Census 2027 is in these notes.
- Full texts not read: WDR 2023 chapters, the full *Global Jobs Challenge* report (downloaded), the WMR 2026 PDF, the full Global Wage Report,
  WESO 2025 chapters 1–3, and the Economic Survey 2010-11 passages beyond the grepped lines.
