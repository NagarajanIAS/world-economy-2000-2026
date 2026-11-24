# Reading notes: theme chapter "Development, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers). URLs were taken from publisher listing
or issue pages (worldbank.org publication pages and openknowledge.worldbank.org, pip.worldbank.org, un.org, unstats.un.org,
childmortality.org, who.int, oecd.org, wir2022.wid.world, niti.gov.in, mospi.gov.in, indiabudget.gov.in and others named in each entry);
any guessed URL is flagged. Downloads are in the session scratchpad folder `dev_dl/` (subfolders `wb/`, `un/`, `oth/`, `in/`). PDFs were
converted with `pdftotext` (plain and `-layout`) and read in the text. Quotes are verbatim, under 15 words, copied from the converted
text; everything else is paraphrase. Page numbers are printed page numbers unless stated (PDF page numbers are marked "PDF").

Item labels: DV-WB-n (World Bank), DV-UN-n (UN, WHO, UNICEF, UNESCO, UNDP), DV-OTH-n (OECD, academic, other), DV-IN-n (India). Indian
years are fiscal or survey years (2022-23). PPP = purchasing power parity; IPL = international poverty line; WDR = World Development
Report; MDG/SDG = Millennium/Sustainable Development Goals; FCS = fragile and conflict-affected situations; SSA = Sub-Saharan Africa;
ODA = official development assistance; GNI = gross national income; HCES = Household Consumption Expenditure Survey; MPCE = monthly per
capita consumption expenditure; MPI = multidimensional poverty index.

---

## World Bank

### DV-WB-1. World Bank, *Poverty, Prosperity, and Planet Report 2026: Jobs at the Center of Poverty Eradication*, Overview booklet, 2026 (listing page dated 17 October 2026 in its metadata)
Listing page: https://www.worldbank.org/en/publication/poverty-prosperity-and-planet (title "Poverty, Prosperity, and Planet Report
2026"; this URL now carries the 2026 edition, not the 2024 one).
Overview PDF ("Overview" link on that page): https://openknowledge.worldbank.org/bitstreams/f3b5fcaa-ad60-46c9-ae4f-32e6ecbcd980/download
(36 PDF pages; handle https://hdl.handle.net/10986/45652; printed roman p. vii = PDF 9; printed p. 1 = PDF 25).
Read: foreword, main messages ("Ten facts"), overview pp. 1–4; grepped the rest.
- p. vii (foreword, Kremer and Donohoe): extreme poverty share fell from 43 percent (1990) to 11 percent (2020), mostly through large
  middle-income economies; economies with a Gini above 40 fell from 70 (2000) to 42 (2024). In 2026 an estimated 811 million people,
  1 in 10, live below the $3.00-a-day line, "a rate unchanged since 2019". 3.7 billion (nearly half of humanity) live below $8.30 a day.
  1.5 billion people exposed to climate hazards lack the means to cope. Thematic focus: jobs; new data for over 130 economies.
- p. xv (fact 1): had the 2000–13 pace continued, 243 million more people would have left extreme poverty; stagnation is only at the
  $3.00 line, while at $4.20 and $8.30 poverty fell at the earlier pace. (Overview p. 1 rounds this to "roughly 240 million".)
- p. xv (fact 2): over half the extreme poor live in nine economies (three-quarters in 20, p. 3); by 2030, 87 percent will be in SSA,
  in FCS, or both; at the 2015–24 growth pace both the rate and the number of extreme poor will be higher in 2030 than today.
- p. xv (fact 3): most people who left extreme poverty since 2000 moved only into the $3.00–$8.30 band, "one shock away from falling back".
  The middle class ($8.30–$28.00) roughly doubled as a population share since 2000, mostly in today's upper-middle-income economies.
- p. xvii (fact 4): 37 economies never left the Gini-above-40 group in 25 years; one in five people still live in a high-inequality
  economy, unchanged since 2013; the share of the extreme poor in such economies nearly doubled, to 36 percent (overview p. 4 says "two
  in five").
- p. xvii (fact 5): Prosperity Gap (average factor by which incomes must rise to reach $28.00 a day) was 10.5 in 1990, 5.5 in 2013,
  4.5 in 2026; only about 1.2 percent a year narrowing in the latest decade; SSA 11.1, about where the world was in 1990.
- p. xviii–xix (facts 6–7): 4.6 billion exposed to major climate hazards, 1.5 billion highly vulnerable; share at high risk fell from
  1 in 3 (2010) to 1 in 6 (2024). Global GHG emissions (excluding land use) 52.8 GtCO₂e in 2024, 48 percent above 2000, nearly all the
  increase in upper-middle-income economies. Ending extreme poverty would add under 5 percent to global emissions (p. 6).
- p. 1: by 2020 the share was about 11 percent; over two-thirds of humanity now live in economies where extreme poverty "has
  effectively ended", up from a fifth in 2000. "Progress against extreme poverty has come to a standstill"; poverty rose in COVID,
  recovered, then flatlined; "The slowdown predates the pandemic". Before the Middle East conflict, 2026 extreme poverty was projected at
  808 million rather than 811 million (box 1.2); El Niño is another pressure. Global median income $9.20 a day.
- p. 2: without a change, the 2020s will close as "the first decade in more than a generation" without meaningful progress against
  extreme poverty. Eight "vision indicators" now tracked (poverty at $3.00 and $8.30, Prosperity Gap, high-inequality count, five
  planetary indicators).
- p. 3: at 2015–24 per capita growth, rate and number higher in 2030; only about 4 percent a year per capita growth would bring
  extreme poverty near the 3 percent target, and only by 2050, double the average country growth of the past 25 years.
- p. 4: Gini never rose above 40 in 79 economies and never fell below 40 in 37 (2000–24); high inequality is "a chronic condition
  either avoided or" entrenched (paraphrase of the rest).
- Inconsistency to note: the main messages are headed "Ten facts" while the overview (p. 2) refers to "9 facts".

### DV-WB-2. World Bank, *Poverty, Prosperity, and Planet Report 2024: Pathways Out of the Polycrisis*, Overview, 2024 (OKR issue date 15 October 2024)
Listing: OpenKnowledge item https://hdl.handle.net/10986/42211 (found via the OKR search API
https://openknowledge.worldbank.org/server/api/discover/search/objects, title "Poverty, Prosperity, and Planet Report 2024").
Overview PDF ("PPPR 2024 - Overview.pdf" in that item): https://openknowledge.worldbank.org/bitstreams/f75dd18d-4e3f-44f9-b455-7f0d8e189609/download
(66 PDF pages; printed p. 1 = PDF 17). Read: foreword, overview pp. 1–12. Lines are in 2017 PPPs ($2.15, $3.65, $6.85).
- Foreword (PDF 7–8, Indermit Gill): from 1990 rapid growth "especially in China and India" freed more than 1 billion people from
  extreme poverty; after 2020, starting with COVID, "a major reversal began"; PSP 2022 had found poverty rose for the first time in
  decades; the 3 percent by 2030 goal "slipped out of reach" and at the current pace will not be met for three decades; over a century
  to end poverty at $6.85. The 2020s are "shaping up to be a lost decade". Good news: extreme poverty 8.5 percent in 2024, first time
  below the 8.8 percent of 2019. High-inequality economies at a 24-year low (a one-third fall since 2000), yet 1.7 billion (20 percent)
  live in them, concentrated in SSA and Latin America. Ending poverty at $6.85 for 3 billion people would raise global emissions by
  nearly 50 percent over 2019 by mid-century.
- p. 1: series renamed (previously *Poverty and Shared Prosperity*); first post-COVID assessment; poverty reduction resumed but slower;
  "near standstill" in the past five years, raising fears that 2020–30 would be a lost decade. 692 million below $2.15 in 2024
  (8.5 percent).
- p. 2: extreme poverty fell from 38 percent (1990) to 8.5 percent (2024); at $3.65, about 1.7 billion (21.4 percent); at $6.85, 3.5
  billion (43.6 percent), share down from 70 percent since the 1990s but number barely changed since 1990. Projection: 7.3 percent in
  extreme poverty in 2030, more than double the 3 percent goal; only 69 million projected to escape extreme poverty by 2030. At 2010–19
  growth, extreme poverty stays above 7 percent until 2050; at 2 percent per capita growth everywhere, 60 more years to reach 3 percent
  (20 years if Ginis also fall 2 percent a year).
- p. 5: low-income countries' extreme poverty rose in 2020–21 and has not fallen much; 43 percent of people in low-income countries in
  extreme poverty in 2024; lower-middle-income countries recovered only in 2022.
- p. 6: COVID cut global life expectancy at birth by over 1.5 years; 9.3 million more children acutely malnourished and 2.6 million more
  stunted by 2022; learning losses around 30 percent in several countries; this generation risks $21 trillion in lifetime earnings
  (17 percent of global GDP). China lifted over 800 million out of extreme poverty over three decades; SSA's extreme poor rose from 282
  million (1990) to 464 million (2024); MENA's doubled from 15 to 30 million.
- p. 7: share of extreme poor in SSA or FCS: one-quarter in 2000, half by 2014, three-quarters by 2024; 42 percent in FCS in SSA. SSA GDP
  per capita grew 0.7 percent a year 1990–2022 vs 1.6 percent for the world. New Prosperity Gap measure (standard $25 a day, 2017 PPP):
  incomes must rise fivefold on average; 1.7 in Europe and Central Asia, over 12 in SSA; SSA is 39 percent of the gap, 16 percent of
  population.
- p. 10: 1990–2024 Prosperity Gap improved 2.34 percent a year (mean income +1.48 percent a year, global inequality −0.86 percent a
  year), the inequality fall driven by between-country convergence; 2019–24 gains limited by slower growth and a rise in global
  inequality.
- p. 12: on the latest survey for each economy, 49 of 166 economies had a Gini above 40 (down from 66 a decade earlier); about 1.7
  billion people lived in them in 2022.
- Comparison with DV-WB-1 (2026 edition, 2021 PPPs): the counts and standards changed with the PPP revision ($25 → $28.00 prosperity
  standard; 49 of 166 high-inequality economies on latest surveys → 42 in 2024 in a balanced 2000–24 series; 692 million at $2.15 in
  2024 → 811 million at $3.00 in 2026). The 2024 edition says poverty reduction "resumed" (8.5 percent below the 2019 rate); the 2026
  edition says the rate is "unchanged since 2019".

### DV-WB-3. World Bank (Federica Alfani, ..., Christoph Lakner, ..., Nishant Yonzan and Ayago Wambile), "June 2025 Update to the Poverty and Inequality Platform (PIP): What's New", Global Poverty Monitoring Technical Note 44, June 2025 (OKR issue date 11 June 2025)
Listing: OKR item https://hdl.handle.net/10986/43324 (OKR search API listing of all "Update to the Poverty and Inequality Platform"
notes, April 2022 to March 2026).
PDF: https://openknowledge.worldbank.org/bitstreams/8d28b28f-c071-40e6-91c6-f08efb411ceb/download (50 PDF pages; printed p. 1 = PDF 3).
Read: abstract, sections 1–3 (pp. 1–13).
- Abstract: the most important change is adoption of the 2021 PPPs; new India data incorporated and its series adjusted; estimates to
  2023 with nowcasts to 2025; 74 new country-years, over 2,400 surveys for 172 economies.
- p. 2: 2021 PPPs published by the International Comparison Program in May 2024. Lines revised: $2.15 → $3.00 (IPL), $3.65 → $4.20,
  $6.85 → $8.30. Lines still derived from countries' own national poverty lines; national lines rose by more than price changes alone,
  especially for the IPL. India's revision and new 2022 survey "significantly affects" South Asia and world estimates.
- pp. 2–3 (Table 1, reference year 2022, Sep 2024 vintage → Jun 2025 vintage): world extreme poverty revised up from 9.0 to 10.5
  percent (712.8 → 838.0 million). SSA, "home to two thirds of the global extreme poor": 37.0 → 45.5 percent (448 → 559 million). South
  Asia revised down 9.7 → 7.3 percent (45 million fewer), driven by India. At $4.20, world revised down 22.4 → 20.1 percent (South Asia
  38.8 → 27.7, 209 million fewer); at the upper line world 44.9 → 48.0 percent (3,574 → 3,832 million). Global survey coverage for
  low- and lower-middle-income countries in 2022: 81.1 percent; SSA coverage 48.8 percent.
- p. 4 (Table 2, $3.00 line): world 11.2 percent (2020), 11.0 (2021), 10.5 (2022), 10.2 (2023), 10.0 (2024 nowcast), 9.9 (2025
  nowcast). South Asia 10.3 → 4.8 over 2020–25; SSA 46.2 → 44.4; MENA rising 8.6 → 9.4. At $8.30, world 50.4 (2020) → 45.5 percent
  (2025). Nigeria's last survey is from 2018, a major source of uncertainty.
- p. 6: the IPL rose about 40 percent, the upper-middle line about 20 percent; the jump reflects higher national poverty lines in
  low-income countries, tied to better consumption surveys (especially in West Africa); the new IPL reflects "better information on the
  cost of basic needs" in the poorest countries. Trends are consistent whichever PPPs are used. A 2017-PPP legacy series is kept.
- p. 7: World Bank deviates from ICP PPPs for 4 countries (Egypt, Guinea, São Tomé and Príncipe, Sudan), against 8 exceptions in 2017
  and 6 in 2011.
- p. 8 (India): estimates rebuilt on the 2022-23 HCES, released by NSSO "after an 11-year gap"; switch from uniform reference period
  (URP) to modified mixed reference period (MMRP); welfare aggregate (PDS rations and free school uniforms valued at market unit
  values; durables, hospitalisation, jewellery and rents excluded, pp. 9–11); new spatial (Fisher, Tendulkar Committee 2009 method) and
  within-year price deflators (p. 11). Estimates for 2015/16–2021/22, which had been imputed from CMIE's Consumer Pyramids Household
  Survey (CPHS) "in the absence of official survey data", were removed as not comparable (p. 9).
- p. 12: comparability caveats (CAPI interviewing, items 347 → 405, three questionnaires over several visits, new rural stratum). The
  CES inequality estimates may be underestimated (missing top households; exclusions bias down better-off consumption).
- p. 13 (Tables 4–6): India at $3.00 (2021 PPP): 27.12 percent (344.41 million) in 2011-12 → 5.25 percent (75.22 million) in
  2022-23; at $4.20: 57.68 → 23.89 percent; at $8.30: 92.48 → 82.06 percent; Gini 28.78 → 25.51. Old vintage (URP, 2017 PPP) had put
  2011-12 at 22.86 percent at $2.15 with Gini 35.40; new MMRP 2017-PPP series gives 16.22 (2011) → 2.35 percent (2022) at $2.15.

### DV-WB-4. World Bank (R. Andres Castaneda Aguilar et al.), "March 2026 Update to the Poverty and Inequality Platform (PIP): What's New", Global Poverty Monitoring Technical Note 50, March 2026 (updated March 2026; OKR issue date 20 March 2026)
Listing: OKR item https://hdl.handle.net/10986/44626 (same OKR listing as DV-WB-3; no September 2026 PIP note was found in an OKR
search on 23 Nov 2026). PDF: https://openknowledge.worldbank.org/bitstreams/3284631f-f83a-410a-a5be-1c3d2c031e56/download
Read: abstract, update note, section 1 with Table 1 (pp. 1–3).
- Abstract/update note: 28 more country-years, over 2,500 distributions for 172 economies; Luxembourg Income Study bins 400 → 1,000;
  regional aggregates through 2024; the 2026 nowcast of extreme poverty was corrected from 9.8 to 10.0 percent.
