# Reading notes: country lens "India, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies, no form postbacks). URLs were
taken from publisher listing or issue pages where possible: the imf.org India country page (https://www.imf.org/en/Countries/IND, 200; its
`index.md` version, 200) links only the 2025 Article IV issue page; the IMF DataMapper API (`/external/datamapper/api/v1/…`, 200); the RBI
Annual Report 2025-26 HTML chapters (`/Scripts/AnnualReportPublications.aspx?Id=1460–1467`, all 200); the World Bank "World Bank Country
and Lending Groups" help page (datahelpdesk.worldbank.org, 200), which links the historical classification file; the World Bank India
country page (https://www.worldbank.org/en/country/india, 200), which links the latest India Development Update and the 2025 Country
Economic Memorandum; and the World Bank Documents & Reports search API (search.worldbank.org/api/v2 and v3, 200). **The IMF country page
lists no India Article IV before 2025**, so every earlier staff report (IN-IMF-1 to IN-IMF-14) comes from a GUESSED URL built on the IMF's
file-naming pattern: `/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/YYYY/crYYNNN.pdf` in 2017 and 2018;
`/-/media/files/publications/cr/YYYY/english/1indeaYYYYnnn.pdf` from 2019 (India code "ind"; the February 2025 report needed the suffix
`-print-pdf`). For each file the title page and "Country Report No." were read to confirm it is the India Article IV named; a wrong hit
(CR 20/208, a Tamil Nadu technical-assistance report) was discarded (see Not obtained). Downloads are in the session scratchpad folder
`lens_india_dl/`, one subfolder per batch: `imf/` (country page, DataMapper JSON) and `imf/g/` (staff reports), `rbi/`, `wb/`, `oth/`
(empty). PDFs were converted with `pdftotext` (plain and `-layout`); HTML pages were stripped of tags and read as text. Python that read
downloads was run with `python3 -I`, from scripts kept outside the download folder. Economic Survey texts were **not refetched**: they were
read from the Econ Subject folder (`sources/text/es*.txt`, where text page = PDF page = "st."), and the printed page number was taken from
the running header or footer. Quotes are verbatim and under 15 words, and a script checked each one against the converted text (whitespace-,
quote- and line-end-hyphen-normalised). Everything else is paraphrase. Page numbers are printed page numbers unless stated; "PDF p." is used
for unnumbered pages (the Key Issues pages and Board press releases at the front of IMF reports). Rankings, shares and ratios computed from
IMF or World Bank data are marked "own reading" or "own arithmetic".

Printed-page offsets for IMF reports: CR 06/55, 08/51, 09/187: printed = PDF − 2. CR 11/50, 13/37, 14/57: printed = PDF − 1. CR 16/75,
17/54, 18/254, 23/426: printed = PDF − 5. CR 19/385: printed = PDF − 6. CR 21/230, 22/386, 25/54, 25/314: printed = PDF − 4. World Bank
India Development Update March 2018: printed = PDF − 1.

Item labels:
- IN-IMF-n: IMF Article IV consultations with India; the IMF India page; IMF DataMapper (WEO October 2026).
- IN-RBI-n: Reserve Bank of India (new items only; the RBI framework documents are already in the book, see below).
- IN-GOV-n: Economic Surveys (on disk, not refetched) on India's rank and services share.
- IN-WB-n: World Bank (income classification, GNI per capita, India Development Updates, Country Economic Memorandum).
- No IN-OTH item was needed: the WTO services-share figure is already in the book (TR-WTO-3).

Indian years are fiscal years (April–March). IMF tables use "2024/25" for FY2024-25; IMF WEO India figures are on a fiscal-year basis (the
"2025" column is FY2025/26). Growth outturns are quoted by vintage, because India's GDP was rebased twice in the period (2011-12 base from
January 2015; 2022-23 base from 27 February 2026) and early estimates were revised heavily.

Abbreviations: AE = advance estimate; AR = RBI Annual Report; CAD = current account deficit; CEM = Country Economic Memorandum; CR = IMF
Country Report; ED = IMF Executive Director; FIT = flexible inflation targeting; FSR = Financial Stability Report; GNPA = gross
non-performing assets; IBC = Insolvency and Bankruptcy Code; IDU = India Development Update; LMI = lower-middle income; MPC = Monetary Policy
Committee; NPA = non-performing asset; PSB = public sector bank; WEO = IMF World Economic Outlook.

Already in the book (cite, do not duplicate):
- **Economic Surveys, every year 2001-02 to 2025-26**: `India_ES_2001-2003.md`, `India_ES_2003-2008.md`, `India_ES_2010-2014.md`,
  `India_ES_2015-2020.md`, `India_ES_2020-2022.md`, `India_ES_2022-2024.md`, `India_ES_2024-2026.md`, each with a "Cross-Survey reference
  figures" table (growth by vintage, CPI/WPI, repo path, fiscal deficit, CAD, reserves, rupee, GNPA). Key items for the long run:
  high-growth years ES05-1, ES06-2 ("Taken off"), GDP 9.4/9.6/8.7% in 2005-06 to 2007-08 (`India_ES_2003-2008.md` reference table);
  slowdown and taper ES11-1, ES13-1 to ES13-15, ES14-1/ES14-2 (near-crisis of July–August 2013), ES14-7 (new GDP series rewrites 2012-14);
  twin balance sheet ES15-11, ES16-8; demonetisation ES16-3, ES16-4, ES17-7; GST and IBC ES16-11, ES17-1, ES17-14, ES18-12, ES19-11; FIT
  codified ES16-13; pandemic ES20-3, ES20-10, ES22-2; "fastest-growing major economy" and fifth-largest ES22-12, ES22-13, ES23-20;
  potential and Viksit Bharat ES24-13, ES25-5; tariffs ES25-6, ES25-7; GST 2.0 ES25-18; rebasing ES25-4. GNPA path 2.36% (March 2011) →
  11.5/11.2% (March 2018) → 2.2% (September 2025) is in the reference tables and GR-IN-6.
- `India_2026.md`: the 2026 energy shock; MPC holds at 5.25% (April, June, August) and the **7 October 2026 rise to 5.50%** (IN26-21 to
  IN26-25), the latest policy statement; FY26 GDP 7.6% on the new base (IN26-36); reserves; RBI AR 2025-26 Chs I–III, V; IMF India page
  note that no 2026 Article IV is published (Not found). **Not refetched here.**
- `Theme_money.md` MO-IN-1 (Urjit Patel Committee, 21 January 2014: 4% ± 2, glide path 8% in 12 months and 6% in 24 months), MO-IN-2 (RCF
  2020-21: 4% ± 2 "appropriate"), MO-IN-3 (Finance Act 2016; target notified 5 August 2016; retained 31 March 2021 and 25 March 2026),
  MO-IN-4 (August 2025 discussion paper: CPI 7.4% pre-FIT vs 4.4% in the first FIT period; 2014 glide path "overachieved"), MO-IN-5.
  **Not refetched.**
- `Theme_growth.md` GR-IN-1 (ES 2007-08: higher growth path, Tenth Plan 7.8%), GR-IN-2 (ES 2013-14), GR-IN-3 (ES 2015-16: potential 8–10%),
  GR-IN-4 (ES 2022-23: 6.5%), GR-IN-5 (ES 2024-25: about 8% needed), GR-IN-6 (ES 2025-26 Box I.4: potential about 7%).
- `Theme_debt.md` DF-IN-1, DF-IN-2 (FRBM; N.K. Singh committee), DF-IN-3/4 (debt anchor 50±1% by FY2030-31), DF-IN-5, DF-IN-6, **DF-IN-7 (IMF
  2025 Article IV, CR 25/314: fiscal section, general government debt 80.7–83.5% of GDP 2021/22–2026/27)**, DF-IN-8 (16th Finance
  Commission).
