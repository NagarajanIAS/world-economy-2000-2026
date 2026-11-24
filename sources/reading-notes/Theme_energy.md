# Reading notes: theme chapter "Energy, commodities and climate, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers). URLs were taken from publisher listing
or issue pages (openknowledge.worldbank.org via its search and item/bundle APIs; imf.org WEO listing, WEO issue pages and the 2006 WEO index
pages; treaties.un.org; docs.un.org / documents.un.org for the UNFCCC decision; climate.copernicus.eu; wmo.int; globalcarbonbudget.org;
ember-energy.org; fao.org; fred.stlouisfed.org; eia.gov; pib.gov.in; ppac.gov.in); any guessed URL is flagged. Downloads are in the session
scratchpad folder `energy_dl/` (subfolders `wb/`, `imf/`, `oth/`, `in/`). PDFs were converted with `pdftotext` (plain and `-layout`) and read in
the text; HTML pages were stripped of tags and read as text. Economic Survey texts were not refetched: they were read from the Econ Subject
folder (`sources/text/es*.txt`; the number of form feeds equals the PDF page count for every Survey used, so text page = PDF page) and the
printed page number was taken from the running header or footer on that page. Quotes are verbatim, under 15 words, and were checked by a
script against the converted text; everything else is paraphrase. Page numbers are printed page numbers unless stated (PDF page numbers are
marked "PDF"). Oil-price levels not stated in a report were computed by me from the FRED copies of the EIA daily spot series (EN-OTH-10) and
are marked "own calculation".

Item labels: EN-WB-n (World Bank), EN-IMF-n (IMF), EN-OTH-n (UNFCCC/UN, IPCC, C3S, WMO, NASA, Global Carbon Project, Ember, FAO, EIA/FRED,
other), EN-IN-n (India). Indian years are fiscal or survey years (2022-23, FY26). CMO = Commodity Markets Outlook; GEP = Global Economic
Prospects; WDR = World Development Report; WEO = World Economic Outlook; EMDE = emerging market and developing economy; mb/d = million barrels
a day; NDC = nationally determined contribution; ETS = emissions trading system; OMC = oil marketing company; LNG = liquefied natural gas.

Note on the Middle East war of 2026: the sources date its start differently in wording. The IMF (April 2026) says the conflict has engulfed
the Middle East "since the end of February" (EN-IMF-5); the World Bank's October 2026 special focus says "late February 2026" (EN-WB-7 p. 56);
the IMF commodity feature says oil shipments through the Strait of Hormuz stopped in March (EN-IMF-6). No source read here names the exact
day; the daily Brent series jumps from $71.32 (27 February) to $77.24 (2 March) (EN-OTH-10, own reading of the series).

---

## World Bank

### EN-WB-1. World Bank, *World Development Report 2010: Development and Climate Change*, Overview "Changing the Climate for Development", 2010 (OKR item dated 2010)
Listing: OKR item https://hdl.handle.net/10986/4387 (found via the OKR search API
https://openknowledge.worldbank.org/server/api/discover/search/objects). Overview PDF ("9780821379875_overview.pdf"):
https://openknowledge.worldbank.org/bitstreams/a08836eb-7d78-5987-8cdf-548f4fb09352/download (36 PDF pages; printed p. 1 = PDF 2, printed =
PDF − 1). Read: overview pp. 1–4, 10, 22, grepped the rest.
- p. 1: thirty years ago half the developing world lived in extreme poverty, now a quarter; the number of hungry people passed one billion
  that year for the first time. At current rates warming could reach 5°C or more by century's end; even best efforts are unlikely to hold
  warming below 2°C. Developing countries' average per capita emissions are a third of high-income countries'; existing technologies could
  cut energy use in industry and power by 20–30 percent.
- p. 2: global subsidies to petroleum products about $150 billion a year, against public energy RD&D of about $10 billion; high-income
  countries, with one-sixth of the world's population, are responsible for nearly two-thirds of the greenhouse gases in the atmosphere.
- p. 4: the world has already warmed by close to 1°C since the start of the industrial period; slogan of the report: "Act now, act together,
  act differently".
- p. 10: holding warming around 2°C would require 2050 emissions 50 percent below 1990 levels.
- p. 22: mitigation costs in developing countries could reach $140–175 billion a year by 2030 (financing needs $265–565 billion), against
  mitigation finance of about $8 billion a year to 2012; adaptation could need $30–100 billion a year against under $1 billion now.

### EN-WB-2. World Bank, *Global Economic Prospects 2009: Commodities at the Crossroads*, 2009 (OKR item dated 2009)
Listing: OKR item https://hdl.handle.net/10986/2581 (OKR search API). PDF ("468200REPLACEM10Box334115B01PUBLIC1.pdf"):
https://openknowledge.worldbank.org/bitstreams/2b80a404-e8f8-5aa1-9dd5-ef7e87a467b1/download (202 PDF pages; overview p. 3 = PDF 20,
printed = PDF − 17). Read: contents, overview pp. 3–4, 11, chapter 2 opening p. 51.
- p. 3 (PDF 20): the five-year rise in commodity prices came with strong growth, loose policy and uncertainty; "This most recent boom has been
  the most marked of the past century" in magnitude, duration and breadth (figure O.1: "the largest and longest of any boom since 1900").
- p. 51 (PDF 68): before prices fell in the second half of 2008, real energy and metal prices more than doubled in five years and real traded
  food prices rose 75 percent; average commodity prices doubled in dollar terms; the boom ended, like earlier ones, when global growth slowed.
  Low prices in the 1980s–90s and idle capacity had deterred investment, explaining the weak supply response.
- p. 11 (PDF 28): food prices rose between 2005 and early 2008 enough to raise extreme poverty by 1 or more percentage points in East Asia,
  the Middle East and South Asia. Figure list: metal intensities have "reversed in China since 1993" and are much higher there than elsewhere.

### EN-WB-3. World Bank, *Global Economic Prospects, January 2015: Having Fiscal Space and Using It*, Chapter 4 essay "Understanding the Plunge in Oil Prices: Sources and Implications" (team led by John Baffes, Ayhan Kose, Franziska Ohnsorge and Marc Stocker), 13 January 2015
Listing: OKR item https://hdl.handle.net/10986/20758 (OKR search API). PDF ("9781464804441.pdf"):
https://openknowledge.worldbank.org/bitstreams/b2fde618-adbc-551b-93b4-e3e7b1811861/download (217 PDF pages; p. 159 = PDF 181,
printed = PDF − 22). Read: pp. 159–161.
- p. 159: oil prices fell sharply in the second half of 2014, ending four years of stability around $105 a barrel; the fall, much larger
  than in non-oil commodity indices since their early-2011 peaks, "may signal an end to a price “supercycle”". Footnote: since 2000 monthly
  average oil prices peaked at an all-time high of $133 (July 2008). Parallel drawn with 1985–86, when Saudi Arabia switched to defending
  market share and oil fell 61 percent in seven months.
- p. 160: since 2011 US shale oil output has surprised on the upside, by some 0.9 mb/d (about 1 percent of world supply) in 2014; projected
  2015 demand was cut by 0.8 mb/d between July and December 2014; oil intensity of world GDP has almost halved since the 1970s. In late
  November 2014 OPEC failed to agree cuts, signalling a shift from a price band to market share.
- p. 161: the dominant factor was supply (US output, receding disruption fears, OPEC's switch); a 10 percent dollar appreciation is
  associated with an oil-price fall of between about 3 and 10 percent in the literature.
- p. 159 (chapter opening): oil prices expected to stay low in 2015 and rise only marginally in 2016.

### EN-WB-4. World Bank, *Global Economic Prospects, January 2016: Spillovers amid Weak Growth*, Chapter 3 on spillovers from major emerging markets, 6 January 2016
Listing: OKR item https://hdl.handle.net/10986/23435 (OKR search API; the item title in the API is "Global Economic Prospects, January 2016").
PDF ("9781464806759.pdf"): https://openknowledge.worldbank.org/bitstreams/e84a15ae-c750-5722-9414-45df4eb3fb93/download (286 PDF pages;
p. 186 = PDF 210, printed = PDF − 24). Read: pp. 186, 193 and a passage in ch. 1 (PDF 71).
- p. 186 (box on commodity linkages): "The commodity super-cycle, however, began to unwind in early 2011" as new capacity came on stream while
  growth in major emerging markets tilted away from commodity-intensive industry; oil was held up for a time by OPEC.