- p. 2 (Table 1, $3.00 line, 2021 PPP): world 11.3 percent (2021), 10.9 (2022), 10.6 (2023), 10.4 (2024), 10.2 (2025 nowcast), 10.0
  (2026 nowcast). South Asia 7.9 (2021) → 3.8 (2024) → 2.5 percent (2026). SSA 46.2 → 45.1 → 43.3 percent. MENAAP (Middle East, North
  Africa, Afghanistan and Pakistan; new Pakistan data) 13.4 (2021) → 14.4 (2024), the only region where poverty is rising. At $8.30,
  world 48.8 (2021) → 46.1 (2024) → 44.4 percent (2026).
- Note for the book: the 2021–23 global figures differ slightly from the June 2025 vintage (DV-WB-3: 11.0, 10.5, 10.2) because of
  new data and regional regrouping; cite the vintage.

### DV-WB-5. World Bank, *Poverty and Shared Prosperity 2016: Taking on Inequality*, Overview, 2016 (OKR issue date October 2016)
Listing: OKR item https://hdl.handle.net/10986/25078 (OKR search API). Overview PDF ("210958ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/b2a6b5bf-835a-562b-bbcb-86677f8a7584/download (22 PDF pages; printed = PDF page).
Read: pp. 1–11. Lines in 2011 PPPs ($1.90).
- p. 1: on 20 April 2013 the World Bank Board adopted two goals: end extreme poverty (from 10.7 percent in 2013 to 3.0 percent by 2030)
  and promote shared prosperity (income growth of the bottom 40 percent in each country); linked to SDGs 1 and 10. This report
  inaugurates the annual *Poverty and Shared Prosperity* series; its focal theme is inequality.
- p. 2: the poorest children are four times less likely than the richest to be in primary school; of 780 million illiterate adults
  nearly two-thirds are women. Recovery from the 2008 crisis and slower growth put the 2030 goal at risk without faster growth or lower
  within-country inequality.
- p. 3: 767 million people below $1.90 in 2013 (10.7 percent), 1.7 points below 2012. A trade-off between efficiency and equity "is not
  inevitable" (paraphrase; equity-enhancing policies can also help growth).
- p. 4: SSA had 41.0 percent and 389 million poor, more than all other regions combined; in 1990 half the poor were in East Asia, by 2013
  only 9.3 percent. Nearly 1.1 billion fewer poor in 2013 than 1990 while world population grew almost 1.9 billion; 114 million left
  extreme poverty in 2013 alone (net). South Asia's fall "driven by India's growth".
- p. 6: half the global poor were children under 18 (2013); rural poverty 18.2 percent vs urban 5.5 percent.
- p. 7: bottom 40 had positive income growth in 60 of 83 countries (c. 2008–13); 49 had a positive "shared prosperity premium"; in 23
  the bottom 40's incomes fell. Average premium only 0.5 percentage points.
- p. 9: the narrowing of global inequality since the 1990s is the first since the industrial revolution; global Gini fell from 66.8
  (2008) to 62.5 (2013).
- p. 10: driven by convergence of average incomes "spurred by rising incomes in populous countries such as China and India"; between-
  country inequality fell, so within-country inequality now explains about a third of the total. Population-weighted average within-
  country Gini rose from 34 to 40 (1988–98), then fell to 39 (2013): within-country inequality for the average person "was wider in 2013
  than 25 years previously".

### DV-WB-6. World Bank, *Poverty and Shared Prosperity 2020: Reversals of Fortune*, Overview, 2020 (OKR issue date 7 October 2020)
Listing: OKR item https://hdl.handle.net/10986/34496. Overview PDF ("211602ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/65448440-da46-5fcf-9d83-9407c1896cc0/download (35 PDF pages; printed p. 1 = PDF 15).
Read: foreword and overview pp. 1–3; grepped the rest.
- Contents (PDF 5): COVID-19, conflict and climate change "have reversed the gains in poverty eradication for the first time in a
  generation".
- Foreword (PDF 7, David Malpass): 88–115 million could fall back into extreme poverty in 2020, plus 23–35 million in 2021, a total of
  110–150 million "new" extreme poor; climate change may push about 100 million more into poverty by 2030.