- `Theme_development.md` DV-WB-3 (June 2025 PIP update: India at $3.00 27.12% in 2011-12 → 5.25% in 2022-23), **DV-WB-13 (Poverty & Equity
  Brief India, October 2026: $3.00 poverty 27.1% (2011) → 2.6% (2023); $4.20 57.7% → 16.1%; with the 2022 and 2024 briefs)**, DV-WB-15, DV-IN-1
  (NITI MPI), DV-IN-2 (ES 2025-26 ch. 13). **Poverty is not re-read here.**
- `Theme_trade.md` TR-WTO-3 (WTO, October 2026, Appendix Table 3 p. 42: India eighth services exporter in 2025, US$412 bn, 4.3% of world;
  19th merchandise exporter, 1.7%); TR-WTO-1 p. 28 (India second IT-services exporter in 2017); TR-IN-1 (ES 2019-20: merchandise share 0.6%
  (1991) → 1.7% (2018)); TR-IN-4, TR-IN-5, TR-IN-6.
- `Theme_technology.md` TE-IN-1 to TE-IN-12 (software exports from 2001, JAM, UPI, AI); `Theme_demography.md` DL-IN-1 to DL-IN-9;
  `Theme_energy.md` EN-IN-1 to EN-IN-9; `Theme_markets.md` MK-IN-1 to MK-IN-12.
- Lenses: `Lens_china.md` CN-IN-1 to CN-IN-8 (China's share of India's imports; manufacturing comparison); `Lens_us.md` US-IN-1 to US-IN-9
  (2025 tariffs and the February 2026 deal); `Lens_euro.md` EA-IN-1 to EA-IN-6; `Lens_japan.md` JP-IN-1 to JP-IN-10.
- IMF WEO India projections by edition: `IMF_2000-2002.md` to `IMF_2026.md` (India threads at the end of each; e.g. `IMF_2003-2006.md`: India
  repeatedly revised up, 2003 projected 5.1 → 7.4; `IMF_2010-2014.md`: October 2013 cut to 3¾%; `IMF_2020-2021.md`: 2020 forecasts 1.9 →
  −4.5 → −10.3; `IMF_2026.md`: WEO July 2026 p. 6 India "remains among the fastest-growing major economies"; WEO October 2026 Table 1.1 p. 10:
  India 7.8/7.0/7.0 for FY2025/26–FY2027/28, and p. 15 "India stands out with upward revisions" in medium-term growth).

## IMF Article IV consultations with India

### IN-IMF-1. IMF, *India: 2005 Article IV Consultation—Staff Report; Staff Statement; Public Information Notice…*, IMF Country Report No. 06/55, February 2006 (staff report dated 22 December 2005; Board 6 February 2006)
PDF: https://www.imf.org/external/pubs/ft/scr/2006/cr0655.pdf (GUESSED; 200; 68 PDF pages). Read: front matter (pp. 1–3), Executive Summary
(p. 4), Staff Appraisal (pp. 27–29), Table 2 (p. 39), Table 9 (p. 46).
- p. 4: performance "impressive for the third year running"; growth above 8% y/y in H1 2005/06; projected to moderate to 6¾% in 2006/07 as
  the economy adjusts to high oil prices and rising rates. Staff pressed for tax-base broadening "by quickly … introducing a goods and services
  tax", subsidy reform and pension reform. "India’s growth spurt provides a golden opportunity" to fast-forward structural reform (labour
  laws, tariffs, FDI). Credit boom welcome as deepening, but regulation should tighten.
- p. 27 (para 41): "The Indian economy is reaping the rewards of the structural reforms" since the early 1990s; growth near 7% in 2004/05 and
  above 7½% expected for 2005/06. p. 28: the government aims at 8–10% growth; rupee close to fair value; two-way flexibility urged. p. 28
  (para 48): public debt "remains high"; recent improvement partly cyclical and oil costs shifted off-budget.
- Table 2, p. 39: nominal GDP 2004/05 US$691 billion, population 1.08 billion, GDP per capita US$640. General government deficit 9.7% (2002/03)
  → 7.4% (2004/05); general government debt 85.7–86.1% of GDP 2002/03–2005/06. Reserves US$141.5 bn (end-2004/05).
- Table 9, p. 46 (projections): real GDP (factor cost) 6.8% (2006/07), then 6.5% in each of 2007/08–2009/10; general government debt to
  fall to 80.4% by 2009/10; gross reserves US$171.1 bn by end-2009/10; CAD about 2–2½% of GDP.

### IN-IMF-2. IMF, *India: 2007 Article IV Consultation*, IMF Country Report No. 08/51, February 2008 (staff report dated 26 December 2007)
PDF: https://www.imf.org/external/pubs/ft/scr/2008/cr0851.pdf (GUESSED; 200; 80 PDF pages). Read: front matter (p. 1), Executive Summary (p. 3).
- p. 1: focus "managing financial globalization"; the authorities tightened monetary policy and debt/GDP fell "mainly due to rapid growth",
  but structural reform progress was limited.
- p. 3: "India’s dream run of strong growth and macroeconomic stability" credited to sound policy and past reforms; growth about 8½% for four
  years running; record capital inflows. Large inflows strain the "impossible trinity"; capital controls could dampen investment; greater
  exchange-rate flexibility and a corporate bond market recommended.

### IN-IMF-3. IMF, *India: 2008 Article IV Consultation*, IMF Country Report No. 09/187, June 2009 (staff report dated 22 January 2009)
PDF: https://www.imf.org/external/pubs/ft/scr/2009/cr09187.pdf (GUESSED; 200; 81 PDF pages). Read: front matter and contents (pp. 1–2),
Staff Appraisal and Summary (pp. 3–4).
- p. 2: section II is titled "First International Financial Crisis Since India Went Global".
- p. 3: "India’s growth is likely to slow sharply": from an average of 8¾% over five years to 6¼% in 2008/09 and 5¼% in 2009/10, led by
  investment; CAD about 3% of GDP in 2008/09; inflation below 3% by March 2009 and about 2% in 2009/10. With public debt at 80% of GDP,
  monetary and structural policies must carry the response.
- p. 4: banks well capitalised, low NPAs, but the downturn "likely to lead to a substantial increase in NPAs"; loss recognition and
  recapitalisation recommended; protectionism to be resisted.

### IN-IMF-4. IMF, *India: 2010 Article IV Consultation*, IMF Country Report No. 11/50, February 2011 (staff report dated 22 December 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2011/cr1150.pdf (GUESSED; 200; 86 PDF pages). Read: Executive Summary (p. 3), Context (p. 4),
Staff Appraisal (pp. 15–16), Table 7 (p. 27).
- p. 3: recovered from the crisis, but inflation elevated; prompt normalisation of monetary and fiscal stance needed; CAD widening.
- p. 4: Q3 2010 growth 8.9% y/y; inflation in an 8½–10½% range. p. 15 (para 45): "India’s growth remains among the strongest in the world"
  and medium-term prospects "favorable". p. 16: rupee broadly in line with fundamentals; appreciation should be the first line of defence
  against inflows.
- Table 7, p. 27 (outturns as of late 2010): real GDP (factor cost) 9.7 (2006/07), 9.2 (2007/08), 6.7 (2008/09), 7.4 (2009/10), 8.8
  projected 2010/11; **projections 8.1% in every year 2011/12–2014/15**; gross investment to rise to 44.0% of GDP by 2014/15; CAD 3.3–3.5%
  of GDP; reserves 279.1 (2009/10, end) → 419.2 projected (2014/15); general government debt 75.0% (2010/11) → 71.6% (2014/15).

### IN-IMF-5. IMF, *India: 2013 Article IV Consultation* (consultation concluded early 2013), IMF Country Report No. 13/37, February 2013 (staff report dated 21 December 2012)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr1337.pdf (GUESSED; 200; 94 PDF pages). Read: Key Issues (PDF p. 2), Context (p. 4),
Box 2 "Potential Growth" (p. 8), Table 2 (p. 36).
- PDF p. 2: the economy "has slowed markedly due to a confluence of structural, external and other factors"; subdued recovery with
  elevated inflation; switch to cash transfers welcomed; capital injections into public banks needed for Basel III; asset quality
  deteriorating.
