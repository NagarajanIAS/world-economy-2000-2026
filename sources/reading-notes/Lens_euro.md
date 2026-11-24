# Reading notes: country lens "The euro area, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies). URLs were taken from publisher
listing or issue pages where possible: the ECB's yearly listing includes (`/press/govcdec/mopo/YYYY/html/index_include.en.html`,
`/press/pr/date/YYYY/html/index_include.en.html`, and the 2008 monetary-policy-statement include); the Commission's EU financial assistance
page, the economic-forecasts listing, the Stability and Growth Pact pages, the NextGenerationEU page and the Draghi report page; the EU trade
pages for India; the imf.org Greece country page (GRC) and its 2025 Article IV issue page. Every guessed URL is flagged GUESSED. **The IMF has no
country page for the euro area**: https://www.imf.org/en/Countries/EUQ, /EUR, /EMU, /XEU and /Euro-Area all return 404 (see Not obtained). So
every euro-area Article IV staff report (EA-IMF-1 to EA-IMF-13) and the two Greece programme papers (EA-IMF-14, EA-IMF-15) come from GUESSED
URLs built on the IMF's file-naming pattern: `/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/2018/crYYNNN.pdf`
in 2018; `/-/media/files/publications/cr/YYYY/[english/]1eureaYYYYnnn.pdf` from 2019 (euro-area code "eur"). For each file the title page
and "Country Report No." were read, to confirm it is the euro-area (or Greece) report named. Downloads are in the session scratchpad folder
`lens_euro_dl/`, one subfolder per batch: `imf/` (404 pages), `imf/g/` (euro-area reports), `imf/grc/` (Greece), `ecb/`, `ecb/inc/` (listing
includes), `ecb/pr/` (press releases), `eu/`, `eu/g/` (EMU@10, Occasional Paper 61), `eu/draghi/` and `in/`. PDFs were converted with
`pdftotext` (plain and `-layout`). HTML pages were stripped of tags and read as text. Python that read downloads was run with `python3 -I`,
from scripts kept outside the download folders. The Draghi speech of 26 July 2012 is the one ECB page fetched from a GUESSED URL. Economic Survey texts were not refetched. They were read from the Econ Subject folder
(`sources/text/es*.txt`, where text page = PDF page), and the printed page number was taken from the running header or footer: ES 2012-13
printed = PDF; ES 2014-15 Vol. 1 printed = PDF − 6. Quotes are verbatim and under 15 words, and a script checked each one against the
converted text (whitespace-normalised, with a column-split pass for two-column pages). Everything else is paraphrase. Page numbers are printed
page numbers unless stated. "PDF p." is used where only the PDF page can be given, for example the unnumbered Key Issues and press-release
pages of IMF reports. The ECB yield and inflation series (EA-OTH-1) and the India–EU surplus are my own reading or arithmetic of data already
held, and are marked "own reading".

Item labels:
- EA-IMF-n: IMF Article IV consultations on euro-area policies, and IMF Greece papers.
- EA-ECB-n: ECB decisions, press conferences and speeches.
- EA-EU-n: European Commission, Council, Eurogroup and ESM sources (the Council and ESM sites blocked all fetches; see Not obtained).
- EA-OTH-n: data already in the book.
- EA-IN-n: India and the euro area, from the Economic Surveys.

Indian years are fiscal years (April–March) or survey years.

Abbreviations: APP = asset purchase programme; BTIA = Broad-based Trade and Investment Agreement; CA = current account; CBAM = Carbon Border
Adjustment Mechanism; CR = IMF Country Report; DFR = deposit facility rate; EDP = excessive deficit procedure; EFSF/EFSM = European Financial
Stability Facility/Mechanism; ESM = European Stability Mechanism; HICP = harmonised index of consumer prices; MLF = marginal lending facility;
MRO = main refinancing operations rate; NGEU = NextGenerationEU; OMT = Outright Monetary Transactions; PEPP = Pandemic Emergency Purchase
Programme; PSI = private sector involvement; RRF = Recovery and Resilience Facility; SBA = Stand-By Arrangement; SGP = Stability and Growth
Pact; SMP = Securities Markets Programme; TPI = Transmission Protection Instrument.

Already in the book (cite, do not duplicate):
- `IMF_2010-2014.md`: WEO April 2010 on contagion from Greece; WEO October 2012 on banking union; the Blanchard–Leigh Box 1.1 on fiscal
  multipliers; WEO April 2014 on deflation risk in the euro area.
- `IMF_2014-2019.md`: ECB QE welcomed; the ECB's March 2016 easing; negative yields in 2019.
- `IMF_2022-2023.md`: euro-area inflation near 7 percent; ECB +1.25 points.
- `IMF_2024-2025.md`: the ECB's cut of 5 June 2024; the Draghi report in the October 2024 WEO Foreword.
- `IMF_2026.md`: euro-area forecasts for 2026; TTF gas prices.
- `Theme_money.md`:
  - MO-CB-2: the ECB strategy reviews of 2021 and 2025 (symmetric 2 percent);
  - MO-BIS-2 p. 65: the March 2016 DFR of −0.40 percent;
  - MO-IMF-2 p. 10: ECB policy too loose for Ireland and Spain.
- `Theme_energy.md`:
  - EN-IMF-3: October 2022 gas (Russian pipeline gas down to about 20 percent; natural gas +129.2 percent);
  - EN-WB-6: European gas at all-time highs in August 2022;
  - EN-WB-8: CBAM in force.
- `Theme_debt.md`: DF-IMF-3 (Blanchard–Leigh multipliers).
- `Theme_trade.md`: TR-IN-4 and TR-IN-5 (CBAM; the EU FTA concluded).
- `India_ES_2010-2014.md`:
  - ES10-10: the 9 percent forecast for 2011-12;
  - ES11-2 and ES11-3: the euro zone among the causes of India's slowdown;
  - ES12-1: growth of 6.2 percent in 2011-12;
  - ES12-9 and ES12-13 (Box 6.1 p. 135 and Box 6.2 p. 136): the euro crisis and risk-on/risk-off flows.
- `India_ES_2024-2026.md`: ES25-10 (trade agreements, including the EU FTA).

## IMF Article IV consultations on euro-area policies

### EA-IMF-1. IMF, *Euro Area Policies: Staff Report…*, IMF Country Report No. 04/234, August 2004 (staff report dated 2 July 2004)
PDF: https://www.imf.org/external/pubs/ft/scr/2004/cr04234.pdf (GUESSED; 200; 62 PDF pages; printed = PDF − 2). Read: Executive Summary
(p. 4), p. 7, Staff Appraisal (pp. 39–41).
- p. 4: the recovery was led by foreign demand, and domestic demand was weak, especially in Germany. Four countries, France and Germany among
  them, breached the 3 percent deficit limit, and the SGP was "in abeyance". Staff advised fiscal adjustment of at least ½ percent of GDP.
- p. 7: regional divergences had grown since 2000, and Germany's current-account surplus had risen by about 4½ percent of GDP.
- p. 39 (appraisal): area-wide fundamentals (fiscal deficits, private balance sheets, the current account) "seem relatively sound", but
  potential growth had weakened and the SGP was in "procedural limbo".
- p. 41 (para 60): the integrity of fiscal data should be a priority.