- p. 193: China accounts for 30 percent or more of world demand for copper, iron ore, nickel, aluminum and soybeans.
- PDF 71 (ch. 1): with the turn in the commodity supercycle, industry investment spending has dropped sharply; hydrocarbon projects face a
  risk of "stranded assets" as climate policy shifts demand.

### EN-WB-5. World Bank, *Commodity Markets Outlook, April 2020*, 23 April 2020 (OKR issue date)
Listing: OKR item https://hdl.handle.net/10986/33624 (OKR search API). PDF ("CMO-April-2020.pdf"):
https://openknowledge.worldbank.org/bitstreams/36dec260-78fe-5cee-a2ab-e7d201765ed1/download (100 PDF pages; p. 1 = PDF 9, printed = PDF − 8).
Read: executive summary pp. 1–2, special focus p. 11, energy pp. 19–20, box on OPEC+ (PDF 37).
- p. 1: COVID-19 mitigation measures caused an unprecedented fall in oil demand; crude expected to average $35/bbl in 2020 and $42 in 2021.
  Crude averaged $32/bbl in March, down 50 percent from January. "Prices reached a historic low in April with some benchmarks trading at
  negative levels"; travel and transport are about two-thirds of oil demand.
- p. 11 (special focus): the largest one-month fall in oil prices on record, one and a half times the previous record (paraphrase; the
  converted text breaks the hyphen).
- p. 20 and PDF 37: the temporary fall in WTI to negative levels was an early sign of storage pressures; OPEC+ agreed in mid-April a
  historically large cut of 9.7 mb/d, but prices fell to historic lows anyway.

### EN-WB-6. World Bank, *Commodity Markets Outlook, October 2022*, 26 October 2022, and its Special Focus "Pandemic, war, recession: Drivers of aluminum and copper prices"
Listing: OKR item https://hdl.handle.net/10986/38160 (OKR search API). Full PDF ("CMO-October-2022.pdf"):
https://openknowledge.worldbank.org/bitstreams/813e7ba3-332f-55f0-a857-85c2cc773d7a/download (50 PDF pages; p. 1 = PDF 9). Special focus PDF:
https://openknowledge.worldbank.org/bitstreams/d35940a5-0f3e-5835-81c7-24f7d134c62c/download (10 PDF pages). Read: executive summary pp. 1–3,
special focus PDF 1–3, 8.
- p. 1: energy prices volatile since the war in Ukraine began; "Natural gas prices in Europe reached all-time highs in August 2022" as
  countries rebuilt stocks and Russian flows fell; over the past four quarters European gas and seaborne coal prices averaged 420 and 180
  percent above their five-year averages. Brent fell nearly 6 percent in dollars from February to September 2022, yet almost 60 percent of
  oil-importing EMDEs saw domestic-currency oil prices rise.
- p. 2: energy prices expected to surge 60 percent in 2022, then fall 11 percent in 2023 and 12 percent in 2024; Brent forecast $100/bbl in
  2022, $92 in 2023, $80 in 2024.
- p. 3: high gas prices may force a shift in industrial models in Northern Europe and could cut EU emissions; Russia's exports could be up to
  2 mb/d lower next year under the EU embargo; the G7 price cap is "an untested mechanism" (paraphrase).
- Special focus PDF 3, 8: more metal price volatility can be expected as the energy transition shifts demand from fossil fuels to metals; the
  war is likely to accelerate the transition.

### EN-WB-7. World Bank, *Commodity Markets Outlook, October 2026*, 28 October 2026 (OKR issue date), with Special Focus "Commodity Price Connections: How Does Volatility Spread?"
Listing: OKR item https://hdl.handle.net/10986/45735 (OKR search API). Full PDF ("CMO-October-2026.pdf"):
https://openknowledge.worldbank.org/bitstreams/1c9dc022-37f3-4d4f-95be-1e353b232a8c/download (70 PDF pages; p. 1 = PDF 9, printed = PDF − 8).
Special focus PDF: https://openknowledge.worldbank.org/bitstreams/4ae4bae8-2fb7-41a8-8c1e-95f321eb9794/download. Read: executive summary
pp. 1–5, energy pp. 14–16, fertilizers p. 39, metals pp. 41–43, special focus p. 56.
- p. 1: "The Middle East conflict has dealt a historic shock to energy supplies"; also Black Sea grain disruption, Russian refining damage, a
  very strong El Niño. Commodity prices forecast up 23 percent in 2026, to their second-highest level since 2013; energy up 32 percent; Brent
  to average $91/bbl in 2026 and $79 in 2027 (adverse case $105 in 2027). World oil production to fall more than 5 percent; oil demand to fall
  2.5 percent, the third-largest drop after 2020 and 1980. Brent futures reached about $110 in mid-October. Inventories drawn by about 2.4 mb/d
  from March to September.
- p. 2: IEA members agreed in early October to release 100 million barrels; European gas prices nearly tripled from pre-conflict levels by
  mid-October; LNG shipments through Hormuz about a quarter of pre-conflict cargoes.
- p. 3: metals index up 31 percent this year; aluminum, copper and tin hit records; "structural conditions for a sustained spell of elevated
  base metal prices" are in place as investment shifts to metal-intensive sectors.
- p. 5 (figure 4.F): drivers of future metal demand split into core economy, energy transition, AI and data centers, and defense; oil demand
  in 2027 to lag its 2010–19 trend by more than 9 percent, partly because faster EV adoption has a lasting effect.
- p. 14: European gas prices to rise almost 60 percent in 2026; US diesel at records in October. p. 15: restricted transit through Hormuz cut
  world oil production 9.1 mb/d (8.6 percent) y/y in 2026Q2; Saudi Arabia and Iraq lost about 4.4 and 2.1 mb/d; EVs displaced 0.6 mb/d of
  China's oil use; consumption also fell in India. p. 16: OECD government stocks at end-September the lowest in more than three decades; US
  strategic reserve lowest since 1982.
- p. 39: fertilizer index fell 22 percent in 2026Q3, reversing the 2026Q2 surge after the closure of the Strait of Hormuz; China acted as a
  swing urea supplier. p. 56 (special focus): conflict began "in late February 2026"; oil's role in transmitting volatility rose sharply.