- p. 4: growth averaging 8½% and social programmes cut poverty by 1.5 points a year in 2004–09, double the previous decade's pace; growth
  slumped to 5.4% in the first three quarters of 2012; the slowdown is unusual among EMs for its high inflation.
- p. 8 (Box 2): a year earlier, potential growth estimates were 8–9%, "with some forecasting India overtaking China"; the RBI lowered its
  estimate from 8% to 7%; staff estimates suggest "potential growth has declined to about 6½ percent" (range 6.2–6.8 across methods; no
  production-function estimate because of unreliable employment data).
- Table 2, p. 36: real GDP (factor cost) 6.7 (2008/09), 8.4 (2009/10), 8.4 (2010/11), 6.5 (2011/12); projections 5.4 (2012/13), 6.0 (2013/14).

### IN-IMF-6. IMF, *India: 2014 Article IV Consultation*, IMF Country Report No. 14/57, February 2014 (staff report dated 9 January 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr1457.pdf (GUESSED; 200; 95 PDF pages). Read: Key Issues (PDF p. 2), Context paras 1–5
(pp. 4–5), para 8 (p. 6).
- PDF p. 2: tightening global liquidity "heightened the focus" on high inflation, large current-account and fiscal deficits and supply
  bottlenecks. Growth expected at 4.6% in 2013/14, "the lowest level in a decade"; CPI near double digits; "India has very little room to
  adopt countercyclical policies". Rupee flexibility to be the first line of defence, with reserves, short-term rate rises and fiscal action.
- p. 4 (paras 1–3): growth averaged 8½% before and for two years after the GFC; about two-thirds of the slowdown is explained by domestic
  factors. In summer 2013 portfolio debt outflows hit currency, equity and bond markets; the response combined liquidity tightening, looser
  FDI/ECB limits, capital-flow measures and higher gold duties; then the RBI's dollar swaps for oil companies and banks (NRI deposit inflows)
  and the Fed's September decision calmed markets.
- p. 5: growth projected at 5.4% in 2014/15 (factor cost; 5.4% for calendar 2014 at market prices). p. 6 (para 8): "The current account
  deficit reached a record 4.8 percent of GDP in 2012/13" (oil, gold, supply constraints in coal and iron ore).

### IN-IMF-7. IMF, *India: 2016 Article IV Consultation*, IMF Country Report No. 16/75, March 2016 (staff report dated 27 January 2016)
PDF: https://www.imf.org/external/pubs/ft/scr/2016/cr1675.pdf (GUESSED; 200; 95 PDF pages). Read: Key Issues (PDF p. 6), pp. 4–6.
- PDF p. 6: recovery helped by a large terms-of-trade gain; monetary stance should stay tight on the RBI's glide path to 4%; the FY2015/16
  Union deficit target of 3.9% likely met; GST recommended; "NPAs on public banks’ balance sheets should be fully recognized".
- p. 4, footnote 1: the January 2015 new national accounts series revised up 2012/13–2013/14 growth "in part" through method changes; the
  lack of back-cast data "constrains a comparison of current growth with past growth".
- p. 5: growth 7.3% (FY2015/16) rising to 7.5% (FY2016/17). p. 6: medium-term growth "around 7¾ percent"; CPI 5.6% (December 2015), down
  from a 10% average in 2009–13.

### IN-IMF-8. IMF, *India: 2017 Article IV Consultation*, IMF Country Report No. 17/54, February 2017 (staff report dated 6 January 2017)
PDF: https://www.imf.org/-/media/files/publications/cr/2017/cr1754.pdf (GUESSED; 200; 108 PDF pages). Read: Key Issues (PDF p. 6), paras 1–2
(p. 4), para 6 (p. 6); Box on the currency exchange initiative (p. 29, searched).
- PDF p. 6: "Cash shortages arising from the currency exchange initiative have weakened the near-term outlook"; medium-term prospects
  improved by reforms. Priorities: full NPA recognition, stronger PSB buffers, debt recovery; inflation target of 5% by March 2017; FY2016/17
  deficit target 3.5%. Reforms credited: the GST constitutional amendment, "a new bankruptcy code", Aadhaar-based transfers.
- p. 4: growth bottomed at 5.6% (FY2012/13) and reached 7.6% (FY2015/16); after the 2013 taper tantrum, external vulnerabilities "now in
  check". The 8 November 2016 withdrawal of Rs 500 and Rs 1000 notes, "which accounted for 86 percent of the value of currency in
  circulation", strained consumption and business. p. 6: growth projected at 6.6% in FY2016/17 and 7.2% in FY2017/18.

### IN-IMF-9. IMF, *India: 2018 Article IV Consultation*, IMF Country Report No. 18/254, August 2018 (staff report dated 2 July 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2018/cr18254.pdf (GUESSED; 200; 82 PDF pages). Read: Board press release (PDF p. 2),
Key Issues (PDF p. 6), pp. 8, 10, 19, 29.
- PDF p. 6: India "among the fastest-growing economies in the world"; main reforms the inflation-targeting framework, the IBC, the GST and
  FDI liberalisation. "The IBC has the potential to improve significantly NPA resolution"; a large fraud at a PSB shows weaknesses; consider
  "more aggressive disinvestment". Domestic risks: GST revenue shortfalls and delay on "the twin bank-corporate balance sheet problems".
- PDF p. 2: growth forecast 7.3% (FY2018/19) and 7.5% (FY2019/20); CPI 5.2%; CAD 2.6% of GDP.
- p. 8: the RBI's Asset Quality Review (from 2015) improved recognition; PSBs hold about 70% of bank assets; 11 PSBs under PCA; "NPA ratio for
  the total banking sector increased to 11.6 percent" in March 2018 (9.6% a year earlier); October 2017 recapitalisation adds at least 0.8% of
  GDP to debt.
- p. 10: potential growth estimate 0.5 point lower than at the previous consultation (slower reform impact; revised historical GDP). p. 19:
  the authorities expected the IBC to speed resolution and the NPA ratio "to peak within a year". p. 29: potential growth 7.3% in FY2017/18;
  reforms "boost potential growth to around 7¾ percent over the medium-term", most from the GST.

### IN-IMF-10. IMF, *India: 2019 Article IV Consultation*, IMF Country Report No. 19/385, December 2019 (staff report dated 16 October 2019)
PDF: https://www.imf.org/-/media/files/publications/cr/2019/1indea2019001.pdf (GUESSED; 200; 104 PDF pages). Read: Board press release
(PDF p. 3), Key Issues (PDF p. 7), p. 8.
- PDF p. 7: "growth slowed to a six-year low in the first half of 2019": weak rural incomes, NBFC stress, regulatory uncertainty. Baseline:
  growth "gradually rises to its medium-term potential of 7.3 percent". Recommends a credible consolidation path, more realistic revenue
  projections, better PSB governance and a smaller state role in finance, to reach the US$5 trillion goal.
- p. 8: growth 6.1% in FY2019/20 ("lowest in 7 years"), rebounding to 7.0% in FY2020/21; CPI about 3.4%; CAD 2.0%.

### IN-IMF-11. IMF, *India: 2021 Article IV Consultation*, IMF Country Report No. 21/230, October 2021 (staff report dated 31 August 2021)
PDF: https://www.imf.org/-/media/files/publications/cr/2021/english/1indea2021001.pdf (GUESSED; 200; 89 PDF pages). Read: press release (PDF
p. 2), Key Issues (PDF p. 5), selected indicators (PDF p. 4), pp. 10–11.
- PDF p. 2: "GDP contracted an unprecedented 7.3 percent in FY2020/21"; growth projected at 9.5% (FY2021/22) and 8.5% (FY2022/23); CPI 5.6%.
- PDF p. 5: two COVID waves caused a deep, broad-based downturn "with the potential for a longer lasting impact"; additional fiscal support
  warranted until recovery is entrenched, with a credible medium-term consolidation plan.