### EA-IMF-2. IMF, *Euro Area Policies: 2006 Article IV Consultation*, IMF Country Report No. 06/287, August 2006
PDF: https://www.imf.org/external/pubs/ft/scr/2006/cr06287.pdf (GUESSED; 200; 71 PDF pages; printed = PDF − 2). Read: Box 3 (p. 26).
- p. 26, Box 3 "Euro Area Divergences": persistent inflation differentials had contributed to divergence in competitiveness and current
  accounts. These divergences "might take a painfully long time to unwind".

### EA-IMF-3. IMF, *Euro Area Policies: 2007 Article IV Consultation*, IMF Country Report No. 07/260, July 2007 (staff report dated 10 July 2007)
PDF: https://www.imf.org/external/pubs/ft/scr/2007/cr07260.pdf (GUESSED; 200; 69 PDF pages; printed = PDF − 2). Read: Executive Summary
(p. 1), pp. 7, 11, Staff Appraisal (pp. 25–27).
- p. 1: "The outlook is the best in years." The external position and the real effective exchange rate were within the range of
  equilibrium.
- p. 7: the medium-run weaknesses were "stretched housing sectors" and insufficient competitiveness in parts of the area. p. 11: divergences
  in competitiveness needed faster adjustment.
- pp. 25–27 (appraisal): "The external position remains roughly balanced". The home–host model of supervision precluded effective crisis
  management for large cross-border financial institutions.

### EA-IMF-4. IMF, *Euro Area Policies: 2008 Article IV Consultation*, IMF Country Report No. 08/262, August 2008
PDF: https://www.imf.org/external/pubs/ft/scr/2008/cr08262.pdf (GUESSED; 200; 63 PDF pages; printed = PDF − 2). Read: Executive Summary
(p. 3), Staff Appraisal (p. 21), Table 1 (p. 39).
- p. 3: EMU was widely hailed as a success, and the euro was above its fundamentals. Staff favoured holding rates, while the ECB pointed to a
  possible rise.
- p. 21 (appraisal): "monetary union is a distinct and promising success"; "policy rates are best kept on hold"; growth was expected to
  reaccelerate toward trend in 2009.
- Table 1, p. 39, projections for 2009: GDP 1.2 percent, unemployment 7.4 percent, CPI 2.3 percent, debt 64.4 percent of GDP. Current
  account 0.3 percent of GDP (2007) and −0.5 percent (2008).

### EA-IMF-5. IMF, *Euro Area Policies: 2010 Article IV Consultation*, IMF Country Report No. 10/221, July 2010 (staff report dated 1 July 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2010/cr10221.pdf (GUESSED; 200; 65 PDF pages; printed = PDF − 1). Read: Executive Summary
(PDF p. 2), p. 12, Staff Appraisal (pp. 24–25), Table 1 (p. 42).
- PDF p. 2: "The current crisis is a wake-up call for the euro area." The crisis was caused largely by unsustainable policies in some
  members.
- p. 12: the EFSM (up to €60 bn) had been available since early May, and the EFSF was expected to be operational in July 2010.
- pp. 24–25 (appraisal): "divergences in economic performance have been allowed to fester". The ECB was an "anchor of stability", and the
  SMP is discussed.
- Table 1, p. 42, for 2009: GDP −4.1 percent, unemployment 9.4 percent, CPI 0.3 percent; debt 79.0 percent of GDP (69.5 in 2008).

### EA-IMF-6. IMF, *Euro Area Policies: 2012 Article IV Consultation*, IMF Country Report No. 12/181, July 2012 (staff report dated 3 July 2012)
PDF: https://www.imf.org/external/pubs/ft/scr/2012/cr12181.pdf (GUESSED; 200; 52 PDF pages; printed = PDF − 1). Read: Key Issues
(PDF p. 2), Staff Appraisal (pp. 25–26), Table 1 (p. 33).
- PDF p. 2: the crisis had "reached a new and critical stage", "raising questions about the viability of the monetary union itself". The
  report cites financial fragmentation, and "the first priority is a banking union for the euro area".
- pp. 25–26 (appraisal): a common deposit guarantee, a resolution authority and limited common debt. The ECB should keep inflation not far
  below 2 percent.
- Table 1, p. 33: debt 91.4 percent of GDP in 2012; projections for 2013 of GDP 0.7 percent and unemployment 11.3 percent.

### EA-IMF-7. IMF, *Euro Area Policies: 2014 Article IV Consultation*, IMF Country Report No. 14/198, July 2014 (staff report dated 25 June 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14198.pdf (GUESSED; 200; 52 PDF pages; printed = PDF − 1). Read: Key Issues
(PDF p. 2), Staff Appraisal (pp. 23–24), Table 1 (p. 26).
- PDF p. 2 and p. 24: "Inflation has been too low for too long." The report notes negative deposit rates and advises considering asset
  purchases.
- pp. 23–24 (appraisal): spreads were back to pre-crisis levels, and the ECB would take over supervision in November. A negative shock "could
  tip the economy into deflation".
- Table 1, p. 26, for 2013: GDP −0.4 percent, unemployment 12.0 percent, debt 95.2 percent of GDP. CPI projections: 0.7 (2014), 1.2 (2015),
  1.3 (2016). Current account 0.1 (2011), 1.3 (2012), 2.2 (2013) percent of GDP.

### EA-IMF-8. IMF, *Euro Area Policies: 2015 Article IV Consultation*, IMF Country Report No. 15/204, July 2015 (staff report dated 10 July 2015)
PDF: https://www.imf.org/external/pubs/ft/scr/2015/cr15204.pdf (GUESSED; 200; 56 PDF pages; printed = PDF − 4). Read: press release
(PDF p. 3), Key Issues (PDF p. 5), pp. 4–5.
- PDF p. 5: "Quantitative easing (QE) has boosted confidence and improved financial conditions." The recovery was underpinned by lower oil
  prices and QE.
- p. 4: "widespread deflation in early 2015"; HICP inflation 0.2 percent in June.
- p. 5 (para 7): on contagion from Greece, spillovers were lower thanks to QE, OMT and TLTROs. PDF p. 3 (press release): Directors urged
  readiness to manage contagion from Greece.

### EA-IMF-9. IMF, *Euro Area Policies: 2019 Article IV Consultation*, IMF Country Report No. 19/219, July 2019 (Board 8 July 2019; staff report dated 20 June 2019); with CR 18/223 (July 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2019/1eurea2019001.pdf (GUESSED; 200; 61 PDF pages; PDF p. 7 = printed 2). Also
https://www.imf.org/-/media/files/publications/cr/2018/cr18223.pdf (GUESSED; 200; 64 PDF pages; PDF p. 5 = printed 4). Read: 2019 Key Issues
(PDF p. 6) and table (PDF p. 5); 2018 Table 1 (p. 4).
- 2019, PDF p. 6: the danger of "a prolonged period of anemic growth and inflation"; reform of the euro-area architecture was "too slow".
- 2019, PDF p. 5 (unnumbered table): projections for 2020 of GDP 1.6 percent and CPI 1.6 percent.
- 2018, Table 1 p. 4: CPI 0.0 percent (2015) and 0.2 percent (2016); current account 3.2 (2015) and 3.6 (2016) percent of GDP.