- p. 1: poverty reduction "has suffered its worst setback in decades" after nearly a quarter century of declines. The "new poor" are
  more urban, better educated and less likely to work in agriculture. COVID expected to push some 100 million into extreme poverty in
  2020 alone; MENA extreme poverty nearly doubled 2015–18 (3.8 → 7.2 percent; Syria, Yemen); up to 132 million may fall into poverty by
  2030 from climate change (note: the foreword says "about 100 million").
- p. 2: the 3 percent by 2030 goal, at risk before the crisis, "is now harder than ever to reach". The decline continued through 2017
  but was stalling: 741 million (2015) → 689 million (2017) below $1.90. Global extreme poverty fell about 1 point a year 1990–2015,
  0.6 points a year 2013–15, about half a point a year 2015–17.
- p. 3: in 2018 the Bank added $3.20 and $5.50 lines, a societal poverty line and a multidimensional measure. South Asia lined-up
  estimates not reported after 2014 for lack of population coverage (box 1.2 on India); for 2017 a range of 7.7–10.0 percent is given.

### DV-WB-7. World Bank, "WDR Reports" (World Development Report archive page), accessed 23 Nov 2026; with the WDR 2024 and WDR 2026 publication pages
Listing page: https://www.worldbank.org/en/publication/wdr/wdr-archive (title "WDR Reports"); WDR 2024 page
https://www.worldbank.org/en/publication/wdr2024 (page title "World Development Report 2024: The Middle-Income Trap"); WDR 2026 page
https://www.worldbank.org/en/publication/wdr2026 (page title "WDR 2026: The Promise of Artificial Intelligence"; OKR item
https://hdl.handle.net/10986/45296, "World Development Report 2026: The Promise of Artificial Intelligence", issue date 4 August 2026).
Read: whole archive page (2026 back to 1978) and the "About"/"Main Messages" text of the 2024 and 2026 pages.
- Titles 2000/01–2026 as printed on the archive page (subtitle as the page gives it): WDR 2000-2001 *Attacking Poverty*; 2002 *Building
  Institutions for Markets*; 2003 *Sustainable Development in a Dynamic World*; 2004 *Making Services Work for Poor People*; 2005 *A
  Better Investment Climate for Everyone*; 2006 *Equity and Development*; 2007 *Development and the Next Generation*; 2008 *Agriculture for
  Development*; 2009 *Reshaping Economic Geography*; 2010 *Development and Climate Change*; 2011 *Conflict, Security, and Development*;
  2012 *Gender Equality and Development*; 2013 *Jobs*; 2014 *Risk and Opportunity*; 2015 *Mind, Society, and Behavior*; 2016 *Digital
  Dividends*; 2017 *Governance and the Law*; 2018 *LEARNING to Realize Education's Promise*; 2019 *The Changing Nature of Work*; 2020
  *Trading for Development in the Age of Global Value Chains*; 2021 *Data for Better Lives*; 2022 *Finance for an Equitable Recovery*; 2023
  *Migrants, Refugees, and Societies*; 2024 (archive gives no subtitle; WDR 2024 page title: *The Middle-Income Trap*); 2025 *Standards for
  Development*; 2026 (archive "FEATURED", no subtitle; WDR 2026 page and OKR: *The Promise of Artificial Intelligence*). Earlier: 1999-2000
  *Entering the 21st Century*; 1990 *Poverty*; 1980 *Poverty and Human Development*.
- Archive blurbs: WDR 2006 says inequality of opportunity "sustains extreme deprivation" and wastes human potential; WDR 2018 "is the
  first ever devoted entirely to education"; WDR 2019 finds robot job-loss fears on balance "unfounded"; WDR 2022 on finance for the
  pandemic recovery.
- WDR 2024 page (Main Messages): middle-income countries are home to 6 billion people; since the 1990s only 34 middle-income economies
  reached high income; 108 remained middle-income at end-2023; since 1970 median middle-income per capita income has never exceeded 10
  percent of the US level. "3i strategy": investment (low income, 1i), plus infusion (lower-middle, 2i), plus innovation (upper-middle,
  3i).
- WDR 2026 page (About): "development progress has dipped to its weakest pace in 75 years"; AI offers a "rare path" to prosperity;
  countries need not build trillion-dollar models but must adapt AI locally; "small AI"; framework "adopt, adapt, and advance". AI is
  diffusing faster than steam (about 80 years to reach lower-income countries), electricity (40) and the internet (20).

### DV-WB-8. World Bank, *World Development Report 2000/2001: Attacking Poverty*, Overview "Attacking Poverty: Opportunity, Empowerment, and Security", 2001 (OKR date 2001)
Listing: archive page (DV-WB-7) → OKR item https://hdl.handle.net/10986/11856. Overview PDF ("9780195211290_overview.pdf"):
https://openknowledge.worldbank.org/bitstreams/8ba237ae-3d80-599a-afd0-ba2ffbff69d3/download (12 PDF pages; PDF page numbers used).
Read: PDF pp. 1–6.
- PDF 1: poverty as lack of "fundamental freedoms of action and choice"; meagre assets and missing markets lock people in material
  poverty, so promoting opportunity (growth, markets that work for the poor, asset building) is key, but "only part of the story"; state
  institutions are often unresponsive or corrupt towards the poor. Opens with the story of Basrabai, first woman sarpanch of Mohadi
  village, Gujarat (box, PDF 2: the teacher came once a month; SEWA organisers).
- PDF 3: three pillars: opportunity, empowerment (making state and social institutions more responsive to poor people) and security
  (reducing vulnerability to illness, violence, economic shocks, bad weather, disasters). Background study *Voices of the Poor*: more than
  60,000 poor people in 60 countries.
- PDF 3: of the world's 6 billion people, 2.8 billion (almost half) live on less than $2 a day and 1.2 billion (a fifth) on less than
  $1 a day, 44 percent of them in South Asia; average income of the richest 20 countries is 37 times the poorest 20, a gap that doubled
  in 40 years; in East Asia the $1-a-day poor fell from about 420 to 280 million (1987–98), but numbers rose in Latin America, South Asia
  and SSA, and more than twentyfold in Europe and Central Asia.
- PDF 6: "international development goals" (benchmark 1990, mostly for 2015): halve the share in $1-a-day poverty, universal primary
  education, gender parity in schooling, cut infant and child mortality by two-thirds, maternal mortality by three-quarters, universal
  reproductive health access, national sustainable-development strategies by 2005. Halving poverty 1990–2015 needs a 2.7 percent a year
  decline; the Bank estimated about 1.7 percent a year in 1990–98.

### DV-WB-9. World Bank, *World Development Report 2006: Equity and Development*, Overview, 2005 (OKR date 2005)
Listing: archive page (DV-WB-7) → OKR item https://hdl.handle.net/10986/5988. Overview PDF ("9780821362495_overview.pdf"):
https://openknowledge.worldbank.org/bitstreams/b1f52d68-2cff-5979-949f-78bb85e2c3fd/download (17 PDF pages). Read: PDF pp. 1–3.
- PDF 1: two South African children born in 2000: Nthabiseng (black, rural Eastern Cape) has a 7.2 percent chance of dying in her first
  year vs Pieter's (white, Cape Town) 3 percent; life expectancy 50 vs 68; schooling under 1 year vs 12. Sven (average Swede): 0.3
  percent infant mortality, life to 80, 11.4 years of schooling, math score 500 vs a South African average of 264.
- PDF 2: definition: equity means individuals "should have equal opportunities to pursue a life of their choosing" and be spared extreme
  deprivation in outcomes. Main message: equity is complementary to long-term prosperity; a "level playing field" aids growth; greater
  equity is "doubly good" for poverty reduction. Two reasons: market failures (credit, insurance, land, human capital), and unequal power
  producing institutions that favour the influential. Self-reproducing "inequality traps".

### DV-WB-10. World Bank, *World Development Report 2018: Learning to Realize Education's Promise*, Overview, 2018 (OKR date 2018)
Listing: archive page (DV-WB-7) → OKR item https://hdl.handle.net/10986/28340. Overview PDF ("211096ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/e3b10485-6eaf-556c-a82e-13cd30420600/download. Read: foreword and overview opening
(PDF pp. 7, 15–18).
- PDF 7 (foreword, Jim Yong Kim): Korea's post-war rise through education; "Schooling without learning is a terrible waste"; "a moral
  and economic crisis".
- PDF 15: "Schooling is not the same as learning." In Kenya, Tanzania and Uganda three-quarters of grade 3 pupils could not understand a
  simple sentence; in rural India just under three-quarters of grade 3 students could not do a two-digit subtraction (46 – 17) and half
  still could not by grade 5 (data: ASER Centre 2017, PDF 17); some 260 million children not enrolled in primary or secondary school;
  "This learning crisis is a moral crisis". Three fronts: assess learning, act on evidence, align actors.
- PDF 17: in rural India in 2016 only half of grade 5 students could fluently read text at the level of the grade 2 curriculum.

