# Reading notes: lens 'Other emerging markets' — part B (Indonesia, Russia, Gulf, cross-cutting) (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies, no form postbacks), with a
`--max-time` limit. Listing pages used: the imf.org country pages https://www.imf.org/en/Countries/IDN (200; `index.md` and `index.json`
200), /RUS (429 on the HTML and `index.md`; `index.json` 200), /SAU (HTML 200; `index.md` and `index.json` 429) and /ARE (HTML 200;
`index.md` and `index.json` 429). Each lists only the latest Article IV issue page, and those four issue pages (all 200, Saudi on a
second try after a 429) gave the PDF links for ID-IMF-6, RU-IMF-5, GC-IMF-4 and GC-IMF-5. **The Russia country page's latest Article IV
is the 2020 consultation (CR 21/36, February 2021): the IMF has published no Russia Article IV since.** Every earlier staff report comes
from a GUESSED URL built on the IMF file-naming pattern (`/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016;
`/-/media/files/publications/cr/YYYY/crYYNNN.pdf` in 2017–18; `/-/media/files/publications/cr/YYYY/english/1<iso3>eaYYYYnnn.pdf` from
2019), and for each the title page and "IMF Country Report No." were read to confirm it is the Article IV named. Wrong hits and 404s are
listed under Not obtained. Other listing pages: the Bank of Russia key-rate page (https://www.cbr.ru/eng/press/keypr/, 200), its key-rate
database (https://www.cbr.ru/eng/hd_base/KeyRate/, 200, queried by date range with the page's own GET parameters) and its key-rate
publications page (`/eng/dkp/mp_dec/decision_key_rate/`, 200, which lists only 2024–26 material); the New Development Bank "History" page
(https://www.ndb.int/about-ndb/history/, 200); the University of Toronto BRICS Information Centre's document pages for the 2014, 2023,
2024 and 2025 summit declarations (GUESSED paths, all 200, titles checked). Downloads are in the session scratchpad folder
`lens_em_dl/b/`, one subfolder per publisher: `imf/` (country and issue pages), `imf/g/` (staff reports), `cbr/`, `brics/` (NDB, BRICS
declarations), `gov/` (Vision 2030), `oth/` (Goldman Sachs, World Bank), `bi/` (empty: Bank Indonesia timed out). PDFs were converted
with `pdftotext` (plain and `-layout`) into `lens_em_dl/b_txt/`; HTML pages were stripped of tags and read as text. Python that read
downloads was run with `python3 -I`, from scripts kept outside the download folder (`emb_scripts/`). Economic Survey texts were **not
refetched**: they were read from the Econ Subject folder (`sources/text/es*.txt`, text page = PDF page = "st."), and the printed page was
taken from the running header or footer. Quotes are verbatim and under 15 words, and a script checked every one against the converted
text (whitespace-, quote- and line-end-hyphen-normalised). Everything else is paraphrase. Page numbers are printed page numbers unless
stated; "PDF p." is used for unnumbered pages (Key Issues pages, press releases and their tables at the front of IMF reports). Shares and
forecast-vs-outturn gaps are marked "own arithmetic".

Printed-page offsets: CR 07/272, 09/246: printed = PDF − 2. CR 13/362, 14/175: printed = PDF − 1. CR 15/211, 15/251, 21/46, 22/84, 23/221,
25/327: printed = PDF − 4. CR 16/326, 17/316, 25/223, 26/10: printed = PDF − 5. CR 21/36: printed = PDF − 6. Goldman Sachs Global Paper 66:
printed "S.0n" = PDF n. Vision 2030: printed = PDF + 1. World Bank GEP January 2016: p. 89 = PDF 113. World Bank India Development Update
March 2018: printed = PDF − 1.

Item labels:
- ID-IMF-n: IMF Article IV consultations with Indonesia. (No ID-BI item: www.bi.go.id did not answer; see Not obtained.)
- RU-IMF-n: IMF Article IV consultations with Russia. RU-CBR-n: Bank of Russia.
- GC-IMF-n: IMF Article IV consultations with Saudi Arabia and the UAE. GC-GOV-n: Saudi Vision 2030.
- EM-X-n: cross-cutting (BRICs paper, "Fragile Five", BRICS and the NDB).
- EM-IN-B-n: India links from the Economic Surveys (on disk).

Abbreviations: BI = Bank Indonesia; CBR/BoR = Bank of Russia; CEPA = Comprehensive Economic Partnership Agreement; CR = IMF Country Report;
CRA = Contingent Reserve Arrangement; GCC = Gulf Cooperation Council; NDB = New Development Bank; NFA = net foreign assets; NWF = National
Wealth Fund; PIF = Public Investment Fund; SAMA = Saudi Arabian Monetary Authority (now Saudi Central Bank); SWF = sovereign wealth fund;
UMP = unconventional monetary policy.

---

## Indonesia

### ID-IMF-1. IMF, *Indonesia: 2007 Article IV Consultation—Staff Report; Staff Statement; Public Information Notice…*, IMF Country Report No. 07/272, August 2007
URL: https://www.imf.org/external/pubs/ft/scr/2007/cr07272.pdf (GUESSED; title page confirms CR 07/272, Indonesia 2007 Article IV). HTTP 200.
Accessed 23 Nov 2026. Staff report dated 26 June 2007; Board discussion 18 July 2007.
- p. 3 (Executive Summary): growth about 6% over the past year on domestic demand and exports; bank and corporate balance sheets
  stronger, public debt ratio falling, current account in surplus, reserves up. "Macroeconomic policies have been geared successfully
  towards promoting stability while supporting growth". BI had cut the policy rate by 425 bp since May 2006. Portfolio inflows were
  pushing the rupiah up; staff and authorities agreed to let it appreciate while smoothing disruptive moves.
- p. 4: Indonesia repaid its remaining IMF obligations early in October 2006, ending post-program monitoring (the extended arrangement
  had expired on 31 December 2003, PDF p. 3). Poverty rose back to 18% in 2006 on higher staple prices.
- p. 9 (Box 1, "1997 vs. 2007"): ten years after the Asian crisis, vulnerability is lower: more flexible exchange rate, lower credit
  growth, reserves up, current account in surplus (−2.2% of GDP average 1992–96 vs +2.2% in 2002–06), non-bank cross-border borrowing
  down from 194% of reserves (1997 Q2) to 56% (2006 Q3). Remaining weak spots: large state banks, contagion through capital markets,
  governance perceptions.
- p. 34 (Table 3): real GDP 5.5% (2006), projected 6.0% (2007) and **6.3% (2008)**; CPI average 13.1% (2006), 6.2% (2007), 5.4% (2008);
  central government debt 38.6% of GDP (2006) → 33.9% (2008 proj.); gross reserves $42.6bn (2006), $55.0bn (2007), $61.8bn (2008 proj.);
  total external debt 36.6% of GDP (2006).

### ID-IMF-2. IMF, *Indonesia: Staff Report for the 2013 Article IV Consultation*, IMF Country Report No. 13/362, December 2013
URL: https://www.imf.org/external/pubs/ft/scr/2013/cr13362.pdf (GUESSED; title page confirms CR 13/362). HTTP 200. Accessed 23 Nov 2026.
Staff report dated 1 November 2013.
- PDF p. 2 (Key Issues): slowing EM growth, lower commodity prices and the prospective exit from easy global money put pressure on the
  balance of payments; growth projected at 5–5½% in 2013 and 2014; inflation to peak just below 10% at end-2013 after the June fuel price
  rise; current account deficit above 3% of GDP in 2013 and 2014; BI's heavy FX intervention in mid-2013 cost reserves. Advice: use the
  delay in tapering to rebuild buffers; let the exchange rate and bond yields adjust; tax and subsidy reform.
- p. 5 (para 1–2): Indonesia's current account went into deficit in 2012 for the first time in more than a decade. Taper talk in May 2013
  caused a sharp reversal of flows; "Indonesia has been one of the most seriously affected by recent market volatility". Net bond and
  equity outflows of $2.7bn from 22 May to end-October; the rupiah down 17% against the dollar in 2013.
- p. 5 (para 3): subsidised fuel prices raised by 33% on average in June 2013, the first change since 2009; BI began raising rates in June.
- p. 6 (Box 1): BI raised the policy rate and the deposit facility rate by a total of 150 bp from June 2013, to 7.25% and 5.5%.
- p. 35 (Table 1): main exports 2012: oil and gas 18.7%, coal 13.6%, palm oil 8.6%, rubber 7.1%. Real GDP 6.2% (2012), projected 5.3%
  (2013) and **5.3% (2014)** (H1 2013 actual 5.9%); CPI average projected 7.2% (2013) and **7.6% (2014)**; current account −$24.4bn (2012),
  −$30.4bn (2013 proj.); gross reserves $112.8bn (2012), $95.7bn (September 2013).

### ID-IMF-3. IMF, *Indonesia: 2020 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 21/46, March 2021
URL: https://www.imf.org/-/media/files/publications/cr/2021/english/1idnea2021001.pdf (GUESSED; title page confirms CR 21/46). HTTP 200.
Accessed 23 Nov 2026. Press Release PR21/54, 1 March 2021; staff report dated 29 January 2021.
- PDF p. 2 (press release): GDP estimated to have fallen 1.9% in 2020; projected **4.8% in 2021** and 6% in 2022; inflation 1.7% at
  end-2020, below BI's 3±1% band.
- PDF p. 5 (Key Issues): a "bold and comprehensive" pandemic package; the plan to return to the 3%-of-GDP deficit ceiling by 2023 is a
  welcome commitment; BI bond purchases appropriate in exceptional circumstances, in 2021 only as a last resort.
- p. 6 (para 6–7): reserves up $7bn to $136bn at end-2020. To respond, "the ceiling on the budget deficit of 3 percent of GDP was
  suspended" through 2022, and the ban on BI buying long-term government bonds in the primary market was lifted.
- p. 9 (para 12–13): growth 4.8% in 2021; GDP in 2025 projected 5% below the January 2020 WEO path (scarring).
- p. 17 (referenced, PDF 21): the July 2020 BI–government "burden sharing" agreement (Appendix V).

### ID-IMF-4. IMF, *Indonesia: 2022 Article IV Consultation—Press Release; Staff Report; Staff Statement; and Statement by the Executive Director*, IMF Country Report No. 22/84, March 2022
URL: https://www.imf.org/-/media/files/publications/cr/2022/english/1idnea2022001.pdf (GUESSED; title page confirms CR 22/84). HTTP 200.
Accessed 23 Nov 2026. Press Release PR22/84, 11 March 2022; staff report dated 22 February 2022.
- PDF p. 2: staff project growth of **5.4% for 2022** and 6.0% for 2023, helped by commodity prices; risks tilted down.
- PDF p. 5 (Key Issues): restoring the 3% deficit ceiling (by 2023) is appropriate; the tax reform bill eased fears of a steep cut;
  BI primary-market purchases should end in 2022 as intended; a carbon tax is a welcome first step.
- p. 9: output gap from −4.9% of GDP (2020) to −1.9% (2023).

### ID-IMF-5. IMF, *Indonesia: 2023 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 23/221, June 2023
URL: https://www.imf.org/-/media/files/publications/cr/2023/english/1idnea2023002.pdf (GUESSED; title page confirms CR 23/221; the
`…2023001` file is a different report, see Not obtained). HTTP 200. Accessed 23 Nov 2026. Staff report dated 5 May 2023.
- PDF p. 2 (press release): growth to moderate to **5% in 2023**; Directors welcomed meeting the 3% deficit ceiling a year early and urged
  "phasing out export restrictions and not extending" them to other commodities (PDF p. 3).
- PDF p. 5 (Key Issues): keep the 3% ceiling as anchor; benefits of downstreaming must be weighed against costs, including cross-border
  spillovers; "export restrictions should be avoided".
- p. 10 (PDF 14): fiscal deficit narrowed to 2.4% of GDP in 2022.
- p. 24 (para 40–41): the 2020–24 development plan aims to cut dependence on raw commodity exports; tax holidays and export
  restrictions on raw materials promote downstream processing; the authorities may extend the policy to copper, bauxite, tin and farm goods,
  and see a chance to make EV batteries. Aim: high-income status by 2045.
- p. 27 (Box 1): Indonesia produced nearly half of world nickel output in 2022. Export tariff on nickel ore 2012; export ban 2014; ban
  lifted 2017; **ban reinstated January 2020** with a domestic processing requirement. FDI $22bn in 2022; 11 nickel smelters (3 in 2014),
  19 more expected; nickel exports $4.5bn (2019) → $19.6bn (2022), less than a third of the rise explained by prices. Footnote: a WTO
  panel (November 2022) found the ban inconsistent with GATT Article XI:1; Indonesia appealed on 8 December 2022.

### ID-IMF-6. IMF, *Indonesia: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 26/10, January 2026
Listing: IDN country page → issue page https://www.imf.org/en/publications/cr/issues/2026/01/21/indonesia-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-573330
(200). PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1idnea2026001-source-pdf.pdf (from the issue page). HTTP 200.
Accessed 23 Nov 2026. Board 14 January 2026; Press Release PR 26/010, 21 January 2026; staff report dated 16 December 2025.
- PDF p. 2: "Indonesia remains a global bright spot"; growth 5.0% in 2025 and **5.1% in 2026**; risks tilted to the downside (trade
  tensions, market volatility; large domestic policy shifts without guardrails). The IMF country page shows 5.0% for 2026 from the July 2026
  WEO Update.
- PDF p. 6 (Key Issues): keep the long-standing fiscal rules; limit quasi-fiscal activity; further BI rate cuts data-dependent; reduce BI's
  presence in the government bond market; exchange rate as shock absorber.
- p. 8: projections assume a 19% US tariff following trade talks.
- p. 14 (Text Table 1): Danantara, a super-holding for all state firms (including public banks), established February 2025, operating from
  October 2025; assets estimated at $900bn (63% of GDP), "one of the world's largest sovereign wealth funds"; initial funding $20bn.
- p. 29: since the 2020 nickel-ore export ban, Indonesia's share of world nickel production rose to about 60% (2024); refined-nickel export
  value has plateaued since 2023.

## Russia

### RU-IMF-1. IMF, *Russian Federation: 2009 Article IV Consultation—Staff Report; Staff Statement; Public Information Notice…*, IMF Country Report No. 09/246, August 2009
URL: https://www.imf.org/external/pubs/ft/scr/2009/cr09246.pdf (GUESSED; title page confirms CR 09/246). HTTP 200. Accessed 23 Nov 2026.
Staff report dated 13 July 2009.
- PDF p. 3 (summary): Russia was "hit hard by the dual shocks of declining oil prices and capital flow reversals"; banks under strain,
  private credit contracting; staff thought the fiscal stimulus too large and poorly targeted; monetary policy should move to inflation
  control with a flexible exchange rate. Regime reclassified to "other managed arrangement" from 1 November 2008.
- p. 9: gross reserves fell from a peak of $598bn (August 2008) to $375bn (March 2009), back above $400bn by end-June.
- p. 15: GDP to contract by 6½% in 2009 after 7–8% a year before the crisis; footnote: the 2010 forecast was raised from ½% to 1½% after
  the oil price assumption rose from $62.5 to $74.5.
- p. 29 (Table 1): real GDP 8.1% (2007), 5.6% (2008), **−6.5% (2009)**, **1.5% (2010)**; CPI average 14.1% (2008), 12.3% (2009);
  general government balance +4.3% of GDP (2008) → −5.4% (2009); non-oil balance −13.8% (2009).

### RU-IMF-2. IMF, *Russian Federation: 2014 Article IV Consultation—Staff Report; Informational Annex; Press Release*, IMF Country Report No. 14/175, July 2014
URL: https://www.imf.org/external/pubs/ft/scr/2014/cr14175.pdf (GUESSED; title page confirms CR 14/175). HTTP 200. Accessed 23 Nov 2026.
Staff report dated 11 June 2014 (before the oil price collapse).
- PDF p. 2 (Key Issues): structural slowdown in 2013; fallout from the Ukraine tensions "is bringing the economy to a standstill"; CBR
  raised rates and intervened to support the ruble; it should return to exchange-rate flexibility; keep the fiscal rule.
- p. 4–5 (Box 1): sanctions after Russia's actions in Crimea; Russian counter-sanctions of 20 and 24 March 2014.
- p. 13 (para 15–17): capital outflows to exceed $100bn in 2014 ($51bn in Q1); **growth 1% projected for 2015**; risks "starkly on the
  downside"; sanctions could derail integration.
- p. 36 (Table 2): real GDP 1.3% (2013), **0.2% (2014 proj.)**, 1.0% (2015 proj.); CPI average 6.6% (2014), **6.0% (2015)**.

### RU-IMF-3. IMF, *Russian Federation: 2015 Article IV Consultation—Press Release; and Staff Report*, IMF Country Report No. 15/211, August 2015
URL: https://www.imf.org/external/pubs/ft/scr/2015/cr15211.pdf (GUESSED; title page confirms CR 15/211). HTTP 200. Accessed 23 Nov 2026.
Press Release No. 15/368, 3 August 2015 (Board 29 July 2015).
- PDF p. 2: the slowdown was worsened by "the dual external shocks" of the oil price fall and sanctions; the authorities moved faster to a
  floating rate, raised rates and added FX liquidity; GDP to fall **3.4% in 2015**, growth to resume in 2016, medium-term growth 1.5%.
- p. 4 (para 3–4): net capital outflows $154bn (about 8% of GDP) in 2014, the highest since 1999–2000; terms-of-trade shock about 8% of GDP
  (footnote 2); in mid-December 2014 deposit outflows and the CBR rate rise hit banks.
- p. 5 (Box 1): sanctions bar new debt over 30 days for major state banks and energy firms; Russia banned food imports from 7 August
  2014. Model estimates: sanctions and counter-sanctions cut GDP by 1–1½% at first, up to 9% cumulatively over the medium term if prolonged.
- p. 5 (Box 2): the CBR floated the ruble in November 2014 and raised the policy rate to 17%, including by 650 bp on 16 December 2014.
- p. 7 (para 10–11): FX reserves to fall to about $360bn; recovery in 2016 muted because, unlike 2008–09, oil prices are assumed to stay low.
- p. 12 (para 24): in the authorities' view, "the recent oil price decline should be treated as permanent".
- PDF p. 4 (press-release table): real GDP 0.6% (2014), −3.4% (2015), **0.2% (2016)**; CPI average 7.8% (2014), **15.6% (2015)**.

### RU-IMF-4. (not obtained) IMF Russia 2019 Article IV — the two GUESSED file names returned 404; see Not obtained. Label kept so RU-IMF-5 is unchanged.

### RU-IMF-5. IMF, *Russian Federation: 2020 Article IV Consultation—Press Release; Staff Report*, IMF Country Report No. 21/36, February 2021
Listing: RUS country page (`index.json`) → issue page https://www.imf.org/en/publications/cr/issues/2021/02/08/russian-federation-2020-article-iv-consultation-press-release-staff-report-50068
(200). PDF: https://www.imf.org/-/media/files/publications/cr/2021/english/1rusea2021001.pdf (from the issue page). HTTP 200 (a first,
stalled download was killed and repeated). Accessed 23 Nov 2026. Press Release PR21/36, 9 February 2021. **This is the last Russia Article
IV the IMF lists.**
- PDF p. 2: "Russia entered the COVID-19 crisis with low growth but strong policy frameworks" and big buffers; since 2014 disciplined
  fiscal policy and inflation targeting brought low debt, reserve accumulation and de-dollarisation; but low oil prices, tight policies,
  sanctions and structural constraints meant lacklustre growth. GDP fell 3.1% in 2020 (less than the 3.6% in the staff report); fiscal
  support about 4.5% of GDP; policy rate cut 200 bp to a record-low 4.25%.
- PDF p. 4 (table): real GDP −3.6% (2020 staff est.), **3.0% (2021)**, 3.9% (2022); CPI average 3.4% (2020), 4.3% (2021); non-oil primary
  balance −10.3% of GDP (2020).
- p. 41 (Annex III, PDF 47): NIIP $556.6bn, 38.9% of GDP (Q3 2020); reserve assets 40.8% of GDP; the fiscal rule was suspended in 2020.

### RU-CBR-1. Bank of Russia, "Key Rate of the Bank of Russia" database (rate in effect, by day)
URLs: https://www.cbr.ru/eng/hd_base/KeyRate/ (200) and the same page with the page's own query parameters
`?UniDbQuery.Posted=True&UniDbQuery.From=…&UniDbQuery.To=…` for 1–31 Dec 2014, 20 Feb–31 Dec 2022 and 1 Jul 2023–31 Dec 2025 (all 200).
Accessed 23 Nov 2026. The page says data run from 17 September 2013 and the rate applies on every calendar day. Dates below are the first
day a new rate was in effect (own reading of the daily series; no PDF page).
- 2014: 9.50% (1 Dec) → 10.50% (12 Dec) → **17.00% (16 Dec)**.
- 2022: 9.50% (21 Feb) → **20.00% (28 Feb)** → 17.00% (11 Apr) → 14.00% (4 May) → 11.00% (27 May) → 9.50% (14 Jun) → 8.00% (25 Jul) →
  7.50% (19 Sep).
- 2023–25: 7.50% (Jul 2023) → 8.50% (24 Jul) → 12.00% (15 Aug 2023) → 13.00% → 15.00% → 16.00% (18 Dec 2023) → 18.00% (29 Jul 2024) →
  19.00% (16 Sep) → **21.00% (28 Oct 2024)** → 20.00% (9 Jun 2025) → 18.00% → 17.00% → 16.50% → 16.00% (22 Dec 2025). On 23 Nov 2026 the
  rate was 14.00%.

### RU-CBR-2. Bank of Russia, "Bank of Russia keeps the key rate at 14.00% p.a.", press release, 23 October 2026
URL: https://www.cbr.ru/eng/press/keypr/ (the latest key-rate release; 200). Accessed 23 Nov 2026. HTML, no page numbers.
- The Board "decided to keep the key rate at 14.00% per annum"; underlying inflation 5–6% annualised; seasonally adjusted price growth
  8.0% annualised in Q3 2026 (4.8% in Q2), core 6.2%; annual inflation 6.8% on 19 October, expected 7.1–7.6% at end-2026, back to 4.0%
  in 2027; key rate expected to average 12.5–13.5% in 2027. Unemployment near historic lows. Next meeting 18 December 2026.

## Gulf (Saudi Arabia, UAE)

### GC-IMF-1. IMF, *Saudi Arabia: 2015 Article IV Consultation—Press Release; Staff Report; and Informational Annex*, IMF Country Report No. 15/251, September 2015
URL: https://www.imf.org/external/pubs/ft/scr/2015/cr15251.pdf (GUESSED; title page confirms CR 15/251). HTTP 200. Accessed 23 Nov 2026.
Press Release No. 15/383, 17 August 2015 (Board 29 July 2015).
- PDF p. 2: oil prices down close to 50% over the past year; growth to slow to **2.8% in 2015** and **2.4% in 2016**; central government
  deficit **19.5% of GDP** projected for 2015; government debt 1.6% of GDP at end-2014; current account surplus 10.9% of GDP (2014), small
  deficit in 2015.
- PDF p. 3: Directors urged a gradual but sizable multi-year adjustment, energy price reform and new revenue, "including by introducing a
  VAT and a land tax".
- p. 11 (para 15): the fiscal "breakeven oil price rose to $106 a barrel in 2014" from $69 in 2010.
- PDF p. 4 (press-release table), 2014: revenue 37.3% of GDP, of which oil 32.6% (**own arithmetic: oil 87% of revenue**); exports $343.3bn,
  of which oil and refined products $285.2bn (**own arithmetic: 83%**); SAMA net foreign assets $724.3bn (36.3 months of imports),
  projected $659.8bn (2015).

### GC-IMF-2. IMF, *Saudi Arabia: 2016 Article IV Consultation—Press Release; Staff Report; and Informational Annex*, IMF Country Report No. 16/326, October 2016
URL: https://www.imf.org/external/pubs/ft/scr/2016/cr16326.pdf (GUESSED; title page confirms CR 16/326). HTTP 200. Accessed 23 Nov 2026.
Press Release No. 16/368, 28 July 2016 (Board 18 July 2016).
- PDF p. 2: growth to slow to **1.2% in 2016**, recover to **2% in 2017**; deficit to narrow to 13% of GDP in 2016; Vision 2030 and the
  National Transformation Program set out "a bold and ambitious transformation of the Saudi Arabian economy"; aim of budget balance in 5 years.
- p. 4 (para 3): end-2015 government deposits at SAMA about $280bn; SAMA net reserves $609bn (32 months of imports); government debt about
  5% of GDP.
- p. 5 (para 7): the deficit widened to 15.9% of GDP in 2015 from 3.4% in 2014, mainly because oil revenue fell 51%.
- p. 15 (Box 4, Vision 2030 and NTP targets): unemployment 11.6% → 7%; women's participation 22% → 30%; non-oil exports 16% → 50% "of
  total" (the Vision document itself says of non-oil GDP: see GC-GOV-1); non-oil revenue SR163bn (2015) → SR1 trillion by 2030; private
  sector 40% → 65% of GDP.

### GC-IMF-3. IMF, *Saudi Arabia: 2017 Article IV Consultation—Press Release; and Staff Report*, IMF Country Report No. 17/316, October 2017
URL: https://www.imf.org/-/media/files/publications/cr/2017/cr17316.pdf (GUESSED; title page confirms CR 17/316). HTTP 200. Accessed 23 Nov
2026. Press Release No. 17/292, 21 July 2017 (Board 17 July 2017).
- PDF p. 2: non-oil growth 1.7% in 2017 but overall growth near zero as oil output is cut under the OPEC+ agreement; Saudi unemployment
  12.3%; VAT due at the start of 2018; deficit 17.2% of GDP (2016) → 9.3% (2017) → under 1% by 2022.
- PDF p. 3: Vision 2030 was announced in 2016.
- p. 4 (table): real GDP 1.7% (2016), **0.1% (2017 proj.)**.
- p. 9 (Box 1): VAT at an initial 5% from the start of 2018, threshold SAR 375,000; revenue rising to about 1.6% of GDP by 2020; Saudi
  Arabia and the UAE have ratified the GCC VAT and excise agreements.
- p. 11 (para 9): **2018 growth projected at 1.1%**; oil output to fall 1.9% in 2017.

### GC-IMF-4. IMF, *Saudi Arabia: 2025 Article IV Consultation—Press Release and Staff Report*, IMF Country Report No. 25/223, August 2025
Listing: SAU country page → issue page https://www.imf.org/en/publications/cr/issues/2025/08/02/saudi-arabia-2025-article-iv-consultation-press-release-and-staff-report-569252
(200 on second try). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1sauea2025001-source-pdf.pdf. HTTP 200. Accessed 23
Nov 2026. Press Release PR 25/275, 4 August 2025 (Board 28 July 2025). Written before the 2026 Middle East war.
- PDF p. 2: non-oil GDP +4.5% in 2024; OPEC+ cuts held oil output at 9 mbpd (oil GDP −4.4%); overall growth 2.0%; current account −0.5%
  of GDP (2024) after +2.9% (2023); central bank NFA $415bn; real GDP to reach **3.9% by 2026**.
- p. 4 (table): oil and oil products 77% of exports; real GDP 2.0 / 3.6 / 3.9% (2024 / 2025 / 2026); fiscal balance −2.5 / −4.0 / −3.9% of
  GDP; public debt 26.2 / 29.8 / 32.6% of GDP; reserves 14.9 months of imports (2024).
- p. 15: Saudi Arabia is half of the GCC economy, holds $1.5 trillion of international assets (net IIP 59% of GDP) and is "the world's
  second largest sender of remittances" ($45.7bn in 2024, about 5% of the global total).
- p. 32 (Text Figure 19): 77% of PIF assets under management in Saudi Arabia (2023).

### GC-IMF-5. IMF, *United Arab Emirates: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 25/327, December 2025
Listing: ARE country page → issue page https://www.imf.org/en/publications/cr/issues/2025/12/08/united-arab-emirates-2025-article-iv-consultation-press-release-staff-report-and-statement-572397
(200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1areea2025001-source-pdf.pdf. HTTP 200. Accessed 23 Nov 2026. Press
Release PR25/274, 1 December 2025. Written before the 2026 war.
- PDF p. 2: growth **4.8% in 2025**, **5.0% in 2026**, on hydrocarbon output as OPEC+ quotas rise and on tourism, construction and finance;
  inflation 1.6% (2025); CEPAs support resilience and diversification.
- p. 9: expanding CEPAs expected to support external resilience; UAE markets less sensitive to global shocks than other GCC and EMs.
- p. 14: "The currency peg to the U.S. dollar remains appropriate."
- p. 29 (Table 3a): fiscal breakeven oil price $54.0 (2023), $48.3 (2024), $45.7 (2025), $44.8 (2026); hydrocarbon revenue AED 299.8bn of
  AED 564.4bn total in 2024 (**own arithmetic: 53%**), 44% in 2025 (projected).

### GC-GOV-1. Kingdom of Saudi Arabia, *Vision 2030* (document, 82 PDF pages, undated; announced in 2016 per GC-IMF-3)
URL: https://www.vision2030.gov.sa/media/rc0b5oy1/saudi_vision203.pdf (GUESSED; the site's home page https://www.vision2030.gov.sa/en
returned 403, but this PDF returned 200; title and foreword by King Salman and Mohammad bin Salman confirm the document). Accessed 23 Nov 2026.
- p. 7 (foreword): Aramco to become a global industrial conglomerate; "transform the Public Investment Fund into the world's largest
  sovereign wealth fund".
- p. 39: unemployment 11.6% → 7%; SME share of GDP 20% → 35%; women's workforce participation 22% → 30%.
- p. 47: from 19th largest economy to top 15; oil and gas localisation 40% → 75%; PIF assets from SAR 600bn to over SAR 7 trillion.
- p. 61: non-oil exports from 16% to 50% of non-oil GDP. p. 67: non-oil government revenue from SAR 163bn to SAR 1 trillion.

## Cross-cutting

### EM-X-1. Jim O'Neill, "Building Better Global Economic BRICs", Goldman Sachs Global Economics Paper No. 66, 30 November 2001
URL: https://www.goldmansachs.com/pdfs/insights/archive/archive-pdfs/build-better-brics.pdf (GUESSED; two other guessed goldmansachs.com
URLs returned 404). HTTP 200. Accessed 23 Nov 2026. 16 PDF pages, printed "S.01"–.
- S.01: at end-2000 Brazil, Russia, India and China (BRIC) were about 23.3% of world GDP at PPP and 8% at current prices; China's GDP was
  bigger than Italy's; the G7 should be adjusted to include BRIC representatives.
- S.03: four scenarios for 2001–11; in all, the BRICs' weight rises from 8.0% to 14.2% (current dollars), or from 23.3% to 27.0% at PPP,
  led by China. Euro-area G7 seats should fall from three to one, and China and probably Brazil and Russia, possibly India, should join.
  "It is time for the world to build better global economic BRICs."

### EM-X-2. World Bank, *Global Economic Prospects, January 2016: Spillovers amid Weak Growth*, Chapter 2, Europe and Central Asia, p. 89 (with footnote 3)
URL: https://openknowledge.worldbank.org/bitstreams/e84a15ae-c750-5722-9414-45df4eb3fb93/download (taken from the book's own note
EN-WB-4, which found it through the OKR search API; refetched here). HTTP 200. Accessed 23 Nov 2026.
- p. 89: in mid-2013, when markets reassessed the timing of US tapering, the "Fragile Five" countries "came under severe currency pressure
  as a result of a loss of investor confidence"; Kazakhstan, Russia and Ukraine now face similar vulnerabilities.
- p. 89, footnote 3 (exact naming): the "Fragile Five" comprised Brazil, India, Indonesia, Turkey, and South Africa; Turkey's position
  somewhat improved but still vulnerable (citing Arteta et al. 2015). No document read attributes the term to Morgan Stanley; that
  attribution is not confirmed here.

### EM-X-3. World Bank, *India Development Update: India's Growth Story*, March 2018, pp. 34–35 and Table 3
URL: http://documents.worldbank.org/curated/en/814101517840592525/pdf/India-development-update-Indias-growth-story.pdf (taken from the
book's note IN-WB-3, which found it through the Documents & Reports API; refetched here). HTTP 200. Accessed 23 Nov 2026.
- p. 34: taper talk began on 22 May 2013 (Bernanke); "market commentary focused on five countries", Brazil, Indonesia, India, Turkey and
  South Africa, called the "Fragile Five"; India had the second-largest depreciation and reserve fall in the group; the rupee fell 18% at
  one point.
- p. 35 (Table 3, April–August 2013, from Basu, Eichengreen and Gupta 2015): exchange-rate depreciation Brazil 17.01%, Indonesia 8.33%,
  India 15.70%, Turkey 9.21%, South Africa 10.60%; reserves Brazil −3.07%, Indonesia −13.30%, India −5.89%, Turkey −4.56%, South Africa −5.05%.
  India's current account deficit rose from about 1% of GDP (2006) to nearly 5% (2013).

### EM-X-4. BRICS, *6th BRICS Summit: Fortaleza Declaration*, Fortaleza, Brazil, 15 July 2014 (text as held by the University of Toronto BRICS Information Centre)
URL: http://www.brics.utoronto.ca/docs/140715-leaders.html (GUESSED path; title "2014 Fortaleza Declaration"). HTTP 200. Accessed 23 Nov
2026. HTML, paragraph numbers. (No official brics or government host was tried; ndb.int has the founding date, EM-X-6.)
- Para 11: signing of the Agreement establishing the New Development Bank, to mobilise resources for infrastructure and sustainable
  development in BRICS and other EMDCs.
- Para 12: initial authorised capital US$100bn; initial subscribed capital US$50bn, equally shared; first Board of Governors chair from
  Russia, Board of Directors chair from Brazil, first President from India. "The headquarters of the Bank shall be located in Shanghai."
  An Africa Regional Center in South Africa.
- Para 13: Treaty for the BRICS Contingent Reserve Arrangement, initial size US$100bn.

### EM-X-5. BRICS, *XV BRICS Summit Johannesburg II Declaration*, Sandton, 22–24 August 2023; *XVI BRICS Summit Kazan Declaration*, 22–24 October 2024; *BRICS Rio de Janeiro Declaration*, 6–7 July 2025 (University of Toronto BRICS Information Centre texts)
URLs: http://www.brics.utoronto.ca/docs/230823-declaration.html, …/241023-declaration.html, …/250706-declaration.html (all GUESSED paths;
titles checked). HTTP 200 each. Accessed 23 Nov 2026. HTML.
- Johannesburg II (paragraph on expansion, near the end): BRICS invited Argentina, Egypt, Ethiopia, Iran, Saudi Arabia and the UAE "to
  become full members of BRICS from 1 January 2024". (Who actually took up membership is not stated in this text.)
- Kazan (para 5): endorses the "Modalities of BRICS Partner Country Category"; no list of members in the paragraphs read.
- Rio (para 3): "We welcome the Republic of Indonesia as a BRICS member", and names ten partner countries (Belarus, Bolivia, Kazakhstan,
  Cuba, Nigeria, Malaysia, Thailand, Vietnam, Uganda, Uzbekistan).

### EM-X-6. New Development Bank, "History" page
URL: https://www.ndb.int/about-ndb/history/ (linked from https://www.ndb.int/about-ndb/, 200). HTTP 200. Accessed 23 Nov 2026. HTML.
- Agreement signed at the sixth BRICS summit in Fortaleza (2014); established 2015; inaugural Board of Governors 7 July 2015; first paid-in
  capital 2016. "NDB admitted Bangladesh, Egypt, UAE, and Uruguay as new member countries." (2021); Algeria (listed under 2024); Uzbekistan,
  Colombia and Ethiopia (2025). India Regional Office in GIFT City (2022); Dilma Rousseff elected President (2023), re-elected (2025).

Taper tantrum and EM resilience: already in the book (see below); not refetched.

## India links (Economic Surveys on disk)

### EM-IN-B-1. ES 2021-22, Vol. 2, Ch. 3 "External Sector", Box on taper, p. 111 (st. 137), footnote 7 — **already in the book** (`India_ES_2020-2022.md`, Economic Survey 2021-22 section)
- After the May 2013 taper signal India saw portfolio outflows of ₹79,375 crore (23 May–30 August 2013); after the November 2021 taper,
  ₹34,178 crore. India went from the Fragile Five to the fourth-largest reserve holder. Footnote 7 names the five (Indonesia, South Africa,
  Brazil, Turkey, India), which "were identified to be most at risk when tapering began in 2013".

### EM-IN-B-2. ES 2022-23, Ch. 2 "India's Medium-Term Growth Outlook: With Optimism and Hope", para 2.29, p. 36 (st. 79)
- Global capital flows and "optimism about BRICS" fed India's credit and investment boom; non-financial private debt rose from 72.9% of
  GDP (March 2004) to 113.6% (December 2010); the twin-deficit crisis of 2013 exposed it.

### EM-IN-B-3. ES 2017-18, Vol. 2, Ch. 8 "Industry and Infrastructure", p. 130 (st. 278)
- India needs about US$4.5 trillion of infrastructure investment to 2040 (gap about US$526bn); among funders the Survey names the AIIB and
  the New Development Bank, "erstwhile BRICS Bank", focused on sustainable and infrastructure projects (paraphrase; two-column text).

### EM-IN-B-4. ES 2025-26, Ch. 4 "External Sector", para 4.7, p. 147 (st. 198)
- The Russia-Ukraine war, rerouted energy trade and "the expansion of BRICS exemplify this realignment" towards "geostrategic
  globalisation"; also names the Quad, IPEF and the India–Middle East–Europe Corridor.

### EM-IN-B-5. ES 2022-23, Ch. 11 "External Sector: Watchful and Hopeful", paras 11.19–11.21, pp. 320 and 323 (st. 363, 366)
- p. 320: India signed FTAs with the UAE and Australia in 2022. In July 2022 the RBI allowed "invoicing, payment, and settlement of
  exports/imports in Indian Rupees (INR)", with market exchange rates and special Rupee Vostro accounts at Indian banks.
- p. 323: the India–UAE CEPA was signed on 18 February 2022 and entered into force on 1 May 2022.

### EM-IN-B-6. ES 2023-24, Ch. 4 "External Sector", paras 4.36–4.38, p. 128 (st. 175)
- The UAE has been among India's top three trade partners for two decades; bilateral trade US$83.7bn in FY24; the UAE is India's second-
  largest export market (about US$35.6bn) and eighth-largest investor (US$18bn; Indian investment in the UAE about US$85bn). CEPA aims at
  US$100bn of goods trade within five years and US$15bn of services; first Indian FTA with a pharmaceuticals annex and digital trade.

### EM-IN-B-7. ES 2023-24, Ch. 4, para 4.56, p. 134 (st. 181), and p. 137 (st. 184)
- p. 134: remittances helped by the "agreement with the UAE to promote the use of Dirhams and Rupees"; India the top recipient in 2023
  (about US$120bn, World Bank chart); forecast US$124bn (2024) and US$129bn (2025).
- p. 137: the mix of skilled migrants in OECD countries and less-skilled migrants in the GCC should keep remittances stable; UPI links with
  the UAE and Singapore should cut costs.

### EM-IN-B-8. ES 2025-26, Ch. 4, para 4.65, p. 174 (st. 225) — also used in `India_2026.md` IN26-8
- RBI's sixth remittance survey (FY24): GCC countries historically dominated, but "AEs now contribute more, indicating a shift towards
  skilled and professional workers": US 27.7%, UAE 19.2%, UK 10.8%, Singapore 6.6%.

### EM-IN-B-9. ES 2017-18, Vol. 2, Ch. 6 "External Sector" (Invisibles), para 6.13, p. 86 (st. 234)
- Gross private transfers fell from US$69.8bn (2014-15) to US$65.6bn and US$61.3bn (2015-16, 2016-17), largely because of the oil price
  fall. Indian workers emigrating to Saudi Arabia (third-largest remittance source) fell from 3.0 lakh (2015) to 1.6 lakh (2016), to the UAE
  (largest source) from 2.2 to 1.6 lakh; labour market adjustment in the GCC cited.

### EM-IN-B-10. ES 2022-23, Ch. 11, para 11.15, p. 318 (st. 361); ES 2025-26, Ch. 4, paras 4.41–4.42, p. 163 (st. 214)
- p. 318 (ES 2022-23): China, UAE, USA, Russia and Saudi Arabia together supplied 40% of India's imports (April–November 2022).
- p. 163 (ES 2025-26): in April–November 2025 crude imports from Russia, Saudi Arabia, Iraq and Venezuela fell; the US share rose to 8.1%
  (from 4.6%), the UAE's to 11.1% (from 9.4%). No Survey read gives Russian crude volumes or the post-2022 discount (see Not obtained;
  `India_ES_2024-2026.md` ES25-8 already holds the p. 163 passage).

### EM-IN-B-11. ES 2021-22, Vol. 2, Ch. 3 "External Sector", p. 96 (st. 122); ES 2020-21, Vol. 2, Ch. 5 "Prices and Inflation", p. 175 (st. 547); ES 2022-23, Ch. 5, para 5.14, p. 125 (st. 168)
- ES 2021-22 p. 96: Indonesia, the second-biggest source of crude palm oil, among India's top ten suppliers (2.9% of imports,
  April–November 2021).
- ES 2020-21 p. 175: edible-oil imports were hit in 2020 when Malaysia and Indonesia imposed export tariffs on crude palm oil, raising
  domestic palm oil prices in January–June 2020.
- ES 2022-23 p. 125: India imports 60% of its edible oil; sunflower oil (15% of edible-oil imports) comes mainly from Ukraine and Russia.

---

## Forecast vs outturn pairs (own arithmetic; outturns from `data/clean/weo/NGDP_RPCH.json` and `PCPIPCH.json`, WEO October 2026; last actual year 2025 for all four countries, so 2026 values are still projections)

| Country | Report (page) | Forecast | Outturn (WEO Oct 2026) | Gap |
|---|---|---|---|---|
| Indonesia | CR 07/272 p. 34 | GDP 6.3% for 2008 | 7.4% | +1.1 (current series; GDP since rebased) |
| Indonesia | CR 13/362 p. 35 | GDP 5.3% for 2014 | 5.0% | −0.3 |
| Indonesia | CR 13/362 p. 35 | CPI 7.6% for 2014 | 6.4% | −1.2 |
| Indonesia | CR 21/46 PDF p. 2 | GDP 4.8% for 2021 | 3.7% | −1.1 (Delta wave) |
| Indonesia | CR 22/84 PDF p. 2 | GDP 5.4% for 2022; 6.0% for 2023 | 5.3%; 5.0% | −0.1; −1.0 |
| Indonesia | CR 23/221 PDF p. 2 | GDP 5% for 2023 | 5.0% | 0.0 |
| Indonesia | CR 26/10 PDF p. 2 | GDP 5.1% for 2026 | 5.1% (projection) | — |
| Russia | CR 09/246 p. 29 | GDP −6.5% for 2009; 1.5% for 2010 | −7.8%; 4.5% | −1.3; +3.0 |
| Russia | CR 14/175 p. 36 | GDP 0.2% for 2014; 1.0% for 2015 | 0.7%; −2.0% | +0.5; −3.0 (oil collapse, sanctions) |
| Russia | CR 14/175 p. 36 | CPI 6.0% for 2015 | 15.5% | +9.5 |
| Russia | CR 15/211 PDF p. 4 | GDP −3.4% for 2015; 0.2% for 2016 | −2.0%; 0.2% | +1.4; 0.0 |
| Russia | CR 15/211 PDF p. 4 | CPI 15.6% for 2015 | 15.5% | −0.1 |
| Russia | CR 21/36 PDF p. 4 | GDP 3.0% for 2021 | 5.9% | +2.9 |
| Saudi Arabia | CR 15/251 PDF p. 2 | GDP 2.8% for 2015; 2.4% for 2016 | 4.7%; 1.7% | +1.9; −0.7 |
| Saudi Arabia | CR 16/326 PDF p. 2 | GDP 1.2% for 2016; 2% for 2017 | 1.7%; 1.2% | +0.5; −0.8 |
| Saudi Arabia | CR 17/316 p. 4, p. 11 | GDP 0.1% for 2017; 1.1% for 2018 | 1.2%; 3.2% | +1.1; +2.1 |
| Saudi Arabia | CR 25/223 p. 4 | GDP 3.6% for 2025; 3.9% for 2026 | 4.6%; −3.3% (projection) | +1.0; −7.2 (2026 war) |
| UAE | CR 25/327 PDF p. 2 | GDP 4.8% for 2025; 5.0% for 2026 | 6.2%; −3.9% (projection) | +1.4; −8.9 (2026 war) |

Caution: later WEO vintages include data revisions (Saudi and Indonesian GDP series have been revised since the early reports); this note
did not check how much of each gap is revision rather than forecast error.

## Already in the book (cite; not refetched)

- Taper tantrum: `IMF_2010-2014.md`, WEO October 2013 Ch. 1 pp. 7, 16 (taper hints; EM local bond yields jumped about three times the April
  2013 scenario) and "India threads" (rupee among the hardest hit); `Theme_markets.md` MK-OTH-7 (BIS Annual Report 2014, Ch. II pp. 24,
  28–29: currencies of Brazil, India, Indonesia, South Africa and Turkey fell more than 10%; Brazil, India, Indonesia and Russia each lost
  more than $10bn of reserves); MK-IMF-4 (GFSR April 2020 Ch. 3, COVID outflows vs the 2013 taper; includes an "original sin" remark); `Theme_money.md` MO-IMF-3 (WEO October 2018 Ch. 3, EM monetary frameworks, pp. 113–114: pass-through 14% in the taper tantrum for
  less-anchored EMs; better-anchored ones more resilient); MO-IN-4 (Indonesia cut its target from 6% to 2.5%).
- Fragile Five: `India_ES_2020-2022.md`, ES 2021-22 taper box (= EM-IN-B-1).
- BRICS growth: `Theme_growth.md` GR-IMF-3 (WEO April 2017 Ch. 2 Box 2.1 p. 89: BRICS income gap narrowed 2002–14; Russia +26 points of
  US level); GR-IMF-4 (WEO April 2024 Ch. 3 p. 67: five-year forecasts cut for Brazil, China, India, Indonesia, Russia).
- Oil: `IMF_2014-2019.md` WEO April 2015 Ch. 1 p. 5 (OPEC's November 2014 decision; supply-driven fall); `Theme_energy.md` EN-WB-3 (GEP
  January 2015, oil plunge; OPEC shift to market share) and EN-WB-7 (CMO October 2026: Saudi Arabia and Iraq lost about 4.4 and 2.1 mb/d);
  `IMF_2020-2021.md` WEO April 2020 Ch. 1 p. 2 and CSF pp. 17–19 (OPEC+ breakdown 6 March 2020).
- Russia 2022: `IMF_2022-2023.md` WEO April 2022 Ch. 1 p. 4 (Russia −8.5% 2022 forecast; ruble fell close to 60% then recovered; spreads
  +2,500 bp), Table 1.1 p. 6; later WEO tables for Russia.
- Gulf 2026 war: `IMF_2026.md` WEO October 2026 Ch. 1 p. 13 (Saudi Arabia −3.3% in 2026, 7.9% in 2027; Bahrain, Iraq, Kuwait, Qatar double-
  digit contractions), Table 1.1 p. 11 (Saudi Q4/Q4 −6.2%), CSF p. 31 (Gulf crude exports 16.7 mb/d in September); "How the 2026 forecast
  moved" (Saudi 2026: 4.5 → 3.1 → 1.7 → −3.3); `Theme_energy.md` note on the war's start date.
- Remittances and the Gulf: `Theme_demography.md` DL-WB-3 (WDR 2023: about 17% of migrants, 31 million, in the Gulf states) and DL-OTH-4
  (IOM 2026: Saudi Arabia second-largest sender, $46.56bn in 2024); `India_2026.md` IN26-8 (GCC 38% of India's FY24 remittances; 9.2
  million Indians in West Asia); WDI `BX.TRF.PWKR.CD.DT` series.
- Fragmentation: `Theme_trade.md` TR-IMF-3 (WEO April 2023 Ch. 4 p. 104: India and Indonesia in the baseline); IN26-40 (MER September 2026:
  US "Graham Bill" on buyers of Russian crude; flagged single-source).

## Not obtained

- **Bank Indonesia** (https://www.bi.go.id/en/default.aspx and https://www.bi.go.id/en/): no response (curl status 000, time-outs at 60 s and
  120 s, three tries). No ID-BI item.
- **IMF Russia 2019 Article IV**: GUESSED https://www.imf.org/-/media/files/publications/cr/2019/english/1rusea2019001.pdf and `…2019002.pdf`
  — both 404. Not pursued further. **No Russia Article IV after CR 21/36 exists on the IMF country page.**
- **IMF Saudi Arabia 2018 Article IV**: GUESSED `/-/media/files/publications/cr/2018/cr18263.pdf` (404), `cr18264.pdf` (404); `cr18262.pdf`
  (200) is Mauritius, a price-statistics TA report — discarded.
- **IMF Indonesia 2024 Article IV**: GUESSED `/cr/2024/english/1idnea2024001.pdf` — 404. `/cr/2023/english/1idnea2023001.pdf` (200) is CR
  23/59, an Indonesia financial soundness indicators TA report — discarded.
- **Bank of Russia press releases of 16 December 2014 and 28 February 2022**: GUESSED `https://www.cbr.ru/eng/press/pr/?file=28022022_093000Key_e.htm`
  and `…?file=16122014_004000key_e.htm` returned 200 but an empty "Press release" shell with no text. The decisions page lists only 2024–26
  material. Rates and dates are taken from the key-rate database instead (RU-CBR-1); the IMF gives the 650 bp rise of 16 December 2014 (RU-IMF-3).
- **Vision 2030 website** https://www.vision2030.gov.sa/en — 403 (the PDF on the same host was 200; GC-GOV-1).
- **Goldman Sachs**: https://www.goldmansachs.com/insights/archive/building-better.html,
  https://www.goldmansachs.com/intelligence/archive/archive-pdfs/build-better-brics.pdf and https://www.goldmansachs.com/insights/archive/
  — all 404 (EM-X-1 came from a third GUESSED path).
- **Morgan Stanley's original "Fragile Five" note (2013)**: not attempted; no document read names Morgan Stanley as the source of the term.
- **IMF Regional Economic Outlook, Middle East and Central Asia**: not fetched (time); the 2026 Gulf forecasts are already in `IMF_2026.md`.
- **Official BRICS/government host for the declarations** (e.g. brics.br, mea.gov.in): not tried; University of Toronto copies used.
- **Who joined BRICS in 2024**: no document read states which of the six invitees took up membership (Argentina, Saudi Arabia status
  not confirmed). The Rio 2025 text confirms Indonesia as a member.
- **Russian crude volumes/discounts to India after 2022** in the Surveys: searched ES 2022-23 to 2025-26 for "Russia" with oil/crude/import
  terms; no figures found.

## Bibliography rows

| Key | Title | Publisher | Year | Edition / report no. | URL |
|---|---|---|---|---|---|
| imf-idn-2007 | Indonesia: 2007 Article IV Consultation—Staff Report | IMF | 2007 | CR 07/272 | https://www.imf.org/external/pubs/ft/scr/2007/cr07272.pdf |
| imf-idn-2013 | Indonesia: Staff Report for the 2013 Article IV Consultation | IMF | 2013 | CR 13/362 | https://www.imf.org/external/pubs/ft/scr/2013/cr13362.pdf |
| imf-idn-2021 | Indonesia: 2020 Article IV Consultation | IMF | 2021 | CR 21/46 | https://www.imf.org/-/media/files/publications/cr/2021/english/1idnea2021001.pdf |
| imf-idn-2022 | Indonesia: 2022 Article IV Consultation | IMF | 2022 | CR 22/84 | https://www.imf.org/-/media/files/publications/cr/2022/english/1idnea2022001.pdf |
| imf-idn-2023 | Indonesia: 2023 Article IV Consultation | IMF | 2023 | CR 23/221 | https://www.imf.org/-/media/files/publications/cr/2023/english/1idnea2023002.pdf |
| imf-idn-2026 | Indonesia: 2025 Article IV Consultation | IMF | 2026 | CR 26/10 | https://www.imf.org/-/media/files/publications/cr/2026/english/1idnea2026001-source-pdf.pdf |
| imf-rus-2009 | Russian Federation: 2009 Article IV Consultation | IMF | 2009 | CR 09/246 | https://www.imf.org/external/pubs/ft/scr/2009/cr09246.pdf |
| imf-rus-2014 | Russian Federation: 2014 Article IV Consultation | IMF | 2014 | CR 14/175 | https://www.imf.org/external/pubs/ft/scr/2014/cr14175.pdf |
| imf-rus-2015 | Russian Federation: 2015 Article IV Consultation | IMF | 2015 | CR 15/211 | https://www.imf.org/external/pubs/ft/scr/2015/cr15211.pdf |
| imf-rus-2021 | Russian Federation: 2020 Article IV Consultation | IMF | 2021 | CR 21/36 | https://www.imf.org/-/media/files/publications/cr/2021/english/1rusea2021001.pdf |
| cbr-keyrate | Key Rate of the Bank of Russia (database) | Bank of Russia | 2026 | accessed 23 Nov 2026 | https://www.cbr.ru/eng/hd_base/KeyRate/ |
| cbr-2026-10 | Bank of Russia keeps the key rate at 14.00% p.a. | Bank of Russia | 2026 | press release, 23 Oct 2026 | https://www.cbr.ru/eng/press/keypr/ |
| imf-sau-2015 | Saudi Arabia: 2015 Article IV Consultation | IMF | 2015 | CR 15/251 | https://www.imf.org/external/pubs/ft/scr/2015/cr15251.pdf |
| imf-sau-2016 | Saudi Arabia: 2016 Article IV Consultation | IMF | 2016 | CR 16/326 | https://www.imf.org/external/pubs/ft/scr/2016/cr16326.pdf |
| imf-sau-2017 | Saudi Arabia: 2017 Article IV Consultation | IMF | 2017 | CR 17/316 | https://www.imf.org/-/media/files/publications/cr/2017/cr17316.pdf |
| imf-sau-2025 | Saudi Arabia: 2025 Article IV Consultation | IMF | 2025 | CR 25/223 | https://www.imf.org/-/media/files/publications/cr/2025/english/1sauea2025001-source-pdf.pdf |
| imf-are-2025 | United Arab Emirates: 2025 Article IV Consultation | IMF | 2025 | CR 25/327 | https://www.imf.org/-/media/files/publications/cr/2025/english/1areea2025001-source-pdf.pdf |
| ksa-vision2030 | Vision 2030 | Kingdom of Saudi Arabia | 2016 | — | https://www.vision2030.gov.sa/media/rc0b5oy1/saudi_vision203.pdf |
| oneill-2001 | Building Better Global Economic BRICs | Goldman Sachs (Jim O'Neill) | 2001 | Global Economics Paper No. 66 | https://www.goldmansachs.com/pdfs/insights/archive/archive-pdfs/build-better-brics.pdf |
| wb-gep-2016-01 | Global Economic Prospects, January 2016: Spillovers amid Weak Growth | World Bank | 2016 | January 2016 | https://openknowledge.worldbank.org/bitstreams/e84a15ae-c750-5722-9414-45df4eb3fb93/download |
| wb-idu-2018-03 | India Development Update: India's Growth Story | World Bank | 2018 | March 2018 | http://documents.worldbank.org/curated/en/814101517840592525/pdf/India-development-update-Indias-growth-story.pdf |
| brics-fortaleza-2014 | 6th BRICS Summit: Fortaleza Declaration | BRICS (via U. of Toronto BRICS Information Centre) | 2014 | 15 July 2014 | http://www.brics.utoronto.ca/docs/140715-leaders.html |
| brics-johannesburg-2023 | XV BRICS Summit Johannesburg II Declaration | BRICS (via U. of Toronto) | 2023 | 23 Aug 2023 | http://www.brics.utoronto.ca/docs/230823-declaration.html |
| brics-kazan-2024 | XVI BRICS Summit Kazan Declaration | BRICS (via U. of Toronto) | 2024 | 23 Oct 2024 | http://www.brics.utoronto.ca/docs/241023-declaration.html |
| brics-rio-2025 | BRICS Rio de Janeiro Declaration | BRICS (via U. of Toronto) | 2025 | 6 July 2025 | http://www.brics.utoronto.ca/docs/250706-declaration.html |
| ndb-history | History | New Development Bank | 2026 | web page, accessed 23 Nov 2026 | https://www.ndb.int/about-ndb/history/ |