### EA-IMF-10. IMF, *Euro Area Policies: 2021 Article IV Consultation with Member Countries—Press Release; Staff Report… on Common Euro Area Policies*, IMF Country Report No. 22/29, February 2022 (staff report dated 21 December 2021)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1eurea2022001.pdf (GUESSED; 200; PDF p. 4 = printed 3). Read: Key Issues
(PDF p. 5), table (p. 3).
- PDF p. 5: inflation was rising because of "transitory factors", and it "is projected to moderate during 2022 and remain below the ECB's
  inflation target" over the medium term.
- p. 3: CPI 2.6 (2021), projected 3.0 (2022) and 1.7 (2023); GDP −6.4 percent in 2020; debt 97.3 percent of GDP in 2020.
- The July 2022 consultation was not found (see Not obtained).

### EA-IMF-11. IMF, *Euro Area Policies: 2023 Article IV Consultation*, IMF Country Report No. 23/264, July 2023 (staff report dated 28 June 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1eurea2023001.pdf (GUESSED; 200; PDF p. 4 = printed 3). Read: Key Issues
(PDF p. 5), table (p. 3).
- PDF p. 5: the area had suffered "the largest terms of trade loss in several decades", with a mild technical recession in early 2023.
  Inflation was expected to return to target by mid-2025.
- p. 3: CPI 8.4 percent in 2022, projected 5.2 in 2023; GDP 3.5 percent in 2022.

### EA-IMF-12. IMF, *Euro Area Policies: 2024 Annual Consultation*, IMF Country Report No. 24/248, July 2024 (Board 22 July 2024; staff report dated 1 July 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1eurea2024001.pdf (GUESSED; 200; 100 PDF pages; offset varies: PDF 4 =
p. 3, PDF 20 = p. 16, PDF 75 = p. 71). Read: Key Issues (PDF p. 5), p. 3, p. 16, Annex III (pp. 71–72).
- PDF p. 5: "Energy-intensive industries, in particular, have struggled to adjust to higher input costs". Inflation was expected at target
  in the second half of 2025, and the report urged a focus on productivity.
- p. 3: CPI 5.4 percent and GDP 0.5 percent in 2023. p. 16 (para 25): the planned consolidation was significant by historical standards.
- p. 71 (Annex III), on the new EU economic governance framework:
  - it entered into force on 30 April 2024;
  - net primary expenditure is the single operational indicator;
  - the adjustment period is 4 years, extendable to 7;
  - debt safeguard: a fall of 1 point a year if debt is above 90 percent of GDP, 0.5 point if it is 60–90 percent;
  - deficit resilience safeguard: 0.4 or 0.25 point;
  - 17 of the 27 states were above the reference values.
- p. 72: under an EDP, the minimum structural improvement is 0.5 percent of GDP a year.

### EA-IMF-13. IMF, *Euro Area Policies: 2026 Annual Consultation*, IMF Country Report No. 26/177, July 2026 (staff report dated 26 June 2026)
PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1eurea2026001.pdf (GUESSED; 200; 881 KB; PDF 5 = p. 4, PDF 12 = p. 7,
PDF 13 = p. 8, PDF 15 = p. 10, PDF 40 = p. 35). Read: Key Issues (PDF pp. 6–7), pp. 4, 7, 8, 10, 35.
- PDF p. 6: growth in 2025 was slightly above potential and inflation close to target. The Middle East war lowers baseline growth by 0.5
  point (2026) and 0.2 point (2027), to 0.9 and 1.2 percent. Headline inflation is projected at 2.9 and 2.3 percent. The report also notes
  "Europe's persistently weak potential growth that reflects subdued productivity growth and aging".
- PDF p. 7: the priorities include a "28th regime" and the savings and investments union.
- p. 7: the ECB cut rates until June 2025, to a DFR of 2.0 percent, then raised them 25 bp in June 2026. p. 10: the baseline has the DFR at
  2.5 percent by end-2026; defence spending rises from 2 to 2.4 percent of GDP by 2031.
- p. 8:
  - the Turnberry deal set a 15 percent tariff ceiling;
  - the Mercosur agreement has applied provisionally since May 2026;
  - "The EU has concluded additional free trade agreements with Australia, India, and Indonesia", which await signature and ratification;
  - the effective US tariff on the EU is about 11.4 percent.
- Table 1, p. 4:

  | | 2022 | 2023 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|---|
  | GDP (%) | 3.6 | 0.5 | 1.0 | 1.4 | 0.9 |
  | CPI (%) | 8.4 | 5.4 | 2.4 | 2.1 | 2.9 |
  | Debt (% of GDP) | 88.9 | 86.5 | 86.6 | 87.4 | 88.4 |

  Debt reaches 92.9 percent of GDP in 2031. The current account is 2.7 percent of GDP in 2024 and 1.7 percent in 2025.
- p. 35: the appraisal begins; the baseline assumes 50 bp of rate rises over 2026.
- Also downloaded but not used: CR 25/203 (euro-area FSSA, July 2025), CR 25/206 and 25/207 (FSAP technical notes), CR 11/184 (2011) and
  CR 13/231 (2013).

## IMF and Greece

### EA-IMF-14. IMF, *Greece: Staff Report on Request for Stand-By Arrangement*, IMF Country Report No. 10/110, May 2010 (staff report dated 5 May 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2010/cr10110.pdf (GUESSED; 200; 146 PDF pages; printed = PDF − 2). Read: Executive Summary
(PDF p. 3), p. 20, Table 1 (p. 26), Annex 1 (p. 35).
- PDF p. 3: "The Greek economy is teetering due to heavy public debt". The package:
  - a €30 bn SBA (3,212 percent of quota);
  - €80 bn from euro-zone partners;
  - measures worth 7½ percent of GDP in 2010.
  On debt, "the debt-ratio would peak at 149 percent of GDP in 2013".
- p. 20: debt was judged sustainable, but not with high probability; the systemic exemption was used.
- p. 26 (Table 1): GDP −4.0 (2010), −2.6 (2011), 1.1 (2012), 2.1 (2013) percent.
- p. 35 (Annex 1): debt peaks at 149 percent of GDP in 2013 and falls to 120 percent by 2020. Debt was 115 percent of GDP in 2009 and the
  deficit 13.6 percent.

### EA-IMF-15. IMF, *Greece: Ex Post Evaluation of Exceptional Access under the 2010 Stand-By Arrangement*, IMF Country Report No. 13/156, June 2013 (dated 20 May 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13156.pdf (GUESSED; 200; 51 PDF pages; printed = PDF − 1). Read: Executive Summary
(pp. 1–2), pp. 12, 14, ~16.
- pp. 1–2:
  - there was a competitiveness gap of 20–30 percent, and the programme had "notable failures";
  - "Market confidence was not restored", and banks lost 30 percent of their deposits;
  - public debt "eventually had to be restructured";
  - "the baseline macro projections can also be criticized for being too optimistic".
- p. 12: "real GDP in 2012 was 17 percent lower than in 2009", against a projected 5½ percent. Unemployment was 25 percent, against 15
  percent projected.
- p. 14: the March 2012 restructuring cut privately held debt by 60 percent, and debt fell by €62.4 bn to €305.5 bn.
- p. ~16: by the fourth review, debt at end-2013 was projected at 170 percent of GDP.