- p. 10: "Potential growth is expected at around 6 percent over the medium term" (persistent pandemic impact, financial-sector repair).
  p. 11 (Text Table 1): 6.6, 6.3, 6.2, 6.1% for FY2023/24–FY2026/27. PDF p. 4: general government debt 74.1% (FY2019/20) → 89.6% (FY2020/21)
  → 90.7% projected (FY2021/22).

### IN-IMF-12. IMF, *India: 2022 Article IV Consultation*, IMF Country Report No. 22/386, December 2022 (staff report dated 4 November 2022)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1indea2022001.pdf (GUESSED; 200; 90 PDF pages). Read: Key Issues (PDF p. 5),
pp. 7–8.
- PDF p. 5: rebound but new headwinds; front-loaded monetary tightening appropriate; "A world class public digital infrastructure is
  facilitating innovation"; with "fiscal space at risk", credible consolidation needed.
- p. 7 (paras 7–8 and Text Table 1): growth 6.8% (FY2022/23), 6.1% (FY2023/24); "Potential growth is expected at 6 percent over the medium
  term"; CAD 3.5% of GDP in FY2022/23; CPI 6.9% in FY2022/23, back in the band next year; public debt 83.5% (FY2022/23), 83.9% (FY2023/24).

### IN-IMF-13. IMF, *India: 2023 Article IV Consultation*, IMF Country Report No. 23/426, December 2023 (staff report dated 3 November 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1indea2023001.pdf (GUESSED; 200; 142 PDF pages). Read: Key Issues (PDF
p. 6), pp. 10, 14, 19–20; Statement by the Executive Director (PDF p. 136, statement p. 5).
- PDF p. 6: on track to be "one of the fastest growing major economies"; sovereign debt risks "moderate", mitigated by debt composition.
- p. 10: "Potential growth has been revised up to 6.3 percent" (higher capital spending and employment); growth above 6% over five years.
- p. 14 (para 20): given past shocks and fiscal slippages (2000–20), "debt would exceed 100 percent of GDP in the medium term" if similar
  shocks recur; long-term sustainability risks high.
- p. 19: in December 2022–October 2023 the rupee moved in a very narrow range, so staff reclassified the de facto regime "from “floating” to
  “stabilized arrangement”"; the authorities called this "unjustified" (p. 20).
- ED statement (PDF p. 136): the 100% scenario "sounds extreme"; general government debt barely rose from 81% (2005-06) to 84% (2021-22) and
  back to 81% (2022-23); with a negative r−g, "the debt-GDP ratio cannot exceed 100%".

### IN-IMF-14. IMF, *India: 2024 Article IV Consultation*, IMF Country Report No. 25/54, February 2025 (staff report dated 6 February 2025; Board 21 February 2025)
PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1indea2025001-print-pdf.pdf (GUESSED; 200; 137 PDF pages). Read: press
release (PDF p. 2), Key Issues (PDF p. 5), pp. 7–8.
- PDF p. 2: Directors cite "India’s ambition of becoming an advanced economy by 2047".
- PDF p. 5: growth to recover from a recent softening; gradual, data-dependent rate cuts; FIT regime "successful" and should be supported by
  greater exchange-rate flexibility.
- p. 7: growth 6.5% in FY2024/25 and FY2025/26 and 6.5% over the medium term (potential); CPI 4.8% and 4.3%. p. 8: the authorities saw
  "staff's potential growth estimate of 6.5 percent being at the lower end" of their range, and stressed services-export potential.

### IN-IMF-15. IMF, *India: 2025 Article IV Consultation*, IMF Country Report No. 25/314, November 2025 (staff report dated 6 November 2025; Board 21 November; PR 25/292 of 26 November 2025)
Listing: country page https://www.imf.org/en/Countries/IND links the issue page (see DF-IN-7). PDF:
https://www.imf.org/-/media/files/publications/cr/2025/english/1indea2025003-source-pdf.pdf (200; 116 PDF pages). Read here (fiscal pages
already in DF-IN-7): press release (PDF p. 2), Key Issues (PDF p. 5), p. 4, Annex VII (p. 66).
- PDF p. 2: growth 6.5% in FY2024/25, 7.8% in Q1 FY2025/26; NPAs at multi-year lows. "Under the baseline assumption of prolonged 50 percent
  U.S. tariffs", growth 6.6% (FY2025/26) and 6.2% (FY2026/27); GST reform cushions the tariff hit.
- p. 4: the US tariffs (25% reciprocal plus 25% for Russian oil purchases) raise the effective rate on India's exports to the US to 37.8%.
  p. 8: potential growth 6.5% over the medium term.
- p. 66 (Annex VII): overall data adequacy rating B, but national accounts rated C: outdated 2011/12 base, WPI-based single deflation,
  production–expenditure discrepancies, no seasonally adjusted data; consolidated centre-plus-state fiscal data not published since
  mid-2019. Staff "warrant an overall sectoral rating for the national accounts of C".

### IN-IMF-16. IMF India country page, https://www.imf.org/en/Countries/IND (200; index.md 200), read 23 November 2026
- At a glance: 2026 projected real GDP 6.4% and CPI 4.7% (from the **July 2026** WEO Update, as the page says); population 1,476.6 million;
  member since 27 December 1945; latest Article IV country report 26 November 2025; quota SDR 13,114.4 million.
- The page still says the last Board consultation was 21 February 2025 (stale; see `India_2026.md` FLAG). No 2026 Article IV is listed.

### IN-IMF-17. IMF DataMapper API, WEO October 2026 vintage (indicator metadata "source: World Economic Outlook (October 2026)", last modified 8 October 2026) — own reading
URLs: https://www.imf.org/external/datamapper/api/v1/NGDPD/…, …/PPPSH/…, …/PPPPC/…, …/indicators, …/countries (all 200; the API returned
all economies). India data are fiscal years (WEO convention) and, from 2022, on the 2022-23 base (`IMF_2026.md`).
- India's share of world GDP at PPP: 3.9% (2000), 4.7% (2007), 5.3% (2010), 6.9% (2019), 7.9% (2024), 8.2% (2025), 8.6% (2026), 9.9% (2030
  proj.). China 6.7% → 19.6% (2000 → 2025); US 20.4% → 14.6%.
- Nominal GDP, US$ billion, and India's rank among countries (own ranking): 2000 468 (13th); 2007 1,217 (13th); 2014 2,024 (10th); 2019
  2,781 (**6th**, behind UK 2,891); 2022 3,257 (5th, ahead of UK 3,205); 2024 3,760 (5th); **2025 3,909 (6th, behind Japan 4,453 and UK
  4,012); 2026 4,060 (6th, behind Japan 4,342 and UK 4,268); 2027 proj. 4,521 (4th, ahead of UK 4,489 and Japan 4,468)**; 2030 6,130 (4th,
  just below Germany 6,154).
- GDP per capita, PPP international dollars: India 1,863 (2000) → 11,853 (2025); US 36,313 → 90,267; China 2,641 → 29,369. Own arithmetic:
  India at 5.1% of the US level in 2000 and 13.1% in 2025; India at 70.5% of China's level in 2000 and 40.4% in 2025.
- Caution: these are the current (post-rebasing, October 2026) vintage; past claims about India's rank were made on earlier data and
  exchange rates (IN-GOV-1 to IN-GOV-4).

## Reserve Bank of India

### IN-RBI-1. RBI, *Annual Report 2025-26*, Chapter I "Assessment and Prospects", para I.20 (HTML edition, released 29 May 2026)
Listing/URL: https://www.rbi.org.in/Scripts/AnnualReportPublications.aspx?Id=1461 (200; no page numbers). Chapters Id=1460, 1462–1467 also
fetched and searched (200); Id=1466 is Ch VI (financial stability, regulation, supervision).
- Para I.19–I.20: reserves US$691.1 billion at end-March 2026 (about 11 months of imports); bank credit to the commercial sector up 15.9% in
  2025-26; "The gross non-performing assets (GNPA) ratio declined to a multi-decadal low" (no figure given in the paragraph); CRAR comfortably
  above requirements.