### EN-WB-8. World Bank, *State and Trends of Carbon Pricing 2026*, 19 May 2026 (OKR issue date), Executive Summary
Listing: OKR item https://hdl.handle.net/10986/44787 (OKR search API). Executive summary PDF:
https://openknowledge.worldbank.org/bitstreams/f08636ad-9ccc-43e2-b71d-97de6df41183/download (17 PDF pages, unnumbered); full report also
downloaded (https://openknowledge.worldbank.org/bitstreams/9ae836ed-db57-4766-92a5-4616cb1e81f9/download, 76 PDF pages) but only grepped.
Read: foreword and key messages PDF 2–8.
- PDF 2 (foreword): new ETSs and carbon taxes implemented in India, Japan, Mauritania, Serbia and Viet Nam; "There is no single model for
  carbon pricing"; nearly 30 percent of world GHG emissions now covered by 87 policies; EU CBAM in force; Brazil and Türkiye preparing.
- PDF 4: direct carbon pricing covers 29 percent of world emissions; ETS coverage tripled since 2016 (8 to over 24 percent), carbon taxes
  steady at 4–5 percent; 2026 increase driven by national ETSs in India, Japan and Viet Nam; if planned schemes are implemented, nearly
  one-third by 2030; CBAM covers under 0.5 percent of world emissions.
- PDF 6: average carbon price doubled from US$10 to nearly US$21/tCO2e between 2016 and 2026; ETS prices volatile in 2026 since the
  commodity-market disruptions began.
- PDF 8: revenues over US$107 billion in 2025, up from under US$30 billion in 2016, mostly in developed economies.

### EN-WB-9. Kirsten Hund, Daniele La Porta, Thao P. Fabregas, Tim Laing and John Drexhage, *Minerals for Climate Action: The Mineral Intensity of the Clean Energy Transition*, World Bank Climate-Smart Mining Facility, © 2020 (OKR item dated 2023-05-24)
Listing: OKR item https://hdl.handle.net/10986/40002 (OKR search API). PDF:
https://openknowledge.worldbank.org/bitstreams/00c880aa-47e2-4c6f-80fd-db285b40f105/download (112 PDF pages; printed = PDF). Read: executive
summary pp. 11–12.
- p. 11: "A low-carbon future will be very mineral intensive"; under a 2°C scenario production of graphite, lithium and cobalt must rise by
  more than 450 percent by 2050 from 2018 levels; aluminum and copper demand from energy technologies 103 and 29 million tons by 2050; total
  mineral demand to 2050 of 3.1 billion tons (2°C) or 3.5 billion (below 2°C); about 3,000 solar panels per MW of PV.
- p. 12: graphite and lithium output would need to rise nearly 500 percent by 2050 just for energy technologies.

---

## IMF

### EN-IMF-1. IMF, *World Economic Outlook Update, July 2008: Global slowdown and rising inflation*, including Annex "Surging Fuel and Food Prices: Origins, Prospects, and Risks"
Listing: WEO listing https://www.imf.org/en/Publications/WEO → issue page
https://www.imf.org/en/publications/weo/issues/2016/12/31/global-slowdown-and-rising-inflation (title confirmed in page title, July 2008).
PDF: https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2008/update/02/pdf/_0708pdf.pdf (6 PDF pages, page
numbers printed as 1–6). Read: all.
- p. 1: world growth to slow from 5 percent (2007) to 4.1 (2008) and 3.9 (2009); rising energy and commodity prices have pushed up inflation,
  especially in emerging economies; top priority is heading off inflation.
- p. 2: oil prices have risen well above previous record highs in real terms, driven by supply concerns, limited spare capacity and
  inelastic demand; food boosted by poor weather and biofuel demand.
- p. 5 (annex): the boom's origins lie in strong growth in 2003–07, especially commodity-intensive growth in emerging economies; but growth
  alone cannot explain "the broadest and most buoyant commodity price boom since the early 1970s"; supply problems and low short-run price
  responsiveness matter; expected very low spare capacity and tight markets to persist.

### EN-IMF-2. IMF, *World Economic Outlook, October 2020: A Long and Difficult Ascent*, Chapter 3 "Mitigating Climate Change—Growth- and Distribution-Friendly Strategies" (Philip Barrett, Christian Bogmans, Benjamin Carton, Johannes Eugster, Florence Jaumotte (lead), Adil Mohommad, Evgenia Pugacheva, Marina M. Tavares, Simon Voigts)
Listing: WEO listing → issue page https://www.imf.org/en/Publications/WEO/Issues/2020/09/30/world-economic-outlook-october-2020. PDF:
https://www.imf.org/-/media/files/publications/weo/2020/october/english/ch3.pdf (30 PDF pages; p. 85 = PDF 1, printed = PDF + 84). Read:
pp. 85–86, 94, 96, grepped the rest.
- p. 85: an initial green investment push plus steadily rising carbon prices would deliver the needed cuts at reasonable output cost; warming
  about 1°C so far; 2015–19 the warmest five years recorded; net carbon emissions need to reach zero by mid-century.
- p. 86: "Tangible policy responses to reduce greenhouse gas emissions have been grossly insufficient to date"; under unchanged policies
  temperatures could rise a further 2–5°C by 2100; most NDCs judged insufficient.
- p. 94: required carbon prices start at $6–20 a ton, reach $10–40 in 2030 and $40–150 in 2050, with a quarter of revenues returned to
  households.
- p. 96: the package raises world output by about 0.7 percent a year in the first 15 years, then a net drag of about 0.7 percent in 2036–50
  and slightly over 1 percent by 2050, against expected cumulative GDP growth of 120 percent over 30 years. p. 99: co-benefits for India
  0.3 percent of GDP at once and 1.4 percent by 2050.

### EN-IMF-3. IMF, *World Economic Outlook, October 2022: Countering the Cost-of-Living Crisis*, Chapter 1 and Special Feature "Commodity Market Developments and Food Inflation Drivers"
Listing: WEO listing → issue page https://www.imf.org/en/publications/weo/issues/2022/10/11/world-economic-outlook-october-2022 (title
confirmed in page title). PDF: https://www.imf.org/-/media/files/publications/weo/2022/october/english/text.pdf (186 PDF pages; p. 6 = PDF 24,
printed = PDF − 18). Read: ch. 1 pp. 6–7, special feature p. 37.
- p. 6: the EU embargoed Russian coal from August 2022 and announced a seaborne-oil ban from end-2022; Russian pipeline gas to Europe down to
  about 20 percent of its level a year earlier, behind the steep rise in gas prices.
- p. 37: commodity prices rose 19.1 percent between February and August 2022; "Energy—especially natural gas, up 129.2 percent—led the
  increase"; crude surged to $120 in early March after Russia's invasion, fell below $100 in April, back to $120 in early June; Russian oil
  rerouted to China and India at a discount to Brent.

### EN-IMF-4. Simon Black, Antung A. Liu, Ian Parry and Nate Vernon, "IMF Fossil Fuel Subsidies Data: 2023 Update", IMF Working Paper WP/23/169, August 2023
Listing: issue page https://www.imf.org/en/Publications/WP/Issues/2023/08/22/IMF-Fossil-Fuel-Subsidies-Data-2023-Update-537281 (guessed
URL, returned 200; the WP listing was not used). PDF: https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023169-print-pdf.pdf
(32 PDF pages; printed numbers at page foot, e.g. 18 = PDF 20). Read: abstract, executive summary, results p. 18.
- PDF 2 (abstract): "Globally, fossil fuel subsidies were $7 trillion in 2022 or 7.1 percent of GDP"; explicit subsidies more than doubled
  since 2020 but are only 18 percent of the total; nearly 60 percent is undercharging for global warming and local air pollution; 80 percent
  of coal use priced below half its efficient level. Full reform would cut CO2 43 percent below baseline in 2030, raise 3.6 percent of world
  GDP and prevent 1.6 million air-pollution deaths a year.
- PDF 5–6 (executive summary): explicit subsidies rose from $0.5 trillion (2020) to $1.3 trillion (2022), much of it temporary price support.
- p. 18 (PDF 20): by country, China $2.2 trillion, US $760 billion, Russia $420 billion, India $350 billion, EU $310 billion (total explicit
  plus implicit, 2022).

### EN-IMF-5. IMF, *World Economic Outlook, April 2026: Global Economy in the Shadow of War*, Chapter 1 "Global Prospects and Policies"
Listing: WEO listing → issue page https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026 (running head
of the chapter gives the title). PDF: https://www.imf.org/-/media/files/publications/weo/2026/april/english/ch1.pdf (46 PDF pages; printed =
PDF). Read: pp. 1–6.
- p. 1: the economy has withstood a series of shocks, but another—"a military conflict engulfing the Middle East since the end of February"—is
  testing it; commodity-importing EMDEs at risk of being hit harder; China's goods trade surplus hit a record $1.2 trillion (6 percent of
  GDP) in 2025.
- p. 4: reference forecast assumes the conflict lasts a few more weeks with production normalising by mid-2026 (sentence cut at the page
  edge); energy prices to rise 19 percent in 2026, oil 21.4 percent, average petroleum spot price $82 a barrel; gas hit harder than oil;
  near-term prospects worsened by the closure of the Strait of Hormuz.
- p. 5: pre-conflict forecast would have been 3.4 percent world growth in 2026; reference forecast 3.1 percent (2026) and 3.2 (2027).
- p. 6: severe scenario assumes oil (gas) prices 100 (200) percent above the January 2026 forecast from 2026Q2.

### EN-IMF-6. IMF, *World Economic Outlook, April 2026*, Commodity Special Feature "Market Developments and the Economics of Rare Earths" (Christian Bogmans (co-lead), Patricia Gomez-Gonzalez, Jorge Miranda Pinto, Jean-Marc Natal (team lead), Andrea Paloschi)
Listing: same issue page as EN-IMF-5. PDF: https://www.imf.org/-/media/files/publications/weo/2026/april/english/commodityspecialfeature.pdf
(8 PDF pages; p. 31 = PDF 1). Read: pp. 31–34.
- p. 31: "Oil prices increased 57.6 percent between August 2025 and March 2026" to $105.8 a barrel; Hormuz shipments stopped in March,
  curtailing about 8.5 mb/d of crude exports; usually about 20 mb/d (20 percent of world consumption) passes through the strait, 15 mb/d of
  it crude.