### EA-IMF-16. IMF, *Greece: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 25/85, April 2025
Listing: https://www.imf.org/en/countries/grc (200) → issue page
https://www.imf.org/en/publications/cr/issues/2025/04/04/greece-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-565906
(200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1grcea2025001-print-pdf.pdf (from the issue page; 200). Read: Key
Issues (PDF p. 5), Table 1 (p. 26, PDF 30).
- PDF p. 5: debt is "on a firm downward trajectory", and NGEU funds are driving investment.
- p. 26 (Table 1):
  - debt (percent of GDP): 183.7 (2019), 209.9 (2020), 197.8 (2021), 178.4 (2022), 165.2 (2023), 150.8 (2024), 142.4 (2025 proj.),
    124.9 (2030 proj.);
  - unemployment: 17.3 percent (2019) to 10.1 percent (2024);
  - GDP −9.2 percent in 2020.

## European Central Bank (URLs from ECB listing includes unless flagged GUESSED)

### EA-ECB-1. ECB, monetary policy decisions, 3 July 2008, and the introductory statement to the press conference (Trichet), 3 July 2008
https://www.ecb.europa.eu/press/pr/date/2008/html/pr080703.en.html (200);
https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2008/html/is080703.en.html (200).
- The MRO was raised 25 bp to 4.25 percent, and the deposit rate to 3.25 percent.
- Press conference: "the euro area does not suffer from major imbalances"; "the economic fundamentals of the euro area are sound".

### EA-ECB-2. ECB, "Monetary policy decisions" (coordinated cut), 8 October 2008
https://www.ecb.europa.eu/press/pr/date/2008/html/pr081008.en.html (200).
- A rate cut coordinated with the Bank of Canada, the Bank of England, the Federal Reserve, the Riksbank and the Swiss National Bank: the MRO
  was cut 50 bp to 3.75 percent and the deposit rate to 2.75 percent.

### EA-ECB-3. Mario Draghi, speech at the Global Investment Conference, London, 26 July 2012
https://www.ecb.europa.eu/press/key/date/2012/html/sp120726.en.html (GUESSED; 200; page title "Verbatim of the remarks made by Mario Draghi", Global Investment Conference, London, 26 July 2012, confirmed).
- The speech uses the bumblebee metaphor, speaks of convertibility premia, and calls the euro irreversible. Draghi said "the ECB is ready to
  do whatever it takes to preserve the euro", and added "And believe me, it will be enough."

### EA-ECB-4. ECB, "Technical features of Outright Monetary Transactions", 6 September 2012
https://www.ecb.europa.eu/press/pr/date/2012/html/pr120906_1.en.html (200).
- OMT is conditional on an EFSF/ESM programme and covers maturities of 1–3 years. "No ex ante quantitative limits are set on the size of
  Outright Monetary Transactions." The SMP was terminated.

### EA-ECB-5. ECB, monetary policy decisions and measures, 5 June 2014
https://www.ecb.europa.eu/press/pr/date/2014/html/pr140605.en.html and pr140605_3.en.html (200).
- From 11 June 2014 the MRO was 0.15 percent and the deposit rate −0.10 percent, the first negative rate.

### EA-ECB-6. ECB, "ECB announces expanded asset purchase programme", 22 January 2015
https://www.ecb.europa.eu/press/pr/date/2015/html/pr150122_1.en.html (200).
- The APP was expanded to €60 bn a month, until at least September 2016, with 20 percent risk sharing. It was intended "to address the risks
  of a too prolonged period of low inflation".

### EA-ECB-7. ECB, "ECB announces €750 billion Pandemic Emergency Purchase Programme (PEPP)", 18 March 2020
https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.pr200318_1~3949d6f266.en.html (200).
- PEPP: €750 bn until end-2020, with a waiver for Greek securities. The ECB "will not tolerate any risks to the smooth transmission of its
  monetary policy", and "The Governing Council will do everything necessary within its mandate."

### EA-ECB-8. ECB, monetary policy decisions, 21 July 2022; and "The Transmission Protection Instrument", 21 July 2022
https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220721~53e5bdd317.en.html (200);
https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.pr220721~973e6e7273.en.html (200).
- Rates rose 50 bp from 27 July: MRO 0.50 percent, MLF 0.75 percent, DFR 0.00 percent.
- The TPI counters "unwarranted, disorderly market dynamics that pose a serious threat to the transmission" of policy. It buys securities of
  1–10 years' maturity and is "not restricted ex ante". Eligibility criteria include not being under an EDP, among others.

### EA-ECB-9. ECB, monetary policy decisions, 6 June 2024 and 5 June 2025
https://www.ecb.europa.eu/press/pr/date/2024/html/ecb.mp240606~2148ecdb3c.en.html (200);
https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.mp250605~3b5f67d007.en.html (200).
- 2024: the first cut, to a DFR of 3.75 percent: "it is now appropriate to moderate the degree of monetary policy restriction". Inflation had
  fallen by more than 2.5 points since September 2023.
- 2025: DFR 2.00 percent.

### EA-ECB-10. ECB, monetary policy decisions of 11 June, 23 July, 10 September and 29 October 2026
URLs (all 200):
- https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html
- …/ecb.mp260723~29f24d99bc.en.html
- …/ecb.mp260910~314e508016.en.html
- …/ecb.mp261029~9a493adf17.en.html

Notes:
- 11 June: +25 bp from 17 June, to DFR 2.25, MRO 2.40 and MLF 2.65 percent. Inflation projections 3.0 / 2.3 / 2.0.
- 23 July: rates unchanged.
- 10 September: +25 bp from 16 September, to DFR 2.50, MRO 2.65 and MLF 2.90 percent. "inflation is set to remain well above target for an
  extended period". Inflation projections 3.0 / 2.5 / 2.1; growth 0.9 / 1.4 / 1.5.
- 29 October: rates unchanged, DFR 2.50 percent.
- The 2026 listing also shows decisions on 5 February, 19 March and 30 April (not read).

## European Union (Commission, Council, Eurogroup, ESM)

### EA-EU-1. European Commission (DG ECFIN), *EMU@10: successes and challenges after 10 years of Economic and Monetary Union*, European Economy 2/2008
PDF: https://ec.europa.eu/economy_finance/publications/pages/publication12682_en.pdf (GUESSED; 200; 352 PDF pages). Read: Foreword
(PDF p. 5), p. 6 (PDF 22).
- PDF p. 5 (Almunia): "The Economic and Monetary Union and the euro are a major success."
- p. 6: the euro area had added 16 million jobs, but there were "substantial and lasting differences" in inflation and unit labour costs.
  "This has led to accumulated competitiveness losses and large external imbalances", which need a long adjustment.

### EA-EU-2. European Commission, *The Economic Adjustment Programme for Greece*, Occasional Papers 61, May 2010
PDF: https://ec.europa.eu/economy_finance/publications/occasional_paper/2010/pdf/ocp61_en.pdf (GUESSED; 200; 93 PDF pages; printed "x/90",
printed = PDF − 3). Read: pp. 1, 3, 8.
- p. 1: the €110 bn joint package was agreed on 2 May.
- p. 3: growth was close to 4 percent in 2000–09, but the "growth performance of Greece over the last decade was based on unsustainable
  drivers". The Greek current-account deficit peaked at 14 percent of GDP in 2008.
- p. 8: €80 bn in bilateral loans and €30 bn from the IMF (approved 9 May); debt was 115 percent of GDP in 2009.