- Ch VI (Id=1466): the Financial Stability Department brings out the half-yearly FSR; no GNPA number in the HTML chapter.
- The RBI's monetary framework (Patel Committee 2014; FIT 2016; retention 2021 and 2026) and the 2026 MPC decisions are already in the book
  (MO-IN-1 to MO-IN-4; IN26-21 to IN26-25). For the 2018 GNPA peak see IN-IMF-9 (11.6%, IMF) and the ES reference tables (11.5% in ES
  2018-19; 11.2% in ES 2019-20 onward).

## Government of India (Economic Surveys, on disk; not refetched)

### IN-GOV-1. *Economic Survey 2019-20*, Vol. 1, Preface (January 2020) — `es2019-20.txt`, p. vii (st. 7)
- "With India having become the fifth largest economy in the world in 2019", aspiring to be third-largest "by 2025" and a US$5 trillion
  economy by 2025.

### IN-GOV-2. *Economic Survey 2022-23* (January 2023) — `es2022-23.txt`, Ch 1 p. 21 (st. 64) and Ch 12 para 12.1, p. 343 (st. 386)
- p. 21: "India is the third-largest economy in the world in PPP terms" and fifth-largest at market exchange rates. p. 343: "India is the
  world’s fifth largest economy". (ES22-12 in `India_ES_2022-2024.md` has the Preface version.)

### IN-GOV-3. *Economic Survey 2023-24* (July 2024) — `es2023-24.txt`, Ch 5 opening p. 155 (st. 202) and para 5.33, p. 176 (st. 223)
- p. 155: India "soon set to become the third-largest economy in the world"; 7%-plus sustained growth possible.
- p. 176 (para 5.33): third-largest "following the US and China"; cites the IMF's April 2024 upgrade to 6.8% for 2024-25; "India has
  graduated from being a low-income country to a low-middle-income country". (The World Bank dates the move to FY2009; IN-WB-1.)

### IN-GOV-4. *Economic Survey 2025-26* (January 2026) — `es2025-26.txt`, chapter summary box, p. 335 (st. 386)
- "Despite being the world's fourth-largest economy", India's gross R&D spending is about 0.64% of GDP, against 2.5–5% in the US, China and
  Israel. This is the Survey's statement of rank (January 2026, pre-rebasing); compare IN-IMF-17.

### IN-GOV-5. India's share of world services exports in the Surveys — `es2013-14.txt` p. 178 (st. 178); `es2023-24.txt` p. 117 (st. 164); `es2024-25.txt` para 8.3, p. 220 (st. 265)
- ES 2013-14 p. 178 (para 10.14): share 0.6% (1990) → 1.1% (2000) → 3.3% (2013), "increasing faster than its share in world merchandise
  exports"; services export growth above world growth every year since 1996 except 2009, reversed in 2013.
- ES 2023-24 p. 117: share 0.5% (1993) → 4.3% (2022); seventh-largest services exporter, "with a phenomenal rise from its 24th position in
  2001"; second in telecom, computer and information services.
- ES 2024-25 p. 220: in 2023 the US led with 13%; "India ranks seventh globally, representing a 4.3 per cent share". (The WTO's 2025 figure,
  4.3% and eighth, is TR-WTO-3.)

## World Bank

### IN-WB-1. World Bank, "World Bank Country and Lending Groups" (datahelpdesk article 906519) and the historical classification file (OGHIST.xlsx)
Listing: https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups (200), which links
"historical classification by income in XLSX format": https://ddh-openapi.worldbank.org/resources/DR0095334/download (200; Excel). Read:
help page text; sheets "Country Analytical History" (FY89–FY27) and "Thresholds".
- India is classified **low income (L) from FY89 to FY08 and lower-middle income (LM) from FY09 (based on 2007 GNI) to FY27 (based on 2025
  GNI)**. FY09 lower-middle-income range: GNI per capita (Atlas) US$936–3,705 (2007 data). Comparators: China LM from FY01 (after L in
  FY00), UM from FY12; Indonesia UM in FY21 and from FY24; Viet Nam LM from FY11, UM by FY27; Bangladesh LM from FY16.
- FY27 thresholds (help page): LMI US$1,176–4,635; UMI US$4,636–14,375; high income above US$14,375 (2025 GNI).
- File note: classifications are fixed as published on 1 July each year, "irrespective of any revisions" to income data (relevant to IN-WB-2).

### IN-WB-2. World Bank WDI API, GNI per capita, Atlas method (current US$), NY.GNP.PCAP.CD, last updated 11 November 2026
URL: https://api.worldbank.org/v2/country/IND;CHN;USA/indicator/NY.GNP.PCAP.CD?format=json&per_page=200&date=2000:2025 (200).
- India US$440 (2000), 700 (2005), 910 (2007), 1,210 (2010), 1,580 (2015), 1,900 (2020), 2,550 (2024), 2,760 (2025). China 950 → 14,230;
  US 35,960 → 88,810 (2000 → 2025).
- Own arithmetic: India's GNI per capita rose 6.3-fold in dollars (2000–25); from 1.2% to 3.1% of the US level, and from 46% to 19% of
  China's. India's 2025 figure is about 60% of the FY27 upper-middle threshold (US$4,636). The revised 2007 value (US$910) is below the
  FY09 LM floor (US$936); the classification used the data available in 2008 (IN-WB-1 note), so do not read the current series as the
  basis for the 2008 decision.

### IN-WB-3. World Bank, *India Development Update: India's Growth Story*, March 2018
Found via the Documents & Reports search API (https://search.worldbank.org/api/v2/wds, qterm "India Development Update"; doc date 1 February
2018). PDF: http://documents.worldbank.org/curated/en/814101517840592525/pdf/India-development-update-Indias-growth-story.pdf (200; 122 PDF
pages; title page "March 2018"). Read: Executive Summary (pp. 8–11), Outlook (p. 95).
- p. 8: over 50 years India's growth accelerated slowly and became more stable; 2004–08 saw "an unprecedented high of 8.8 percent a year",
  helped by a global boom and a decade of prior reform; the post-GFC slowdown reflected tepid world growth and "an excessive fiscal response".
- p. 9: the dip below 7% (Q3 2016-17 to Q2 2017-18) was "an aberration" due to demonetisation and GST preparation; "economic activity should
  revert to the trend growth rate of about 7.5 percent"; sustained 8%+ needs reform. Only one durable 8% episode in five decades (2004–08).
- p. 95: growth 6.7% (2017-18), 7.3% (2018-19), 7.5% (2019-20).

### IN-WB-4. World Bank, *India Development Update: India and Artificial Intelligence – Seizing the Development Opportunity*, 13 October 2026 (abstract only)
Listing: World Bank India country page (200) links https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099455510022634209
(200, a script shell). Metadata and abstract from https://search.worldbank.org/api/v3/wds?format=json&fl=*&guid=099455510022634209 (200;
docdt 13 October 2026). **PDF** https://documents.worldbank.org/curated/en/099455510022634209/pdf/IDU-26df18db-fc2b-4e0b-91ed-be8ced3d9bce.pdf
returned **403** (not bypassed). Read: the abstract only (no page numbers).
- Abstract: real GDP growth 7.8% in FY26 (7.2% the year before) and 7.8% in Q1 FY27; CPI 2.1% in FY26, 4.8% by August 2026; RBI held at
  5.25% (the abstract predates the October rise, IN26-25); CAD 0.7% of GDP; reserves an all-time high of US$785.7 bn in September 2026.
  "The World Bank upgraded India's growth forecast for FY27 to 7.1%", medium-term growth above 7% through FY29; general government deficit
  about 7.4% of GDP in FY27; debt below 80% of GDP by FY29.