### DV-WB-11. World Bank, *World Development Report 2024: The Middle-Income Trap*, Overview, 2024 (OKR item date 1 August 2024)
Listing: WDR 2024 page (DV-WB-7) "DOWNLOAD OVERVIEW" link https://bit.ly/WDR2024_Overview_ENG, which redirected to
https://openknowledge.worldbank.org/server/api/core/bitstreams/ef6b29bf-6596-4587-b7af-578740106050/content (30 PDF pages; printed =
PDF). Also read: "WDR 2024 Summary.pdf" (OKR item https://hdl.handle.net/10986/41919,
https://openknowledge.worldbank.org/bitstreams/de4e6fa8-c80f-4edf-a029-0c3501acc075/download, 4 pages, printed pp. xxi–xxiv). Read:
overview pp. 1–4; grepped for India.
- p. 1: middle-income countries "are in a race against time"; the sense that three decades were great for development comes from
  "abysmally low expectations"; 108 middle-income countries (per capita income $1,136–$13,845) aim at high income in two or three
  decades, but the 34 economies that made it since 1990 have under 250 million people in total, the population of Pakistan. Debt, ageing,
  protectionism and the energy transition make it harder. Two transitions: 1i (investment) → 2i (investment + infusion of foreign
  technology) → 3i (adding innovation). Discipline incumbents, reward merit, capitalise on crises.
- p. 2: since the 1970s median middle-income per capita income has stayed below a tenth of the US level; the "middle-income trap" term
  was coined by World Bank economists; India's vision is to become a developed economy by 2047; recommends value added, socioeconomic
  mobility and emissions intensity over firm size, income inequality and energy mix as policy metrics.
- p. 22 (approx., PDF): Aadhaar (begun 2009 under Nandan Nilekani) cited as building Indians' "digital capital".
- Summary (p. xxi): growth slowdowns are more frequent in middle-income countries; capital investment yields diminishing returns.
- Focus shift: from poverty and the poor's agency (2000/01) to growth strategy for middle-income countries; poverty barely features.

### DV-WB-12. World Bank, *World Development Report 2026: The Promise of Artificial Intelligence*, Overview booklet, 2026 (OKR issue date 4 August 2026)
Listing: OKR item https://hdl.handle.net/10986/45296 (WDR 2026 page, DV-WB-7). Overview PDF ("WDR 2026 Overview Booklet.pdf"):
https://openknowledge.worldbank.org/bitstreams/2caf7522-b4b1-4733-b086-3e5ae801ba4d/download (68 PDF pages). Read: foreword (PDF 9–11);
grepped the rest.
- Foreword (Indermit Gill, PDF 9): rich-country AI debates are "exercises in self-absorption"; for developing economies AI could put
  scarce knowledge within reach of millions by text message or voice call; could lift global growth to its strongest pace since the
  2000s; "development progress has dipped to a 75-year low". Risks: closing a route to middle-class jobs (call centres, entry-level
  software, finance), power and water shortages, technological dependence, inequality, misinformation. Industrial Revolution
  precedent: Britain about four times richer per person than India at the outset, 10 times by the end of the 20th century.
- PDF 10: under a tenth of developing-economy jobs are susceptible to AI automation vs over a third in high-income economies; one in six
  would be enhanced. One in five small firms surveyed in six developing economies already use AI chatbots. Examples: Bangladesh
  diabetic-eye screening up 40 percent a day; AI weather forecasts saved up to $560 per small farmer in Telangana, India; Ghana's Rori
  tutor gave nearly a year of maths learning for as little as $5 per student. India's UPI and Brazil's Pix as models of
  interoperability rather than "AI sovereignty".
- PDF 11: recommends adaptation as the mainstay, predictive AI in back-end functions, interoperability, voluntary standards, "small AI".

### DV-WB-13. World Bank, *Poverty & Equity Brief: India*, October 2026 (with the October 2024 and October 2022 India briefs for comparison)
Listing: https://www.worldbank.org/en/topic/poverty/publication/poverty-and-equity-briefs (page "Last Updated: Oct 9, 2026"); its
country table is an embedded Datawrapper chart whose data file https://datawrapper.dwcdn.net/AKPr7/35/dataset.csv (latest version;
36+ returned 404) links India "SM25" to https://documents1.worldbank.org/curated/en/099722104222534584/pdf/IDU-25f34333-d3a3-44ae-8268-86830e3bc5a5.pdf.
That URL now serves a two-page brief dated **October 2026** (the file appears to have been replaced in place; the column label is
older). October 2024 brief: found via the World Bank Documents & Reports search API
(https://search.worldbank.org/api/v2/wds), PDF https://documents.worldbank.org/curated/en/099125001062531830/pdf/IDU199905bac11419140a71be1018e573001fc40.pdf.
October 2022 brief: guessed URL https://databankfiles.worldbank.org/public/ddpext_download/poverty/987B9C90-CB9F-4D93-AE8C-750588BF00QA/current/Global_POVEQ_IND.pdf
(flag: guessed; returned 200 and an old brief stamped "Fall 2022 ... latest available"). Read: all three in full.
- Oct 2026 (p. 1): "one of the fastest poverty declines in the world"; between 2011 and 2023 the share below $4.20 a day (2021 PPP) fell
  from 57.7 to 16.1 percent, "lifting an estimated 496 million people out of poverty"; extreme poverty ($3.00) fell from 27.1 to 2.6
  percent. Projection: $4.20 poverty 14.2 percent in 2026 → 12.1 percent in 2028. MPI (OPHI): 53.8 percent (2005–06) → 16.4 percent
  (2019–21); World Bank MPI 15.5 percent (2022–23). Drivers: consumption growth, rising employment especially among women, social
  transfers including food subsidies. Top-10-percent median earnings about 13 times the bottom 10 percent (2023). A belt from Uttar
  Pradesh to West Bengal holds about 57 percent of India's poor. Employment up about 134 million 2017–23, nearly twice working-age
  population growth; youth unemployment 14.6 → 15.9 percent between Q1 FY2026 and Q1 FY2027.
- Oct 2026 (p. 2 tables, 2023): $3.00: 36.99 million poor, 2.6 percent; $4.20: 231.76 million, 16.1 percent; $8.30: 1,150.2 million,
  80.0 percent; Gini 23.0 (2023); Prosperity Gap 4.9. At $4.20: urban 8.6 vs rural 19.3 percent; ages 0–14 21.8 percent. MPI components:
  29.6 percent lack limited-standard sanitation; 1.0 percent no electricity.
- Oct 2026 methodology: based on three official surveys, 2011–12 CES and 2022–23 and 2023–24 HCES (MMRP, spatially and temporally
  deflated); "broadly comparable", but the big gain between 2022–23 and 2023–24 likely reflects "both genuine welfare gains and better
  measurement"; surveys may miss wealthier households and "are likely to understate inequality". Survey weights anchored in the 2011
  Census frame, likely understating the urban share. PLFS revamped since January 2025 (monthly estimates).
- Oct 2024 brief (2017 PPP, pre-revision): in FY2021/22, 12.9 percent below $2.15 and 44 percent below $3.65; Gini 33 ("steady
  inequality"); MPI 16.4 percent (2019–21); HCES 2022/23 shows real per capita consumption growth of 3 percent a year 2011/12–2022/23.
  Youth unemployment 13.8 percent (2022/23).
- Oct 2022 brief: "The most recent official poverty estimates for India are from 2011 at 21.9 percent"; "considerable uncertainty" over
  the trend; PIP then used imputed CPHS estimates: 22.5 percent (2011) → 10 percent (2019) at $2.15; the pandemic "would have
  interrupted almost 3 decades" of progress. Gini 35.7 (2019).
- Note: the PEB Gini (23.0 for 2023) is far below the Oct 2024 brief's 32.8–33 (2021, CPHS-based) and the PIP 2022-23 value of 25.51
  (DV-WB-3); the brief itself warns that inequality is understated.

### DV-WB-14. World Bank, UNESCO, UNICEF, FCDO, USAID and Bill & Melinda Gates Foundation, *The State of Global Learning Poverty: 2022 Update*, Conference Edition, 23 June 2022
Listing page (URL guessed, returned 200 with title "The State of Global Learning Poverty: 2022 Update"):
https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty. PDF ("Report: State of Global Learning
Poverty: 2022 Update" link): https://thedocs.worldbank.org/en/doc/e52f55322528903b27f1b7e61238e416-0200022022/original/Learning-poverty-report-2022-06-21-final-V7-0-conferenceEdition.pdf
(77 PDF pages; PDF page numbers used). Read: executive summary (PDF 5–11).
- PDF 5/15: learning poverty = share of children unable to read and understand a simple text by age 10; indicator launched in 2019 by the
  World Bank and the UNESCO Institute for Statistics.
- PDF 7: in 2019 learning poverty in low- and middle-income countries was 57 percent ("nearly 6 out of 10"); SSA 86 percent. It had
  fallen from 61 to 53 percent over 2000–2015 but rose from 53 to 57 percent in 2015–19. Schools fully closed for in-person teaching
  about 141 days on average between February 2020 and February 2022; South Asia lost 273 and Latin America 225 full days (PDF 8).
- PDF 8–9: simulations put learning poverty at an estimated 70 percent in 2022: one more child in eight, and "all of the gains ... since
  2000 have been lost"; largest rises in South Asia and Latin America (longest closures); remote learning a poor substitute.
- PDF 10: early measured data (São Paulo, Karnataka in India, some Mexican states) show learning losses roughly equal to the length of
  closure.
- PDF 11: the current generation risks losing $21 trillion in lifetime earnings (the PPP 2024 report repeats this, DV-WB-2).

### DV-WB-15. World Bank, *Poverty and Shared Prosperity 2022: Correcting Course*, Overview, 2022 (OKR item 10986/37739, dated 2022)
Listing: OKR item https://openknowledge.worldbank.org/handle/10986/37739 (found via the OKR search API). PDF ("9781464818936ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/d1d1b66e-e097-565d-8fa1-8fa4112730e6/download (45 PDF pages; printed p. v = PDF 7,
p. xiii = PDF 15, p. 5 = PDF 23). Read: foreword, main messages, overview pp. 1–5 incl. box O.2. Lines in 2017 PPPs ($2.15, $6.85).
- p. v (foreword, David Malpass): COVID "marked the end of a phase" of progress; more than 1 billion escaped extreme poverty in the
  three preceding decades; poverty reduction slowed after 2015; in 2020 the number in extreme poverty rose by over 70 million, "the
  largest one-year increase since global poverty monitoring began" in 1990. 574 million (nearly 7 percent) projected below $2.15 in
  2030; over 3 billion below $6.85. Global median income fell 4 percent in 2020, the first decline since 1990.
- p. v–vi: fiscal responses kept the average developing-economy poverty rate 2.4 points lower; UMICs offset about half the poverty
  impact, LICs and LMICs barely a quarter. India gave food or cash support to 85 percent of rural and 69 percent of urban households
  (digital cash transfers). Recommends targeted cash transfers over broad subsidies.
- p. xiii (main messages): extreme poverty 8.4 percent (2019) → 9.3 percent (2020), over 700 million; 2020 turned global income
  convergence into divergence; global inequality rose for the first time in decades; poverty reduction had already slowed to 0.6
  points a year in the five pre-pandemic years; up to 685 million in 2022; 47 percent of the world below $6.85 in 2019.
- p. 5: India's 2020 increase is uncertain: a national accounts projection gives 23 million, CPHS-based estimates 56 million (used for
  the global figure). Box O.2: India "has not published official survey data on poverty since 2011"; the Bank used the private CMIE
  Consumer Pyramids survey, re-weighted (Sinha Roy and van der Weide 2022), noting the dispute with the national-accounts approach
  of Bhalla, Bhasin and Virmani (2022).
- Link: these CPHS-based India estimates were later removed from PIP when HCES 2022-23 arrived (DV-WB-3).

## UN, WHO, UNICEF, UNESCO, UNDP

### DV-UN-1. United Nations (DESA), *The Sustainable Development Goals Report 2025*, 2025
Issue page: https://unstats.un.org/sdgs/report/2025/ (200; the general listing https://unstats.un.org/sdgs/report/ returned 403).
PDF: https://unstats.un.org/sdgs/report/2025/The-Sustainable-Development-Goals-Report-2025.pdf (linked from the issue page). PDF page
numbers used. Read: foreword (PDF 4), progress chart text (PDF 6), Goal 1 (PDF 10).
- PDF 4 (foreword, António Guterres): "only 35 per cent of SDG targets are on track or making moderate progress"; nearly half too slow;
  18 per cent "in reverse"; "We face a global development emergency." Over 800 million in extreme poverty; over 120 million forcibly
  displaced, more than double 2015. Social protection now covers over half the world, up 10 points in a decade; women hold 27 percent of
  parliamentary seats, up from 22.
- PDF 6: of 169 targets, 139 assessable; 18 percent on track, 17 percent moderate progress, 48 percent insufficient (31 marginal, 17 no
  progress), 18 percent regressed below the 2015 baseline.
- PDF 10: World Bank revision of June 2025 (prices and national lines from over 160 countries): IPL $2.15 (2017 PPP) → $3.00 (2021 PPP).
  Under the new line 1.5 billion escaped poverty 1990–2022 (1.3 billion under the old). 2025: an estimated 808 million in extreme
  poverty (previous estimate 677 million), 9.9 percent of world population. At current trajectory 8.9 percent still extremely poor in
  2030; only 1 in 5 countries projected to halve national poverty by 2030.

### DV-UN-2. United Nations (DESA), *The Sustainable Development Goals Report 2026*, with its press release (7 July 2026)
Issue page: https://unstats.un.org/sdgs/report/2026/ (200). PDF: https://unstats.un.org/sdgs/report/2026/The-Sustainable-Development-Goals-Report-2026.pdf
(51 PDF pages); press release https://unstats.un.org/sdgs/files/report/2026/SDG_Report_2026_Press_Release_EN.pdf (both linked from the
issue page). Read: press release in full; report PDF 4–7 and 10.
- Press release, 7 July 2026: since 2015 nearly 1 billion gained safely managed drinking water and 1.2 billion safely managed sanitation;
  new HIV infections down 30 percent and AIDS deaths 35 percent (2015–24); electricity reaches 92 percent; internet use 40 → 74 percent;
  social protection covers over half the world "for the first time in history". Of 139 targets with trend data, 36 percent on track or
  moderate progress, 49 percent too slow, 15 percent regressed below 2015. One in ten in extreme poverty; 2.3 billion moderately or
  severely food insecure; over 150 million children stunted; maternal mortality nearly three times the target; no gender target on
  track. "Official development assistance fell by a record 23.1 per cent in 2025 — the largest annual decline ever recorded —
  returning to roughly 2015 levels." SDG financing gap about $4 trillion a year. Extreme poverty projected at only 10 percent in 2026,
  "just 3 percentage points below its 2015 level". 273 million children and youth out of school. Stunting: 30.2 million fewer stunted
  children 2012–24. LMIC external debt a record $8.9 trillion (2024).