### EA-EU-3. European Commission, "Financial assistance to Greece"
Listing: https://economy-finance.ec.europa.eu/eu-financial-assistance_en (200) → https://economy-finance.ec.europa.eu/eu-financial-assistance/euro-area-countries/financial-assistance-greece_en (200).
- Second programme (approved 14 March 2012):
  - an additional €130 bn, for a total of €164.5 bn, of which €144.7 bn from the EFSF;
  - PSI: €197 bn of €205.6 bn of bonds exchanged (95.7 percent);
  - the programme expired on 30 June 2015.
- Third programme:
  - ESM request on 8 July 2015 and Euro Summit on 12–13 July 2015;
  - a €7.16 bn EFSM bridge loan;
  - MoU on 19 August 2015, for up to €86 bn over 2015–18;
  - completed on 21 August 2018.
- A 2023 ex-post evaluation is listed (not read).

### EA-EU-4. European Commission, "NextGenerationEU" (borrower-investor relations page)
https://commission.europa.eu/strategy-and-policy/eu-budget/eu-borrower-investor-relations/nextgenerationeu_en (200).
- The envelope is €806.9 bn "as set in 2021", with up to €634 bn raised by end-2026. The RRF offers up to €360 bn in grants and €213 bn in
  loans (of €385 bn available). Repayment runs from 2028 to 2058, backed by a 0.6 point increase in own-resources headroom (percent of GNI).

### EA-EU-5. European Commission, Stability and Growth Pact pages, including "Escape clauses" (preventive arm)
https://economy-finance.ec.europa.eu/economic-governance-framework/stability-and-growth-pact/preventive-arm/escape-clauses_en (200) and
the SGP overview pages.
- There are a general and a national escape clause (Articles 25 and 26 of Regulation 2024/1263). Of the national clause: "This clause was
  introduced by the 2024 reform of the Stability and Growth Pact."
- Defence: activation was proposed in the Communication of 19 March 2025, for up to 1.5 percent of GDP until 2028. Nineteen member states
  requested it and the Council activated it for them.
- It was broadened to energy security on 3 June 2026 and 18 August 2026 (Greece, Italy [and Portugal]).
- National medium-term fiscal-structural plans cover 4–5 years.

### EA-EU-6. Mario Draghi, *The future of European competitiveness – Part A: A competitiveness strategy for Europe*, September 2024
Listing: https://commission.europa.eu/topics/eu-competitiveness/draghi-report_en (200) → Part A PDF (200; 73 PDF pages; printed = PDF − 2).
Read: Foreword (p. 5), p. 63.
- p. 5:
  - real disposable income per head grew almost twice as much in the US;
  - only four of the top 50 tech firms are European;
  - the investment share must rise by about 5 points;
  - "This is an existential challenge."
- p. 63: "a minimum annual additional investment of EUR 750 to 800 billion is needed" (4.4–4.7 percent of EU GDP), against 1–2 percent for
  the Marshall Plan.

### EA-EU-7. European Commission, *Autumn 2026 Economic Forecast*, 17 November 2026
Listing: https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/economic-forecasts_en (200) → forecast page (200). The listing
starts in 2015, so no spring 2008 forecast is available.
- Euro-area forecasts:

  | | 2026 | 2027 | 2028 |
  |---|---|---|---|
  | GDP (%) | 1.2 | 1.2 | 1.3 |
  | Inflation (%) | 3.2 | 3.1 | 2.1 |
  | Budget balance (% of GDP) | −3.5 | −3.6 | −3.8 |
  | Unemployment (%) | 6.4 | 6.5 | 6.6 |

- "In October, euro area inflation rose to 4.0%, from 3.8% in September.", with energy prices up 21 percent.
- Policy rates rose 25 bp in June and in September. Markets expect the DFR to peak around 3.4 percent by mid-2027.

### EA-EU-8. European Commission (DG Trade), "EU trade relations with India" and "EU-India agreement" pages
https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/india_en (200) and
…/india/eu-india-agreement_en (200).
- Negotiations relaunched on 17 June 2022. On 27 January 2026 "the EU and India concluded negotiations for a Free Trade Agreement". On 11
  September 2026 the Commission presented it to the Council for signature.
- Tariffs will be cut on more than 96 percent of EU goods exports, saving about €4 bn a year. The EU's FDI stock in India was €132.8 bn in
  2024.
- Discrepancy: one page calls the EU India's "third-largest trading partner" (€118 bn in 2025, 11.1 percent); the other calls it the largest
  (€120 bn in 2024, 11.5 percent). Cite both with their years.
- On 16 November 2026 the EU imposed anti-dumping duties on cold-rolled steel from India and other countries.

## Data already in the book

### EA-OTH-1. ECB rate, yield and HICP series held in `data/clean/ecb/`, plus FRED and Eurostat series — own reading
- ECB_DFR:
  - minimum −0.5 percent (from September 2019);
  - maximum 4.0 percent (September 2023);
  - 2.0 (June 2025), 2.25 (June 2026) and 2.5 percent (September 2026).
- Ten-year yields:
  - peaks: Greece 29.24 percent (February 2012), Portugal 13.849 (January 2012), Ireland 12.45 (July 2011);
  - October 2026: Greece 4.41, Italy 4.68, Germany 3.416, Spain 4.066, Portugal 3.917, Ireland 3.5525.
- EA_HICP: peak 10.6 percent (October 2022); the last observation is 1.9 percent (December 2025).
- Also held: FRED DEXUSEU, ECBASSETSW, PNGASEUUSDM and CLVMNACSCAB1GQEA19; Eurostat EA_HICP_ANR. `data/clean/india` has no series for
  exports to the EU.

## India and the euro area

### EA-IN-1. *Economic Survey 2012-13*, Chapter 6 "Balance of Payments" and Chapter 7 "International Trade" (on disk)
Read: Box 6.1 (p. 135), Box 7.3 (p. 158), pp. 159, 168. Boxes 6.1 and 6.2 are already ES12-9 and ES12-13; only the new points are listed here.
- p. 135 (Box 6.1): "The fallout for the Indian economy has been a sharp deceleration in exports".
- p. 158 (Box 7.3): "India has been fairly successful in diversifying its export markets". Europe's share of India's exports was 25.9
  percent (2000-01), 24.2 (2005-06), 19.0 (2011-12) and 18.7 (April–November 2012-13).
- p. 159: the euro-zone crisis and the Chinese slowdown hit India's exports harder than the 2009-10 shock did.
- p. 168: the India–EU BTIA had gone through 15 rounds, the 15th held on 4–7 December 2012.

### EA-IN-2. *Economic Survey 2014-15*, Vol. 1, Chapter 1 (on disk)
Read: pp. 16–17 (PDF 22–23).
- p. 16: one of four external risks was "possible turmoil if the viability of the Eurozone were to come into question" after a Greek exit.
  p. 17: India was now more resilient.
- Vol. 2, PDF p. 166 (printed page not checked): the rupee had appreciated against the euro and the yen since September 2014.

### EA-IN-3. *Economic Survey 2023-24*, Chapter on climate and energy transition (on disk)
- p. 160 (PDF 207): Europe was on course to apply a "Carbon Border Adjustment Tax", against the spirit of common but differentiated
  responsibilities (CBDR): "These taxes are in contravention to the spirit of the Paris Agreement". CBAM is also mentioned at PDF p. 507.

