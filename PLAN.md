# PLAN — *The World Economy 2000–2026*

Status: **draft for review** (22 November 2026). Nothing below has been built yet. Step 1 of the brief.

What is already checked, and how, is marked ✔ (fetched this session) or ☐ (to fetch in step 2). Every series code marked ☐ will be confirmed against the live API before a chart uses it. Codes that fail get swapped and logged in `NOTES.md`; they are never guessed.

---

## 1. What the sources say the latest edition is

| Item | Finding | How checked |
|---|---|---|
| Latest WEO | **October 2026, *Resilience Under Strain, Urgent Choices*** (13 Oct 2026). World growth projected at 3.1% in 2026 and 3.4% in 2027. Global headline inflation projected to *rise* to 4.7% in 2026, then 4.1% in 2027. Ch. 1 names "the war in the Middle East" as the main shock, with AI investment as the main support. Data cut-off 30 Sep 2026 | ✔ imf.org WEO page (built-in browser) and ✔ IMF SDMX `IMF.RES,WEO` (publication date 2026-10-13; G001 NGDP_RPCH 2026 = 3.06) |
| WEO sequence in 2026 | Jan 2026 Update *Steady amid Divergent Forces* (3.3% for 2026); Apr 2026 *Global Economy in the Shadow of War*; Jul 2026 Update *Crosscurrents of War and Technology* (3.0%); Oct 2026 (3.1%) | ✔ imf.org WEO list page |
| Latest GFSR / Fiscal Monitor | GFSR Oct 2026 *Resilience, Risk, and Transformation*; FM Oct 2026 *Taxing Better to Boost Growth* | ✔ imf.org |
| Latest WDR | **WDR 2026** on artificial intelligence (document dated 4 Aug 2026). Page title reads "The Promise of Artificial Intelligence"; framework "adopt, adapt, advance" | ✔ worldbank.org WDR page + WDS API. Exact cover title ☐ |
| WDI | Last updated 2026-11-11. World GDP growth 2025 available; poverty at $3.00/day (2021 PPP) through 2024 | ✔ WDI API |

**Consequence for the skeleton:** the brief's Phase 8 (2024–2026: AI boom, tariffs, fragmentation) misses the biggest event of 2026 in the IMF's own telling: a Middle East war, an energy shock and inflation turning back up. I propose splitting it (see §2).

---

## 2. Periodisation, with reasons

The brief's skeleton holds up well. I change three boundaries and add one phase.

| # | Phase | Years | Change from skeleton | Why |
|---|---|---|---|---|
| 1 | **The bust and the turn** | 2000–2002 | none | Nasdaq peak (Mar 2000) to trough (Oct 2002). The US recession, 9/11, Argentina's default and China's WTO entry (Dec 2001) set up everything that follows. |
| 2 | **The great boom** | 2003–mid-2007 | ends mid-2007 | The boom's own logic (cheap credit, commodity demand from China, reserve accumulation, EM growth) runs until the money markets seize in **August 2007**. Ending the boom in Dec 2007 would put the start of the crisis in the wrong chapter. |
| 3 | **The global financial crisis** | Aug 2007–2009 | starts Aug 2007 | One arc: subprime losses, Bear Stearns, Lehman, the collapse of world trade, the G20 London response, and the trough in 2009. |
| 4 | **Uneven recovery** | 2010–mid-2014 | ends mid-2014 | Euro crisis (Greece 2010 to "whatever it takes", 2012), QE2/QE3, the taper tantrum (May–Jun 2013). Ends when oil starts to fall (Jun 2014), which opens a different story. |
| 5 | **Slow growth and slowbalisation** | mid-2014–2019 | starts mid-2014 | Oil and commodity bust, China's 2015 devaluation and stock crash, negative rates, Brexit, the US–China tariffs of 2018–19, and trade growing no faster than GDP. |
| 6 | **Pandemic shock and response** | 2020–2021 | none | Sharpest global recession since the war and the largest fiscal and monetary response. |
| 7 | **Inflation, tightening, war and energy** | 2022–2023 | none | Russia's invasion of Ukraine, the energy and food shock, the fastest tightening cycle in decades, SVB. |
| 8 | **AI, tariffs and fragmentation** | 2024–2025 | narrowed | Disinflation and easing, the AI capex surge and market concentration, the 2025 US tariff increases and their effects. Each 2025 claim checked against Oct 2025 and Oct 2026 WEO. |
| 9 | **2026: a new energy shock (in progress)** | 2026 | **new** | The Apr–Oct 2026 WEOs describe a Middle East war, an energy price shock and global inflation rising to 4.7%. This chapter is written as "history in progress": every 2026 figure is labelled an estimate or projection and dated to its vintage. |