- p. 32: metals index up 36.6 percent August 2025–March 2026; gold up 44.4 percent to records above $5,000 an ounce before a sharp correction;
  copper up 29.5 and aluminum 29.8 percent (Middle East about 9 percent of world aluminum output).
- p. 33: China's share of light rare-earth mining fell from 97 percent (2010 peak) to 58 percent (2024), but it holds 88 percent of oxide
  separation and 93 percent of metal refining; near-monopoly in heavy rare earths (98 percent of mining, 97 percent of separation). p. 34:
  China holds 90 percent of permanent-magnet manufacturing.

### EN-IMF-7. IMF, *World Economic Outlook Update, July 2026: Global Economy in Crosscurrents of War and Technology*
Listing: WEO listing → issue page https://www.imf.org/en/publications/weo/issues/2026/07/08/world-economic-outlook-update-july-2026. PDF:
https://www.imf.org/-/media/files/publications/weo/2026/update/july/english/text.pdf (15 PDF pages, unnumbered). Read: PDF 2–3.
- PDF 2: world growth 3.0 percent in 2026, 3.4 in 2027; the Middle East war is a negative supply shock partly offset by an AI-driven
  technology upturn; energy importers outside the technology value chain (many low-income countries) weaken; headline inflation up from 4.1
  (2025) to 4.7 percent (2026), so "the disinflation trend in place since the beginning of 2024 has stalled".
- PDF 3: ceasefires and an Iran–US memorandum of understanding cooled prices from April peaks; energy prices about 25 percent above prewar;
  futures imply an average petroleum price of $78 a barrel for 2026 versus $82 assumed in April.

---

## UN/UNFCCC, IPCC, C3S, WMO, NASA, Global Carbon Project, Ember, FAO, EIA/FRED

### EN-OTH-1. *Paris Agreement*, adopted 12 December 2015 (UN certified true copy, Treaty Series chapter XXVII-7-d)
Listing: UN Treaty Collection page https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XXVII-7-d&chapter=27&clang=_en (200). PDF:
https://treaties.un.org/doc/Treaties/2016/02/20160215%2006-03%20PM/Ch_XXVII-7-d.pdf (174 PDF pages, all languages; English text on PDF
29–30; the English text's own page "-3-"). The UNFCCC copy was blocked (see Not obtained). Read: Articles 2–4 (English).
- Art. 2.1(a): aim of "Holding the increase in the global average temperature to well below 2°C above pre-industrial levels" and pursuing
  efforts to limit it to 1.5°C; 2.1(c) making finance flows consistent with low-emission development; 2.2 equity and common but
  differentiated responsibilities.
- Art. 4.1 (printed as "Article 23" in the converted text, an OCR artefact): peak emissions as soon as possible and balance sources and sinks
  in the second half of the century; 4.2 each Party shall prepare successive NDCs.

### EN-OTH-2. IPCC, *Climate Change 2023: Synthesis Report*, Summary for Policymakers (AR6), 2023
Listing: https://www.ipcc.ch/report/ar6/syr/ returned 403 (Cloudflare challenge). PDF fetched from a guessed URL on the same site:
https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf (200; 42 PDF pages; SPM p. 4 = PDF 10, printed = PDF − 6). Read:
A.1–A.4, B.1, C.1, grepped C.3.
- p. 4 (A.1): human activities "have unequivocally caused global warming", with surface temperature 1.1°C above 1850–1900 in 2011–2020.
  A.1.3: cumulative net CO2 1850–2019 of 2400 ± 240 GtCO2, about 42 percent of it since 1990. A.1.4: net GHG emissions 59 ± 6.6 GtCO2-eq in
  2019, 12 percent above 2010 and 54 percent above 1990.
- p. 5 (A.2.2): 3.3 to 3.6 billion people live in highly vulnerable contexts.
- p. 11 (A.4): 2010–2019 unit costs fell 85 percent for solar, 55 percent for wind and 85 percent for lithium-ion batteries; solar deployment
  rose more than 10× and EVs more than 100×.
- p. 12 (B.1): best estimate of reaching 1.5°C in the near term in the scenarios considered. p. 24 (C.1): "a rapidly closing window" of
  opportunity (paraphrase with phrase).

### EN-OTH-3. UNFCCC, Decision 1/CMA.5 "Outcome of the first global stocktake", in FCCC/PA/CMA/2023/16/Add.1 (Report of the CMA on its fifth session, United Arab Emirates, 30 November–13 December 2023; document dated 15 March 2024)
Listing: UN document system https://undocs.org/FCCC/PA/CMA/2023/16/Add.1 → https://docs.un.org/en/FCCC/PA/CMA/2023/16/Add.1 (200). PDF:
https://documents.un.org/api/symbol/access?s=FCCC/PA/CMA/2023/16/Add.1&l=en&t=pdf (51 PDF pages; printed = PDF). Read: paras 1–32.
- p. 3 (paras 3–5): reaffirms the Paris goal; impacts much lower at 1.5°C than 2°C; serious concern that 2023 is set to be the warmest year
  on record.
- p. 5 (paras 25–27): historical cumulative CO2 already about four-fifths of the 50-percent 1.5°C carbon budget; 1.5°C pathways need cuts of
  43 percent by 2030 and 60 percent by 2035 from 2019 and net-zero CO2 by 2050; emissions projected to peak before 2025 in such pathways,
  not necessarily in all countries.
- p. 6 (para 28): calls on Parties to contribute, in a nationally determined manner, to: (a) "Tripling renewable energy capacity globally" and
  doubling the rate of efficiency gains by 2030; (b) phase-down of unabated coal power; (d) "Transitioning away from fossil fuels in energy
  systems", in a just, orderly and equitable manner, to reach net zero by 2050; (h) phasing out inefficient fossil fuel subsidies. Para 29:
  transitional fuels can play a role. Para 30: unit costs of wind, solar and storage have fallen continuously.

### EN-OTH-4. Copernicus Climate Change Service (C3S)/ECMWF, *Global Climate Highlights 2025*, published 14 January 2026 (updated 28 January 2026)
Listing: https://climate.copernicus.eu/global-climate-highlights-2025 (200). PDF:
https://climate.copernicus.eu/sites/default/files/custom-uploads/GCH-2025/GCH2025-full-report.pdf (39 PDF pages; printed page = PDF − 2).
Read: pp. 4–7, 10, 36 (grep).
- p. 5: 2025 surface air temperature +0.59°C vs 1991–2020, i.e. +1.47°C above pre-industrial, third highest (2024 +0.72, 2023 +0.60 vs
  1991–2020).
- p. 7: 2025 was marginally cooler than 2023, while "2024 remains the warmest year on record" and the first year clearly above 1.5°C.
- p. 10: the 2023–2025 average exceeded 1.5°C (1.52°C ERA5, 1.50°C JRA-3Q): "This is the first three‑year average to do so in the
  instrumental period"; all of 2015–2025 are the 11 warmest years.
- p. 36: the C3S trend monitor points to crossing the 1.5°C long-term level in 2029; cites WMO's 70 percent chance that the 2025–29 average
  exceeds 1.5°C.

### EN-OTH-5. NASA, "Temperatures Rising: NASA Confirms 2024 Warmest Year on Record", news release, 10 January 2025
Listing/URL: https://www.nasa.gov/news-release/temperatures-rising-nasa-confirms-2024-warmest-year-on-record/ (guessed URL, 200; date from page
metadata). Read: whole release.
- 2024 was 1.28°C above NASA's 1951–1980 baseline and about 1.47°C above 1850–1900, topping 2023; 15 consecutive monthly records June 2023–
  August 2024; the annual average may have exceeded 1.5°C for the first time, within uncertainty. Administrator: "2024 was the hottest year
  since record keeping began in 1880". (Note: NASA's 1.47°C for 2024 differs from C3S's ranking, which puts 2024 clearly above 1.5°C and 2025
  at 1.47°C; different datasets.)