### EA-IN-4. *Economic Survey 2024-25*, Chapter 3 "External Sector", Box III.2 on CBAM (on disk)
Read: pp. 88–89 (PDF 133–134).
- CBAM reporting began on 1 January 2024 and the levy on 1 January 2026, covering steel, aluminium, cement and fertilisers. "CBAM is
  effectively a carbon price equalisation measure."
- The CBAM-covered share of India's exports to the EU rose from 6.3 percent (2014) to 10.5 percent (2023). Table III.1: iron and steel rose
  from $2,962.6 mn to $5,557.1 mn, aluminium from $151.4 mn to $1,801 mn.
- India's score on the World Bank exposure index is 0.03. CBAM risks "negating the comparative advantage of developing members like India".

### EA-IN-5. *Economic Survey 2025-26* (January 2026), Preface and chapters on statecraft, climate and globalisation (on disk)
- p. xii (Preface): India concluded a "free trade agreement with the European Union after three years of negotiations". The agreement needs
  ratification by the European Parliament (also in ES25-10 and TR-IN-5).
- p. 88: CBAM is "fully effective from 2026", "targeting high-pollution exporters (e.g., China, India) as classified under EU methodology".
- p. 450: CBAM replaces free allocation of allowances from 2026.
- p. 687 (para 16.27): carbon border mechanisms are among the signs of "the end of naïve globalisation".

### EA-IN-6. *Economic Survey 2025-26*, Statistical Appendix, Tables 5.4, 6.4(A) and 6.4(B) (on disk)
- Table 6.4(B), p. 139 (exports):
  - to the EU: $75.937 bn (2023-24) and $75.854 bn (2024-25), a share of 17.33 percent;
  - Europe as a whole: 22.49 percent;
  - the Netherlands: $22.8 bn;
  - April–November 2025-26: EU $48.989 bn (−3.97 percent).
- Table 6.4(A), p. 128: imports from the EU were $60.681 bn in 2024-25 (8.4 percent), so India's surplus with the EU was about $15.2 bn (own
  arithmetic).
- Table 5.4, pp. 110–111, rupees per euro:

  | Period | Rs per euro |
  |---|---|
  | 2000-01 | 41.483 |
  | 2007-08 | 57.060 |
  | 2008-09 | 65.058 |
  | 2011-12 | 65.894 |
  | 2013-14 | 81.175 |
  | 2015-16 | 72.289 |
  | 2020-21 | 86.584 |
  | 2024-25 | 90.760 |
  | September 2025 | 103.644 |
  | November 2025 | 102.713 |

## Synthesis

1. **Before 2008 the official verdict was success, with divergence noticed but treated as slow-moving.**
   - IMF 2004: fundamentals "seem relatively sound" (EA-IMF-1 p. 39).
   - IMF 2006: divergences "might take a painfully long time to unwind" (EA-IMF-2 p. 26).
   - IMF 2007: "The outlook is the best in years." (EA-IMF-3 p. 1).
   - IMF 2008: monetary union was "a distinct and promising success" (EA-IMF-4 p. 21).
   - Commission 2008: "a major success", while noting accumulated competitiveness losses (EA-EU-1 PDF p. 5, p. 6).
   - Meanwhile Greece's current-account deficit reached 14 percent of GDP in 2008 (EA-EU-2 p. 3).
2. **The ECB tightened into the crash.**
   - 3 July 2008: rates up to 4.25 percent, with "no major imbalances" (EA-ECB-1).
   - 8 October 2008: a coordinated cut of 50 bp (EA-ECB-2).
   - 2009: GDP −4.1 percent, against the IMF's +1.2 projection a year earlier (EA-IMF-5 p. 42; EA-IMF-4 p. 39).
3. **2010 reframed the problem as one of governance.** The IMF called the crisis "a wake-up call" and said divergences had been "allowed to
   fester" (EA-IMF-5 PDF p. 2, pp. 24–25). The first backstops were improvised: the €60 bn EFSM, then the EFSF (EA-IMF-5 p. 12).
4. **Greece: the programme projections failed badly.**
   - 2010: debt was to peak at 149 percent of GDP in 2013 and fall to 120 percent by 2020 (EA-IMF-14 PDF p. 3, p. 35).
   - Outturn: real GDP in 2012 was 17 percent below 2009, against a projected 5½ percent (EA-IMF-15 p. 12).
   - Private debt was cut 60 percent in 2012 (EA-IMF-15 p. 14; EA-EU-3), and two further programmes followed (€164.5 bn and €86 bn; EA-EU-3).
   - Debt was 209.9 percent of GDP in 2020 and 150.8 percent in 2024 (EA-IMF-16 p. 26).
5. **Words did what money had not, and the institutions followed.**
   - The 2012 IMF report saw the union's viability in question and banking union as "the first priority" (EA-IMF-6 PDF p. 2).
   - Draghi's "whatever it takes" (EA-ECB-3) and OMT, with "No ex ante quantitative limits" (EA-ECB-4), came weeks later.
   - Ten-year Greek yields had peaked at 29.24 percent in February 2012 (EA-OTH-1); by 2014 spreads were back to pre-crisis levels (EA-IMF-7
     p. 23).
6. **Then a lowflation decade.**
   - IMF 2014: "Inflation has been too low for too long." (EA-IMF-7 p. 24).
   - Negative rates from June 2014 (EA-ECB-5) and QE from January 2015 (EA-ECB-6).
   - CPI was 0.0 percent in 2015, against the 1.2 percent the IMF had projected (EA-IMF-9, CR 18/223 p. 4; EA-IMF-7 p. 26).
   - The DFR reached −0.5 percent in 2019 (EA-OTH-1), and the IMF warned of "anemic growth and inflation" (EA-IMF-9 PDF p. 6).
7. **External surplus, internal slack.** The current account moved from about balance (0.1 percent of GDP in 2011) to 3.6 percent in 2016
   (EA-IMF-7 p. 26; EA-IMF-9), as deficit countries adjusted by compressing demand. Germany's surplus had already risen 4½ points by 2004
   (EA-IMF-1 p. 7).
8. **The pandemic produced joint borrowing.** PEPP brought €750 bn (EA-ECB-7). NGEU brought €806.9 bn, repaid 2028–2058 (EA-EU-4). Greek
   bonds were bought under a waiver (EA-ECB-7).
9. **The 2021–22 inflation call was wrong, and the energy shock was a terms-of-trade loss.**
   - December 2021: the IMF projected 3.0 percent for 2022 (EA-IMF-10 p. 3).
   - Outturn: 8.4 percent (EA-IMF-11 p. 3), with HICP peaking at 10.6 percent in October 2022 (EA-OTH-1).
   - The IMF called it "the largest terms of trade loss in several decades" (EA-IMF-11 PDF p. 5).
   - The ECB raised rates from July 2022 and created the TPI (EA-ECB-8); the DFR peaked at 4.0 percent (EA-OTH-1).
10. **New fiscal rules, and a second inflation wave in 2026.**
    - The 2024 framework uses an expenditure rule with debt safeguards (EA-IMF-12 p. 71). Escape clauses were activated for defence in
      2025 and for energy security in 2026 (EA-EU-5).
    - After cutting to 2.0 percent by June 2025, the ECB raised the DFR to 2.25 in June 2026 and 2.5 in September 2026 (EA-ECB-9, EA-ECB-10).
    - Euro-area inflation was 4.0 percent in October 2026, and the Commission forecasts 3.2 percent for 2026 (EA-EU-7). The IMF's June
      projection had been 2.9 percent (EA-IMF-13 p. 4).