- PDF 5 (foreword): ODA "collapsed by a record 23 per cent in 2025"; 134 countries have met the child-mortality target; disaster deaths
  down 65 percent on the previous decade; 2.1 billion lack safely managed drinking water; 118 million forcibly displaced; data now cover
  nearly every indicator (3 million data points; the press release says 3.2 million).
- PDF 7: ODA declined 23.1 percent in 2025 from 2024, "the largest annual drop ever recorded", back to levels at the start of the 2030
  Agenda; further cuts expected in 2026.
- PDF 10 (Goal 1): "Progress towards eradicating extreme poverty has stalled." 2026: an estimated 10 percent, "some 826 million
  people", below $3.00 a day (2021 PPP), only 3 points lower than 2015; about 9 percent still in 2030, four in five of them in SSA or
  FCS. SSA's extreme poverty rose 2 points in the pandemic and regained pre-pandemic levels only in 2025. Over half the world covered by
  at least one social protection benefit in 2023, but 3.8 billion unprotected. ODA grants targeting poverty reduction fell 8.7 percent
  between 2023 and 2024.
- Disagreement: the UN's 826 million for 2026 vs the World Bank's 811 million (DV-WB-1), both at $3.00 2021 PPP and both about 10
  percent; probably different PIP vintages or population data (not explained in either text read).

### DV-UN-3. United Nations General Assembly, resolution 55/2, "United Nations Millennium Declaration" (A/RES/55/2), adopted at the 8th plenary meeting, 8 September 2000 (distributed 18 September 2000)
Document viewer: https://docs.un.org/en/A/RES/55/2 (UN Official Document System; un.org pages returned 403, see Not obtained). PDF (the
viewer's embedded source): https://documents.un.org/api/symbol/access?s=A/RES/55/2&l=en&t=pdf (9 pages). Read: whole text, sections I
and III closely (pp. 1–5).
- para. 1: heads of state and government met in New York, 6–8 September 2000, "at the dawn of a new millennium".
- para. 11: "We will spare no effort to free our fellow men, women and children" from extreme poverty, to which "more than a billion" are
  subjected; commitment to "freeing the entire human race from want".
- para. 15: calls on industrialised countries for duty- and quota-free access for LDC exports, enhanced HIPC debt relief and
  cancellation of official bilateral debts, and "more generous development assistance".
- para. 19 (the targets that became the MDGs): by 2015 halve the share of people with income under one dollar a day and the share
  suffering hunger, and halve the share without safe drinking water; universal completion of primary schooling, equal access for girls
  and boys; cut maternal mortality by three quarters and under-five mortality by two thirds "of their current rates"; halt and reverse
  HIV/AIDS, malaria and other major diseases; by 2020 improve the lives of at least 100 million slum dwellers. para. 20: gender equality.
- Note: the Declaration's baseline is "current rates" (2000); the WDR 2000/01 international development goals use 1990 benchmarks
  (DV-WB-8).

### DV-UN-4. World Health Organization, *World health statistics 2026: monitoring health for the SDGs, sustainable development goals*, 2026 (ISBN 978-92-4-012248-2)
Listing: https://www.who.int/data/gho/publications/world-health-statistics (lists editions 2005–2026) → item page
https://www.who.int/publications/i/item/9789240122482. PDF (from the item page): https://iris.who.int/server/api/core/bitstreams/45189137-2f10-48e1-ae43-91b0d8ddd120/content
(printed page = PDF − 7). Read: key messages (pp. 2–3), under-5 section (p. 22–23), section 2.2 life expectancy (p. 39).
- p. 2 (key messages): maternal mortality ratio down 40 percent and under-5 mortality rate down 51 percent since 2000, "yet progress
  has slowed down in the SDG era"; 2023 maternal mortality nearly three times the target. UHC service coverage index rose only 68 → 71
  (2015–23), a deceleration of about two-thirds compared with 2000–2015; 1.6 billion people living in or pushed into poverty by health
  spending (2022). New HIV infections down 40 percent 2010–24; malaria incidence up 8.5 percent since 2015. 961 million more people
  gained safely managed drinking water and 1.2 billion safely managed sanitation (2015–24).
- p. 3: an estimated 22.1 million excess deaths associated with COVID-19 in 2020–23, about three times the 7.0 million reported; peak
  10.4 million in 2021. Life expectancy and HALE rose 2000–19, "but the COVID‑19 pandemic erased nearly a decade of progress"; female
  life expectancy back to pre-pandemic level by 2023; many lower-income countries recovered or surpassed 2019 levels by 2023. Only 18
  percent of countries report mortality data within a year; of 61 million deaths in 2023 only 21 million were reported with cause.
- p. 22 (citing UN IGME, ref. 42): child survival is "one of the success stories of global public health". Under-5 deaths: 10.1
  million (2000, rate 76.7 per 1,000 live births) → 4.9 million (2024, 37.4 per 1,000). WHO African Region: nearly 60 percent of under-5
  deaths (2.8 million) but about 30 percent of births; 57-fold gap between highest and lowest country rates. Neonatal share of under-5
  deaths rose from 41 to 47 percent (2000–24); 2.3 million of the 4.9 million died in the first month.
- p. 39: global life expectancy at birth 67 years (2000) → 73 (2019); HALE 58 → 63. COVID cut life expectancy to 73 in 2020 (a fall of
  under 1 year) and 71 in 2021, back to 2011 levels; rebounded to 73 in 2022 and 2023. Men: 71 → 69 → nearly 71 (2019, 2021, 2023);
  women: 76 → 74 → 76.

## OECD, academic and other