### IN-WB-5. World Bank, *India – Country Economic Memorandum: Becoming a High-Income Economy in a Generation*, 2025 (doc date 5 March 2025; abstract only)
Listing: World Bank India country page (openknowledge entity link). Metadata via https://search.worldbank.org/api/v3/wds?…&guid=099022725232041885
(200). **PDF** https://documents.worldbank.org/curated/en/099022725232041885/pdf/P175027-38446b18-85d1-45c2-8628-9662d283ed24.pdf returned
**403**. Read: the abstract only.
- Since 2000 the economy grew nearly four-fold in real terms and GDP per capita almost tripled; India's "share in the global economy has
  doubled" from 1.6% (2000) to 3.4% (2023), making it the world's fifth-largest economy. High income by 2047 is not possible on
  business as usual: "GNI per capita will have to increase by nearly 8 times".

## Synthesis

1. **Two decades of near-continuous top-tier growth, with one boom, one bust and one shock.** The IMF called 2003–05 "impressive for the
   third year running" and a "golden opportunity" (IN-IMF-1 p. 4), then a "dream run" of about 8½% (IN-IMF-2 p. 3); the World Bank later
   put 2004–08 at "an unprecedented high of 8.8 percent a year" (IN-WB-3 p. 8). Growth then fell to 4.5–4.7% in 2012-14 (old series;
   `India_ES_2010-2014.md`), collapsed by 7.3% in FY2020/21 (IN-IMF-11 PDF p. 2; later −5.8%, `India_ES_2022-2024.md`), and recovered to 7–9%
   (FY26 7.6% on the new base, IN26-36; IN-WB-4).
2. **The IMF kept being too pessimistic about India's booms and too optimistic before its slumps.** It projected 6.5–6.8% for 2006/07–2009/10
   when outturns were 9.7, 9.2, 6.7 and 7.4 (IN-IMF-1 p. 46; IN-IMF-4 p. 27); 8.1% a year for 2011/12–2014/15 just before the slowdown
   (IN-IMF-4 p. 27); 7.3/7.5% for 2018/19–2019/20 and 6.1/7.0% for 2019/20–2020/21 before the 2019 slowdown and the pandemic (IN-IMF-9 PDF
   p. 2; IN-IMF-10 p. 8); then 6.1–6.6% for FY2023/24–FY2024/25 against outturns of 8.2–9.2% and 6.5% (IN-IMF-11 p. 11; IN-IMF-12 p. 7).
3. **Potential growth estimates swung with the cycle.** RBI 8% → 7% and IMF about 6½% in 2012 (IN-IMF-5 p. 8); IMF 7¾% medium term in 2016
   and 2018 (IN-IMF-7 p. 6; IN-IMF-9 p. 29); 7.3% in 2019 (IN-IMF-10 PDF p. 7); about 6% after the pandemic (IN-IMF-11 p. 10; IN-IMF-12 p. 7);
   6.3% (IN-IMF-13 p. 10) and 6.5% (IN-IMF-14 p. 7; IN-IMF-15 p. 8). The Surveys ran higher: 8–10% (GR-IN-3), 6.5% (GR-IN-4), about 7%
   (GR-IN-6); India told the IMF 6.5% was "at the lower end" (IN-IMF-14 p. 8).
4. **2013 was a balance-of-payments near-miss built on domestic imbalances.** A record CAD of 4.8% of GDP in 2012/13, high inflation and
   fiscal deficits left "very little room" (IN-IMF-6 PDF p. 2, p. 6); the IMF judged two-thirds of the slowdown domestic (IN-IMF-6 p. 4). The
   defence (MSF, gold duty, FCNR(B) swaps) is in ES13-8 to ES13-15.
5. **The twin balance sheet problem took a decade to clear.** NPAs were "low" in 2009 (IN-IMF-3 p. 4); the IMF urged full recognition from
   2016 (IN-IMF-7 PDF p. 6; IN-IMF-8 PDF p. 6); GNPA peaked at 11.6% in March 2018 (IN-IMF-9 p. 8; 11.5/11.2% in the Surveys) after the AQR;
   the IBC "has the potential" to fix resolution (IN-IMF-9 PDF p. 6). By September 2025 GNPA was 2.2% (GR-IN-6) and the RBI calls it
   "a multi-decadal low" (IN-RBI-1 para I.20).
6. **The reform sequence the IMF asked for from 2005 eventually arrived.** The GST was urged in 2005 (IN-IMF-1 p. 4) and arrived in 2017; the
   inflation-targeting framework (MO-IN-1, MO-IN-3), the IBC and Aadhaar-linked transfers were credited by 2017–18 (IN-IMF-8 PDF p. 6; IN-IMF-9
   PDF p. 6). Demonetisation was treated as a temporary shock: growth cut to 6.6% for FY2016/17 (IN-IMF-8 p. 6; outturn 7.1% PE, ES16).
7. **Inflation went from India's chronic weakness to a managed variable.** CPI averaged about 10% in 2009–13 (IN-IMF-7 p. 6); FIT brought 4.4%
   in its first period (MO-IN-4) and the IMF called the regime "successful" in 2025 (IN-IMF-14 PDF p. 5); the breach of 2022 is in MO-IN-3.
8. **Debt: the IMF's warnings and India's rebuttals.** General government debt was 86% of GDP in 2003–05 (IN-IMF-1 p. 39), 75–77% around 2010
   (IN-IMF-4 p. 27), 89.6% in FY2020/21 (IN-IMF-11 PDF p. 4) and 80.7–81.6% in 2023/24–2024/25 (DF-IN-7). In 2023 staff warned debt could
   exceed 100% in shocks; India's Executive Director replied the ratio "cannot exceed 100%" (IN-IMF-13 p. 14; PDF p. 136). The 2023 exchange-
   rate reclassification to "stabilized arrangement" was a second open dispute (IN-IMF-13 p. 19).
9. **India's weight in the world economy roughly doubled.** Share of world GDP at PPP 3.9% (2000) → 8.2% (2025) (IN-IMF-17); at market rates
   1.6% (2000) → 3.4% (2023) (IN-WB-5). Services exports went from 1.1% of the world (2000) to 4.3% (2022–25), seventh or eighth largest (IN-GOV-5;
   TR-WTO-3), against 1.7% of merchandise exports (TR-WTO-3, TR-IN-1). The IMF repeatedly called India among the fastest-growing (IN-IMF-9 PDF
   p. 6; IN-IMF-13 PDF p. 6; `IMF_2026.md` WEO July 2026 p. 6).
10. **Rank claims depend on the vintage.** The Surveys said fifth-largest in 2019 (IN-GOV-1), fifth in 2022–23 (IN-GOV-2), soon third (IN-GOV-3)
    and fourth-largest in January 2026 (IN-GOV-4). The IMF's October 2026 data (post-rebasing, current dollars) put India sixth in 2019,
    fifth in 2022–24, **sixth in 2025 and 2026** behind Japan and the UK, and fourth only from 2027 (projection) (IN-IMF-17, own ranking).
11. **Convergence is real but far from complete.** GDP per capita at PPP rose from 5.1% to 13.1% of the US level (2000–25), but fell from
    70.5% to 40.4% of China's (IN-IMF-17, own arithmetic). India moved from low to lower-middle income in FY2009 and is still LMI in FY27
    (IN-WB-1); its Atlas GNI per capita of US$2,760 (2025) is about 60% of the upper-middle threshold (IN-WB-2, own arithmetic). The
    World Bank's 2047 high-income goal needs GNI per capita up "nearly 8 times" (IN-WB-5). Poverty at $3.00 fell from 27.1% (2011) to 2.6%
    (2023) (DV-WB-13).