11. **The long-run problem is productivity.** Draghi called it "an existential challenge" and asked for €750–800 bn a year of extra
    investment (EA-EU-6 pp. 5, 63). The IMF repeats the point, citing "persistently weak potential growth" (EA-IMF-13 PDF p. 6; EA-IMF-12 PDF
    p. 5).
12. **For India, Europe mattered first as a demand shock, then as a rule-maker.**
    - Demand: the euro crisis was blamed for India's 2011-12 slowdown (ES11-2, ES12-1) and for slower exports (EA-IN-1 pp. 135, 159).
      Europe's share of India's exports fell from 25.9 percent (2000-01) to 18.7 (2012-13) (EA-IN-1 p. 158), but Europe still took 22.49
      percent in 2024-25 (EA-IN-6 p. 139).
    - Rules: CBAM (EA-IN-3, EA-IN-4, EA-IN-5).
    - Trade agreement: BTIA talks of 2007–2012 (EA-IN-1 p. 168), then an FTA concluded on 27 January 2026 but not yet signed (EA-EU-8;
      EA-IN-5 p. xii; EA-IMF-13 p. 8).
    - Exchange rate: the rupee went from 41.5 per euro to over 100 (EA-IN-6 Table 5.4).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2004 | IMF (EA-IMF-1 p. 39) | Area-wide fundamentals "seem relatively sound" | Greek CA deficit peaked at 14% of GDP in 2008 (EA-EU-2 p. 3); IMF in 2010: divergences "allowed to fester" (EA-IMF-5 p. 24) |
| 2007 | IMF (EA-IMF-3 p. 1) | "The outlook is the best in years." | GDP −4.1% in 2009 (EA-IMF-5 p. 42) |
| 2008 | IMF (EA-IMF-4 p. 39) | 2009 GDP +1.2%, debt 64.4% of GDP | 2009 GDP −4.1%, debt 79.0% (EA-IMF-5 p. 42) |
| Jul 2008 | ECB (EA-ECB-1) | Hike to 4.25%; "the euro area does not suffer from major imbalances" | Coordinated 50 bp cut by 8 Oct 2008 (EA-ECB-2); Greek 10-yr yield 29.24% in Feb 2012 (EA-OTH-1) |
| 2008 | Commission EMU@10 (EA-EU-1) | "a major success" | Two years later the IMF called the crisis "a wake-up call" (EA-IMF-5 PDF p. 2) |
| 2010 | IMF Greece SBA (EA-IMF-14 p. 35) | Debt peaks at 149% of GDP in 2013, 120% by 2020 | 2012 PSI cut privately held debt 60% (EA-IMF-15 p. 14); debt still 209.9% in 2020 (EA-IMF-16 p. 26) |
| 2010 | IMF Greece SBA (EA-IMF-15 p. 12, on the SBA) | Real GDP 5½% lower in 2012 than 2009; unemployment 15% | 17% lower; unemployment 25% (EA-IMF-15 p. 12) |
| 2012 | IMF (EA-IMF-6 p. 33) | 2013 GDP +0.7% | 2013 GDP −0.4% (EA-IMF-7 p. 26) |
| 2014 | IMF (EA-IMF-7 p. 26) | 2015 CPI 1.2% | 2015 CPI 0.0% (CR 18/223 p. 4, EA-IMF-9); "widespread deflation in early 2015" (EA-IMF-8 p. 4) |
| Dec 2021 | IMF (EA-IMF-10 p. 3) | Inflation "transitory"; 2022 CPI 3.0% | 2022 CPI 8.4% (EA-IMF-11 p. 3); HICP peak 10.6% in Oct 2022 (EA-OTH-1) |
| 2023 | IMF (EA-IMF-11 PDF p. 5) | Inflation back to target by mid-2025 | 2.1% in 2025 (EA-IMF-13 p. 4), but 4.0% in Oct 2026 and 3.2% forecast for 2026 (EA-EU-7) |
| Jun 2026 | IMF (EA-IMF-13 p. 4) | 2026 CPI 2.9%; DFR 2.5% by end-2026 (p. 10) | DFR 2.5% reached in Sep 2026 (EA-ECB-10); markets expect a peak of about 3.4% by mid-2027 (EA-EU-7) |
| 2011 | India: ES 2010-11 (ES10-10 p. 21) | 9% growth in 2011-12; a double dip very unlikely | 6.2% (ES12-1); the euro-zone crisis named as a cause (ES11-2; EA-IN-1 p. 159) |
| 2013 | India: ES 2012-13 (EA-IN-1 p. 158) | Exports diversifying away from Europe (share down to 18.7%) | Europe 22.49%, EU 17.33% of exports in 2024-25 (EA-IN-6 p. 139) |
| 2013 | India: ES 2012-13 (EA-IN-1 p. 168) | BTIA after 15 rounds | FTA concluded 27 Jan 2026; presented to the Council for signature on 11 Sep 2026, still unsigned (EA-EU-8; EA-IMF-13 p. 8) |
| 2015 | India: ES 2014-15 (EA-IN-2 p. 16) | Risk of "turmoil" from a Greek exit | Greece stayed in: €86 bn ESM programme, completed 21 Aug 2018 (EA-EU-3) |
| 2025 | India: ES 2024-25 (EA-IN-4 p. 88) | CBAM exposure: 10.5% of exports to the EU | Levy in force from 2026 (EA-IN-5 p. 88); EU anti-dumping duties on Indian cold-rolled steel, 16 Nov 2026 (EA-EU-8) |

### Candidate quotes (all verified by script against the converted text)