### DV-OTH-1. OECD Development Assistance Committee, DAC1 table "Flows by provider (ODA+OOF+Private)" via the OECD SDMX data API, dataflow OECD.DCD.FSD:DSD_DAC1@DF_DAC1 (version 1.8), donor "DAC countries", queried 23 Nov 2026
Source: the OECD press-release pages for the preliminary 2024 and 2025 ODA data could not be fetched (oecd.org returns a Cloudflare
"Just a moment..." challenge, see Not obtained). Data instead from the OECD's public SDMX API (URL built from the API's own structure
query, not from a listing page; flag): https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,/DAC._Z.......?startPeriod=2000
(CSV with labels; structure from https://sdmx.oecd.org/public/rest/dataflow/OECD.DCD.FSD/DSD_DAC1@DF_DAC1/latest). Values in USD
million. All observations flagged "A: Normal value"; the API does not say which years are preliminary.
- ODA, grant-equivalent measure (headline since 2018; measure 11010), DAC countries, constant 2024 prices: 2018 172,112; 2019 172,761;
  2020 179,746; 2021 194,378; 2022 226,995; 2023 229,212; 2024 215,142; 2025 165,513. Current prices: 2023 223,921; 2024 215,142; 2025
  174,302.
- My calculations from these figures: real fall of 6.1 percent in 2024 and 23.1 percent in 2025 (matches the UN's "record 23.1 per cent",
  DV-UN-2); 2025 real ODA is below 2018 and close to 2016 (164,380).
- ODA as percent of GNI (grant equivalent, measure 11002): 0.30 (2018), 0.30 (2019), 0.32 (2020), 0.33 (2021), 0.37 (2022), 0.37
  (2023), 0.34 (2024), 0.26 (2025). (The 0.7 percent UN target is not stated in this dataset.)
- Older series, net disbursements of ODA (measure 1010, constant 2024 prices): 2000 82,970; 2005 137,309; 2006 129,632;
  2010 144,387; 2015 156,229; 2020 180,985. Net ODA as share of DAC GNI, my division of measure 1010 by measure 1 (GNI), current
  prices: 0.22 percent (2000), 0.32 (2005), 0.31 (2010), 0.30 (2015). So real net ODA roughly doubled 2000–2023 before the 2024–25 cuts.

### DV-OTH-2. World Inequality Lab (Lucas Chancel, Ricardo Gómez-Carrera, Rowaida Moshrif, Thomas Piketty et al.), *World Inequality Report 2026*, Executive Summary (English), uploaded November 2025
Listing: https://wir2026.wid.world/ (title "World Inequality Report 2026"; links the Executive Summary and the full report, uploaded
2026/09). Executive Summary PDF: https://wir2026.wid.world/www-site/uploads/2025/11/WIR26_Executive_Summary_English.pdf (22 PDF pages;
PDF page numbers used). Full report https://wir2026.wid.world/www-site/uploads/2026/09/World_Inequality_Report_2026.pdf not read.
Read: Box 1 and pp. 4–6.
- PDF 3 (Box 1): third edition after 2018 and 2022; supported by UNDP. Education spending per child about €200 (PPP) in SSA vs €7,400
  in Europe and €9,000 in North America & Oceania, "a gap of more than 1 to 40", about three times the per capita GDP gap. Rich
  economies' "exorbitant privilege": about 1 percent of world GDP a year, "approximately three times as much as development aid", flows
  from poorer to richer nations through net foreign income. Women earn 32 percent of men's hourly income counting unpaid work, 61
  percent without.
- PDF 5: the top 10 percent of global income earners earn more than the other 90 percent; the bottom half gets under 10 percent of
  income (figure: 8 percent of income at 2025 PPP; top 10 percent 53 percent). Wealth: top 10 percent own three-quarters (75 percent),
  bottom half 2 percent. The top 0.001 percent, "fewer than 60,000 multi-millionaires" (figure: about 56,000 adults), hold three times
  the wealth of half of humanity; their share rose from almost 4 percent (1995) to over 6 percent. Billionaire and centi-millionaire
  wealth grew about 8 percent a year since the 1990s, nearly twice the bottom half's rate. Top 10 percent account for 77 percent of
  emissions linked to private capital ownership; bottom half 3 percent.
- PDF 6: average income in North America & Oceania about 13 times SSA's (about €125 vs €10 a day).

### DV-OTH-3. World Inequality Lab (Lucas Chancel, Thomas Piketty, Emmanuel Saez, Gabriel Zucman et al.), *World Inequality Report 2022*, Summary (English), January 2022
Listing: https://wir2022.wid.world/ → https://wir2022.wid.world/www-site/uploads/2022/01/Summary_WorldInequalityReport2022_English.pdf
(19 PDF pages). Read: foreword (PDF 3–4) and pp. 7–10.
- PDF 4 (foreword, Abhijit Banerjee and Esther Duflo): 1945/50–1980 saw shrinking inequality in many places including India and China;
  the pro-market turn was used to justify ignoring inequality, so that "India is now among the most unequal countries in the world"
  (on the report's estimates).
- PDF 7 (2021, PPP): global bottom 50 percent 8 percent of income and 2 percent of wealth; top 10 percent 52 percent of income and 76
  percent of wealth.
- PDF 8: between-country inequality fell: the ratio of average incomes of the richest 10 percent of countries to the poorest 50 percent
  of countries dropped from about 50x to a little under 40x; within-country inequality rose sharply: top-10/bottom-50 ratio within
  countries "almost doubled, from 8.5x to 15x"; within-country inequality is now greater than between-country inequality. India named
  among the very unequal (with Brazil).
- PDF 9–10: the bottom half's share of world income is about half what it was in 1820; global top-10/bottom-50 income ratio 18x
  (1820), 41x (1910), 53x (1980), 38x (2020).
- Contrast with the World Bank (DV-WB-1, DV-WB-5): the Bank's survey-based Gini series shows falling global and (since c. 2000)
  within-country inequality, and only 42 economies with a Gini above 40; WIL's tax-and-national-accounts series stress rising top shares
  and within-country divergence since 1980.

## India

### DV-IN-1. NITI Aayog (Ramesh Chand and Yogesh Suri, with technical inputs from UNDP and OPHI), "Multidimensional Poverty in India since 2005-06: A Discussion Paper", January 2024 (file folder 2024-01; cites PIP accessed 12 January 2024)
Listing: NITI Aayog site search https://niti.gov.in/search/node?keys=multidimensional+poverty (the "whats-new" and discussion-paper
pages returned 404). PDF: https://niti.gov.in/sites/default/files/2024-01/MPI-22_NITI-Aayog20254.pdf (12 pages; printed = PDF). Read:
whole paper.
- p. 1 (abstract): national MPI uses Alkire-Foster with 12 indicators (global MPI 10). Because surveys exist only for 2005-06, 2015-16
  and 2019-21 (NFHS), the 2013-14 and 2022-23 headcounts "have been estimated" by compound growth rates (interpolated and extrapolated,
  p. 4). MPI headcount fell from 29.17 percent (2013-14) to 11.28 percent (2022-23), "about 24.82 crore people escaping poverty"; Uttar
  Pradesh 5.94 crore, Bihar 3.77 crore, Madhya Pradesh 2.30 crore.
- p. 1: argues monetary measures miss state provision (subsidised grain, sanitation, free education and health).
- p. 3: actual survey estimates: 55.34 percent (2005-06) → 24.85 percent (2015-16) → 14.96 percent (2019-21); intensity 54.96 → 47.14
  → 44.39 percent; MPI value 0.304 → 0.117 → 0.066.
- p. 4: headcount fell 7.7 percent a year (compound) 2005-06 to 2015-16 and faster after; 13.5 crore escaped 2015-16 to 2019-21; rural
  32.59 → 19.28 percent, urban 8.65 → 5.27 percent.
- p. 5: cites PIP: $2.15 (2017 PPP) poverty 18.73 percent (2015) → 11.9 percent (2021); India expected to reach "single digit level of
  poverty by the year 2024-25" (the conclusion, p. 10, says "during 2024").
- pp. 9–10: credits schemes: NFSA grain to 81.35 crore people; free grain under PMGKAY for five years from 1 January 2024; Ujjwala 10
  crore LPG connections; Jal Jeevan Mission 14 crore tap connections; 11.33 crore rural household latrines; over 50 crore Jan Dhan
  accounts; over 4 crore PM Awas homes. Conclusion links progress to Viksit Bharat @2047.
- Caution for the book: the headline 24.82 crore compares two modelled years, not two surveys.

### DV-IN-2. Government of India, Ministry of Finance, *Economic Survey 2025-26*, Chapter 13 "Rural Development and Social Progress: From Participation to Partnership" and Chapter 11 "Education and Health: What Works and What's Next", January 2026
Listing: https://www.indiabudget.gov.in/economicsurvey/ (chapter list). PDFs: https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap13.pdf
(35 PDF pages; printed p. 513 = PDF 1) and https://www.indiabudget.gov.in/economicsurvey/doc/eschapter/echap11.pdf (48 PDF pages; printed
p. 419 = PDF 1). Read: ch. 13 pp. 513–516 and para 13.94 (p. 547); ch. 11 paras 11.15–11.16 (pp. 426–427) and 11.35–11.36 (p. 442), Box
XI.9. (Month: the chapter PDFs carry a creation date of 28 January 2026; no release date read in the text.)
- p. 513 (ch. 13 summary): inclusive growth "has yielded measurable gains", "sustained poverty reduction, narrowing inequalities".
- p. 515, para 13.7–13.8: cites the June 2025 IPL revision ($2.15 → $3.00, 2021 prices); with it, India's 2022-23 rates are 5.3 percent
  (extreme) and 23.9 percent (lower-middle-income line) (footnote 2: World Bank India Poverty and Equity Brief, October 2025, based on
  HCES August 2022–July 2023); World Bank MPM 15.5 percent (2022-23); NITI MPI 55.3 percent (2005-06) → 14.96 (2019-21) → est. 11.28.
- p. 515, para 13.9: researchers using the Tendulkar line (footnote 7: Panagariya and More 2025) estimate poverty fell from 21.9
  percent (2011-12) to 4.7 percent (2022-23) and 2.3 percent (2023-24). Paras 13.7–13.9 cite no official government *monetary*
  poverty estimate: the monetary figures are the World Bank's and academics'; the only government figure is NITI Aayog's MPI.
- p. 547, para 13.94: HCES 2023-24 shows "a decline in consumption inequality"; the largest MPCE growth between 2022-23 and 2023-24 was
  among the bottom 5–10 percent in both rural and urban areas.