Phase boundaries are drawn by month on monthly charts and rounded to years on annual ones (phase 2 = 2003–2007, phase 3 = 2007–2009, overlapping in 2007, with a hatched band).

**Recession shading** (consistent on every time-series chart):
- *Global recessions* on annual world charts: 2009 and 2020, using the World Bank definition (a fall in world real GDP per capita) in *Global Economic Prospects* (June 2020), Box 1.1 ☐ (verify chapter and box number).
- *US recessions* on US monthly charts: NBER dates via FRED `USREC` ✔ (series available to Oct 2026).
- *Euro-area recessions* on euro charts: CEPR Business Cycle Dating Committee dates ☐.
- *Phase bands* on every chart as a light background, toggleable.

---

## 3. Chapter list

25 chapters plus front and back matter. Every chapter follows the brief's template: *What happened* (one paragraph), narrative (1,500–2,500 words), 3–5 interactive charts, a box called **What the reports said at the time**, key terms, footnotes, and cross-links.

**Added after step 2 review (22 Nov 2026): India in every chapter.** Each phase and theme chapter carries a section headed *India: impact and response* (500–800 words, on top of the main narrative), with one India chart, and India appears in the chapter's other charts wherever it is comparable. The section answers three questions: how the global shock or trend reached India (trade, capital flows, oil, remittances, the rupee, markets); how Indian policy responded (RBI, the Centre's budget, regulation); and how India fared relative to other economies. The "What the reports said at the time" box gets an India row, setting the contemporary **Economic Survey** (and, where useful, the RBI Annual Report or the IMF's India Article IV) against what we now know. See §4a for the India focus and chart of each phase.

### Part I — Phases (9 chapters, `phase-1.html` … `phase-9.html`)
As in §2.

### Part II — Themes (9 chapters, `theme-*.html`)
1. Growth and convergence
2. Trade
3. Money: rates, balance sheets, inflation, the dollar, reserves
4. Debt and fiscal policy
5. Stock markets and capital flows
6. Development: poverty, inequality, health, education, MDGs to SDGs, and how the WDR's focus moved
7. Technology and the productivity puzzle
8. Energy, commodities and climate
9. Demography and labour

### Part III — Country and regional lenses (7 shorter chapters, `lens-*.html`, 1,500–2,000 words each)
United States · China · Euro area · Japan · India · Other emerging markets (Brazil, Mexico, Indonesia, Türkiye, South Africa, Russia, Gulf) · Sub-Saharan Africa

**Decision for you:** the brief lists the lenses as one theme. Seven economies in 2,500 words would give each a paragraph, so I've made them a short Part III. The alternative is a single "lenses" chapter with a tabbed country switcher.

### Front and back matter
- `index.html`: the master timeline, the three parts, and how to read the book
- `wdr-shelf.html`: 27 WDR cards (2000/01 to 2026)
- `explorer.html`: compare countries
- `map.html`: world map with a year slider
- `glossary.html`, `sources.html` (bibliography, data series register), `about.html` (method, vintages, what is unverified)

---

## 4. Charts per chapter (exact series)

Source key: **WEO** = IMF WEO Oct 2026 via SDMX `IMF.RES,WEO` (codes ✔ in the WEO codelist; aggregates: G001 World, G110 AEs, G200 EMDEs, G201 LIDCs, G163 Euro area, G603 SSA, G505 EM & developing Asia, G205 LAC ✔). **WDI** = World Bank API. **FRED** = St Louis Fed CSV. **BIS** = BIS bulk CSV. **ECB** = ECB Data Portal API. **SHL** = Shiller, *Irrational Exuberance* data (Yale). **HF** = IMF WEO historical forecasts (real-time vintages) ☐.

Every annual WEO chart marks years after the latest actual data as projections: dashed line and a "projection" label in the tooltip. Countries are coloured the same everywhere (§7).

### Home timeline
- World real GDP growth, 2000–2027 (WEO `NGDP_RPCH`, G001), with AE/EMDE toggles; 2026–27 dashed.
- Event layer: about 60 dated events, each with a footnote source, filterable by theme.
- Phase bands are clickable and open the chapter.

### Phase 1 — 2000–2002
1. Nasdaq Composite and S&P 500, monthly 1998–2003 (FRED `NASDAQCOM` ✔; SHL S&P composite ☐), with Shiller CAPE (SHL ☐).
2. Real GDP growth 1998–2003: US, euro area, Japan, China, EMDEs (WEO `NGDP_RPCH`).
3. Policy rates 1999–2004: Fed, ECB, BoJ, BoE (BIS `WS_CBPOL` ✔ bulk file reachable).
4. China's share of world goods exports, 1995–2026 (WDI `TX.VAL.MRCH.CD.WT`, China ÷ World ☐).
5. Argentina 2001–02: GDP growth and the peso (WEO `NGDP_RPCH`; BIS `WS_XRU` ☐).

### Phase 2 — 2003–mid-2007
1. Global imbalances: current accounts in US$ bn, 1997–2026, US, China, Germany, Japan, fuel exporters (WEO `BCA`; G080 for fuel-exporting EMDEs).
2. Commodity price indices, 2000–2026: energy, metals, food (WEO `PNRGW`, `PMETAW`, `PFOODW`, annual; IMF `PCPS` monthly ☐).
3. EMDE vs AE growth, 2000–2027 (WEO `NGDP_RPCH` G200, G110).
4. FX reserves: China, other EMs, Japan (WDI `FI.RES.TOTL.CD`; COFER via SDMX ☐).
5. US house prices and household debt (FRED `CSUSHPINSA` ☐; BIS `WS_TC` household credit % GDP ☐).

### Phase 3 — Aug 2007–2009
1. Money-market stress: 3-month LIBOR–OIS or TED spread (FRED `TEDRATE` ☐; it may be discontinued, with an ECB/BIS alternative).
2. Collapse of world trade vs GDP, 2006–2011 (WEO `TRADEPCH`, `NGDP_RPCH`; CPB World Trade Monitor monthly ☐).
3. Central bank balance sheets, indexed (FRED `WALCL` ✔, `ECBASSETSW` ✔, `JPNASSETS` ✔).
4. Equity drawdowns from peak: S&P 500, Euro Stoxx 50, Nikkei 225 (SHL; ECB `FM.M.U2.EUR.DS.EI.DJES50I.HSTA` ✔; FRED `NIKKEI225` ✔).
5. **Forecast vs outturn:** WEO Apr 2008, Oct 2008 and Apr 2009 forecasts of 2009 growth vs actual (HF ☐).

### Phase 4 — 2010–mid-2014
1. Euro sovereign 10-year spreads over Bunds: GR, IT, ES, PT, IE (ECB `IRS.M.{cc}.L.L40.CI.0000.EUR.N.Z` ☐).
2. Unemployment: US, euro area, Spain, Greece (WEO `LUR`).
3. Real GDP, 2007 = 100: US, euro area, Japan, UK, China, India (built from WEO `NGDP_R`).
4. Taper tantrum: US 10-year yield and EM currencies for Brazil, India, Indonesia, Türkiye, South Africa (FRED `DGS10` ✔; BIS `WS_XRU` daily ☐).
5. Fiscal consolidation: change in structural balance 2010–13 (WEO `GGSB_NPGDP`).

### Phase 5 — mid-2014–2019
1. Brent crude, monthly 2000–2026 (FRED `DCOILBRENTEU` ✔ daily → monthly).
2. Trade volume growth ÷ GDP growth, 1990s–2026: the slowbalisation ratio (WEO `TRADEPCH` ÷ `NGDP_RPCH`, G001).
3. US effective tariff rate: customs duties ÷ goods imports, 2000–2026 (FRED `B235RC1Q027SBEA` ÷ `A255RC1Q027SBEA` ☐), with 2018–19 and 2025 marked.
4. Negative yields: 10-year bonds for Germany, Japan, US (FRED `IRLTLT01DEM156N` ✔, `IRLTLT01JPM156N` ☐, `DGS10` ✔).
5. China's credit to the private non-financial sector, % GDP (BIS `WS_TC` ☐).

### Phase 6 — 2020–2021
1. Quarterly real GDP, 2019Q4 = 100: US, euro area, UK, Japan, China, India (OECD QNA ☐, or FRED national series).
2. Fiscal response: change in general government balance 2019 → 2020 by country (WEO `GGXCNL_NGDP`).
3. Central bank balance sheets as % of GDP (FRED balance sheets ÷ WEO `NGDP`).
4. Scarring: GDP level vs the pre-pandemic WEO path (Oct 2019 vintage) for AEs, EMDEs and LIDCs (HF ☐, or the archived Oct 2019 WEO database ☐).

### Phase 7 — 2022–2023
1. Headline inflation, monthly: US CPI, euro-area HICP, UK CPI, Japan CPI (FRED `CPIAUCSL` ✔; ECB `ICP.M.U2.N.000000.4.ANR` ☐; others ☐).
2. Policy rates, 2020–2026 (BIS `WS_CBPOL`).
3. European gas (TTF) and Brent (WEO `PNGASEU`, `POILBRE` annual; World Bank Pink Sheet monthly ☐).
4. The dollar: broad nominal effective rate (BIS `WS_EER` ☐; FRED `DTWEXBGS` ✔ from 2006).
5. Forecast vs outturn: WEO Oct 2021 inflation forecast for 2022 vs actual (HF ☐).

### Phase 8 — 2024–2025
1. US effective tariff rate, 2024–2026 detail (as in Phase 5).
2. AI investment: US real investment in information-processing equipment and software, contribution to GDP growth (BEA NIPA Table 1.1.2 via FRED ☐).
3. Market concentration and valuation: CAPE and the Nasdaq vs Euro Stoxx vs Nikkei (SHL; FRED; ECB).
4. Disinflation 2023–2025 by region (WEO `PCPIPCH`).
5. Trade diversion: China's exports to the US vs ASEAN and Mexico (IMF IMTS via SDMX ☐).

### Phase 9 — 2026 (in progress)
1. Brent and European gas, daily or monthly 2025–Nov 2026 (FRED `DCOILBRENTEU` ✔; Pink Sheet ☐).
2. How the 2026 forecast moved: world growth for 2026 in each WEO from Oct 2025 to Oct 2026 (WEO vintages ✔ SDMX has `WEO_2025_OCT_VINTAGE` and `WEO_2026_APR_VINTAGE`; Jan and Jul updates come from the report text).
3. Inflation 2024–2027 by group (WEO `PCPIPCH`), with projections marked.
4. Energy importers vs exporters, growth in 2026 (WEO; G080 vs G402 and others).

### Theme charts (3–5 each; most have a country selector and a year range slider)
- **Growth and convergence:** GDP per capita PPP relative to US (WEO `PPPPC`); share of world GDP at PPP, 2000–2030 (WEO `PPPSH`); growth by income group (WEO G110/G200/G201); a convergence scatter of initial income vs growth 2000–2025 (WDI `NY.GDP.PCAP.PP.KD`).
- **Trade:** trade % of GDP (WDI `NE.TRD.GNFS.ZS`); world trade volume growth (WEO `TRADEPCH`); services exports share (WDI `BX.GSR.NFSV.CD` ÷ `BX.GSR.GNFS.CD`); GVC participation (WTO TiVA / OECD TiVA ☐); tariffs (above).
- **Money:** policy rates (BIS); balance sheets % GDP; inflation (WEO `PCPIPCH`); the dollar's share of reserves (COFER ☐); real long rates (FRED `DFII10` ☐).
- **Debt and fiscal:** general government gross debt % GDP (WEO `GGXWDG_NGDP`); total private credit % GDP (BIS `WS_TC`); a sovereign crisis and default table (from WEO, GFSR and IMF programme documents, footnoted); interest burden (WEO / FM ☐).
- **Stocks and capital flows:** indices rebased to 2000 = 100; CAPE; market cap % GDP (WDI `CM.MKT.LCAP.GD.ZS`); net capital flows to EMDEs (WEO `BF`, `BFD`, `BFP`, `BFO` for G200).
- **Development:** extreme poverty at $3.00/day (WDI `SI.POV.DDAY` ✔); Gini (WDI `SI.POV.GINI`); under-5 mortality (WDI `SH.DYN.MORT`); life expectancy (WDI `SP.DYN.LE00.IN`); WDR theme timeline (interactive, from the shelf).
- **Technology:** internet users and mobile subscriptions (WDI `IT.NET.USER.ZS`, `IT.CEL.SETS.P2`); US labour productivity growth by decade (FRED `OPHNFB` ☐); TFP (Penn World Table 11 ☐, a proposed addition); ICT investment (BEA).
- **Energy, commodities, climate:** oil and metals prices (WEO); CO₂ emissions by region (WDI `EN.GHG.CO2.MT.CE.AR5` ☐; Global Carbon Budget ☐ as a proposed addition); renewables share (WDI `EG.FEC.RNEW.ZS`); energy intensity (WDI `EG.EGY.PRIM.PP.KD`).
- **Demography and labour:** working-age share (WDI `SP.POP.1564.TO.ZS`); old-age dependency (WDI `SP.POP.DPND.OL`); fertility (WDI `SP.DYN.TFRT.IN`); unemployment (WEO `LUR`); female labour force participation (WDI `SL.TLF.CACT.FE.ZS`); migration and remittances (WDI `BX.TRF.PWKR.DT.GD.ZS`).

### Lens charts (3 each)
Each lens has: (a) real growth and inflation (WEO); (b) a signature series for that economy: US Fed funds and 10-year; China investment share `NID_NGDP` and credit (BIS); euro-area spreads; Japan debt and BoJ assets; India per-capita PPP and services exports; EMs current accounts and FX; SSA debt service `DS_BX` and per-capita growth; and (c) general government debt and balance (WEO).

**Total: about 105 charts.**

---

## 4a. India in each phase (focus to research; nothing below is asserted yet)

India data come from two places: the IMF WEO (India rows, which are on a **fiscal-year basis**, April–March, so WEO "2008" is FY2008-09) and a curated import from the author's Indian-economy book (`data/clean/india/`), built from the Economic Survey Statistical Appendices and the RBI Handbook, each value tied to its table. Monthly series: rupee per dollar (FRED `DEXINUS` ✔), RBI policy rate (BIS `WS_CBPOL`, India ☐), Indian share prices (FRED OECD series ☐). Contemporary Indian sources: the Economic Survey of each year (all editions 2001-02 to 2025-26 already downloaded with text, in the Indian-economy book), RBI Annual Reports (rbi.org.in may block scripts ☐), IMF India Article IV reports (read in the browser).

Convention: an FY is plotted at the calendar year in which it starts (FY2008-09 → 2008), matching the WEO, and every India chart says so.

| Phase | India focus to research | India chart |
|---|---|---|
| 1. 2000–02 | The US tech bust and Indian software exports; slow growth at home; reserves and the rupee | Software exports and GDP growth, FY01–FY04 |
| 2. 2003–mid-2007 | India's high-growth years; capital inflows, reserve build-up and sterilisation; savings and investment surge | Saving and investment rates, and FX reserves |
| 3. 2007–09 | Capital-flow reversal, rupee and Sensex falls, liquidity squeeze; RBI easing and fiscal stimulus; growth dip and rebound | Rupee, net foreign investment, GDP growth vs world |
| 4. 2010–mid-2014 | High inflation and deficits; the 2013 taper tantrum; current account deficit and gold imports | Current account % GDP and rupee, 2010–14 |
| 5. mid-2014–2019 | Oil windfall; inflation targeting; demonetisation and GST; twin balance sheets and the NBFC stress | CPI inflation vs target band; oil import bill |
| 6. 2020–21 | Lockdown contraction and recovery; RBI and fiscal response | Quarterly GDP index vs other large economies ☐ |
| 7. 2022–23 | Oil, food and fertiliser prices after the Russia–Ukraine war; rupee and RBI tightening; Russian oil imports ☐ | CPI and repo rate; oil import bill |
| 8. 2024–25 | Tariffs and India–US trade ☐; supply-chain shifts; services and capability-centre exports ☐ | Exports to the US; services exports |
| 9. 2026 | The 2026 energy shock for an oil importer ☐ | Oil import bill and CAD, with projections marked |

Themes get an India subsection too (for example Trade: India's share of world services exports; Money: the RBI's framework; Development: poverty and per-capita income). Part III's India lens remains, and becomes the place for the long-run story; the per-chapter sections stay focused on that period.

## 5. "What the reports said at the time"

For each phase chapter I'll read the WEO editions inside the phase in full (Ch. 1 and the executive summary; analytical chapters where relevant), plus the GFSR (from 2002) and the Fiscal Monitor (from 2009), plus the WDRs published in the phase. The box contrasts 2–4 specific contemporary judgements with what we now know, each footnoted to edition and chapter. Where real-time forecast data exists, the box adds a forecast-vs-outturn chart. Examples I expect to check (none asserted yet):
- Phase 2: how the IMF framed global imbalances (orderly vs disorderly unwinding) and how the GFSR described risk transfer through securitisation.
- Phase 3: how the Apr and Oct 2008 WEO growth forecasts compared with the 2009 outturn.
- Phase 4: fiscal multipliers (WEO Oct 2012, Box 1.1 ☐) and the reassessment of austerity.
- Phase 7: the 2021 view that inflation would be transitory.

**Contested questions** each get a "competing views" panel:
- Causes of 2008: the savings glut, the Fed's low rates, a regulatory and banking failure, or housing policy (Phase 3, Money, Debt).
- Secular stagnation vs a debt supercycle vs measurement (Phase 5, Technology).
- The 2021–23 inflation: demand and fiscal excess vs supply shocks vs a late Fed (Phase 7, Money).
- Effects of tariffs: incidence on US buyers, trade diversion, macro effects (Phases 5 and 8, Trade).
- Also: the productivity puzzle, austerity and multipliers, and China's growth model.

---

## 6. Sources

### Reports (all fetched in step 2; titles below were read from publisher pages on 22 Nov 2026)
**World Development Reports** ✔ (from the worldbank.org WDR archive): 2000/01 *Attacking Poverty* · 2002 *Building Institutions for Markets* · 2003 *Sustainable Development in a Dynamic World* · 2004 *Making Services Work for Poor People* · 2005 *A Better Investment Climate for Everyone* · 2006 *Equity and Development* · 2007 *Development and the Next Generation* · 2008 *Agriculture for Development* · 2009 *Reshaping Economic Geography* · 2010 *Development and Climate Change* · 2011 *Conflict, Security, and Development* · 2012 *Gender Equality and Development* · 2013 *Jobs* · 2014 *Risk and Opportunity* · 2015 *Mind, Society, and Behavior* · 2016 *Digital Dividends* · 2017 *Governance and the Law* · 2018 *Learning to Realize Education's Promise* · 2019 *The Changing Nature of Work* · 2020 *Trading for Development in the Age of Global Value Chains* · 2021 *Data for Better Lives* · 2022 *Finance for an Equitable Recovery* · 2023 *Migrants, Refugees, and Societies* · 2024 *The Middle-Income Trap* ☐ (archive gives no title; text describes the middle-income trap) · 2025 *Standards for Development* · 2026 *AI* ☐ (exact title). WDR 1999/2000 *Entering the 21st Century* also goes on the shelf as context for 2000. Source: World Bank Open Knowledge Repository PDFs (reachable ✔).

**IMF:** WEO Apr 2000 – Oct 2026 (54 main editions) plus Updates where needed; GFSR Mar 2002 – Oct 2026; Fiscal Monitor 2009 – Oct 2026. Through the built-in browser on imf.org ✔. Scripted access to imf.org returns 403, but the IMF SDMX API works ✔.

**Supporting:** BIS Annual Economic Reports 2000–2026; WTO World Trade Reports; UNCTAD Trade and Development Reports; World Bank Global Economic Prospects; OECD Economic Outlook. Used where the IMF and WDRs are thin (trade policy, GVCs, crisis chronology).

### Data
| Source | Access | Status |
|---|---|---|
| IMF WEO Oct 2026, plus Oct 2025 and Apr 2026 vintages | SDMX `api.imf.org` | ✔ |
| IMF COFER, PCPS, GDD, IMTS, FM | SDMX | dataflows listed ✔; queries ☐ |
| IMF WEO historical forecasts | imf.org file | ☐ (needs the browser to download) |
| World Bank WDI | API v2 | ✔ |
| World Bank PIP (poverty) | API | ✗ returned a server error; fall back to WDI `SI.POV.*` ✔ |
| World Bank Pink Sheet (monthly commodities) | xlsx | ☐ |
| BIS (policy rates, credit, EER, property, exchange rates) | bulk CSV zips | ✔ reachable |
| FRED | CSV endpoint | ✔ (note: `SP500` only covers the last 10 years, so the S&P history comes from Shiller) |
| ECB Data Portal (Euro Stoxx 50, HICP, yields) | API | ✔ |
| Shiller S&P and CAPE | Yale xls | ✔ reachable |
| WTO statistics | API needs a subscription key (401) | ✗ for now. Fall back to WDI (WTO-sourced `TX.VAL.MRCH.CD.WT`) and WEO trade volumes. **Decision for you:** register a free WTO API key yourself if you want WTO tariff profiles and services detail |
| Stooq | bot-check page | ✗ not used; FRED, ECB and Shiller cover the indices |
| Natural Earth 110m countries (map) | GitHub GeoJSON, public domain | ✔ reachable |
| Proposed additions | Penn World Table 11 (TFP), Global Carbon Budget (CO₂), OECD QNA (quarterly GDP), CEPR euro recession dates, FAO Food Price Index | ☐ need your OK |

---

## 7. Technical design

- **Library:** Apache ECharts 5.6.0, vendored. One library covers line, bar, scatter, maps (registered GeoJSON), `dataZoom` range sliders, legend toggles, `markArea` shading and SVG rendering for print. MiniSearch is vendored for full-text search. I'm reusing the versions already vendored in your Indian-economy book. No CDN calls.
- **Data under `file://`:** charts read `data/js/*.js` files that set `window.WE.DATA[...]`. Each series record carries `{code, source, unit, freq, vintage, retrieved, notes}`, so tooltips and the source line are generated, not typed.
- **One chart wrapper** (`assets/js/charts.js`): `WE.chart(el, spec)` adds phase bands and recession shading, hover values, series toggles, a country selector, a year-range slider, a source and code footer, alt text (from `spec.alt`), a data-table toggle, CSV download, and dashed projections. No chart is built outside it.
- **Colours:** a fixed, colour-blind-safe map from country or aggregate to colour (Okabe–Ito plus a few from Tol's palette), defined once in `assets/js/palette.js`. US, China, euro area, Japan, India, UK, Germany, Brazil, SSA, World, AEs, EMDEs and LIDCs each get one colour everywhere. Line style (solid, dash, dot) backs up colour so charts still read in greyscale.
- **Pages:** one HTML file per chapter with shared `book.css`, `book.js` (TOC sidebar, reading progress, light/dark, glossary hover, footnote popovers, keyboard navigation) and print CSS (charts print as their static SVG with the source line).
- **Accessibility:** a skip link, landmarks, visible focus, arrow-key timeline scrubbing, `aria-live` readouts on sliders, a text alternative and data table for every chart, and WCAG AA contrast in both themes.
- **Responsive** down to 768 px: the sidebar collapses and charts stack.

### File structure
```
World Economy/
  index.html  wdr-shelf.html  explorer.html  map.html  glossary.html  sources.html  about.html
  chapters/  phase-1.html … phase-9.html  theme-*.html  lens-*.html
  assets/  css/book.css  css/print.css  js/{book,charts,palette,timeline,explorer,map,search}.js  vendor/{echarts.min.js, minisearch.min.js}  geo/world-110m.js
  data/  raw/{wdi,imf,fred,bis,ecb,shiller,wb_pink,...}/   (untouched downloads + fetch log)
         clean/*.json                                       (tidy series)
         js/*.js                                            (what pages load)
  sources/  bibliography.csv  (title, publisher, year, edition, URL, date accessed)
            reports/  (PDFs or saved text of WDRs, WEOs, GFSRs, FMs; reading notes per edition)
  scripts/  fetch_wdi.py  fetch_imf_sdmx.py  fetch_fred.py  fetch_bis.py  fetch_ecb.py  fetch_misc.py
            clean.py  build_js.py  build_search.py  check_numbers.py  check_links.py  check_pages.js
  PLAN.md  PROGRESS.md  NOTES.md  README.md
```
`make refresh` (or `python3 scripts/refresh.py`) re-runs the fetches and rebuilds `data/js`. Reading the book needs nothing.

### Quality checks (step 4, scripted where possible)
- `check_numbers.py`: every number in prose is tagged `<span class="n" data-s="SERIES" data-y="YEAR">`, and the script compares it with `data/clean`. Untagged numbers must carry a footnote.
- `check_links.py`: internal links, anchors, footnote back-links.
- `check_pages.js` (headless): opens every page, fails on any console error, checks each chart rendered.
- `NOTES.md` collects every `[unverified]` marker automatically.

---

## 8. Build order
1. **Step 2 (next, then stop for review):** the data pipeline for all sources marked ✔, the site shell (navigation, TOC, search, glossary hovers, theming, print), the master timeline, and **Phase 3 (GFC)** as the sample chapter. It's the most chart-heavy and source-heavy phase, so it tests the most.
2. **Step 3:** the remaining chapters in order (Phases 1–9, then themes, then lenses), updating PROGRESS.md after each. The WDR shelf, explorer and map are built alongside the Development theme.
3. **Step 4:** the full verification pass.

## 9. Decisions I need from you
1. **Nine phases** (adding *2026: a new energy shock*, and moving three boundaries to mid-year), or keep your eight?
2. **Country lenses as Part III** (7 short chapters), or one chapter with a country switcher?
3. **Proposed extra data sources:** Penn World Table, Global Carbon Budget, OECD QNA, CEPR dates, FAO Food Price Index. OK to add?
4. **Project folder:** I've put this in `~/coding2026/World Economy` (empty, git initialised). Is that right?
5. **WTO API key:** do you want to register one (free) so I can use WTO tariff and services data, or should I use the fallbacks?