12. **Statistics are part of the story.** The 2015 GDP series rewrote 2012–14 (IN-IMF-7 p. 4; ES14-7); the IMF rated India's national accounts
    C in 2025 (IN-IMF-15 p. 66); the economy was rebased to 2022-23 in February 2026 (ES25-4), which changed growth rates and dollar GDP and
    therefore India's rank (IN-IMF-17).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| Dec 2005 | IMF (IN-IMF-1 p. 46) | Growth 6.8% (2006/07), then 6.5% a year to 2009/10; reserves US$171 bn by end-2009/10 | 9.7, 9.2, 6.7, 7.4%; reserves US$279.1 bn at end-2009/10 (IN-IMF-4 p. 27) |
| Dec 2005 | IMF (IN-IMF-1 p. 4) | Introduce "a goods and services tax" quickly | GST from July 2017 (ES16-11, ES17-1); GST 2.0 in 2025 (ES25-18) |
| Jan 2009 | IMF (IN-IMF-3 p. 3) | Growth 6¼% (2008/09), 5¼% (2009/10); NPAs to rise substantially | 6.7% and 7.4% (IN-IMF-4 p. 27; later 8.6% for 2009-10, ES); GNPA 2.36% in March 2011 (ES reference table) |
| Dec 2010 | IMF (IN-IMF-4 p. 27) | 8.1% a year 2011/12–2014/15; investment 44% of GDP | 6.2–6.7 (2011-12), 4.5 (2012-13), 4.7% (2013-14) on the old series (`India_ES_2010-2014.md`) |
| Dec 2012 | IMF (IN-IMF-5 p. 36) | 5.4% (2012/13), 6.0% (2013/14) | 4.5% and 4.7% (old series); 5.1% and 6.9% on the new series (ES14-7) |
| Jan 2014 | IMF (IN-IMF-6 PDF p. 2, p. 5) | 4.6% in 2013/14, "the lowest level in a decade"; 5.4% in 2014/15 | New series: 6.9% (2013-14) and 7.2 → 7.5% (2014-15) (ES14-7; `India_ES_2015-2020.md`) |
| Jan 2014 | RBI, Patel Committee (MO-IN-1) | CPI glide path to 8% in 12 months, 6% in 24 months | Glide path "overachieved"; CPI 4.9% (2015-16) (MO-IN-4 para 9; `India_ES_2015-2020.md`) |
| Jan 2016 | ES 2015-16 (GR-IN-3 p. 7) | Medium-term potential "between 8 and 10 percent" | Growth averaged well below 8% outside rebounds; IMF potential 6–7¾% (IN-IMF-7 to IN-IMF-15) |
| Jan 2017 | IMF (IN-IMF-8 p. 6) | Demonetisation cuts FY2016/17 to 6.6%, rebound to 7.2% in FY2017/18 | 7.1% (PE) and 6.5% AE → 7.2% (`India_ES_2015-2020.md`) |
| Mar 2018 | World Bank (IN-WB-3 p. 95) | 7.3% (2018-19), 7.5% (2019-20); trend about 7.5% | 6.8% and 4.0–4.2% (`India_ES_2015-2020.md`; ES20-3) |
| Jul 2018 | IMF (IN-IMF-9 PDF p. 2, p. 19, p. 29) | 7.3% and 7.5%; NPA ratio expected (by the authorities) to peak within a year; potential to 7¾% | NPAs did peak in March 2018 (11.2–11.6%) and fell to 2.2% by Sep 2025 (GR-IN-6); growth 6.8% and 4.0%; IMF potential cut to about 6% by 2021 (IN-IMF-11 p. 10) |
| Oct 2019 | IMF (IN-IMF-10 p. 8) | 6.1% (FY2019/20), 7.0% (FY2020/21); potential 7.3% | 4.0% and −7.3% (IN-IMF-11 PDF p. 4), later −5.8% (`India_ES_2022-2024.md`) |
| Jan 2020 | ES 2019-20 (IN-GOV-1 p. vii) | Fifth-largest in 2019; third-largest and US$5 trillion "by 2025" | 2025 GDP US$3.9 trillion, sixth in the IMF's October 2026 data (IN-IMF-17, own ranking) |
| Aug 2021 | IMF (IN-IMF-11 p. 10–11) | Potential about 6%; 6.6% (FY2023/24), 6.3% (FY2024/25) | 9.2% (FY24, revised) and 6.5% (FY25) (`India_ES_2024-2026.md`) |
| Nov 2022 | IMF (IN-IMF-12 p. 7) | 6.8% and 6.1% (FY23, FY24); CPI 6.9%; CAD 3.5% in FY2022/23 | 7.0 → 7.6% and 8.2 → 9.2%; CPI 6.7%; CAD 2.0% (`India_ES_2022-2024.md`, `India_ES_2024-2026.md`) |
| Nov 2023 | IMF (IN-IMF-13 p. 14) vs India's ED (PDF p. 136) | Debt could exceed 100% of GDP in shocks vs "cannot exceed 100%" | General government debt 80.7% (2023/24), 81.6% (2024/25), 80.7% projected 2026/27 (DF-IN-7) |
| Jul 2024 | ES 2023-24 (IN-GOV-3 p. 155, p. 176) | "Soon set to become the third-largest economy" | Sixth in 2025–26 and fourth in 2027 (proj.) in WEO October 2026 data (IN-IMF-17) |
| Feb 2025 | IMF (IN-IMF-14 p. 7) | 6.5% in FY2025/26 and over the medium term | FY26 7.4% (FAE, old base, ES25-3), 7.6% (new base, IN26-36), 7.8% (WEO Oct 2026, `IMF_2026.md`; IN-WB-4) |
| Nov 2025 | IMF (IN-IMF-15 PDF p. 2) | Under prolonged 50% US tariffs: 6.6% (FY26), 6.2% (FY27) | US tariff cut to 10% after the February 2026 deal (`IMF_2026.md` p. 11; US-IN-8); FY27 forecast 7.0% (WEO Oct 2026) and 7.1% (IN-WB-4) |
| Jan 2026 | ES 2025-26 (IN-GOV-4 p. 335) | "The world's fourth-largest economy" | Sixth in 2025 and 2026 on the IMF's post-rebasing October 2026 data (IN-IMF-17, own ranking) |

### Candidate quotes (all verified by script against the converted text)