- p. 442, para 11.35: since 1990 India cut maternal mortality by 86 percent (global 48), under-five mortality by 78 percent (global 61)
  and neonatal mortality by 70 percent (global 54), 1990–2023 (sources: UN MMEIG 2000–2023; UN IGME 2024). Para 11.36: IMR fell from
  40 per 1,000 live births (2013) to 25 (2023) (SRS 2023); Kerala, Manipur, Sikkim and Goa in single digits.
- p. 427, para 11.16: PARAKH Rashtriya Sarvekshan 2024 (formerly NAS) shows "promising recovery post-COVID" in Grade III: 65 percent
  proficient in maths (42 percent in 2021) and 57 percent in language (39 percent).
- Box XI.9: NFHS-5 Rajasthan: 31.8 percent of under-fives stunted, 27.6 underweight, 16.8 wasted.

### DV-IN-3. ASER Centre (facilitated by Pratham), *Annual Status of Education Report (Rural) 2024*, "ASER 2024 National findings" (pp. 46–49 of the report), 2025 (PDF creation date 13 February 2025)
Listing: https://asercentre.org/aser-2024/ (200; links the national findings, the full report ASER_2024_Final-Report_13_2_24-1.pdf,
state 6-pagers and annexures). PDF: https://asercentre.org/wp-content/uploads/2022/12/ASER-2024-National-findings.pdf (4 PDF pages =
printed pp. 46–49). Read: whole extract. (The full report was not downloaded.)
- p. 46: rural household survey of 649,491 children in 17,997 villages across 605 rural districts; the reading and arithmetic tests
  are unchanged since 2006, so years are comparable (pp. 46–47).
- p. 46: enrolment of 6–14-year-olds has been above 95 percent for close to 20 years (98.4 percent in 2022, 98.1 in 2024). Government
  school share 65.6 percent (2018) → 72.9 (2022, the pandemic) → 66.8 (2024).
- p. 46: Std III government-school children who can read a Std II text: 20.9 percent (2018) → 16.3 (2022) → 23.4 (2024), "the highest
  that they have been since the inception of the ASER survey". Std V government: 44.2 → 38.5 → 44.8 percent; private 65.1 → 56.8 →
  59.3. Std VIII government: 69 → 66.2 → 67.5 percent (p. 47).
- p. 47: Std III who can at least subtract: 28.2 percent (2018) → 25.9 (2022) → 33.7 (2024); Std V who can divide: 27.9 → 25.6 →
  30.7; Std VIII arithmetic 44.1 → 44.7 → 45.8 percent. So in 2024 about two-thirds of Std III children could not do a two-digit
  subtraction with borrowing (my arithmetic from 33.7 percent).
- p. 47: 15–16-year-olds not enrolled fell from 13.1 percent (2018) to 7.5 (2022), 7.9 in 2024; girls not enrolled above 10 percent in
  Madhya Pradesh (16.1), Uttar Pradesh (15), Rajasthan (12.7) and others.
- pp. 47–48: first digital-literacy module (ages 14–16): almost 90 percent have a smartphone at home; 36.2 percent of boys vs 26.9
  percent of girls own one; 57 percent of users used it for education in the past week, 76 percent for social media.
- Use for the book: ASER shows a post-COVID recovery to above the 2018 level in the early grades, consistent with PARAKH (DV-IN-2,
  p. 427), but low absolute levels, which fits the WDR 2018 "learning crisis" framing (DV-WB-10) and Learning Poverty (DV-WB-14).

## Synthesis: development, 2000–2026

1. **Extreme poverty: a long fall, then a stall that began before COVID.** In 2000 the Bank counted 1.2 billion people below $1 a day
   (DV-WB-8 PDF 3) and the Millennium Declaration spoke of "more than a billion" (DV-UN-3 para. 11). By 2013 the count was 767 million
   at $1.90 (DV-WB-5 p. 3) and 689 million by 2017 (DV-WB-6 p. 2), but the pace had already halved (about 1 point a year 1990–2015, 0.6
   points 2013–15, half a point 2015–17; DV-WB-6 p. 2; DV-WB-15 p. xiii). COVID added over 70 million in 2020, "the largest one-year
   increase since global poverty monitoring began" (DV-WB-15 p. v). On the June 2025 line ($3.00, 2021 PPP; DV-WB-3) the Bank now
   counts 811 million, 1 in 10, in 2026, "a rate unchanged since 2019" (DV-WB-1 p. vii); had the 2000–13 pace continued, 243 million more
   would have escaped (p. xv). The 3 percent by 2030 goal has "slipped out of reach" (DV-WB-2 foreword); by 2030, 87 percent of the
   extreme poor will be in SSA, fragile states or both (DV-WB-1 p. xv). Most escapees sit just above the line, "one shock away from
   falling back" (DV-WB-1 p. xv); 3.7 billion live below $8.30 (p. vii).
   **Disagreements and cautions:** (a) The line changed twice in the period ($1.90 → $2.15 → $3.00) and each revision raised the counts
   (2022: 713 → 838 million, DV-WB-3; 2025: 677 → 808 million, DV-UN-1 PDF 10): never compare counts across vintages. (b) For 2026 the
   Bank says 811 million (DV-WB-1) and the UN 826 million (DV-UN-2 PDF 10), both about 10 percent, unexplained in either text. (c) The
   2024 PPP report said poverty reduction had resumed (8.5 percent in 2024, below 2019's 8.8; DV-WB-2 p. 1, foreword); the 2026 report,
   on the new line, says the rate has not moved since 2019 (DV-WB-1). (d) Internal slips: PPP 2026 heads its main messages "Ten facts"
   but the overview says "9 facts" (p. 2), and gives 36 percent vs "two in five" for the share of the extreme poor in high-inequality
   economies (pp. xvii, 4); PSP 2020 gives climate poverty by 2030 as "about 100 million" (foreword) and up to 132 million (p. 1).
2. **Inequality: falling between countries, contested within them.** Survey-based Bank data show global inequality narrowing since the
   1990s for the first time since the industrial revolution (global Gini 66.8 → 62.5, 2008–13; DV-WB-5 p. 9) and high-inequality
   economies (Gini > 40) falling from 70 to 42 (2000–24; DV-WB-1 p. vii). COVID reversed convergence in 2020 (DV-WB-15 p. xiii). The World
   Inequality Lab, using tax and national-accounts data, agrees that between-country gaps shrank (ratio about 50x → under 40x) but finds
   within-country gaps "almost doubled, from 8.5x to 15x" (DV-OTH-3 PDF 8); in 2025 the top 10 percent took 53 percent of income and the
   bottom half 8 percent (DV-OTH-2 PDF 5). **Disagreement:** the Bank's surveys show average within-country inequality flat or falling
   since about 2000 (34 → 40 → 39, DV-WB-5 p. 10); WIL shows it rising since 1980. The Bank itself says surveys miss the rich (DV-WB-13).
3. **From MDGs to SDGs.** The Millennium Declaration (8 September 2000) set 2015 targets: halve $1-a-day poverty and hunger, universal
   primary schooling, cut maternal mortality by three-quarters and under-five mortality by two-thirds (DV-UN-3 para. 19). The UN's 2025
   and 2026 SDG reports find only about a third of targets on track or moderately so (35 percent in 2025, 36 percent in 2026; regression
   18 vs 15 percent; DV-UN-1 PDF 4, 6; DV-UN-2 press release), with extreme poverty "just 3 percentage points below its 2015 level"
   (DV-UN-2). Gains to set against this: nearly 1 billion more people with safely managed water, social protection covering over half
   the world "for the first time in history", HIV infections and AIDS deaths down by a third (DV-UN-2 press release).
   **Caution:** the Declaration's mortality baseline is "current rates" (2000), while the international development goals in WDR 2000/01
   used 1990 benchmarks (DV-UN-3; DV-WB-8 PDF 6). The MDG Report 2015 itself was not obtained, so final MDG scores are not in
   these notes.
4. **Health: the clearest success, with a COVID dent.** Under-five deaths fell from 10.1 million (2000) to 4.9 million (2024), "one of
   the success stories of global public health" (DV-UN-4 p. 22); 134 countries have met the SDG child-mortality target (DV-UN-2 PDF 5).
   Life expectancy rose from 67 (2000) to 73 (2019), fell to 71 in 2021 and recovered to 73 by 2022–23; 22.1 million excess deaths in
   2020–23 (DV-UN-4 pp. 3, 39). Progress slowed after 2015 and neonatal deaths are a rising share (DV-UN-4 p. 22).
5. **Education: enrolment won, learning lagging.** WDR 2018: "Schooling is not the same as learning." (DV-WB-10 PDF 15). Learning poverty
   in low- and middle-income countries fell from 61 to 53 percent (2000–15), rose to 57 percent by 2019 and an estimated 70 percent in
   2022 after school closures (DV-WB-14 PDF 7–9).
6. **Aid: up for two decades, then a record collapse.** DAC net ODA (constant 2024 prices) roughly doubled from 82,970 million (2000) to
   the 2020s; grant-equivalent ODA peaked at 229,212 million in 2023, fell 6.1 percent in 2024 and 23.1 percent in 2025 to 165,513 million
   (my calculations from OECD figures; ODA/GNI 0.37 → 0.26 percent; DV-OTH-1). The UN calls 2025's drop the largest ever recorded, back to
   about 2015 levels (DV-UN-2). WIL notes rich economies' net foreign income from poorer ones is about three times development aid
   (DV-OTH-2 PDF 3).
7. **How the WDR's focus moved.** From the poor's own agency (2000/01: opportunity, empowerment, security; DV-WB-8), to equity (2006,
   "doubly good"; DV-WB-9), services, jobs (2013), learning (2018, "first ever devoted entirely to education"; DV-WB-7, DV-WB-10), data
   (2021), to growth strategy for middle-income countries (2024; poverty barely features; DV-WB-11) and AI (2026; DV-WB-12), which opens by
   saying "development progress has dipped to a 75-year low". The Bank's poverty flagship was relaunched as *Poverty, Prosperity, and
   Planet* in 2024, adding climate (DV-WB-2 p. 1), and the 2026 edition centres on jobs (DV-WB-1).
8. **India, part 1: poverty fell fast, measurement was the fight.** There was no official consumption survey between 2011-12 and
   2022-23: the Bank says India "has not published official survey data on poverty since 2011" and used the private CPHS (DV-WB-15 p. 5;
   DV-WB-6 p. 3); PIP took in HCES 2022-23 "after an 11-year gap" and dropped the CPHS estimates (DV-WB-3). On the new data extreme
   poverty ($3.00) fell from 27.1 percent (2011-12) to 5.25 percent (2022-23) and 2.6 percent (2023), and $4.20 poverty from 57.7 to 16.1
   percent, "lifting an estimated 496 million people out of poverty" (DV-WB-3; DV-WB-13 p. 1). NITI's MPI fell from 29.17 to 11.28 percent
   (2013-14 to 2022-23, "about 24.82 crore people escaping poverty"; DV-IN-1), and the Economic Survey cites Panagariya–More's Tendulkar-
   line estimate of 2.3 percent in 2023-24 (DV-IN-2 p. 515).
   **Disagreements and cautions:** (a) NITI's 24.82 crore compares two modelled years, not two surveys (DV-IN-1 pp. 1, 4). (b) India's
   Gini: 35.7 (2019, CPHS) and about 33 (2021) in earlier briefs, 25.51 in PIP for 2022-23, 23.0 for 2023 in the October 2026 brief
   (DV-WB-13; DV-WB-3); the Bank warns surveys "are likely to understate inequality" and that part of the 2022-23 → 2023-24 gain is
   "better measurement" (DV-WB-13). WIL's Banerjee and Duflo call India "among the most unequal countries in the world" (DV-OTH-3 PDF 4).
   (c) The Economic Survey cites no official government monetary poverty estimate (DV-IN-2 paras 13.7–13.9).
9. **India, part 2: health and learning.** Since 1990 maternal mortality down 86 percent, under-five mortality 78 percent (DV-IN-2 p.
   442); IMR 40 → 25 per 1,000 (2013–2023, SRS). Enrolment of 6–14-year-olds has been above 95 percent for nearly 20 years, and post-COVID
   reading and arithmetic recovered above 2018 levels (Std III government-school reading 23.4 percent in 2024, the highest since ASER
   began), but only a third of Std III children can do a two-digit subtraction (DV-IN-3 pp. 46–47; also PARAKH, DV-IN-2 p. 427; WDR 2018's
   rural-India example, DV-WB-10 PDF 15). During COVID India reached 85 percent of rural households with food or cash support (DV-WB-15
   p. v).

Candidate quotes (all verified in the converted text, under 15 words):
- "a rate unchanged since 2019" (PPP 2026, DV-WB-1 p. vii)
- "Progress against extreme poverty has come to a standstill" (PPP 2026, DV-WB-1 p. 1)
- "The slowdown predates the pandemic" (PPP 2026, DV-WB-1 p. 1)
- "one shock away from falling back" (PPP 2026, DV-WB-1 p. xv)
- "shaping up to be a lost decade" (PPP 2024, DV-WB-2 foreword)
- "has suffered its worst setback in decades" (PSP 2020, DV-WB-6 p. 1)
- "the largest one-year increase since global poverty monitoring began" (PSP 2022, DV-WB-15 p. v)
- "We face a global development emergency." (SDG Report 2025 foreword, DV-UN-1 PDF 4)
- "collapsed by a record 23 per cent in 2025" (SDG Report 2026 foreword, DV-UN-2 PDF 5)
- "freeing the entire human race from want" (Millennium Declaration para. 11, DV-UN-3)
- "one of the success stories of global public health" (WHO WHS 2026, DV-UN-4 p. 22)
- "Schooling is not the same as learning." (WDR 2018, DV-WB-10 PDF 15)
- "This learning crisis is a moral crisis" (WDR 2018, DV-WB-10 PDF 15)
- "doubly good" (WDR 2006 on equity and poverty, DV-WB-9 PDF 2)
- "abysmally low expectations" (WDR 2024, DV-WB-11 p. 1)
- "development progress has dipped to a 75-year low" (WDR 2026 foreword, DV-WB-12 PDF 9)
- "lifting an estimated 496 million people out of poverty" (India PEB October 2026, DV-WB-13 p. 1)
- "has not published official survey data on poverty since 2011" (PSP 2022 box O.2, DV-WB-15 p. 5)
- "India is now among the most unequal countries in the world" (WIR 2022 foreword, DV-OTH-3 PDF 4)
- "promising recovery post-COVID" (Economic Survey 2025-26 on PARAKH, DV-IN-2 p. 427)

## Not obtained

- UN SDG report listing https://unstats.un.org/sdgs/report/ — HTTP 403 (the 2025 and 2026 issue pages under it returned 200 and were used,
  DV-UN-1/2).