- "seem relatively sound" (IMF 2004, EA-IMF-1 p. 39)
- "potential growth has weakened appreciably" (EA-IMF-1 p. 39)
- "might take a painfully long time to unwind" (IMF 2006, EA-IMF-2 p. 26)
- "The outlook is the best in years." (IMF 2007, EA-IMF-3 p. 1)
- "The external position remains roughly balanced" (EA-IMF-3 p. 25)
- "monetary union is a distinct and promising success" (IMF 2008, EA-IMF-4 p. 21)
- "policy rates are best kept on hold" (EA-IMF-4 p. 21)
- "The current crisis is a wake-up call for the euro area." (IMF 2010, EA-IMF-5 PDF p. 2)
- "divergences in economic performance have been allowed to fester" (EA-IMF-5 p. 24)
- "raising questions about the viability of the monetary union itself" (IMF 2012, EA-IMF-6 PDF p. 2)
- "the first priority is a banking union for the euro area" (EA-IMF-6 PDF p. 2)
- "Inflation has been too low for too long." (IMF 2014, EA-IMF-7 p. 24)
- "Quantitative easing (QE) has boosted confidence and improved financial conditions." (IMF 2015, EA-IMF-8 PDF p. 5)
- "a prolonged period of anemic growth and inflation" (IMF 2019, EA-IMF-9 PDF p. 6)
- "is projected to moderate during 2022 and remain below the ECB’s inflation target" (IMF Dec 2021, EA-IMF-10 PDF p. 5)
- "the largest terms of trade loss in several decades" (IMF 2023, EA-IMF-11 PDF p. 5)
- "Energy-intensive industries, in particular, have struggled to adjust to higher input costs" (IMF 2024, EA-IMF-12 PDF p. 5)
- "Europe’s persistently weak potential growth that reflects subdued productivity growth and aging" (IMF 2026, EA-IMF-13 PDF p. 6)
- "The EU has concluded additional free trade agreements with Australia, India, and Indonesia" (EA-IMF-13 p. 8)
- "The Greek economy is teetering due to heavy public debt" (IMF 2010, EA-IMF-14 PDF p. 3)
- "the debt-ratio would peak at 149 percent of GDP in 2013" (EA-IMF-14 PDF p. 3)
- "the baseline macro projections can also be criticized for being too optimistic" (IMF 2013, EA-IMF-15 p. 2)
- "Market confidence was not restored" (EA-IMF-15 p. 1)
- "real GDP in 2012 was 17 percent lower than in 2009" (EA-IMF-15 p. 12)
- "the ECB is ready to do whatever it takes to preserve the euro" (Draghi, 26 July 2012, EA-ECB-3)
- "And believe me, it will be enough." (EA-ECB-3)
- "No ex ante quantitative limits are set on the size of Outright Monetary Transactions." (EA-ECB-4)
- "the euro area does not suffer from major imbalances" (Trichet, 3 July 2008, EA-ECB-1)
- "to address the risks of a too prolonged period of low inflation" (ECB, 22 Jan 2015, EA-ECB-6)
- "will not tolerate any risks to the smooth transmission of its monetary policy" (ECB, 18 Mar 2020, EA-ECB-7)
- "unwarranted, disorderly market dynamics that pose a serious threat to the transmission" (TPI, EA-ECB-8)
- "it is now appropriate to moderate the degree of monetary policy restriction" (ECB, 6 June 2024, EA-ECB-9)
- "inflation is set to remain well above target for an extended period" (ECB, 10 Sep 2026, EA-ECB-10)
- "The Economic and Monetary Union and the euro are a major success." (EMU@10, EA-EU-1 PDF p. 5)
- "This has led to accumulated competitiveness losses and large external imbalances" (EA-EU-1 p. 6)
- "growth performance of Greece over the last decade was based on unsustainable drivers" (EA-EU-2 p. 3)
- "This is an existential challenge." (Draghi report, EA-EU-6 p. 5)
- "a minimum annual additional investment of EUR 750 to 800 billion is needed" (EA-EU-6 p. 63)
- "In October, euro area inflation rose to 4.0%, from 3.8% in September." (Commission, 17 Nov 2026, EA-EU-7)
- "the EU and India concluded negotiations for a Free Trade Agreement" (EU trade page, EA-EU-8)
- "This clause was introduced by the 2024 reform of the Stability and Growth Pact." (EA-EU-5)
- "The fallout for the Indian economy has been a sharp deceleration in exports" (ES 2012-13, EA-IN-1 p. 135)
- "India has been fairly successful in diversifying its export markets" (ES 2012-13, EA-IN-1 p. 158)
- "possible turmoil if the viability of the Eurozone were to come into question" (ES 2014-15, EA-IN-2 p. 16)
- "These taxes are in contravention to the spirit of the Paris Agreement" (ES 2023-24, EA-IN-3 p. 160)
- "CBAM is effectively a carbon price equalisation measure." (ES 2024-25, EA-IN-4 p. 88)
- "thereby negating the comparative advantage of developing members like India" (ES 2024-25, EA-IN-4 p. 88)
- "free trade agreement with the European Union after three years of negotiations" (ES 2025-26, EA-IN-5 p. xii)
- "targeting high-pollution exporters (e.g., China, India) as classified under EU methodology" (ES 2025-26, EA-IN-5 p. 88)

Short phrases quoted inside the item notes but not run through the script ("in abeyance", "procedural limbo", "stretched housing sectors",
"anchor of stability", "could tip the economy into deflation", "transitory factors", "on a firm downward trajectory", "notable failures",
"the end of naïve globalisation", "the economic fundamentals of the euro area are sound", "will do everything necessary within its mandate")
were read in the source, but they should be rechecked before they are printed as quotations.

## Not obtained

- **IMF euro-area listing.** No IMF country or series page for the euro area exists. All of these return 404:
  - https://www.imf.org/en/Countries/EUQ, /EUR, /EMU, /XEU, /Euro-Area, /euro-area and /ResRep/EUQ;
  - https://www.imf.org/en/Publications/SPROLLs/Euro-Area (and variants) and /Publications/Search?… ;
  - https://imf.org/europe and /en/regional-offices/europe.

  All euro-area Article IVs are therefore GUESSED URLs (title pages confirmed).
- **IMF 2022 euro-area Article IV (July 2022)**: …/cr/2022/english/1eurea2022002.pdf, 003.pdf and 004.pdf (GUESSED) — all 404. Other 404s:
  …/2025/english/1eurea2025001.pdf, …/2026/english/1eurea2026002.pdf, and the codes euz, euq, xeu, ema and eua.
- **ESM.** https://www.esm.europa.eu/ and https://www.esm.europa.eu/financial-assistance/greece — 403 (CloudFront "Request blocked"). Not
  pursued, so the ESM Treaty and ESM programme documents were not obtained. The programme facts above come from the Commission (EA-EU-3).
- **Council, Eurogroup and Euro Summit.** These all return 403 ("Browser check"):
  - https://www.consilium.europa.eu/en/policies/eurogroup/;
  - https://www.consilium.europa.eu/media/45109/210720-euco-final-conclusions-en.pdf (GUESSED);
  - https://www.consilium.europa.eu/media/20353/20150712-eurosummit-statement-greece.pdf (GUESSED).

  As a result the following were not obtained: the July 2020 European Council conclusions on NGEU, the Eurogroup statements of May 2010 and
  February 2012, and the Euro Summit statement of 12 July 2015.
- **EUR-Lex, Regulation 2024/1263.** https://eur-lex.europa.eu/eli/reg/2024/1263/oj and
  https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1263 — 202 with an empty body. The rules are taken from the IMF
  (EA-IMF-12 Annex III) and Commission pages (EA-EU-5).
- **Commission RRF page.** …/recovery-and-resilience-facility_en — 200, but only a language-selection stub. RRF figures come from the NGEU
  page (EA-EU-4).
- **Commission Spring 2008 forecast.** It is not on the forecasts listing, which starts in 2015. A GUESSED publication12553_en.pdf returned an
  HTML page, not the PDF.
- **Commission Greece pages.** The guessed Greece-assistance pages on economy-finance.ec.europa.eu and commission.europa.eu returned 404;
  the page was found through the listing instead (EA-EU-3).
- **Indian official sources.** https://www.commerce.gov.in/ is a script shell (200, 9,274 bytes). PIB allRel.aspx and indexd.aspx return 200
  but show only current releases; no release on the India–EU FTA or CBAM was found.
- **Not read** (obtained or listed): the Commission's 2023 ex-post evaluation of Greece; the ECB decisions of 5 February, 19 March and 30 April
  2026; IMF CR 11/184, 13/231 and 25/203; ES 2014-15 Vol. 2 printed page for the rupee–euro point. The ECB Monthly or Economic Bulletin was
  not fetched.
- **India's exports to the EU before 2023-24.** No such series is held in `data/clean/india`. Only Europe's share in ES 2012-13 Box 7.3 is
  available (EA-IN-1).
