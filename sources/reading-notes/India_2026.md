# India and the 2026 energy shock — reading notes

These notes cover the India section of Phase 9, "2026: a new energy shock" (calendar 2026, history in progress). In fiscal-year terms that is the last month of FY2025-26 (March 2026) and the first half-plus of FY2026-27 (FY27). The question is how the shock reached India (oil import bill, current account, rupee, inflation, capital flows, Gulf remittances), how policy responded (RBI; the Centre's budget, fuel taxes, LPG and fertiliser measures), and how India fared. Items are numbered IN26-n; numbering is new to this file. Notes written 22 November 2026.

**Sources.**
- Held locally (`Econ Subject/sources/`):
  - `text/docs/bs2026-27.txt` and `raw/docs/bs2026-27.pdf`: Budget Speech 2026-27, 1 February 2026. I re-fetched https://www.indiabudget.gov.in/doc/Budget_Speech.pdf (linked from the indiabudget.gov.in home page) and it is byte-identical to the local PDF (678,384 bytes).
  - `text/docs/frbm1_2026-27.txt`: FRBM statement (Medium-Term Fiscal Policy cum Fiscal Policy Strategy Statement), Union Budget 2026-27 (https://www.indiabudget.gov.in/doc/frbm1.pdf). The text is two-column and the extraction interleaves columns; quotes were taken from the Budget Speech instead.
  - `text/es2025-26.txt`: Economic Survey 2025-26, used only for its pre-shock outlook (Preface scenarios; Ch 4 remittances; Ch 5 commodity outlook). Stitched-page offsets as in `India_ES_2024-2026.md` (main text p. = st. − 51; Preface p. vii = st. 8).
- Fetched 22 November 2026 with plain curl into `/private/tmp/claude-501/india2026.ObHdaG/`:
  - DEA, **Monthly Economic Review (MER)**, 2026 issues listed at http://dea.gov.in/reports-monthly-economic-report (listing "Last Updated On: 16.11.2026"). Eight issues are listed for 2026: February, March, April, May, June, July, August and September. Files under http://dea.gov.in/files/monthly_economic_report_documents/: `Monthly%20Economic%20Review%20February%202026.pdf` (53 pp.), `File_MER%20March%202026%20%281%29.pdf` (40), `Monthly%20Economic%20Review%20April%202026.pdf` (51), `MER%20May%202026.pdf` (44), `Monthly%20Economic%20Review%20June%202026.pdf` (46), `MER_July_2026.pdf` (44), `MER-Aug-2026.pdf` (39), `MERSept2026.pdf` (46). All eight read for oil, inflation, rupee, current account, remittances, RBI and the government response.
  - RBI (https://www.rbi.org.in), page text:
    - MPC resolutions and Governor's Statements of 8 April (prid 62514, 62515), 5 June (62863, 62864), 5 August (63287, 63288) and 7 October 2026 (63742, 63744), found from https://www.rbi.org.in/Scripts/Annualpolicy.aspx.
    - RBI Annual Report 2025-26 (released 29 May 2026), HTML chapters at https://www.rbi.org.in/Scripts/AnnualReportPublications.aspx?Id=1461 (Ch I), 1462 (Ch II), 1463 (Ch III), 1465 (Ch V).
    - Press release "Developments in India's Balance of Payments for the Month of September 2026", 13 November 2026 (prid 63974).
  - PIB, only releases linked from the MERs: PRID 2245970 (Petroleum, 27 March 2026; reached via the April MER's tinyurl footnote), 2253243 (Cabinet, 18 April 2026; via tinyurl), 2269169 (Finance, 5 June 2026), 2247993 (Commerce, 1 April 2026), 2253000 (Commerce, 17 April 2026), 2280999 (Consumer Affairs, 4 July 2026).
  - IMF India country page, https://www.imf.org/en/Countries/IND (page metadata "dateModified" 30 September 2026).

**Data cut-offs, as the texts show them.**
- Budget Speech and FRBM statement: 1 February 2026, **before the conflict**. RE 2025-26 and BE 2026-27 are pre-shock numbers.
- ES 2025-26: Preface dated 29 January 2026, also pre-shock.
- MER February 2026: body written mostly before the outbreak; the Preface was written after it ("over the last weekend"). Crude price to 27 February 2026.
- MER March 2026: Preface dated 25 March 2026; rupee to 24 March; e-way bills to 22 March.
- MER April 2026: Preface "sixty days" after 28 February; crude to 24 April; reserves to 10 April; FPI to 17 April.
- MER May 2026: FPI to 21 May; rupee to 26 May; reserves to 8 May.
- MER June 2026: FPI and rupee to 22 June; reserves to 12 June; BoP to April 2026.
- MER July 2026: rupee to 24 July; reserves to 10 July; BoP to May 2026.
- MER August 2026: rupee and FPI to 19–20 August; reserves to 14 August (abstract: 7 August); BoP to June 2026.
- MER September 2026: reserves to 18 September; BoP to July 2026.
- RBI Annual Report 2025-26: covers April 2025–March 2026, outlook as of the April 2026 MPC; released 29 May 2026. GDP is the NSO Second Advance Estimate, new base 2022-23 (released 27 February 2026).
- MPC: 6–8 April, 3–5 June, 3–5 August, 5–7 October 2026. Next meeting scheduled 2–4 December 2026 (after today).
- RBI BoP release: data to September 2026, released 13 November 2026. **This is the latest hard data point in these notes.**

**How pages are cited.**
- MER: "PDF p. N" = form-feed count + 1 in the `pdftotext -layout` extract. Printed page numbers differ by issue (for example, March and April MER printed numbers are PDF − 1), so only PDF pages are given. MER paragraph numbers are given where the text has them.
- RBI Annual Report: the HTML edition has no page numbers; cite chapter and paragraph (e.g. "AR para II.7.20"). The PDF chapters could not be fetched (see Not found).
- RBI MPC documents: resolution paragraph ("Res. para") or Governor's Statement paragraph ("GS para") and footnote ("fn").
- Budget Speech: para and PDF p. FRBM: para and PDF p. ES 2025-26: printed p. and stitched (st.) page.

**Quotes.** Every quote below was checked by script against the source extract (case, spaces, curly quotes and line-end hyphens normalised). Each is under 15 words, and each item has at most one. Quotes avoid the ₹ sign.

**On naming the war.** The RBI documents, the RBI Annual Report and most MERs call it "the West Asia conflict", dated from 28 February 2026 (IN26-2). Only the MER February 2026 names the parties and events (IN26-1). Attribute any naming to that MER.

---

## The shock and how it began

**IN26-1 — DEA's first account of the outbreak.** MER February 2026, Preface, PDF pp. 3–5; para 29, PDF p. 25; para 93, PDF p. 48.
- The Preface says that "over the last weekend" the United States and Israel launched an attack on Iran called "Operation Epic Fury". It reports the death of Iran's Supreme Leader, Iranian attacks on several Gulf states, oil and gas installations hit and supplies disrupted, and Gulf airspace shut.
- Para 93 dates the strikes to 28 February 2026, names the Supreme Leader, says about 20% of global oil flows pass the Strait of Hormuz, and reports Brent up about 9% to near USD 80 and LNG prices up about 50%.
- The Preface says scenario exercises suggest crude must stay above 100 dollars a barrel for a sustained period before India's macro aggregates show strain, but gas, cooking gas and sea-lane safety are further unknowns.
- It says the risks to India's balance of payments "may have become elevated", and that the rest of the issue was written mostly before the war.

Quote (Preface, PDF p. 3): "The Strait of Hormuz appears to be closed for all practical purposes"

FLAG (naming): no RBI document read here names the parties. Only this MER does. Use it with attribution, or say "the West Asia conflict" as the RBI does.

FLAG (typo in source): the same Preface calls the US tariff law the "International Economic Emergency Powers Relief Act". Do not copy this name.

**IN26-2 — The RBI's dating: 28 February 2026.** RBI Annual Report 2025-26, para I.29 (Ch I) and para II.7.20 (Ch II).
- Para I.29 dates the outbreak to "end-February 2026" and calls geopolitical risk the dominant drag on global growth in 2026.
- Para II.7.20 gives net FPI outflows of USD 13.1bn in March 2026 alone, triggered by the outbreak on 28 February.
- AR footnote 19 (Ch I) notes the IMF's April 2026 baseline assumed a war of limited duration, with disruptions fading by mid-2026, consistent with futures prices of 10 March 2026.

Quote (para II.7.20): "triggered by the outbreak of the West Asia conflict on February 28, 2026"

**IN26-3 — What the shock was, physically.** MER March 2026, paras 1–4, PDF pp. 7–8.
- The Strait handles about one-fifth of global seaborne oil trade, plus LNG and fertilisers. Transits fell to about one a week, against 200–300 a week.
- Crude prices roughly doubled over a short span. Freight costs surged, with bunker fuel nearly doubling and war-risk premiums up sharply.
- About one-third of global seaborne fertiliser trade passes through the Strait.
- Several Gulf producers (QatarEnergy, Kuwait Petroleum Corporation, Bapco) invoked force majeure. The MER says 17% of Qatar's LNG capacity was lost after Iranian missiles hit Ras Laffan, an outage expected to last "several years", and that Saudi Aramco shut its Ras Tanura refinery in early March.

Quote (para 1): "Ship transits through the Strait have nearly stopped"

FLAG (single source): the Ras Laffan and Ras Tanura details appear only in this MER, not in the RBI texts. Treat them as the DEA's account.

**IN26-4 — The path of the conflict, as the RBI recorded it.** MPC resolutions of 5 June (Res. para 11), 5 August (Res. para 3) and 7 October 2026 (Res. para 3); Governor's Statements of 5 August (GS para 9) and 7 October (GS para 2).
- June: the conflict lingered "amidst a fragile truce".
- August: a temporary ceasefire had given relief, but the conflict resumed in July. GS para 9 says supply pressures eased from June and the re-escalation dates from the first week of July.
- October: a "re-escalation" of the conflict, with sharp swings in crude. GS para 2 places a "sudden reescalation" in September.
- MER June 2026 (abstract, PDF p. 4; para 70, PDF p. 33) credits progress in US–Iran negotiations and "the signing of the MoU between the U.S.A and Iran" for June's easing.

Quote (Aug Res. para 3): "Relief from the temporary ceasefire in West Asia has quickly dissipated"

FLAG (dates): no source read gives the date of the ceasefire, the US–Iran MoU, or the July and September re-escalations. Do not supply them.

## How the shock reached India

**IN26-5 — DEA's four channels and the Box I anatomy.** MER March 2026, Preface, PDF p. 3; Box I, PDF pp. 8–10.
- Preface (by the CEA, V. Anantha Nageswaran, dated 25 March): four channels: (a) supply disruption to oil, gas, fertilisers and exports; (b) higher import prices; (c) higher freight and insurance; (d) a possible fall in remittances from Indians in the Gulf.
- Box I: energy is the most immediate channel. Crude and LNG can be re-sourced with lags and cost. LPG is harder: around 93% is sourced from conflict-affected regions and refinery LPG yields are only 4–6% of throughput.
- Over 80% of ammonia and sulphur imports come from the Gulf, and about 40% of DAP imports from Saudi Arabia.
- MSMEs and continuous-process industries (glass, ceramics) curtailed output where they could not switch fuel.
- The fiscal side: higher fertiliser and fuel subsidies and possible revenue shortfalls could widen the deficit.

Quote (Box I): "LPG faces more acute constraints due to limited substitutability"

**IN26-6 — The RBI's transmission channels.** Governor's Statement, 8 April 2026, GS para 9.
- First, dearer crude raises imported inflation and widens the CAD.
- Second, disruption to energy, fertilisers and other commodities cuts output in industry, agriculture and services.
- Third, uncertainty and safe-haven demand affect liquidity, consumption and investment.
- Fourth, weaker world growth may dampen external demand and reduce remittances.
- Fifth, global financial spillovers tighten domestic conditions.

Quote (GS para 9): "the initial supply shock can potentially transform into a demand shock"

**IN26-7 — India's oil dependence going in.** MER February 2026, para 29, PDF p. 25; MER March 2026, para 38, PDF p. 22, and para 59, PDF p. 33.
- Crude import dependency was 88.6% in April–January FY26 (PPAC). Of 206.3 million tonnes imported, 46.9% came from the Middle East, 34.6% from Eurasia and 7.2% from North America.
- Crude is about one-fourth of India's total imports (para 38).
- India buys crude from 41 countries, up from 27, with "nearly 70 per cent" of imports routed outside the Strait. Strategic reserves are over 5.3 million tonnes (para 59).
- MER February para 29 cites the RBI's October 2025 rule of thumb: 10% higher crude with full pass-through adds 30 bp to inflation. Para 49 (PDF p. 34) cites ICRA: USD 10 a barrel adds 0.3% of GDP to the CAD.

Quote (para 29): "India’s crude oil import dependency stood at 88.6 per cent"

FLAG (internal): 46.9% of crude from the Middle East (February MER) sits uneasily with "nearly 70 per cent" routed outside Hormuz (March MER). Some Middle East crude may avoid the Strait, but neither text explains this.

**IN26-8 — Gulf remittances at risk.** MER March 2026, Box I, PDF p. 10, and para 68, PDF pp. 36–37; MER April 2026, para 53, PDF pp. 31–32; ES 2025-26, para 4.65, p. 174 (st. 225).
- An estimated 9.2 million Indians live and work in West Asia (MEA), about four million of them in the UAE.
- RBI estimates cited: at least 35% of remittances come from West Asia, about USD 40bn a year.
- The GCC accounted for 38% of remittances in FY24, the UAE alone 19.2% (April MER), and hosts nearly half of India's migrants (March MER).
- ES 2025-26 (RBI sixth remittance survey, FY24): the US is now the top source at 27.7%, then the UAE (19.2%), UK (10.8%) and Singapore (6.6%).

Quote (Box I): "at least 35 per cent of India’s annual remittances originate from West Asia"

## Oil prices and the import bill

**IN26-9 — The Indian crude basket, month by month.** Sources as listed per line.
- 27 February 2026: USD 71.2 a barrel, up 10.9% on the month (MER February, para 49, PDF p. 34).
- March 2026 average: USD 124 (RBI AR, Ch III, Table III.3, "Average for Mar-2026"); USD 113 (MER April, Preface, PDF p. 3); USD 113.5 (MER April, para 22, PDF p. 17).
- "Average crude oil prices" up from USD 69 to USD 149.9 a barrel as of 20 March (MER March, para 38, PDF p. 22).
- PIB, 27 March: international crude had surged from about USD 70 to about USD 122 in a month.
- April: USD 114.5; May: USD 106.2 (GS 5 June, fn 15). April–May averaged around USD 110 (GS para 16).
- June: USD 83.22, from USD 106.23 in May. By 31 July, Brent was up 34.5% and the Indian basket 32.5% on end-June (GS 5 August, fn 19).
- July: USD 82.0; August: USD 90.2; September: USD 116.1 (GS 7 October, fn 18).
- MER July (PDF p. 5): crude had fallen "below pre-conflict levels" before rising again.

Quote (GS 5 June, fn 15): "ICB prices averaged $114.5 in April and $106.2 in May."

FLAG (internal): the March average is USD 124 in the RBI AR table and USD 113 or 113.5 in the April MER. The MER's "USD 149.9" on 20 March is not labelled as the Indian basket. Give the source with any March figure.

FLAG (typo): MER April para 22 says "for April 2024 (as on 24th April 2026)". It means April 2026.

FLAG (internal): the June statement's footnote gives May as USD 106.2 and the August footnote as USD 106.23. Consistent.

**IN26-10 — March 2026 trade: the first hit.** MER April 2026, paras 46–49 and fn 22, PDF p. 28.
- March merchandise exports fell 7.4% y-o-y and imports 6.5%. Petroleum imports fell 35.9%.
- Of 30 major export items, 24 fell.
- Exports to the UAE fell 61.93%, to Saudi Arabia 45.67%. Imports from the UAE fell 66.32%, Iraq 64.3%, Qatar 47.89%. Exports to Singapore rose 158.55% and Malaysia 84.47%.
- FY26 merchandise trade deficit: USD 333.2bn, against USD 283.5bn in FY25 (Preface, PDF p. 5).

Quote (para 46): "The trade statistics for March 2026 show the impact of the crisis"

FLAG (internal): FY25 merchandise deficit is USD 283.5bn in the April MER Preface and USD 282.5bn in the RBI AR (para I.18).

**IN26-11 — The import bill after March.** GS 5 August, para 19 and fn 30; GS 7 October, para 20 and fn 31; MER July 2026, PDF p. 24.
- Q1 FY27 merchandise trade deficit: USD 86.6bn, against USD 68.7bn in Q1 FY26, "mainly driven by imports of crude oil, electronic goods and gold". Imports were USD 216.2bn (+19.9%), exports USD 129.3bn (+15.9%).
- June 2026 petroleum imports rose 40.1% y-o-y, partly reflecting a 19.3% higher FOB price of the Indian basket (MER July).
- July–August trade deficit: USD 58.7bn, against USD 55.1bn. Petroleum product exports rose 66.0% to USD 13.8bn (GS 7 October, fn 31). The RBI notes "elevated margins on oil exports".

Quote (GS 5 Aug, para 19): "mainly driven by imports of crude oil, electronic goods and gold"

## Current account, BoP and remittances

**IN26-12 — The current account: FY26 modest, FY27 widening.** RBI AR para I.18 and II.7.16; GS 5 August fn 27; GS 7 October fn 28; RBI BoP release, 13 November 2026.
- FY26: CAD USD 25.4bn, 0.6% of GDP, about the same as FY25 (0.6%, USD 23.1bn) (GS 5 August, fn 27).
- April–December 2025 (pre-shock): USD 30.2bn, 1.1% of GDP (AR para II.7.16).
- Q1 FY27: USD 4.2bn, 0.5% of GDP, against 0.4% in Q1 FY26 (GS 7 October, fn 28).
- April–September 2026: deficit USD 25.8bn, against USD 18.0bn a year earlier. Merchandise deficit USD 176.1bn (against 158.1). September alone: USD 7.4bn deficit (BoP release).
- The DEA expected the CAD to "widen significantly in FY27" (MER March, Preface, PDF p. 4).

Quote (MER March Preface): "the current account deficit too will widen significantly in FY27"

FLAG (internal): April–December 2025 CAD is 1.0% of GDP in AR para I.18 and 1.1% in para II.7.16 (same USD 30.2bn).

FLAG (internal): Q1 FY27 CAD is USD 4.2bn in the October statement and "USD 3.1 bill[ion]" for April–June in MER August (PDF p. 26). The MER figure may be an earlier vintage of the monthly BoP data.

FLAG (vintage): the RBI moved to monthly BoP data in 2026 (MER June, para 66). Monthly and quarterly figures may not match until revised.

**IN26-13 — The BoP swung from deficit to large surplus.** MER July 2026, para 44, PDF p. 29; MER August 2026, para 59, PDF p. 26; MER September 2026, para 57, PDF p. 28; RBI BoP release, 13 November 2026.
- April–May 2026: capital account outflow USD 13.8bn and overall BoP deficit USD 11.0bn (MER July).
- April–June: overall deficit USD 8.1bn (MER August).
- April–July: overall surplus USD 12.7bn, led by banking capital (FCNR(B)) and net FDI (MER September).
- April–September: capital account +USD 92.6bn, overall balance +USD 66.8bn. Banking capital +USD 125.2bn, of which NRI deposits +USD 125.6bn. Net FPI −USD 10.4bn. Net FDI +USD 8.8bn (BoP release).

Quote (MER Sept para 57): "led by banking capital associated with FCNR(B) mobilisation and higher net FDI inflows"

FLAG (unexplained): the BoP release shows net ECBs of −USD 40.6bn for April–September 2026, driven by "By India (Net)" of USD 51.4bn. MER September shows April–July net ECBs of only −USD 1.3bn. No source read explains the swing.

**IN26-14 — Remittances held up — and rose.** MER June 2026, paras 67–68 and Box 2, PDF pp. 31–32; GS 5 August fn 29; GS 7 October fn 30; RBI BoP release.
- FY26 remittances (private transfer receipts): record USD 155.1bn, +14.5%, 4.0% of GDP, from USD 135.4bn (3.6%) in FY25.
- Net transfers: USD 16.0bn in April 2026 against USD 9.4bn; USD 29.6bn in April–May against USD 20.0bn; USD 53.9bn in April–July against USD 43.4bn; USD 77.7bn in April–September against USD 67.2bn.
- Box 2 cites the literature: remittances are acyclical and can be front-loaded as precautionary transfers. The main risk is a sustained fall in Gulf employment.
- The RBI AR (para I.40) expected remittances "from non-gulf countries" to support the current account in 2026-27.

Quote (MER June para 68): "transfer receipts have remained robust"

FLAG (definition): these are total transfers. No source read gives Gulf-only remittances for 2026 (see Not found).

FLAG (internal): FY25 remittances are 3.5% of GDP in MER April (para 52) and 3.6% in MER June (para 67), with the same USD 135.4bn. This probably reflects the GDP rebasing.

## Capital flows, the rupee and reserves

**IN26-15 — Portfolio flight in March, then recovery.** RBI AR para II.7.20; MER April 2026, para 56, PDF pp. 32–33; MER May 2026, para 53, PDF p. 26; GS 5 June para 25; GS 5 August para 20; GS 7 October para 21.
- March 2026 net FPI outflows: USD 13.1bn (AR), USD 13.6bn (MER April, NSDL), about USD 12.5bn to 24 March (MER March, para 6).
- FY26 total: −USD 16.5bn (AR; equity −18.6, debt +2.1 per GS 8 April fn 29), −USD 16.6bn (MER April).
- Cumulative outflows from the outbreak to 21 May: USD 23.6bn (MER May).
- FY27 to 2 June: −USD 13.7bn. June–July: +USD 7.1bn net, mainly debt. April to 5 October: −USD 10.3bn.

Quote (MER April para 57): "rupee depreciation reduces dollar-denominated returns for foreign investors, prompting further outflows"

FLAG (internal): three figures for March FPI outflows (12.5, 13.1, 13.6). They differ by date and source (NSDL vs RBI). MER June fn 31 notes NSDL and RBI BoP FPI figures differ by coverage.

**IN26-16 — The rupee.** MER March 2026, para 46, PDF p. 28; MER April 2026, paras 58–59, PDF p. 33; MER May 2026, para 55, PDF p. 27; MER June para 74, PDF p. 35; MER July para 51, PDF p. 34; MER August para 65, PDF pp. 27–28; RBI AR para II.5.22.
- ₹93.88 per USD on 24 March 2026: down 9% in FY26 and 3.1% since the start of the conflict (MER March).
- End-March 2026: ₹94.83, down 6.4% over H2 FY26 (AR para II.5.22).
- Breached ₹95 intraday in March, a new low (MER April). The RBI moved its baseline assumption to ₹94 from ₹88 (October 2025 MPR).
- ₹95.7 on 26 May, about 4.9% down since the outbreak (MER May).
- Down about 3.9% between 27 February and 22 June (MER June), about 5.8% to 24 July (MER July), about 4.9% to 20 August (MER August). Down only about 0.9% in FY27 to 20 August.
- MER May Box 1 (PDF pp. 27–29): the REER was 92.72 in April 2026, the lowest in over a decade, against a high of 108.03 in November 2024.

Quote (MER May para 55): "rupee has depreciated by ~4.9 per cent since the onset of the conflict"

FLAG (internal): the depreciation since the outbreak is 3.1% (to 24 March) and 4.9% (to 26 May) but only 3.9% (to 22 June). The rupee evidently recovered in June. Always give the end-date.

FLAG (internal): FY26 depreciation is 9% (MER March, to 24 March) and the AR's 6.4% is for H2 only. No full-year AR figure was found in the passages read.

**IN26-17 — The RBI's exchange-rate stance and FX measures.** GS 8 April para 18; GS 5 June para 29; MER April para 59; RBI AR para V.20.
- April: no target level or band; intervene only against excessive volatility.
- 27 March 2026: a prudential cap of USD 100mn on authorised dealers' daily net open position in INR (NOP-INR), to curb speculation (MER April).
- June: the Governor added that the RBI was ready to use "a broad range of regulatory and market-based instruments".
- AR para V.20: interventions in onshore and offshore OTC and exchange-traded segments.

Quote (GS 5 June para 29): "fully prepared to do whatever it takes to preserve orderly market conditions"

**IN26-18 — Reserves: dip, then a record.** GS 8 April para 17; GS 5 June para 26; MER June para 73; MER July para 50; GS 5 August fn 36; MER August para 64; MER September para 64; GS 7 October fn 36; AR para I.19.
- End-March 2026: USD 691.1bn (AR) or USD 689.4bn (MER June).
- USD 697.1bn (3 April), 700.9bn (10 April), 682.3bn (29 May), 671.6bn (12 June, about 10.3 months of imports), 675.2bn (10 July), 692.9bn (31 July), 716.9bn (14 August), 765.9bn (18 September), 734.6bn (2 October).
- The reserves were "aided by the strong response to the RBI's swap facility, operationalised on June 08, 2026" (MER August).

Quote (MER August para 64): "aided by the strong response to the RBI's swap facility"

FLAG (internal): end-March reserves differ: USD 691.1bn (AR) vs USD 689.4bn (MER June).

FLAG (unexplained): reserves fell from USD 765.9bn (18 September) to 734.6bn (2 October). No source read explains the fall.

## Inflation

**IN26-19 — CPI: low going in, rising through the year.** RBI AR paras I.13, II.3.11; MPC resolutions; MER April para 21; MER May abstract, PDF p. 3; MER August abstract, PDF p. 3.
- FY26 headline CPI: 2.1% (AR para I.13).
- New CPI series (2024 = 100): 2.7% (January 2026), 3.2% (February), 3.4% (March), 3.5% (April), 4.4% (June; first above target after 16 months below it), 4.45% (July, MER August), 4.5% (July, MPC October) and 4.8% (August).
- WPI jumped from 2.13% (February) to 3.88% (March) (MER April) and 8.3% (April) (MER May).
- In August core inflation rose to 4.2% (2.9% excluding precious metals). The share of the CPI basket above 4% rose to about 37% (Oct Res. para 8).

Quote (Aug Res. para 7): "after remaining below the target for 16 consecutive months"

FLAG (gap): the MPC resolutions give no May 2026 CPI figure, and no source read gives CPI for September or October 2026 (see Not found).

**IN26-20 — Fuel price pass-through: LPG first, pump prices from May.** GS 8 April fn 17; RBI AR para II.3.11; GS 5 June para 17 and fn 17; Res. 5 June para 9; MER May para 18, PDF p. 13; MER July para 35, PDF p. 21.
- From March: domestic LPG +₹60 per cylinder; commercial LPG +₹115, then +₹195.5 per cylinder; diesel for bulk (industrial) buyers +about 25%; some premium petrol +about ₹2 a litre.
- Petrol and diesel pump prices were unchanged in March and April.
- From mid-May: petrol and diesel raised cumulatively by 7.4% and 8.4%, with about 36 bp direct impact on CPI (RBI). The MER puts the rises at ₹7.38 and ₹7.52 a litre over four occasions.
- June CPI inflation in diesel, petrol and CNG: 8.4%, 7.5% and 6.2% (MER July).

Quote (Res. 5 June para 9): "retail fuel prices have been raised cumulatively by 7.4 per cent for petrol"

FLAG (definition): the RBI gives percentages; the MER gives rupee amounts. Neither gives the base price or the dates of each hike.

## The RBI's response

**IN26-21 — April: hold at 5.25%, "wait and watch".** MPC resolution, 6–8 April 2026, Res. paras 2, 5, 7 and 10.
- Repo unchanged at 5.25% (unanimous); neutral stance.
- FY27 GDP projected at 6.9% and CPI at 4.6%, assuming the conflict's impact stays contained.
- It cites disruption in the Strait of Hormuz as a drag on production.

Quote (Res. para 10): "The economy is confronted with a supply shock."

**IN26-22 — June: hold, with growth cut and inflation raised; capital-flow measures.** MPC resolution and Governor's Statement, 5 June 2026 (Res. paras 2, 7, 10, 14; GS paras 26–28); MER June Box 3, PDF pp. 33–35.
- Repo held at 5.25%. FY27 GDP cut to 6.6%; CPI raised to 5.1%.
- Measures to attract capital:
  - all new 15-, 30- and 40-year G-secs added to the FAR;
  - FPI General Route sub-limits removed;
  - higher limits for NRI, OCI and other individual non-resident investors in listed equity;
  - a concessional forex swap for PSU ECBs;
  - the RBI to bear the full hedging cost of fresh 3–5-year FCNR(B) deposits;
  - export-proceeds realisation restored to nine months.
- The government the same morning exempted FPI interest and capital gains on G-secs from income tax, from 1 April 2026 (PIB 2269169; MER June Box 3).
- MER June Box 3: swap rate fixed at 1.5% a year.

Quote (GS 5 June para 28): "these measures are expected to strengthen our balance of payments"

FLAG (internal): the swap deadlines vary by source:
- GS 5 June: ECB and FCNR(B) facilities "till 30th September 2026".
- MER June: FCNR(B) open till 16 October 2026; ECB and OFCB until 15 January 2027.
- MER August: FCNR(B) restricted to deposits booked by 31 August; ECB and OFCB open till 31 December 2026.

The facility was evidently revised; give the date of the statement used.

**IN26-23 — The FCNR(B) surge.** MER August para 63, PDF p. 27; MER September Box 4, PDF pp. 30–33; GS 7 October fn 35.
- Inflows under the three facilities: USD 72.8bn by 22 August (FCNR(B) USD 65.4bn, OFCB 4.9bn, ECB 2.6bn).
- MER September: "within less than three months" FCNR(B) alone mobilised USD 133bn, and all three USD 143.6bn. It compares 1991 (USD 1.6bn), 1998 (4.2bn), 2000 (5.5bn) and the 2013 FCNR(B) swap (USD 26bn in its table; "about USD 34 billion" including bank borrowing in the text).
- GS 7 October: net NRI-deposit inflows USD 119.2bn in April–August, against USD 5.6bn a year earlier.

Quote (MER Sept Box 4): "The scale of mobilisation is unprecedented in India's history"

FLAG (internal): USD 133bn (MER September, date not stated), USD 119.2bn (RBI, April–August, net NRI deposits) and USD 125.6bn (BoP, April–September, net NRI deposits) measure different things over different periods. Do not mix them.

**IN26-24 — August: hold; inflation above target.** MPC resolution and Governor's Statement, 5 August 2026 (Res. paras 6, 9, 12, 13).
- Repo held at 5.25%, neutral. FY27 GDP 6.7%, CPI 5.0%, with CPI peaking in Q3.
- The MPC wanted "greater clarity" on inflation before acting, and flagged possible "recalibration" of rates.

Quote (Res. para 12): "There is a need for greater clarity to emerge, especially regarding inflation"

**IN26-25 — October: first hike, to 5.50%, stance "calibrated tightening".** MPC resolution, 7 October 2026 (Res. paras 2, 7, 9, 11, 14–15).
- The repo rate was raised 25 bp to 5.50% (unanimous). SDF 5.25%; MSF and Bank Rate 5.75%.
- The stance changed to "calibrated tightening". Two members (Nagesh Kumar, Ram Singh) preferred neutral.
- FY27 GDP was raised to 7.1% after Q1 growth of 7.8%. CPI was projected at 5.2%, with headline expected to average almost 5.8% over the next three quarters.

Quote (Res. para 14): "rate cuts are off the table in the near term"

FLAG (context): the hike came with growth revised up, not down. The MPC cites broadening inflation and strong money and credit growth (Res. paras 11–13), as well as the supply shock.

**IN26-26 — Liquidity and bond yields.** RBI AR para II.5.12; GS 8 April fn 35; MER March para 62, PDF p. 33; GS 7 October fn 19–20.
- ₹1 lakh crore OMO purchases in March 2026. OMOs totalled ₹4.57 lakh crore in Q4 FY26.
- On the last trading day of FY26 the 10-year G-sec crossed 7% for the first time since July 2024 (AR). GS 8 April: 7.05% on 6 April.
- After the FCNR(B) inflows, liquidity surplus averaged ₹5.9 lakh crore. The RBI absorbed it through 55 VRRR auctions and ₹1.0 lakh crore of OMO sales after the August policy (GS 7 October).

Quote (AR para II.5.12): "the 10-year generic G-sec yield crossed the 7 per cent mark"

FLAG (typo): GS 8 April fn 35 compares the 6 April yield with "6.66 per cent as on February 27, 2025". From context the year should be 2026.

## The Centre's response

**IN26-27 — The pre-shock Budget baseline.** Budget Speech 2026-27, paras 93–97, PDF pp. 22–23; FRBM statement, para 27, PDF p. 12; ES 2025-26, p. 222 (st. 273).
- FY26 RE fiscal deficit 4.4% of GDP; FY27 BE 4.3% (₹16.96 lakh crore, FRBM). Debt 55.6% of GDP in BE 2026-27, against 56.1% in RE 2025-26. Gross market borrowing ₹17.2 lakh crore.
- FY27 BE major subsidies ₹4.11 lakh crore (1.0% of GDP): food ₹2.28 lakh crore, fertiliser ₹1.71 lakh crore, petroleum ₹0.12 lakh crore (FRBM).
- The Survey had expected global commodity prices to fall about 7% in FY27, citing the World Bank's October 2025 outlook and subdued crude.

Quote (BS para 94): "the fiscal deficit in BE 2026-27 is estimated to be 4.3 percent of GDP"

FLAG (forecast vs outcome): the BE petroleum subsidy (₹0.12 lakh crore) and the soft-commodity assumption predate the shock. No revised subsidy figure was found (see Not found).

**IN26-28 — An Economic Stabilisation Fund.** MER March 2026, para 62, PDF p. 33; MER April 2026, para 14, PDF p. 13; RBI AR para I.35.
- March MER: an ESF of ₹57,381 crore "has been proposed".
- April MER: created "in the public account". It allows near-term shocks of mild intensity to be absorbed without missing the deficit target. The Budget assumed a gross tax buoyancy of 0.8.
- AR: the Union Government "has set up" an ESF against global headwinds.

Quote (MER April para 14): "offers flexibility to absorb near-term shocks of mild intensity"

FLAG (source gap): the ESF is not in the Budget Speech or the FRBM statement (searched "Stabilis", "57,381"). Its legal basis and date are not given in any source read.

**IN26-29 — Excise cut of ₹10 a litre; pump prices held.** PIB PRID 2245970 (Ministry of Petroleum and Natural Gas, 27 March 2026); MER March 2026 measures table, PDF p. 34; MER April Box 3, PDF p. 30.
- Excise duty on petrol and diesel was cut by ₹10 a litre "with immediate effect".
- The MER gives the instrument: notification of 26 March 2026, cutting Special Additional Excise Duty on petrol from ₹13 to ₹3 and removing it on diesel (from ₹10).
- The cut was not passed on at the pump. It offset part of the OMCs' under-recoveries: about ₹26 a litre on petrol and ₹81.90 on diesel, about ₹2,400 crore a day combined.
- The PIB release likens the approach to the Russia–Ukraine episode of 2022.

Quote (PIB, 27 Mar): "Retail pump prices of petrol and diesel will not change."

FLAG (gap): no source gives the revenue cost of the excise cut (the release says only that the government took "a substantial impact" on tax revenue).

**IN26-30 — Export levies on fuel.** PIB PRID 2245970; MER April Annexure I, PDF p. 47.
- An export levy on diesel was introduced with the excise cut, to keep refinery output at home (PIB).
- Annexure I: the export duty on diesel was raised to ₹55.5 a litre from ₹21.5, and on jet fuel to ₹42 from ₹29.5.

Quote (PIB, 27 Mar): "the Government has simultaneously introduced an export levy on diesel"

FLAG (internal): the PIB release says the diesel levy was "introduced" on 27 March. The MER annexure (as of about 17–24 April) gives a rise from ₹21.5 to ₹55.5. The ₹21.5 may be the 27 March rate, later raised, but no source says so.

**IN26-31 — Rationing gas and LPG.** MER March 2026, measures table, PDF pp. 34–36; MER April Annexure I, PDF pp. 44–47.
- LPG Control Order (8 March): refineries to maximise LPG; output up about 28% within five days.
- Natural Gas Control Order (9 March), priority allocation:
  - domestic PNG/CNG 100%;
  - fertiliser 70% (later 95%; "over 90 per cent" in the agriculture row);
  - industry 80%;
  - refineries 65%;
  - power raised from 63% to 70%.
- Commercial LPG was cut to 20% of normal, then raised in phases to about 50%. Industrial LPG for priority sectors later rose to about 70% of demand.
- Other measures:
  - PNG users had to surrender LPG connections;
  - 48,000+ kl of extra kerosene was allocated;
  - Essential Commodities Act enforcement;
  - a 200-litre per consumer per day cap on retail diesel sales (MER July, para 36);
  - an Inter-Ministerial Group on Supply Chain Resilience from 2 March.

Quote (MER March table): "Commercial LPG supply was initially restricted to 20 per cent of normal levels"

**IN26-32 — Fertiliser: stocks, gas priority, a higher subsidy.** MER March 2026, para 60, PDF p. 33; MER April 2026, para 76, PDF p. 41, and Annexure I, PDF p. 47.
- Stocks were about 177 lakh tonnes in early March, up 36.5% y-o-y.
- 47.50 lakh tonnes were added between 1 March and 16 April. 46% of the Kharif requirement was held as opening stock, against a usual 33%.
- Urea output rose from 56,000 to 67,000 tonnes a day between March and April.
- Nutrient-based subsidy for P&K fertilisers was raised "around 12 per cent" for Kharif 2026, with customs duty waivers.

Quote (MER April para 76): "around 12 per cent increase in nutrient-based subsidy for the upcoming kharif season"

FLAG (gap): no rupee figure for the additional fertiliser subsidy was found.

**IN26-33 — Trade, shipping and import measures.** MER March table, PDF p. 35; MER April para 51 and Annexure I, PDF pp. 29, 45–47; PIB PRID 2253243 (18 April 2026); MER May para 47, PDF p. 24.
- RELIEF scheme (₹497 crore) for freight and insurance costs: up to 100% ECGC risk cover and 50% reimbursement for MSME exporters. Egypt and Jordan were later added.
- RoDTEP rates were fully restored on 23 March.
- Customs duty exemption on 40 critical petrochemical products till 30 June.
- Bharat Maritime Insurance Pool, approved by the Cabinet on 18 April: sovereign guarantee ₹12,980 crore; underwriting capacity about ₹950 crore; covers hull, cargo, P&I and war risk.
- Airport parking and landing charges cut 25% for three months. Only partial pass-through of ATF price rises was allowed (domestic increase capped at 25%).
- Gold, silver and platinum duty raised from 13 May: BCD from 5% to 10% and AIDC to 5%, an effective rate of about 15%. Some silver imports were moved to "restricted".

Quote (MER May para 47): "effective import duty on gold and silver has increased to approximately 15 per cent"

**IN26-34 — Rollback in June–July.** GS 5 August fn 1; MER July 2026, para 36, PDF p. 21; MER June para 45, PDF p. 25.
- On 25 June the government removed all sectoral restrictions on non-domestic packed LPG.
- From 1 July the temporary rules on petrol and diesel retail sales were withdrawn, including the 200-litre diesel cap.
- From 1 July OMCs cut the 19-kg commercial LPG cylinder by up to ₹183.50, and ATF by ₹5 a litre.
- MER June: the "recent de-escalation" and lower crude and fertiliser prices had eased fiscal pressure, "allowing fiscal consolidation to proceed".

Quote (GS 5 Aug fn 1): "restored supplies to the levels prevailing prior to the West Asia crisis"

FLAG (timing): this rollback preceded the July and September re-escalations (IN26-4). No source read says whether restrictions were reimposed after July.

**IN26-35 — The fiscal outturn so far.** MER June 2026, abstract (PDF p. 4) and para 42 (PDF p. 24).
- FY26 Provisional Actuals (CGA, June 2026): fiscal deficit 4.4% of GDP, against 4.9% in FY25, the lowest since 2018-19.
- The MER does not give FY27 deficit figures. The DEA's March view was that fuel and fertiliser subsidies and revenue shortfalls "may widen the fiscal deficit" (MER March, Box I).

Quote (MER June para 42): "the lowest level since 2018-19"

FLAG (vintage): FY25 fiscal deficit is 4.9% here. ES 2025-26 gave 4.8% (see `India_ES_2024-2026.md`). The difference probably reflects the new GDP base.

## How India fared

**IN26-36 — Growth: no collapse.** MPC resolutions (April, June, August, October 2026); MER September 2026, abstract and para 3, PDF pp. 3–5; RBI AR para I.2; MER June abstract, PDF p. 4.
- FY26 GDP: 7.6% (SAE, new base; AR and April MPC), and 7.7% in MER June. Q3 FY26: 7.8%.
- RBI FY27 projections: 6.9% (April), 6.6% (June), 6.7% (August), 7.1% (October).
- Q1 FY27 actual: 7.8%, GVA 8.2%, "the highest first-quarter growth in the current series" (MER September). The DEA's nowcast for Q2 was 7.3%.
- MER September credits "timely Government measures" and limited fuel pass-through.

Quote (MER Sept abstract): "the limited pass-through of global energy prices to domestic fuel prices"

FLAG (vintage): FY26 growth is 7.6% (SAE, April) and 7.7% (MER June, probably the Provisional Estimate released at end-May). Name the vintage.

**IN26-37 — The DEA's "burden-sharing" argument.** MER March 2026, Preface, PDF pp. 3–4; MER April 2026, Preface, PDF pp. 3–5.
- March: keeping the CAD manageable "will require burden-sharing" between government (fiscal absorption) and households and firms (pass-through). Higher interest rates burden the whole economy, while pass-through falls on specific users.
- April: "Some countries have begun to allow prices to be passed on"; pass-through is "inevitable". The IMF's April WEO, assuming USD 82 a barrel, looked "sanguine".
- On 27 February the DEA had put FY27 growth at 7.0–7.4%, with "considerable downside".

Quote (MER March Preface): "Keeping it manageable will require burden-sharing between the government"

**IN26-38 — External forecasters.** IMF India country page (dateModified 30 September 2026); MER April 2026, abstract, PDF p. 7; MER July 2026, para 2, PDF p. 5.
- IMF page "At a Glance": 2026 projected real GDP 6.4% and consumer prices 4.7%, from the July 2026 WEO Update.
- MER April: the IMF's April WEO had raised India's 2026 growth to 6.5%. It credits domestic demand and a cut in US tariffs on Indian goods from 50% to 10%.
- IMF July WEO: world growth 3.0% in 2026, from 3.2% in 2025 (as reported by MER July).

Quote (IMF page): "The last Article IV Executive Board Consultation was held on February 21, 2025."

FLAG (internal): the IMF page says the last Article IV Board consultation was 21 February 2025, but also lists the latest Article IV country report as 26 November 2025. The 2025 Article IV (Country Report 25/314) is already held locally. The "February 21, 2025" line looks stale.

FLAG (vintage): world growth for 2025 is 3.4% in the RBI AR (citing the April WEO) and 3.2% in the July WEO as reported by MER July.

FLAG (definition): the IMF's "2026" for India may be on a fiscal-year basis. The page does not say.

**IN26-39 — The pre-shock warning in ES 2025-26.** ES 2025-26, Preface, pp. viii–x (st. 9–11).
- The Preface gave three 2026 scenarios: "managed disorder" (40–45%), disorderly multipolar breakdown (40–45%), and a systemic shock cascade (10–20%) in which financial, technological and geopolitical stresses amplify one another.
- The common risk for India in all three is disruption of capital flows and the rupee. Policy should focus on "stability of supply, the creation of resource buffers".
- MER February (Preface, PDF p. 4) said the war "brings closer the third" scenario.

Quote (ES Preface p. ix): "a residual probability of 10%-20%"

**IN26-40 — A US tariff threat linked to Russian crude.** MER September 2026, abstract, PDF p. 4.
- The MER reports passage and "Presidential assent" of a "Graham Bill" empowering the US President to impose tariffs of up to 100% on countries buying Russian crude. It says trade relations with the US "remain unsettled".

Quote (MER Sept abstract): "Trade relations with the United States remain unsettled"

FLAG (single source): no other source read mentions this law, its date or India's Russian crude volumes. Verify before use.

---

## Cross-source reference figures

| Measure | Figure (source) |
|---|---|
| Outbreak | 28 February 2026 (AR II.7.20; MER Feb para 93) |
| Indian basket, USD/bbl | 71.2 (27 Feb); 113–124 (Mar avg, MER/AR); 114.5 (Apr); 106.2 (May); 83.2 (Jun); 82.0 (Jul); 90.2 (Aug); 116.1 (Sep) |
| Repo rate | 5.25% (Apr, Jun, Aug holds); 5.50% (7 Oct, +25 bp) |
| RBI FY27 GDP projection | 6.9 → 6.6 → 6.7 → 7.1% (Apr → Oct) |
| RBI FY27 CPI projection | 4.6 → 5.1 → 5.0 → 5.2% (Apr → Oct) |
| CPI (2024 = 100) | 3.2 (Feb), 3.4 (Mar), 3.5 (Apr), 4.4 (Jun), 4.5 (Jul), 4.8% (Aug) |
| Q1 FY27 GDP | 7.8% (NSO, via MPC Oct and MER Sept) |
| CAD | FY26 0.6% of GDP (USD 25.4bn); Q1 FY27 0.5% (USD 4.2bn); Apr–Sep 2026 USD 25.8bn |
| Overall BoP | Apr–May −11.0bn; Apr–Jun −8.1bn; Apr–Jul +12.7bn; Apr–Sep +66.8bn |
| Remittances | FY26 USD 155.1bn (4.0% of GDP); net transfers Apr–Sep 2026 USD 77.7bn |
| Net FPI | Mar 2026 −13.1bn (RBI); FY26 −16.5bn; Apr to 5 Oct 2026 −10.3bn |
| Rupee/USD | 93.88 (24 Mar); 94.83 (end-Mar); >95 intraday (Mar); 95.7 (26 May) |
| Reserves | 691.1bn (end-Mar, AR); 671.6bn (12 Jun, low in sources); 765.9bn (18 Sep); 734.6bn (2 Oct) |
| Excise | −₹10/litre on petrol and diesel (SAED), 26–27 March 2026 |
| Fiscal deficit | FY26 RE 4.4%, PA 4.4%; FY27 BE 4.3% |

## Problems and caveats

1. **History in progress.** The latest hard data are the September 2026 BoP (13 November) and the August CPI (via the October MPC). The war had not ended at the last source. The December MPC has not yet met. Mark every FY27 figure as provisional.
2. **Naming and dating the war.** Only the MER February 2026 names the participants and events. All RBI texts say "the West Asia conflict". No source read dates the ceasefire, the US–Iran MoU or the re-escalations.
3. **Too many March numbers.** The March 2026 crude average (113, 113.5 or 124), March FPI outflows (12.5, 13.1 or 13.6) and end-March reserves (689.4 or 691.1) each differ by source. Name the source.
4. **Monthly BoP is new and revisable.** The Q1 FY27 CAD is USD 3.1bn in MER August and USD 4.2bn in the October statement. The ECB swing in the September BoP is unexplained.
5. **The FCNR(B) numbers are very large.** USD 133bn (MER September) or 125.6bn of net NRI deposits in April–September (BoP) dwarf every earlier diaspora episode. Check against later RBI data before the book leans on the size. The swap-window dates changed at least twice.
6. **The fiscal cost is not measured.** No source gives the revenue cost of the excise cut, the revised petroleum or fertiliser subsidy, or a FY27 RE deficit. The ESF's size (₹57,381 crore) comes from one MER only.
7. **Rebasing.** GDP (2022-23 base, from 27 February 2026), CPI (2024 = 100), IIP and WPI all moved to new series during the shock. Growth and inflation figures here are on the new series unless stated. FY25 ratios (remittances 3.5% vs 3.6%; deficit 4.8% vs 4.9%) shift with the GDP base.
8. **MER page numbers.** Cited as PDF pages. The extraction joins table and chart text into paragraphs in places. Para numbers were checked at each cited page.
9. **RBI AR has no page numbers.** It was read from the HTML edition; cite chapter and paragraph.
10. **DEA's own judgements.** Some statements are the DEA's or the CEA's views, not measurements. Examples: crude must stay above USD 100 for strain to show; IMF forecasts are "sanguine"; pass-through is "inevitable"; FCNR(B) mobilisation is "unprecedented". Attribute them.

## Not found (searched)

Do not fill these in from memory.

- **IMF India 2026 Article IV staff report.** Not published as of the IMF India page (metadata dated 30 September 2026). The page lists the latest Article IV country report as 26 November 2025 (the 2025 Article IV, already held locally as `imf_india_art4_2025`).
- **RBI Annual Report 2025-26 PDF chapters.** Plain curl to https://rbidocs.rbi.org.in/rdocs/AnnualReport/PDFs/... failed with "SSL_read: unexpected eof" on all four chapters tried. No bot-challenge page was served. I did not try to get around it. The same chapters were read from the HTML edition on www.rbi.org.in (no page numbers).
- **dea.gov.in over https.** curl failed certificate verification ("unable to get local issuer certificate"). The listing and PDFs were fetched over http://dea.gov.in, as the existing INDEX.md entries for DEA files do. Verification was not disabled.
- **MER October 2026 and later.** Not on the DEA listing (last updated 16.11.2026).
- **MPC February 2026 resolution** (pre-shock). Not read; the 2025-26 listing needs a form postback.
- **CPI for September and October 2026.** Not in any source fetched.
- **Gulf-only remittance figures for 2026.** Searched MERs and RBI statements for "Gulf", "GCC" and "remittance". Only total transfers are given, plus the FY24 shares (GCC 38%, UAE 19.2%).
- **Return migration or job losses of Indians in the Gulf.** None found. The only figure is "over 2447 Indian seafarers" repatriated (MER April Annexure I).
- **India's oil import bill in dollars for FY27 to date.** Not found as a single figure. Only growth rates (for example, petroleum imports +40.1% in June 2026) and total merchandise imports are given.
- **Revenue cost of the excise cut; revised (RE) fertiliser, LPG or petroleum subsidy for 2026-27; FY27 fiscal deficit to date.** Not found.
- **Economic Stabilisation Fund in the Budget documents.** Not in the Budget Speech 2026-27 or the FRBM statement (searched "Stabilis", "57,381").
- **State VAT changes on fuel.** Not found.
- **PIB release of 22 March 2026** cited in GS 8 April fn 3 (fuel and LPG supply, seafarers). No link is given, so it was not fetched.
- **Dates of the ceasefire, the US–Iran MoU, and the July and September re-escalations.** Not stated in any source read.
- **Russian crude volumes or the Graham Bill's text and date.** Only the MER September abstract mentions the bill.