### EN-OTH-6. WMO, *State of the Global Climate 2025*, one-page summary (March 2026)
Listing: https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025 (200; links the library record
https://library.wmo.int/idurl/4/69807, which is a script page with no PDF link found). PDF read:
https://wmo.int/sites/default/files/2026-03/State%20of%20the%20Climate%202025_1%20pager_final.pdf (200). Read: all.
- "Globally, 2025 was the 2nd or 3rd warmest year on record", 1.43 ± 0.13°C above 1850–1900; CO2 423.9 ppm in 2024, CH4 and N2O at highest
  levels in 800,000 years; ocean heat content at a record in 2025; sea level rose 4.75 mm a year in 2012–2025 vs 2.65 mm in 1993–2011.

### EN-OTH-7. Global Carbon Project, "Fossil CO2 emissions decrease in 2026" (Global Carbon Budget 2026 press release), 10 November 2026
Listing: https://globalcarbonbudget.org/ and https://globalcarbonbudget.org/news/ (200) → https://globalcarbonbudget.org/fossil-co2-emissions-decrease-in-2026/
(200). The full report (ESSD) and key-messages PDF were not downloaded. Read: whole release.
- Fossil CO2 projected to fall 0.4 percent in 2026 to 38.2 billion tonnes, driven by solar and wind and by the Iran conflict; oil emissions
  down 1.9 percent, gas −0.3, coal +0.6 percent. Total CO2 including land use 43.3 billion tonnes (42.8 last year). Remaining 1.5°C budget 150
  billion tonnes, under four years of emissions. Friedlingstein: "a reduction driven partly by geopolitical shocks is not a sustainable
  climate solution".
- China −0.9 percent (32 percent of world fossil emissions; half of emissions avoided by renewables and EVs are in China); US −1.3; EU −1.5;
  India +4.4 percent, above its 3.5 percent ten-year average. Total CO2 grew 0.3 percent a year in the past decade vs 1.7 percent the decade
  before.

### EN-OTH-8. Ember (Nicolas Fulghum, Wilmar Suarez, Katye Altieri, Kostantsa Rangelova), *Global Electricity Review 2026*, 21 April 2026
Listing/URL: https://ember-energy.org/latest-insights/global-electricity-review-2026/ (200; HTML report). Read: highlights, foreword,
executive summary, key takeaways 1–3.
- Renewables were 33.8 percent of world generation in 2025, overtaking coal ("Renewables overtake coal for first time in the modern era");
  coal fell below a third. Solar met 75 percent of demand growth; low-carbon output rose 887 TWh against demand growth of 849 TWh; fossil
  generation fell 38 TWh (−0.2 percent), the first non-rise since 2020.
- Solar rose a record 636 TWh (+30 percent) to 2,778 TWh, up from 256 TWh in 2015; China had more than half of the world increase in solar
  capacity and generation; solar and wind 22 percent of China's mix. Battery costs fell 20 percent in 2024 and a further 45 percent in 2025.
- India: fossil generation fell in both China and India in 2025, the first time this century; India's renewable growth doubled its previous
  record and it installed more new solar capacity than the United States for the first time.

### EN-OTH-9. FAO, *FAO Food Price Index* page (release of 6 November 2026) and monthly data file
Listing/URL: https://www.fao.org/worldfoodsituation/foodpricesindex/en/ (200). Data: https://www.fao.org/media/docs/worldfoodsituationlibraries/wfs-library/food_price_indices_data.csv?sfvrsn=523ebd2a_85&download=true
(200, CSV, nominal, 2014–2016 = 100). Read: release text and the monthly series.
- October 2026 index 133.9, down 1.2 percent on September, 5.9 percent above a year earlier but 16.4 percent below the March 2022 peak.
- Series (my reading of the CSV): 2000 around 53–55; peak 132.7 in June 2008 (132.4 in March 2008), 86.3 by December 2008; 137.7 in February
  2011; all-time peak 160.2 in March 2022.

### EN-OTH-10. US EIA spot prices via FRED: "Crude Oil Prices: Brent – Europe" (DCOILBRENTEU) and "Crude Oil Prices: West Texas Intermediate" (DCOILWTICO), daily
URLs: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU and ...?id=DCOILWTICO (200; last observation 17 November 2026). The EIA
.xls originals (https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls, RWTCd.xls, both 200) could not be parsed locally. All figures own calculation.
- Brent: 2000 average $28.76; daily peak $143.95 on 3 July 2008 (WTI $145.31 the same day), trough $33.73 on 26 December 2008; 2011–mid-2014
  average $110.24; June 2014 average $111.80, end-2014 $55.27; low $26.01 on 20 January 2016; annual averages $52.3 (2015), $43.6 (2016).
- WTI −$36.98 on 20 April 2020 (Brent's April 2020 low $9.12, 21 April). Brent 2022 daily high $133.18 on 8 March; 2022 average $100.93.
- 2026: Brent February average $70.89; March $103.13; April $117.29; daily high $138.21 on 7 April; October average $123.93; 1 January–17
  November average $96.34. (The World Bank's ~$110 for mid-October refers to front-month futures, which it says lagged physical dated Brent.)

### EN-OTH-11. US EIA, "How much shale (tight) oil is produced in the United States?", FAQ, last updated 28 March 2024
URL: https://www.eia.gov/tools/faqs/faq.php?id=847&t=6 (guessed, 200). Read: whole.
- In 2023 about 3.04 billion barrels (about 8.32 mb/d) of crude came directly from tight-oil resources, about 64 percent of total US crude
  output.

---

## India

### EN-IN-1. Government of India, Ministry of Finance, *Economic Survey 2008-09*, Chapter 9 (Energy, Infrastructure and Communications), paras 9.38–9.39 and Table 9.15 (on disk; not refetched)
Files: `sources/text/es2008-09.txt`; PDF `sources/economic-surveys/Economic Survey 2008-09 (English).pdf` (p. 234 = PDF 235). Read: paras
9.35–9.39, and ch. 7 on industry (PDF 201).
- p. 234: the Indian basket of crude averaged US$79.25/bbl in 2007-08, rose to US$142.04 on 3 July 2008, slumped to US$35.83 on 24 December
  2008 and recovered to US$46.02 in March 2009.
- p. 234 (Table 9.15): OMC under-recoveries ₹40,000 crore (2005-06), ₹49,387 crore (2006-07), ₹77,123 crore (2007-08), ₹1,03,292 crore
  (2008-09), of which diesel ₹52,286 crore in 2008-09; burden shared by oil bonds (59.04 percent in 2008-09) and upstream companies (30.98).
- PDF 201: Indian basket at US$105.77 in April 2008 and US$132.47 by July 2008 (monthly averages).

### EN-IN-2. *Economic Survey 2010-11*, Chapter 4 (Prices and Monetary Management), para 4.7 (on disk)
Files: `sources/text/es2010-11.txt`; PDF `Economic Survey 2010-11 (English).pdf` (pp. 70–71 = PDF 70–71). Read: paras 4.5–4.7; ch. on money
(PDF 96).
- pp. 70–71: kerosene and domestic LPG subsidies continued (schemes extended to 31 March 2014), with PDS kerosene up ₹3 a litre and LPG ₹35 a
  cylinder; prices of petrol and diesel at refinery gate and retail "will be market determined", with diesel increases staggered to protect
  the poor. PDF 96: the administered fuel price revision of 25 June 2010 was expected to add to inflation.

### EN-IN-3. *Economic Survey 2013-14*, Chapters 3 (Public Finance) and 4 (Prices), paras on fuel subsidies (on disk)
Files: `sources/text/es2013-14.txt` (pp. 65, 77 = PDF 65, 77). Read: the subsidy and fuel-inflation passages.
- p. 65: petrol prices decontrolled; diesel raised by ₹0.50 a litre a month; OMC under-recoveries rose from ₹77,123 crore (2007-08) to
  ₹1,39,869 crore (2013-14). p. 77: fuel inflation in double digits for three quarters, from crude prices, rupee depreciation after the May
  2013 taper announcement and administered price revisions.

### EN-IN-4. *Economic Survey 2014-15*, Vol. 1 ch. 1 (p. 38) and Chapter 9 "From Carbon Subsidy to Carbon Tax: India's Green Actions" (pp. 122–124) (on disk)
Files: `sources/text/es2014-15.txt` (p. 38 = PDF 44; p. 122 = PDF 128; p. 124 = PDF 130). Read: ch. 9 pp. 122–124; Box 1.2 (PDF 15).
- PDF 15 (Box 1.2): reforms since May 2014 include deregulating diesel prices and raising gas prices from US$4.2 to US$5.6 per mmBtu.
- p. 122: the steep fall in world oil prices is an opportunity to remove subsidies and shift taxes to carbon; the government decontrolled
  diesel while raising petrol and diesel excise. p. 123: since October 2014 excise duties imposed in a series of steps; coal cess doubled from
  ₹50 to ₹100 a ton.
- p. 38 and p. 124: the actions since October 2014 amount to a "de facto carbon tax equivalent to US$ 60 per ton" of CO2 on (unbranded) petrol
  and nearly US$42 on diesel; India described as the third largest GHG emitter.

### EN-IN-5. Prime Minister's Office, "National Statement by Prime Minister Shri Narendra Modi at COP26 Summit in Glasgow", PIB Delhi, posted 1 November 2021
URL: https://pib.gov.in/PressReleasePage.aspx?PRID=1768712 (guessed PRID, 200; title and date verified on the page). Read: whole statement.
- The five "Panchamrit": non-fossil capacity 500 GW by 2030; 50 percent of energy requirements from renewables by 2030; cut total projected
  emissions by one billion tonnes to 2030; reduce carbon intensity by "less than 45 percent" by 2030 (wording as printed); and "by the year
  2070, India will achieve the target of Net Zero". Says promises on climate finance have proved hollow.

### EN-IN-6. *Economic Survey 2022-23*, Chapter VII "Climate Change and Environment: Preparing to Face the Future", para 7.23 and Box VII.1 (on disk)
Files: `sources/text/es2022-23.txt` (p. 222 = PDF 265). Read: pp. 222–226, list of charts/boxes (PDF 37–42).
- p. 222: "Demonstrating higher ambition in its climate action", India submitted its updated NDC on 26 August 2022, translating the Glasgow
  "Panchamrit"; non-fossil share of installed capacity about 40.4 percent (date printed as "31.09.2022") vs 27.3 percent in 2014-15; solar and
  wind share 8.9 → 25.1 percent.
- Box VII.1: first NDC October 2015 (40 percent non-fossil capacity, 33–35 percent lower emissions intensity of GDP vs 2005, 2.5–3 billion
  tonnes CO2e extra sink); updated NDC: emissions intensity 45 percent lower by 2030 vs 2005 and about 50 percent non-fossil capacity by 2030
  "with the help of" technology transfer and low-cost international finance including the GCF; plus LIFE (Lifestyle for Environment).
- Box VII.2 (p. 229, title only read): "Critical Minerals-Key to Green Transition".

### EN-IN-7. *Economic Survey 2023-24*, Chapter 6 "Climate Change and Energy Transition: Dealing with Trade-offs" (on disk)
Files: `sources/text/es2023-24.txt` (p. 179 = PDF 226; p. 183 = PDF 230; p. 189 = PDF 236). Read: pp. 179–184, 187, 189.
- p. 179: India's per capita carbon emission is about one-third of the world average; net zero by 2070 guides policy. Argues that the world's
  "current approach to dealing with climate change is flawed" because it ignores trade-offs; cites the UK delaying its petrol/diesel car ban
  from 2030 to 2035. p. 180: critical minerals race, with China "indispensable"; the Paris Agreement "trumped" the SDGs (paraphrase).
- p. 183: updated NDC targets (45 percent; 50 percent non-fossil). p. 184: GDP grew about 7 percent a year (CAGR) and emissions about 4
  percent in 2005–2019, i.e. decoupling; cites the IFC calling India the only G20 country in line with 2°C.
- p. 187: primary energy mix in 2022-23 almost 84 percent coal, oil and gas; non-fossil power capacity 45.4 percent in May 2024 vs about 32
  percent in April 2014. p. 189: coal is nearly 70 percent of electricity generation.

### EN-IN-8. *Economic Survey 2025-26*, Chapter 9 (Industry/energy, para 9.42) and Chapter 10 "Environment and Climate Change" (on disk)
Files: `sources/text/es2025-26.txt` (p. 366 = PDF 417; p. 390 = PDF 441; p. 392 = PDF 443; p. 399 = PDF 450); External sector ch. 4 (PDF 214).
Read: paras 9.42, 10.19, 10.35–10.41, 4.41–4.42.
- p. 390: "The country has already surpassed the goal of 50 per cent" non-fossil installed capacity (51.93 percent at end-December 2025);
  38.61 GW of renewables added in 2025-26 to 31 December 2025 (30.16 GW solar); IRENA ranks India fourth in installed renewable capacity
  (after China, the US and Brazil).
- p. 366: April–November FY26 added a record 34.56 GW of non-fossil capacity (27.20 GW solar).
- p. 392: challenges remain, since solar and wind are material-intensive and need costly storage; nuclear opened to private participation
  under the SHANTI Act, 2025. Ch. 10 also introduces the Carbon Credit Trading Scheme (structure only read, PDF 433, 450).
- PDF 214: crude sourcing diversified in FY26 (April–November): shares of the US (8.1 percent from 4.6), Egypt, UAE, Nigeria, Libya up;
  Russia, Saudi Arabia, Iraq, Venezuela down.

### EN-IN-9. Petroleum Planning & Analysis Cell (Ministry of Petroleum and Natural Gas), *Snapshot of India's Oil & Gas data*, November 2026 (file name says October 2026)
Listing: https://ppac.gov.in/ (200). PDF: https://ppac.gov.in/download.php?file=rep_studies/1795087072_Final_Snapshot_of_Indias_Oil_Gas_data_Oct_2026_V2_A5.pdf
(200; 45 PDF pages; table on printed p. 6 = PDF 9). Read: table 2 "Crude oil, LNG and petroleum products at a glance".
- Import dependency of crude oil (consumption basis): 88.3 percent (2024-25), 88.6 (2025-26), 88.1 (April–October 2026-27, provisional); oil
  and gas together 80.0, 80.7, 80.3 percent. Domestic crude output 28.7 → 28.0 million tonnes.
- Crude imports April–October 2026-27: 146.6 million tonnes costing $111.0 billion, against 142.8 million tonnes and $72.3 billion a year
  earlier; petroleum imports 22.9 percent of India's gross imports by value (18.9 a year earlier); net oil and gas imports $97.7 billion vs
  $70.3 billion.

---

## Synthesis

1. **The 2000s boom was the biggest in a century, and China was its engine.** The World Bank in 2009 called it "the most marked of the past
   century", with real energy and metal prices more than doubling in five years (EN-WB-2 pp. 3, 51); the IMF in July 2008 traced it to
   commodity-intensive emerging-market growth plus slow supply response (EN-IMF-1 p. 5). China took 30 percent or more of world demand for
   copper, iron ore, nickel, aluminum and soybeans (EN-WB-4 p. 193). Brent rose from about $29 (2000 average) to $143.95 on 3 July 2008 and
   fell to $33.73 by 26 December 2008 (EN-OTH-10).
2. **The supercycle unwound from 2011 and broke in 2014–15.** The World Bank dated the unwinding to early 2011 (EN-WB-4 p. 186) and read the
   2014 oil collapse as the possible end of a "supercycle", driven mainly by supply: US shale surprises, OPEC's switch to market share,
   receding disruption fears (EN-WB-3 pp. 159–161). Brent went from $111.80 (June 2014 average) to $26.01 (20 January 2016) (EN-OTH-10). Tight
   oil was 64 percent of US crude output by 2023 (EN-OTH-11).
3. **Shocks since 2020 came from every direction.** COVID: WTI at −$36.98 on 20 April 2020 and the largest one-month oil fall on record
   (EN-WB-5; EN-OTH-10). 2022: Russia's invasion; European gas at all-time highs in August 2022; natural gas up 129.2 percent February–August
   (EN-WB-6 p. 1; EN-IMF-3 p. 37). 2026: the Middle East war closed the Strait of Hormuz, through which 20 percent of world oil normally passes
   (EN-IMF-6 p. 31); world oil output to fall 5.5 mb/d in 2026, demand to fall 2.5 percent, Brent to average $91 (EN-WB-7 pp. 1, 14); daily
   Brent peaked at $138.21 on 7 April (EN-OTH-10).
4. **Food prices tracked energy.** FAO's index peaked at 132.7 (June 2008), 137.7 (February 2011) and an all-time 160.2 (March 2022); October
   2026 stood at 133.9 (EN-OTH-9). The 2005–08 food spike raised extreme poverty by a point or more in three regions (EN-WB-2 p. 11); in 2026
   the World Bank expects food prices up 10 percent with a strong El Niño and Black Sea disruption (EN-WB-7 p. 1).
5. **Metals and minerals are the new oil.** Minerals for climate action need more than 450 percent more graphite, lithium and cobalt by 2050
   (EN-WB-9 p. 11). By 2026 aluminum, copper and tin hit records, and the World Bank sees structural support for high base-metal prices from
   the energy transition and AI data centres (EN-WB-7 pp. 3, 5). China holds 88–98 percent of rare-earth processing stages (EN-IMF-6 p. 33).
6. **Climate: goals tightened, warming arrived faster.** WDR 2010 thought holding below 2°C unlikely (EN-WB-1 p. 1); Paris set "well below
   2°C" and 1.5°C efforts (EN-OTH-1); IPCC 2023 put warming at 1.1°C for 2011–2020 (EN-OTH-2 p. 4); COP28 called for "Transitioning away from
   fossil fuels in energy systems" and tripling renewables (EN-OTH-3 p. 6). 2024 was the first calendar year clearly above 1.5°C on C3S data
   and 2023–25 averaged 1.52°C (EN-OTH-4); WMO puts 2025 at 1.43 ± 0.13°C (EN-OTH-6). Fossil CO2 may fall 0.4 percent in 2026, partly from the
   war, but the 1.5°C budget is under four years of emissions (EN-OTH-7).
7. **Clean power got cheap, led by China.** Solar unit costs fell 85 percent and batteries 85 percent in 2010–19 (EN-OTH-2 p. 11); battery
   costs fell another 20 and 45 percent in 2024 and 2025; renewables overtook coal in world generation in 2025 at 33.8 percent, with China more
   than half of new solar (EN-OTH-8). Carbon pricing spread (29 percent of emissions covered, average price about $21) but stayed far below
   the IMF's 2020 estimate of $40–150 needed by 2050 (EN-WB-8; EN-IMF-2 p. 94). Fossil fuel subsidies were $7 trillion in 2022, mostly implicit
   (EN-IMF-4).
8. **Finance for developing countries remained the gap.** WDR 2010 put developing-country mitigation costs at $140–175 billion a year by 2030
   against about $8 billion of flows (EN-WB-1 p. 22); Paris made finance flows a goal (EN-OTH-1 Art. 2.1(c)); India made its 50 percent target
   conditional on low-cost international finance and called earlier promises "hollow" (EN-IN-6; EN-IN-5).
9. **India, part 1: oil dependence and the long subsidy exit.** Under-recoveries rose from ₹40,000 crore (2005-06) to ₹1,03,292 crore in
   2008-09 (EN-IN-1) and ₹1,39,869 crore in 2013-14 (EN-IN-3); petrol was freed in 2010 and diesel in October 2014, when excise rises
   amounted to a carbon tax of about US$60/ton on petrol (EN-IN-2, EN-IN-4). Import dependence is still about 88 percent; the 2026 shock
   raised the April–October crude bill from $72.3 billion to $111.0 billion (EN-IN-9).
10. **India, part 2: the non-fossil build-out.** Net zero by 2070 (EN-IN-5); non-fossil capacity rose from 27.3 percent (2014-15) to 40.4
    (2022), 45.4 (May 2024) and 51.93 percent (December 2025), beating the 2030 target early (EN-IN-6, EN-IN-7, EN-IN-8). Yet coal is nearly
    70 percent of generation and 84 percent of primary energy is fossil (EN-IN-7 pp. 187, 189), and the Survey argues the world's climate
    approach ignores trade-offs (EN-IN-7 p. 179). India's fossil generation fell in 2025 (EN-OTH-8) but its CO2 is projected up 4.4 percent
    in 2026 (EN-OTH-7). India launched a national ETS in 2026 (EN-WB-8).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2008 (Jul) | IMF WEO Update (EN-IMF-1) | Very low spare capacity and tight oil markets expected to persist | Brent fell from $143.95 (3 Jul 2008) to $33.73 (26 Dec 2008) (EN-OTH-10) |
| 2009 | GEP 2009 (EN-WB-2) | Boom over as growth slowed; China's metal intensity expected to stabilise then fall | Prices rebounded to 2011 peaks; the supercycle unwound only from 2011 (EN-WB-4) and broke in 2014 (EN-WB-3) |
| 2010 | WDR 2010 (EN-WB-1) | Holding warming below 2°C unlikely; ~1°C warming so far | 2024 the first year clearly above 1.5°C; 2023–25 average 1.52°C (EN-OTH-4) |
| 2015 (Jan) | GEP Jan 2015 (EN-WB-3) | Oil to stay low in 2015 and rise only marginally in 2016 | Brent averaged $52.3 (2015) and $43.6 (2016), low $26.01 in Jan 2016 (EN-OTH-10) |
| 2015 | Paris Agreement (EN-OTH-1) | Peak emissions as soon as possible; well below 2°C | COP28 (2023): emissions trajectories "not yet in line" (para 24, paraphrase); fossil CO2 may fall only 0.4% in 2026, not judged a peak (EN-OTH-7) |
| 2020 (Apr) | CMO Apr 2020 (EN-WB-5) | Brent $35 in 2020, $42 in 2021 | Brent averaged $41.96 (2020) and $70.86 (2021) (EN-OTH-10) |
| 2020 (Oct) | WEO Oct 2020 ch. 3 (EN-IMF-2) | Carbon prices of $10–40 by 2030 and $40–150 by 2050 needed | Average carbon price ~US$21 in 2026, 29% of emissions covered (EN-WB-8) |
| 2020 | Minerals for Climate Action (EN-WB-9) | Transition will be very mineral-intensive | Record aluminum, copper, tin prices in 2026; metals index at all-time high (EN-WB-7) |
| 2022 (Oct) | CMO Oct 2022 (EN-WB-6) | Brent $92 in 2023, $80 in 2024 | Brent averaged $82.49 (2023) and $80.52 (2024) (EN-OTH-10) |
| 2023 | IPCC SYR (EN-OTH-2) | 1.5°C reached in the near term | 2024 above 1.5°C on C3S data; C3S trend monitor projects long-term crossing in 2029 (EN-OTH-4) |
| 2026 (Apr) | WEO Apr 2026 (EN-IMF-5) | Short conflict; petroleum average $82 in 2026 | IMF July: $78 implied (EN-IMF-7); World Bank Oct: Brent $91 (EN-WB-7); Brent Jan–mid-Nov average $96.34 (EN-OTH-10) |
| 2008-09 | ES 2008-09 (EN-IN-1) | Under-recoveries ₹1,03,292 crore, financed mainly by oil bonds | ₹1,39,869 crore by 2013-14 (EN-IN-3); diesel deregulated Oct 2014 (EN-IN-4) |
| 2015 | India's first NDC (EN-IN-6 Box VII.1) | 40% non-fossil capacity by 2030 | 40.4% by Sept 2022; target raised to 50% (Aug 2022); 51.93% by Dec 2025 (EN-IN-6, EN-IN-8) |
| 2021 | COP26 Panchamrit (EN-IN-5) | 500 GW non-fossil and 50% of energy from renewables by 2030; net zero 2070 | Record 34.56 GW non-fossil added in Apr–Nov FY26 (EN-IN-8); but coal ~70% of generation (EN-IN-7) and India's CO2 +4.4% projected for 2026 (EN-OTH-7) |
| 2024-25 | PPAC (EN-IN-9) | Crude import dependence 88.3% | Still 88.1% in Apr–Oct 2026-27; crude bill up from $72.3 bn to $111.0 bn in the 2026 shock (EN-IN-9) |

Candidate quotes (all verified by script against the converted text, under 15 words):
- "Act now, act together, act differently" (WDR 2010, EN-WB-1 p. 4)
- "This most recent boom has been the most marked of the past century" (GEP 2009, EN-WB-2 p. 3)
- "may signal an end to a price “supercycle”" (GEP January 2015, EN-WB-3 p. 159)
- "The commodity super-cycle, however, began to unwind in early 2011" (GEP January 2016, EN-WB-4 p. 186)
- "Prices reached a historic low in April with some benchmarks trading at negative levels" (CMO April 2020, EN-WB-5 p. 1)
- "Natural gas prices in Europe reached all-time highs in August 2022" (CMO October 2022, EN-WB-6 p. 1)
- "The Middle East conflict has dealt a historic shock to energy supplies" (CMO October 2026, EN-WB-7 p. 1)
- "structural conditions for a sustained spell of elevated base metal prices" (CMO October 2026, EN-WB-7 p. 3)
- "There is no single model for carbon pricing" (State and Trends 2026, EN-WB-8 PDF 2)
- "A low-carbon future will be very mineral intensive" (Minerals for Climate Action, EN-WB-9 p. 11)
- "the broadest and most buoyant commodity price boom since the early 1970s" (IMF July 2008, EN-IMF-1 p. 5)
- "Tangible policy responses to reduce greenhouse gas emissions have been grossly insufficient to date" (WEO Oct 2020, EN-IMF-2 p. 86)
- "Energy—especially natural gas, up 129.2 percent—led the increase" (WEO Oct 2022, EN-IMF-3 p. 37)
- "Globally, fossil fuel subsidies were $7 trillion in 2022 or 7.1 percent of GDP" (IMF WP/23/169, EN-IMF-4 PDF 2)
- "a military conflict engulfing the Middle East since the end of February" (WEO April 2026, EN-IMF-5 p. 1)
- "Oil prices increased 57.6 percent between August 2025 and March 2026" (WEO April 2026 CSF, EN-IMF-6 p. 31)
- "the disinflation trend in place since the beginning of 2024 has stalled" (WEO Update July 2026, EN-IMF-7 PDF 2)
- "well below 2°C above pre-industrial levels" (Paris Agreement Art. 2, EN-OTH-1)
- "Transitioning away from fossil fuels in energy systems" (COP28 decision 1/CMA.5 para 28(d), EN-OTH-3 p. 6)
- "Tripling renewable energy capacity globally" (COP28 para 28(a), EN-OTH-3 p. 6)
- "have unequivocally caused global warming" (IPCC AR6 SYR SPM A.1, EN-OTH-2 p. 4)
- "2024 remains the warmest year on record" (C3S GCH 2025, EN-OTH-4 p. 7)
- "This is the first three‑year average to do so in the instrumental period" (C3S, EN-OTH-4 p. 10)
- "Globally, 2025 was the 2nd or 3rd warmest year on record" (WMO, EN-OTH-6)
- "2024 was the hottest year since record keeping began in 1880" (NASA Administrator, EN-OTH-5)
- "a reduction driven partly by geopolitical shocks is not a sustainable climate solution" (Friedlingstein, EN-OTH-7)
- "Renewables overtake coal for first time in the modern era" (Ember, EN-OTH-8)
- "de facto carbon tax equivalent to US$ 60 per ton" (ES 2014-15, EN-IN-4 p. 38)
- "by the year 2070, India will achieve the target of Net Zero" (PM at COP26, EN-IN-5)
- "Demonstrating higher ambition in its climate action" (ES 2022-23, EN-IN-6 p. 222)
- "its current approach to dealing with climate change is flawed" (ES 2023-24, EN-IN-7 p. 179)
- "The country has already surpassed the goal of 50 per cent" (ES 2025-26, EN-IN-8 p. 390)

## Not obtained

- IMF *WEO September 2006*, Chapter 5 "The Boom in Nonfuel Commodity Prices: Can It Last?" (listed on the index page
  https://www.imf.org/external/pubs/ft/weo/2006/02/index.htm, HTTP 200): chapter PDF
  https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2006/02/pdf/_c5pdf.pdf — 404; guessed variant
  http://www.imf.org/external/pubs/ft/weo/2006/02/pdf/c5.pdf — 404. The IMF's 2000s commodity view comes only from the July 2008 Update
  (EN-IMF-1).
- IMF WEO on the 2014–16 oil fall (April 2015 / April 2016 commodity special features): issue pages not found on the WEO listing page read;
  guessed issue URL https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/World-Economic-Outlook-April-2015-Uneven-Growth-Short-and-Long-Term-Factors-42209
  — 404. The 2014–15 story rests on the World Bank (EN-WB-3, EN-WB-4).
- IMF WEO October 2026: not on the WEO listing page (latest listed is the July 2026 Update); guessed issue URL
  https://www.imf.org/en/Publications/WEO/Issues/2026/10/14/world-economic-outlook-october-2026 — 404.
- UNFCCC: https://unfccc.int/process-and-meetings/the-paris-agreement — 200 but an Incapsula bot-check stub (212 bytes);
  https://unfccc.int/sites/default/files/english_paris_agreement.pdf — same stub; https://unfccc.int/sites/default/files/resource/cma2023_16a01E.pdf
  — same stub; NDC registry https://unfccc.int/NDCREG — same stub (837 bytes). Paris and COP28 texts taken from the UN treaty and UN document
  systems instead (EN-OTH-1, EN-OTH-3). India's updated NDC document itself was not read; its contents come from ES 2022-23 Box VII.1
  (EN-IN-6).
- IPCC listing page https://www.ipcc.ch/report/ar6/syr/ — 403 (Cloudflare "Just a moment..."); the SPM PDF came from a guessed URL on the same
  site (EN-OTH-2).
- UNEP *Emissions Gap Report 2025*: https://www.unep.org/resources/emissions-gap-report-2025 — 403; https://www.unep.org/emissions-gap-report-2025
  — 403; https://wedocs.unep.org/bitstream/handle/20.500.11822/48854/EGR2025.pdf (guessed) — 403; https://wedocs.unep.org/handle/20.500.11822/48854
  — 403; https://wedocs.unep.org/server/api/discover/search/objects?query=Emissions%20Gap%20Report%202025 — 403. No emissions-gap figures are in
  these notes.
- IEA *World Energy Outlook 2025*: https://www.iea.org/reports/world-energy-outlook-2025 — 403; *Global Energy Review 2025*:
  https://www.iea.org/reports/global-energy-review-2025 — 403. No IEA document was read; IEA figures appear only as cited by the World Bank and
  IMF.
- IRENA *Renewable Power Generation Costs*: https://www.irena.org/Publications — 403;
  https://www.irena.org/Publications/2025/Jul/Renewable-Power-Generation-Costs-in-2024 (guessed) — 403. Solar/wind/battery cost falls taken from
  IPCC (EN-OTH-2) and Ember (EN-OTH-8).
- WMO full *State of the Global Climate 2025* report: series page https://wmo.int/publication-series/state-of-global-climate-2025 — 404; the
  correct page (200) links https://library.wmo.int/idurl/4/69807 (200, script page, no PDF link extracted). Only the one-page summary was
  read (EN-OTH-6).
- Stern Review: https://webarchive.nationalarchives.gov.uk/ukgwa/20100407172811/https://www.hm-treasury.gov.uk/stern_review_report.htm — 405. Not
  read; no other official copy tried.
- NGFS publications https://www.ngfs.net/en/publications-and-statistics/publications — 403. BIS: nothing relevant identified (one guessed page,
  https://www.bis.org/publ/arpdf/ar2021e3.htm, 200, not on topic, not used).
- Global Carbon Budget 2026 full report (ESSD) and key-messages PDF: not downloaded; only the press release was read (EN-OTH-7).
- Central Electricity Authority installed-capacity report: https://cea.nic.in/installed-capacity-report/?lang=en — 404; the CEA home page
  (200) is a script-driven dashboard with no report PDF link found. Installed-capacity shares come from the Economic Surveys (EN-IN-6 to IN-8).
- PIB release on reaching 50 percent non-fossil installed capacity (2025): not located (no PIB search used); the milestone is taken from ES
  2025-26 (EN-IN-8).
- MNRE physical progress page https://mnre.gov.in/en/physical-progress/ — 200 but a script shell (4.7 KB) with no data.
- EIA daily spot .xls files (RBRTEd.xls, RWTCd.xls) — 200 but not parsable locally (no xlrd); the FRED copies of the same EIA series were used
  (EN-OTH-10).
- Economic Survey 2021-22 and 2024-25 climate/energy passages: grepped only (2021-22 PDF 258 mentions net zero by 2070); not read in full.