- MDG Report 2015 (final MDG assessment): https://www.un.org/millenniumgoals/ and https://www.un.org/millenniumgoals/reports.shtml — 403;
  https://www.undp.org/publications/millennium-development-goals-report-2015 and
  https://www.undp.org/sites/g/files/zskgke326/files/publications/MDG%20Report%202015.pdf — 403;
  https://unstats.un.org/unsd/mdg/Default.aspx redirected to mdgs.un.org, a wiki page, not the report;
  https://mdgs.un.org/unsd/mdg/Resources/Static/Products/Progress2015/English2015.pdf and
  https://unstats.un.org/unsd/mdg/Resources/Static/Products/Progress2015/English2015.pdf — 404. Final MDG scorecard not in these notes.
- Millennium Declaration HTML https://www.un.org/millennium/declaration/ares552e.htm — 403 (the PDF via documents.un.org was used,
  DV-UN-3). https://www.un.org/sustainabledevelopment/progress-report/ — 403.
- UN IGME *Levels and Trends in Child Mortality* report: https://childmortality.org/ is a JavaScript app (no report links in HTML);
  https://childmortality.org/analysis — 404; https://childmortality.org/wp-content/uploads/ — 403;
  https://data.unicef.org/resources/ and https://data.unicef.org/resources/levels-and-trends-in-child-mortality-2025/ (guessed) —
  Cloudflare "Just a moment..." 403; https://www.unicef.org/reports?search=child%20mortality — 200 but no IGME report listed; a guessed
  WHO IRIS IGME item — 404. Child-mortality figures taken from WHO WHS 2026 (DV-UN-4), which cites IGME.
- OECD ODA pages: https://www.oecd.org/en/topics/official-development-assistance-oda.html,
  https://www.oecd.org/en/data/insights/data-explainers/2024/04/official-development-assistance-oda.html, https://one.oecd.org/ and
  https://data-explorer.oecd.org/ — Cloudflare 403. OECD's own 2024/2025 preliminary-ODA press releases not read; figures from the
  SDMX API instead (DV-OTH-1; first query returned 403 "Not enough key values", fixed with a full key).
- UN DESA Financing for Sustainable Development Report: https://financing.desa.un.org/ — HTTP 405 (human-verification page).
- WDR 2024 full report: https://bit.ly/WDR2024_FullReport_ENG led to an OKR "OKR ::Login" page; overview and summary used (DV-WB-11).
- WIR 2026 full report https://wir2026.wid.world/www-site/uploads/2026/09/World_Inequality_Report_2026.pdf: listed but not read
  (Executive Summary used, DV-OTH-2).
- World Bank Poverty & Equity Brief country table: the Datawrapper chart https://datawrapper.dwcdn.net/AKPr7/ (versions /34/ and /35/
  dataset.csv read); later versions (/36/ and above) — 404. No 2025 India brief found by the Documents API (the October 2026 brief was
  reached via the Datawrapper link; the Economic Survey cites an October 2025 brief, not read).
- NITI Aayog listings: https://www.niti.gov.in/whats-new and https://www.niti.gov.in/documents/discussion-paper — 404 (the MPI paper
  was found via site search, DV-IN-1). NITI's 2021 baseline National MPI report
  (http://www.niti.gov.in/sites/default/files/2023-02/National_MPI_India-11242021_0.pdf) not read.
- MoSPI HCES 2022-23 and 2023-24 factsheets (MPCE, Gini): https://www.mospi.gov.in/ is a JavaScript single-page app; the HCES theme route
  /themes/product/71-household-consumption-expenditure-survey-hces is rendered client-side; the API
  https://www.mospi.gov.in/api/main-site/product-search?search=HCES — HTTP 403. HCES findings in these notes come only via the World
  Bank (DV-WB-3, DV-WB-13) and the Economic Survey (DV-IN-2 p. 547). PIB press releases on HCES not tried. No fetched source explains
  why no survey was published between 2011-12 and 2022-23.
- NFHS-5 India fact sheet: https://rchiips.org/nfhs/factsheet_NFHS-5.shtml (guessed) — curl exit, no response (HTTP 000);
  http://rchiips.org/nfhs/factsheet_NFHS-5.shtml — 404. SRS bulletin not tried. India health figures via the Economic Survey (DV-IN-2).
- Planning Commission 2014 Rangarajan report and 2013 Tendulkar-line press note: https://planningcommission.nic.in/reports/genrep/pov_rep0707.pdf
  and https://planningcommission.nic.in/news/pre_pov2307.pdf (both guessed) — curl exit 6 (host not resolved). The 21.9 percent 2011-12
  figure appears only as cited by the Bank (DV-WB-13, Oct 2022 brief) and the Economic Survey (DV-IN-2 p. 515).
- Economic Survey 2024-25 social chapter: not tried (2025-26 used).
- ASER 2024 full report (https://asercentre.org/wp-content/uploads/2022/12/ASER_2024_Final-Report_13_2_24-1.pdf): listed, not
  downloaded (national findings used, DV-IN-3).
- Guessed URLs used (flagged in entries): the Learning Poverty page (DV-WB-14), the October 2022 India PEB databankfiles URL (DV-WB-13),
  the OECD SDMX query (DV-OTH-1).
- rbidocs.rbi.org.in: not tried (known to refuse connections).