- "India’s economic performance continues to be impressive for the third year running" (IMF 2005, IN-IMF-1 p. 4)
- "India’s growth spurt provides a golden opportunity" (IN-IMF-1 p. 4)
- "The Indian economy is reaping the rewards of the structural reforms" (IN-IMF-1 p. 27)
- "India’s dream run of strong growth and macroeconomic stability" (IMF 2007, IN-IMF-2 p. 3)
- "India’s growth is likely to slow sharply." (IMF January 2009, IN-IMF-3 p. 3)
- "First International Financial Crisis Since India Went Global" (section title, IN-IMF-3 p. 2)
- "India’s growth remains among the strongest in the world" (IMF 2010, IN-IMF-4 p. 15)
- "with some forecasting India overtaking China" (IMF 2012, IN-IMF-5 p. 8)
- "potential growth has declined to about 6½ percent" (IN-IMF-5 p. 8)
- "the lowest level in a decade" (IMF 2014, IN-IMF-6 PDF p. 2)
- "India has very little room to adopt countercyclical policies" (IN-IMF-6 PDF p. 2)
- "The current account deficit reached a record 4.8 percent of GDP in 2012/13" (IN-IMF-6 p. 6)
- "NPAs on public banks’ balance sheets should be fully recognized" (IMF 2016, IN-IMF-7 PDF p. 6)
- "medium-term growth is projected to remain at around 7¾ percent" (IN-IMF-7 p. 6)
- "Cash shortages arising from the currency exchange initiative have weakened the near-term outlook." (IMF 2017, IN-IMF-8 PDF p. 6)
- "which accounted for 86 percent of the value of currency in circulation" (IN-IMF-8 p. 4)
- "The IBC has the potential to improve significantly NPA resolution" (IMF 2018, IN-IMF-9 PDF p. 6)
- "NPA ratio for the total banking sector increased to 11.6 percent" (IN-IMF-9 p. 8)
- "boost potential growth to around 7¾ percent over the medium-term" (IN-IMF-9 p. 29)
- "growth slowed to a six-year low in the first half of 2019" (IMF 2019, IN-IMF-10 PDF p. 7)
- "gradually rises to its medium-term potential of 7.3 percent" (IN-IMF-10 PDF p. 7)
- "contracted an unprecedented 7.3 percent in FY2020/21" (IMF 2021, IN-IMF-11 PDF p. 2)
- "Potential growth is expected at around 6 percent over the medium term" (IN-IMF-11 p. 10)
- "A world class public digital infrastructure is facilitating innovation" (IMF 2022, IN-IMF-12 PDF p. 5)
- "Potential growth is expected at 6 percent over the medium term" (IN-IMF-12 p. 7)
- "Potential growth has been revised up to 6.3 percent" (IMF 2023, IN-IMF-13 p. 10)
- "debt would exceed 100 percent of GDP in the medium term" (IN-IMF-13 p. 14)
- "from “floating” to “stabilized arrangement”" (IN-IMF-13 p. 19)
- "the debt-GDP ratio cannot exceed 100%" (Statement by the Executive Director for India, IN-IMF-13 PDF p. 136)
- "India’s ambition of becoming an advanced economy by 2047" (IMF Board, February 2025, IN-IMF-14 PDF p. 2)
- "staff's potential growth estimate of 6.5 percent being at the lower end" (authorities' view, IN-IMF-14 p. 8)
- "Under the baseline assumption of prolonged 50 percent U.S. tariffs" (IMF November 2025, IN-IMF-15 PDF p. 2)
- "warrant an overall sectoral rating for the national accounts of C" (IN-IMF-15 p. 66)
- "The gross non-performing assets (GNPA) ratio declined to a multi-decadal low" (RBI AR 2025-26, IN-RBI-1 para I.20)
- "With India having become the fifth largest economy in the world in 2019" (ES 2019-20, IN-GOV-1 p. vii)
- "India is the third-largest economy in the world in PPP terms" (ES 2022-23, IN-GOV-2 p. 21)
- "India has graduated from being a low-income country to a low-middle-income country" (ES 2023-24, IN-GOV-3 p. 176)
- "Despite being the world's fourth-largest economy" (ES 2025-26, IN-GOV-4 p. 335)
- "has been increasing faster than its share in world merchandise exports" (ES 2013-14, IN-GOV-5 p. 178)
- "with a phenomenal rise from its 24th position in 2001" (ES 2023-24, IN-GOV-5 p. 117)
- "India ranks seventh globally, representing a 4.3 per cent share" (ES 2024-25, IN-GOV-5 p. 220)
- "an unprecedented high of 8.8 percent a year" (World Bank IDU 2018, IN-WB-3 p. 8)
- "economic activity should revert to the trend growth rate of about 7.5 percent" (IN-WB-3 p. 9)
- "The World Bank upgraded India's growth forecast for FY27 to 7.1%" (IDU October 2026 abstract, IN-WB-4)
- "its share in the global economy has doubled" (CEM 2025 abstract, IN-WB-5)
- "GNI per capita will have to increase by nearly 8 times" (CEM 2025 abstract, IN-WB-5)

Short phrases quoted inside the item notes but not run through the script ("impressive for the third year running" variants, "remains
high", "likely to lead to a substantial increase in NPAs", "a confluence of structural, external and other factors", "heightened the
focus", "now in check", "a new bankruptcy code", "more aggressive disinvestment", "to peak within a year", "with the potential for a
longer lasting impact", "fiscal space at risk", "one of the fastest growing major economies", "unjustified", "sounds extreme",
"successful", "an excessive fiscal response", "an aberration", "managing financial globalization", "mainly due to rapid growth",
"among the fastest-growing economies in the world", "soon set to become the third-largest economy in the world", "irrespective of any
revisions") were read in the source but should be rechecked before they are printed as quotations.

## Not obtained

- **IMF listing.** https://www.imf.org/en/Countries/IND (200) and its index.md (200) link only the 2025 Article IV; "See All Documents" is a
  dynamic section not in the fetched page. All earlier reports are GUESSED URLs (title pages confirmed).
- **IMF guesses that failed or missed**: …/cr/2019/english/1indea2019001.pdf and …/1indea2019002.pdf — 404; …/cr/2019/cr19385.pdf — 404;
  …/CR/2019/1INDEA2019001.ashx — 404; …/cr/2021/english/1indea2021002.pdf — 404; …/cr/2025/english/1indea2025001.pdf,
  …/1indea2025001-source-pdf.pdf and …/1indea2025002-source-pdf.pdf — 404. Discarded wrong hit: …/cr/2020/english/1indea2020001.pdf (200) is
  CR 20/208, a Tamil Nadu technical-assistance report.
- **IMF Article IVs not attempted**: 2006, 2009, 2011, 2012 and 2015 consultations, and any FSAP. **IMF 2026 Article IV**: not published
  (country page lists 26 November 2025 as the latest; see `India_2026.md`).
- **IMF SDMX API** (api.imf.org) not used: it needs an `Accept` header, which the method rules out. The DataMapper API (IN-IMF-17) was used
  instead.
- **RBI Financial Stability Report**: the listing https://www.rbi.org.in/Scripts/FsReports.aspx (200) and the half-yearly publications
  page (…/Publications.aspx?publication=HalfYearly, 200) carry no report links in the fetched HTML (the list loads by ASP.NET postback,
  which was not used). RBI PDFs on rbidocs.rbi.org.in fail with plain curl (MO-IN-1, `India_2026.md`), so no FSR PDF was tried. **No FSR
  peak or latest GNPA figure from the FSR itself**; the 2018 peak is from the IMF (IN-IMF-9) and the Surveys, the 2025 level from ES
  2025-26 (GR-IN-6), and the 2026 judgement from the RBI Annual Report (IN-RBI-1, no number).
- **RBI documents already in the book not refetched**: Patel Committee report (MO-IN-1), FIT notification and retentions (MO-IN-3), 2025
  discussion paper (MO-IN-4), MPC statements of 2026 (IN26-21 to IN26-25).
- **World Bank PDFs**: India Development Update October 2026
  (https://documents.worldbank.org/curated/en/099455510022634209/pdf/IDU-26df18db-fc2b-4e0b-91ed-be8ced3d9bce.pdf) and the 2025 Country
  Economic Memorandum (https://documents.worldbank.org/curated/en/099022725232041885/pdf/P175027-38446b18-85d1-45c2-8628-9662d283ed24.pdf) —
  both **403**; not bypassed. Only their API abstracts were read (IN-WB-4, IN-WB-5). The World Bank India publications page
  https://www.worldbank.org/en/country/india/publication (200) is an empty shell. The September 2024 IDU ("India's Trade Opportunities in a
  Changing Global Context", guid 099513209032434771) was found in the API but not fetched.
- **World Bank poverty**: not re-read (DV-WB-3, DV-WB-13 already hold the June 2025 $3.00 update and the October 2026 Poverty & Equity Brief).
- **Official statement of the date India became fifth- or fourth-largest**: no IMF text found that dates it; the Surveys state the rank
  (IN-GOV-1 to IN-GOV-4) without citing the data vintage. PIB releases were not searched. The rank table in IN-IMF-17 is my own ranking of
  current IMF data, not an official statement.
- **WTO**: not fetched afresh (TR-WTO-3 already gives the 2025 services share and rank). No WTO series of India's share for 2000–24 was
  obtained beyond the Survey figures (IN-GOV-5).
- **Fetched but not read**: IMF CR 23/426 beyond pp. 10–20 and the ED statement; IMF CR 25/54 beyond pp. 7–8; the 2018 IDU beyond the
  Executive Summary and Outlook; RBI AR 2025-26 Chapters IV, VI and VII (searched only).
