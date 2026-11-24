# Reading notes: theme chapter "Money: monetary policy, central banks and inflation, 2000–2026" (read 22 Nov 2026)

Method: every document was fetched with plain `curl` (default user-agent, no custom headers). IMF chapters came from imf.org: for older
issues the old contents page "http://www.imf.org/external/pubs/ft/weo/YYYY/NN/index.htm" (which now redirects to the new-style issue page)
gave the chapter PDF links; for newer issues the chapter PDFs are linked from the issue page. BIS Annual Economic Reports came from bis.org,
central-bank documents from federalreserve.gov, ecb.europa.eu and boj.or.jp, and Indian documents from rbi.org.in and the other sites named
in each entry. Downloads are in `/private/tmp/money_dl/` (subfolders `imf/`, `bis/`, `cb/`, `in/`). PDFs were converted with `pdftotext`
(plain and `-layout`). Each quote was checked by script (`/private/tmp/money_scripts/qc.py`) against the plain-text conversion; the check
normalises case, spaces, curly quotes and line-end hyphens. Quotes are verbatim and under 15 words, at most one per bullet; everything else
is paraphrase. Where existing notes (`IMF_*.md`, `India_ES_*.md`) already cover a point, they are cited by file and entry, not re-read.

Page numbers are printed numbers, with the PDF-to-printed offset given in each entry.

India: the Economic Survey extracts in `Econ Subject/sources/text/es<YEAR>.txt`. Pages are cited as in `India_ES_2024-2026.md`: "p." is the
printed page and "st." is the stitched page (form feeds + 1).

Item labels: MO-IMF-n, MO-BIS-n, MO-CB-n (central banks), MO-IN-n. Inflation is annual percent change in consumer prices unless stated.
Indian years are fiscal years (FY23 = 2022-23).

---

## IMF

### MO-IMF-1. WEO April 2006, Chapter III "How Has Globalization Affected Inflation?"
Issue page title: "IMF World Economic Outlook (WEO) -- Globalization and Inflation, April 2006". Contents page
http://www.imf.org/external/pubs/ft/weo/2006/01/index.htm redirects to
https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/Globalization-and-Inflation. Chapter PDF:
https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2006/01/pdf/_c3pdf.pdf (38 PDF pages, pp. 97–134).
Offset: p. = PDF + 96. Main authors (p. 97): Thomas Helbling, Florence Jaumotte and Martin Sommer, with consultancy support from Laurence
Ball. Read: pp. 97–98 (introduction, recent developments), Box 3.1 pp. 102–104 (emerging markets), pp. 106–109 (aggregate perspective,
searched), pp. 122–124 (summary and policy conclusions). The existing note `IMF_2003-2006.md` (WEO April 2006 entry, Foreword p. xi) records
Rajan's summary that globalization cut advanced-economy inflation by about ¼ point a year through import prices (½ point in the US).
- p. 97: inflation in advanced and many emerging economies stayed subdued for two years despite a big rise in commodity prices, strong
  growth and accommodative policy in the major currency areas. The chapter weighs global competition against other explanations: better
  monetary-policy credibility, productivity gains and the cycle.
- p. 98: industrial-country inflation has fluctuated around 2–3% since the early 1990s with little dispersion, against about 9% in the early
  1980s. These low averages "closely match" central banks' explicit or implicit targets. Inflation has also become less volatile.
- p. 103 (Box 3.1): across emerging markets, a trade-to-GDP ratio 25 points higher makes single-digit inflation over 10 points more likely.
  p. 104: the advanced-economy disinflation of the early 1980s raised the likelihood of low EM inflation by 30 points or more; a 10%-of-GDP
  budget deficit raises the likelihood of high inflation by up to 25 points; high turnover of central bank governors (low independence)
  makes low inflation less likely.
- p. 106: the inflation–output elasticity has fallen: a 2-point positive output gap for a year now adds about 0.4 point to inflation in the
  first year, against 0.6 point a couple of decades earlier; trade openness looks like the key factor. (Table 3.6, p. 124: the PPP-weighted
  elasticity was 0.26 in 1960, 0.27 in 1983 and 0.17 in 2004 in the baseline model.)
- p. 109: real import prices fell 3.8% a year in 1997–98 in eight advanced economies, against 1% a year on average in 1960–2004. Only about
  a tenth of a deviation passes through to inflation, but import prices still cut inflation by about ½ point in both 1998 and 1999, and over
  ¼ point in 2002.
- p. 123 (conclusions): over the medium term the nominal anchor, such as the inflation target, determines inflation, so globalization's
  effect is temporary in industrial countries; in emerging markets openness has been, and is likely to remain, an important factor in lower
  inflation.
- p. 123: in slack periods (the 1997–98 Asian crisis, the 2001–02 slowdown) import-price falls shaved more than 1 point off inflation in
  some advanced economies over one to two years. This supports the view that "inflation targets should not be set too close to zero".
- p. 123: globalization reduced the sensitivity of inflation to domestic capacity constraints, partly through labour markets and wages, and
  allowed a more measured tightening. But with strong growth and shrinking slack, "globalization cannot be relied upon to keep a lid on
  inflationary pressures"; the main risk is a further rise in import and commodity prices (pp. 123–124).
- How it explained events: the Great Moderation as a mix of credible inflation targets (the anchor) and a temporary globalization tailwind
  that flattened the response of inflation to domestic demand.

### MO-IMF-2. WEO April 2013, Chapter 3 "The Dog That Didn't Bark: Has Inflation Been Muzzled or Was It Just Sleeping?"
Issue page title: "IMF World Economic Outlook (WEO) - Hopes, Realities, and Risks, April 2013 -- Table of Contents". Contents page
http://www.imf.org/external/pubs/ft/weo/2013/01/index.htm redirects to
https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/Hopes-Realities-Risks. Chapter PDF:
https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2013/01/pdf/_c3pdf.pdf (18 PDF pages). The chapter
file carries its own footer numbering ("International Monetary Fund | April 2013  N"), 1–18, so p. = PDF page; these are not the page
numbers of the bound volume. Authors (p. 1): John Simon (team leader), Troy Matheson and Damiano Sandri. Read: pp. 1–2, 8–15 (results,
risks, the 1970s case study, conclusions).
- p. 1 (summary): inflation stayed remarkably stable after the Great Recession although unemployment rose sharply. Over the past decade
  advanced-economy inflation became less responsive to slack and long-term expectations became more firmly anchored. Ongoing monetary
  accommodation is unlikely to be inflationary while expectations stay anchored, so "preserving central banks’ independence is key".
- p. 1: earlier recessions brought marked falls in inflation; the Great Recession barely made a dent, so "we find a dog that did not bark".
  Some read this as proof that output gaps were small and unemployment structural, and feared overheating as in the 1970s.
- p. 8: better anchoring since the mid-1990s is linked to more central bank independence and the spread of inflation targeting. The flatter
  Phillips curve fits downward nominal wage rigidity and less frequent price changes at low inflation; evidence that globalization flattened
  it is inconclusive or negative (contrast MO-IMF-1).
- p. 9 (Figure 3.8): with 1970s parameters the model predicts significant US deflation from 2010; with current parameters it tracks actual
  inflation. The large 2009 fall in headline inflation reflected commodity prices, not slack.
- p. 10 (Figure 3.9): Ireland, Spain and the UK had unemployment below the NAIRU for about a decade in the 2000s with stable inflation, partly
  because ECB policy was too loose for Ireland and Spain. So the stimulus in the pipeline is unlikely to generate high inflation; the main risk
  is that expectations become disanchored.
- p. 13 (case study): in 1975 the Bundesbank bought government bonds equal to about 4% of the stock, 1% of GDP, in what is now called QE. It
  overestimated the 1975 output gap (about 9% against about 1% ex post) yet kept inflation down. The ECB's 2% target descends from the
  Bundesbank's "unavoidable inflation".
- pp. 13–14: the Fed and the Bundesbank both misjudged slack; what set them apart was actual independence. The Fed's lack of it in the 1970s
  disanchored expectations; inflation fell once Volcker (appointed 1979) established de facto independence.
- p. 14 (conclusions): "the Phillips curve is considerably flatter today than in the past", and expectations are better anchored; together
  these explain the small fall in inflation. As long as expectations hold, "fears about high inflation should not prevent monetary
  authorities" from highly accommodative policy.
- pp. 14–15 (caveats): low consumer-price inflation in the 2000s coexisted with housing bubbles; and the unprecedented growth of central bank
  balance sheets, with possible capital losses on bonds, could expose central banks to political pressure. Inflation "has been muzzled", and
  will stay so provided central banks remain free to respond (p. 15).

### MO-IMF-3. WEO October 2018, Chapter 3 "Challenges for Monetary Policy in Emerging Markets as Global Financial Conditions Normalize"
Issue page title: "World Economic Outlook, October 2018: Challenges to Steady Growth". Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2018/09/24/world-economic-outlook-october-2018. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2018/october/english/c3.pdf (25 PDF pages, pp. 101–125). Offset: p. = PDF + 100.
Authors (p. 101): Rudolfs Bems (lead), Francesca Caselli, Francesco Grigoli, Bertrand Gruss and Weicheng Lian. Sample: 19 emerging markets
including India (p. 101, fn. 1). Read: pp. 101–103 (summary, introduction, conclusions), pp. 107, 109, 113 (searched for estimates),
pp. 116–117 (summary and policy implications). India is in the sample but is not singled out in the pages read.
- p. 101 (summary): EMDE inflation has been low and stable on average since the mid-2000s. Changes in long-term inflation expectations are
  the main determinant of inflation; external conditions play a more limited role, so "domestic, not global, factors are the main
  contributor" to the gains. This partly contradicts the globalization emphasis of MO-IMF-1 for advanced economies (the chapter notes on
  p. 102, fn. 3, that the 2006 chapter reached similar conclusions for emerging markets).
- p. 101: after the Asian crisis of the late 1990s showed the limits of pegs, many EM central banks adopted inflation targeting; price
  stability then survived commodity swings, the global financial crisis and dollar strength. Pessimists point instead to China's trade
  integration and unusually benign post-crisis financial conditions.
- p. 103: the anchoring of expectations improved significantly over two decades, most of it in the 2000s, but remains uneven. Fiscal
  sustainability is a precondition for a credible anchor, as is a credible and independent central bank that communicates clearly.
- p. 107: falling external prices had only a small deflationary effect, about –0.05 point a year on average over the sample.
- p. 113: exchange-rate pass-through after six months was about 11% in less-anchored economies (14% in the 2013 taper tantrum), against 1%
  and 5% in more-anchored economies. Better-anchored economies were more resilient to the taper tantrum (p. 114, Figure 3.13).
- pp. 116–117 (policy): several sample economies still averaged double-digit inflation in 2004–18. "emerging markets are not simply
  bystanders to the forces of globalization"; keeping the gains requires fiscal rules and buffers and more central bank independence and
  transparency. Rising EM public debt and recent depreciations mean past gains "cannot be taken for granted" (p. 117).

### MO-IMF-4. WEO October 2024, Chapter 2 "The Great Tightening: Insights from the Recent Inflation Episode"
Note: the brief placed this chapter in the April 2024 WEO. The April 2024 issue page lists Chapter 2 as "Feeling the Pinch? Tracing the
Effects of Monetary Policy through Housing Markets" (see MO-IMF-5). "The Great Tightening" is Chapter 2 of the October 2024 WEO: the October
2024 issue page lists "Great Tightening: Insights from the Recent Inflation Episode - Online Annex".
Issue page title: "World Economic Outlook, October 2024: Policy Pivot, Rising Threats". Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2024/10/22/world-economic-outlook-october-2024. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2024/october/english/ch2.pdf (24 PDF pages, pp. 41–64). Offset: p. = PDF + 40.
Authors (p. 41): Jorge Alvarez and Emine Boz (co-leads), Thomas Kroen, Alberto Musso, Galip Kemal Ozhan, Nicholas Sander, Sebastian Wende
and Sihwan Yang, under Jean-Marc Natal. Read: pp. 41–44 (summary, introduction, findings, what happened), p. 48 (decompositions), pp. 49–50
(comparison with the 1970s, transmission), p. 53 (counterfactuals), p. 56 (conclusions), Box 2.1 p. 58.
- p. 41 (summary): demand shifted to goods in lockdowns and then to services, against supply disruptions and unprecedented fiscal and
  monetary stimulus, then the war in Ukraine spiked commodity prices. Pass-through of sectoral price pressures to core inflation and a
  steeper Phillips curve explain the surge. Where bottlenecks are widespread and meet strong demand, "tighter policy can bring it down
  quickly with limited output costs".
- p. 41: "By mid-2022, global inflation had tripled relative to its prepandemic level." Fn. 1: pandemic fiscal stimulus averaged about 12%
  of GDP in advanced economies and 4% in emerging markets; QE was about 20% of GDP in several advanced economies.
- p. 41: the global tightening cycle is called the "Great Tightening"; Brazil and Chile moved earlier than others. p. 49: Brazil, Chile and
  Mexico hiked early, Asia was more tempered, and the United States moved relatively late.
- p. 42 (findings): price surges were sector-specific and broadened; "little evidence" in most economies, possibly except the US, that
  labour-market strength drove inflation at its peak. Price Phillips curves steepened but wage Phillips curves did not. Global tightening
  was more effective than national tightening because it lowered commodity prices.
- p. 43: annual inflation peaked in 2022 at about 8% in the median advanced and emerging economy. WEO forecasts underestimated it: the median
  2022 forecast error was 2.5 points for advanced economies (1.1 for emerging markets, 1.5 for low-income countries). Disinflation in 2023–24
  came faster than forecast. "the feared de-anchoring of inflation expectations reminiscent of the 1970s" did not happen, real wage growth
  stayed contained and there were no wage-price spirals.
- p. 48 (decomposition): US inflation in 2021 and early 2022 was driven by sectoral and energy pressures; since mid-2022 mainly by a tight
  labour market, still contributing 2.5 points to US CPI inflation in Q1 2024. In Europe, energy pass-through alone contributed more than
  2.5 points at the peak; in emerging markets import prices (including exchange-rate effects) were a significant driver. **This is the
  chapter's supply-versus-demand verdict: supply and energy first, demand (US labour market) later.**
- p. 49: compared with resolved 1970s episodes, post-2020 nominal rate rises were milder and real rates stayed negative longer; p. 50: the
  recent episode lies between resolved and unresolved 1970s episodes, but expectations were more strongly anchored.
- p. 53 (counterfactual): tightening three quarters earlier would have lowered peak inflation by about 2 points but cut 2022 real GDP by
  0.8 point. Supply constraints steepen the Phillips curve, which makes stimulus more inflationary and disinflation cheaper.
- p. 56 (conclusions): the "new lesson" is that when bottlenecks are widespread, tightening works fast and "the sacrifice ratio is low"; the
  "old lesson" is that when bottlenecks are confined to commodities, rules targeting sticky-price (core) inflation remain appropriate, and
  reacting hard to commodity prices risks a recession. Also p. 56: frameworks could include well-defined escape clauses allowing front-loaded
  tightening.
- Box 2.1 p. 58: in 2020–22 central bank balance sheets grew by more than 20% of GDP in Japan, the UK and the euro area and by about 18% of GDP
  in the US. Quantitative tightening "has had minimal effects so far": one estimate puts the rise in term premiums from a one-standard-
  deviation QT shock at about 12 basis points.

### MO-IMF-5. WEO April 2024, Chapter 2 "Feeling the Pinch? Tracing the Effects of Monetary Policy through Housing Markets"
Issue page title: "World Economic Outlook, April 2024: Steady but Slow: Resilience amid Divergence". Issue page:
https://www.imf.org/en/Publications/WEO/Issues/2024/04/16/world-economic-outlook-april-2024. Chapter PDF:
https://www.imf.org/-/media/files/publications/weo/2024/april/english/ch2.pdf (22 PDF pages, pp. 43–64). Offset: p. = PDF + 42. Authors
(p. 43): Mehdi Benatiya Andaloussi, Nina Biljanovska, Alessia De Stefani and Rui Mano (lead). Read: pp. 43–45 only (summary and
introduction). Chapter 1 of this issue is covered in `IMF_2024-2025.md` (WEO April 2024 entry).
- p. 43: since late 2021 central banks raised rates at a speed, degree and breadth "unprecedented in at least 40 years", yet global growth
  held up. Monetary policy bites harder where fixed-rate mortgages are uncommon, buyers are more leveraged, household debt is high, housing
  supply is restricted and house prices were overvalued.
- pp. 43–45: shifts since the global financial crisis and the pandemic (more fixed-rate mortgages, tighter loan-to-value limits) may have
  limited the drag so far. The cooling effects may still come where fixation periods are short and households are heavily indebted.
- Existing notes, `IMF_2024-2025.md` (WEO April 2024, Ch. 1 p. 6): the ECB and the Fed raised nominal rates only after inflation expectations
  started rising, so real rates first fell; the Bank of Japan kept rates near zero; Brazil and Chile raised early.

---

## BIS

### MO-BIS-1. BIS Annual Economic Report 2022: overview "No respite" and Chapter II "Inflation: a look under the hood"
Landing page: https://www.bis.org/publ/arpdf/ar2022e.htm redirects to https://www.bis.org/publications/aer-2022 (title "BIS Annual Economic
Report 2022"); chapter page https://www.bis.org/publications/aer-2022/inflation-look-under-hood. PDFs: full report
https://www.bis.org/publications/aer-2022.pdf (139 PDF pages; used for all page numbers) and chapter
https://www.bis.org/publications/inflation-look-under-hood.pdf (33 pages, downloaded, not used for citation). The report went to press on
16 June 2022 with data to 30 May 2022 (PDF p. 8). Offsets in the full report: overview p. ix = PDF 11 (so roman page = PDF − 2); Chapter II
p. = PDF − 20. Read: overview pp. ix–xv; Chapter II pp. 41–42 (key takeaways, introduction), p. 60 (monetary policy in a low-inflation
regime), p. 64 (conclusion).
- p. x: the post-GFC challenge had been to lift inflation back to target; what looked like a temporary pandemic blip became a broad surge.
  "By April 2022, three quarters of economies were experiencing inflation above 5%." "Inflation was back, not as a long-sought friend, but
  as a threatening foe."
- p. x: the BIS admits it "did not quite anticipate the strength and persistence of the surge". Its explanation has three parts: a stronger
  rebound in demand (huge stimulus plus pent-up spending), a persistent rotation of demand from services to goods, and supply bottlenecks
  (raw materials, semiconductors, freight), first pandemic-related, then demand-driven. **This weights demand more heavily than MO-IMF-4.**
- p. x: EM central banks in central and eastern Europe and Latin America tightened first; Asia later; the Fed was one of the first among
  advanced economies; the ECB signalled a start later in 2022; the Bank of Japan kept its exceptionally easy policy; China eased.
- p. xi: whether inflation becomes entrenched depends on wage-price spirals; "We may be reaching a tipping point" for inflationary
  psychology. Low- and high-inflation regimes are "very different animals": in low-inflation regimes, price changes are mostly relative
  and self-correcting.
- p. xii: in a stylised exercise, GDP could be about 1.5% lower by 2025 if rates follow the market-implied path, and about 3% lower on the
  steeper early-2000s path, relative to constant rates.
- p. xiv: after the GFC and Covid, with inflation below target, there was "no obvious trade-off" between easy policy and inflation, but
  very low rates for so long built up financial vulnerabilities. Monetary policy loses traction in a low-inflation regime.
- p. xv: "The overriding priority is to avoid falling behind the curve." Central bank balance sheets reached levels previously seen only in
  wartime; because of large-scale asset purchases, "as much as 30–50% of marketable government debt is effectively overnight" in the largest
  advanced economies, and losses could raise political-economy risks for central banks.
- p. 41 (key takeaways): separate relative from generalised price changes; "Transitions from low- to high-inflation regimes tend to be
  self-reinforcing". p. 42: the late-1960s–early-1970s transition combined big relative price rises (oil), strong demand, high pricing power
  of labour and firms, and the loss of the Bretton Woods anchor.
- p. 60: in a low-inflation regime the central bank can tolerate moderate, persistent deviations from target. In US data, policy affects
  prices in "only around one third of sectors, even after three years", mainly cyclical services. Policy also loses traction at very low
  rates, so bigger moves are needed, as after the GFC.
- p. 64: credibility anchors expectations, and "central bank independence is critical": it shields the central bank from political
  pressures that would delay remedial action. Returning from an entrenched high-inflation regime is very costly, so a timely, firm response
  is needed.

### MO-BIS-2. BIS 86th Annual Report 2015/16 (Annual Economic Report 2016), Chapter IV "Monetary policy: more accommodation, less room"
Chosen over the 2019 EME-frameworks chapter because it deals directly with the side effects of negative rates and asset purchases.
Landing page: https://www.bis.org/publ/arpdf/ar2016e.htm redirects to https://www.bis.org/publications/aer-2016 (title "86th Annual
Report, 2015/16"). PDF: https://www.bis.org/publications/aer-2016.pdf (259 PDF pages). Economic chapters went to press on 15–17 June 2016
with data to 30 May 2016 (PDF p. 7). Offset: p. = PDF − 8. Read: pp. 63–65 (introduction, recent developments) and pp. 70–71 (the
diminishing effectiveness of domestic channels).
- p. 63: policy stayed very accommodative against stubbornly low headline inflation; there were concerns about the declining effectiveness
  of domestic channels and the side effects of persistent accommodation, and "growing tensions between price stability and financial
  stability". Major AE central banks began the year with rates near zero and bigger balance sheets; real policy rates had not been so low
  for so long since the start of the postwar period (pp. 63–64).
- p. 64: the Fed's lift-off came in December 2015: a 25 basis point rise took the effective federal funds rate to about 35 basis points,
  with "only gradual" further increases signalled.
- p. 65: in March 2016 the ECB cut its main refinancing rate to zero and its deposit rate to –40 basis points, and extended asset purchases to
  non-financial corporate bonds. The Bank of Japan enhanced QQE to pursue its 2% target and adopted negative policy rates for the first time,
  applied only to marginal increases in current account balances to protect bank profits.
- p. 70: unconventional tools (large-scale asset purchases, cheap long-term lending, forward guidance, negative rates) work through the
  same channels as rate cuts. Graph IV.6: the output response to US asset purchases was weaker in 2011–14 than in 2008–11, and bank lending
  responds less when rates are very low.
- p. 71 (side effects): negative rates and sticky deposit rates squeeze bank margins and lending; in Switzerland "banks initially raised
  mortgage rates in order to protect their profits". Very low rates encourage buybacks and acquisitions rather than investment, and deepen
  pension underfunding; a survey found negative rates made about as many households spend less as spend more.
- p. 71: to move markets, easing must surprise, but "the bar rises with every measure taken"; successive asset-purchase programmes had smaller
  effects on yields per unit of purchases (Graph IV.7). Near the natural limits, "the marginal effect of policy tends to decline" while side
  effects rise.
- How it explained events: the BIS view of the 2010s is diminishing returns from ultra-easy policy plus a build-up of financial risks.
  This contrasts with the IMF's 2013 conclusion (MO-IMF-2, p. 14) that accommodation carried little inflation risk.

### MO-BIS-3. BIS Annual Economic Report 2026: overview "From resilience to robustness?", Chapter I "Progress and peril", Chapter II (independence passages)
Landing page: https://www.bis.org/publ/arpdf/ar2026e.htm redirects to https://www.bis.org/publications/aer-2026 (title "BIS Annual Economic
Report 2026"); chapters listed there: "progress-peril", "high-public-debt-shifting-financial-markets", "anchoring-trust-money". PDF:
https://www.bis.org/publications/aer-2026_0.pdf (134 PDF pages). Went to press on 22 June 2026 with data to 29 May 2026 (PDF p. 8).
Offset: p. = PDF − 10. Read: overview pp. 1–4; Chapter I pp. 17–19 ("An inflation comeback") and p. 28 (policy implications, opening);
Chapter II pp. 61–62 (risks to independence, monetary policy). Graph 7 notes (p. 17) date the start of the conflict in Iran to 28 February
2026 and "US President Trump announces tariffs" to 2 April 2025.
- p. 1: in 2025 growth held up despite tariffs, helped by lower-than-feared effective tariffs, trade diversion, firms absorbing costs, an
  AI capex boom and buoyant markets. In early 2026 the closure of the Strait of Hormuz hit energy supply: "Rising energy prices once again
  pushed inflation well above central banks’ targets", echoing the post-Covid surge.
- p. 1: plastics and fertiliser prices rose 30% and 50% respectively (overview). **Internal discrepancy: Chapter I p. 18 says both were up
  by 50%.** The central question is whether the rises broaden as in 2021–23. Mitigating: more labour-market slack, policy rates higher than in
  2022. Aggravating: fresh memories of the last surge, so "inflation expectations could de-anchor more quickly than in the past".
- p. 3 (policy): central banks showed "notable resolve" against the post-pandemic surge. With high debt, prioritising medium-term price
  stability remains key even with adverse fiscal side effects; "A firm commitment to price stability, underpinned by central bank
  independence", anchors long-term rates and expands fiscal space.
- p. 17: a 10% oil supply loss; "Brent prices surged by 67% to an intraday peak of $120" in under two weeks; some regional physical crude
  prices matched mid-2008 peaks.
- p. 18: "Global inflation has jumped by half a percentage point since the conflict started". Inflation responds more than proportionally to
  large energy shocks (Graph 8.C); "Post-pandemic high inflation may have also weakened the anchoring of inflation expectations".
- p. 19 (mitigating factors): energy intensity has more than halved in some countries over two decades; inflation expectations are lower
  than after the Russia-Ukraine war began in 2022; labour markets have normalised; relief spending is more targeted this time.
- p. 28: "Adverse supply shocks have become more frequent and more intense" (Graph 17.A). High public debt crowds out monetary space; the
  separation of fiscal and monetary policy, "long a cornerstone of central bank independence and credibility", is under growing strain.
- p. 61 (Chapter II): large-scale bond purchases can create the perception that debt exposures or fiscal considerations constrain monetary
  policy, which could de-anchor expectations; losses draw public criticism, and "Such criticism can undermine legitimacy and ultimately
  independence".
- p. 62: if policy looks constrained by debt-service costs or market stress, expectations could loosen. "Central bank independence is
  therefore essential", but no institutional arrangement is fully credible without fiscal sustainability and a resilient financial system.
- Note: in the pages read, the BIS discusses threats to independence in general terms (fiscal dominance, balance-sheet losses, political
  pressure tied to debt). It does not name the 2025–26 US political pressure on the Federal Reserve. For that, see `IMF_2026.md` (WEO Update
  January 2026, p. 2): the dollar came briefly under pressure after an investigation into the Federal Reserve chair was opened; WEO Update
  January 2026 pp. 8–9: central bank independence "paramount".

---

## Central banks

### MO-CB-1. Federal Reserve (FOMC), Statement on Longer-Run Goals and Monetary Policy Strategy: August 2020 and August 2025 versions
Landing page: https://www.federalreserve.gov/monetarypolicy/review-of-monetary-policy-strategy-tools-and-communications.htm redirects to
https://www.federalreserve.gov/monetarypolicy/review-of-monetary-policy-strategy-tools-and-communications-2025.htm (title "Federal Reserve
Board - Review of Monetary Policy Strategy, Tools, and Communications"; "Last Update: August 22, 2025"). PDFs:
https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals_202008.pdf (1 page, "as amended effective August 27, 2020"),
https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals_202508.pdf (2 pages, "as amended effective August 22, 2025") and
the current https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals.pdf ("as reaffirmed effective January 27, 2026"; text
otherwise identical to August 2025, checked by diff). Read in full. The statements carry no page numbers except "1"/"2" on the 2025 PDF;
cited as "2020 st." and "2025 st.", with page where printed. (The 2021–2024 January versions were downloaded but not compared.)
- 2020 st.: the neutral funds rate has fallen relative to its historical average, so the funds rate is likely to be "constrained by its effective
  lower bound more frequently than in the past"; downside risks to employment and inflation have increased.
- 2020 st.: the 2% PCE goal is reaffirmed, and the FOMC "seeks to achieve inflation that averages 2 percent over time". After periods of
  persistently low inflation, policy will likely aim for inflation moderately above 2% for some time (flexible average inflation targeting).
- 2020 st.: maximum employment is called "a broad-based and inclusive goal"; policy responds to "shortfalls of employment from its maximum
  level", not to deviations in both directions.
- 2025 st. p. 1: the strategy is designed to work across "a broad range of economic conditions"; the explicit average-inflation and
  make-up language and the lower-bound diagnosis are gone; the lower bound appears only as a case where the full range of tools would be
  used. Maximum employment is the highest level achievable on a sustained basis in a context of price stability.
- 2025 st. p. 2: new sentence, "The Committee is prepared to act forcefully" to keep long-term expectations anchored at 2%. When goals
  conflict, it "follows a balanced approach in promoting them". It also notes that "employment may at times run above real-time assessments
  of maximum employment" without necessarily creating risks to price stability (replacing the "shortfalls" language).
- Review page: the 2025 review was the Fed's second periodic review; the 2% goal "was not a focus"; it involved 10 Fed Listens events and
  five FOMC meetings from January 2025; the revised statement was released on 22 August 2025, with reviews roughly every five years.
- How it reads: the 2020 framework was built for the low-inflation, zero-lower-bound world of the 2010s (MO-IMF-2); the 2025 revision
  responds to the 2021–23 overshoot by dropping make-up and adding a commitment to act forcefully.

### MO-CB-2. ECB, monetary policy strategy statement 2021 and updated statement after the 2025 strategy assessment
Landing pages: https://www.ecb.europa.eu/mopo/strategy/strategy-review/html/strategy-review-2021.en.html (title "Strategy review") and
https://www.ecb.europa.eu/mopo/strategy/strategy-review/strategy-review-assessment-2025/html/index.en.html (title "Our 2025 monetary
policy strategy assessment"). Documents (HTML, no page numbers; cited by document and paragraph topic):
2021 statement https://www.ecb.europa.eu/mopo/strategy/strategy-review/ecb.strategyreview_monpol_strategy_statement.en.html;
2025 statement https://www.ecb.europa.eu/mopo/strategy/strategy-review/ecb.strategyreview202506_strategy_statement.en.html;
press releases of 8 July 2021 https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.pr210708~dc78cc4b0d.en.html and 30 June 2025
https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250630~aabf988af8.en.html. Read in full (press releases) and the strategy
paragraphs of both statements. No PDF used. (A guessed URL `.../home/search/review/html/ecb.strategydocument202107~a8f6c8f5e5.en.html`
returned HTTP 404.)
- PR 8 July 2021: the new strategy adopts a symmetric 2% target over the medium term: "negative and positive deviations of inflation from
  the target are equally undesirable". Near the lower bound this requires especially forceful or persistent action, which may imply "a
  transitory period in which inflation is moderately above target". The review was launched on 23 January 2020; the previous one was in
  2003; HICP remains the measure, with owner-occupied housing to be included over time; the next assessment was planned for 2025.
- 2021 statement (context paragraph): since 2003, slower trend growth, demographics and the legacy of the GFC drove down equilibrium real
  rates, reducing the scope to rely on policy rates alone. (Inflation-buffer paragraph): the lower bound "will more frequently constrain the
  conduct of monetary policy". Forward guidance, asset purchases and longer-term refinancing operations stay in the toolkit, and decisions
  include a proportionality assessment of side effects.
- PR 30 June 2025: the symmetric 2% target is confirmed. Structural shifts (fragmentation, AI, demography, climate) suggest an inflation
  environment "potentially more volatile, with larger deviations from the symmetric 2% inflation target". Symmetry now means forceful or
  persistent action against "large, sustained deviations of inflation from the target in either direction". All tools remain; scenarios and
  sensitivity analyses will be used; the next assessment is expected in 2030.
- 2025 statement (context paragraph): it cites both "the low-inflation period and the post-pandemic inflation surge". (Symmetry paragraph):
  for disinflationary shocks the lower bound matters; for inflationary shocks, "possible non-linearities in price and wage setting need to
  be taken into account", an echo of the BIS regime argument (MO-BIS-1).
- How it moved: 2021 was framed around the lower bound and undershooting, like the Fed's 2020 statement (MO-CB-1). In 2025 the framing became
  two-sided and shock-driven; both central banks moved away from frameworks built around the lower bound.

### MO-CB-3. Bank of Japan, "Changes in the Monetary Policy Framework", 19 March 2024 (with the 2016 statements that began negative rates and yield curve control)
Landing page: https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240319a.htm (listed on https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2024/index.htm).
PDFs: statement https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2024/k240319a.pdf (6 pages; printed page numbers 1–5 at the foot, PDF page =
printed page); reference chart https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2024/k240319b.pdf (1 page). Earlier statements, from
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2016/index.htm: 29 January 2016 https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2016/k160129a.pdf and
21 September 2016 https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2016/k160921a.pdf (p. 1 of each read). Read: the 2024 statement in full.
- 2024 p. 1: the Board judged that the virtuous cycle between wages and prices had come in sight, so the 2% target would be achieved in a
  sustainable and stable manner. QQE with yield curve control and "the negative interest rate policy to date have fulfilled their roles";
  the short-term rate becomes the main tool, and "accommodative financial conditions will be maintained for the time being".
- 2024 p. 1: the call rate is to stay at "around 0 to 0.1 percent" (vote 7-2), with 0.1% paid on current account balances from 21 March
  2024; fn. 1: the inflation-overshooting commitment on the monetary base is judged fulfilled. Reference chart: the rate had been in the
  range of –0.1 to 0%, with –0.1% on policy-rate balances.
- 2024 p. 2: JGB purchases continue at broadly the same amount, currently "about 6 trillion yen per month" (fn. 3), with nimble responses
  to a rapid rise in long-term rates (vote 8-1). The Bank will discontinue purchases of ETFs and J-REITs and wind down CP and corporate-bond
  purchases in about a year.
- 2024 pp. 2–3: wages are highly likely to rise steadily, following last year's firm increases; services prices are rising moderately.
  Dissents (p. 3): Nakamura wanted negative rates kept until small firms' capacity to raise wages was clearer; Noguchi opposed ending yield
  curve control and negative rates at the same time.
- 2024 p. 4 (attachment): CPI inflation (less fresh food) has been around 2% recently and is likely to stay above 2% through fiscal 2024.
- 29 January 2016 p. 1: introduction of "QQE with a Negative Interest Rate", by a 5-4 vote: minus 0.1% on part of current accounts, through a
  three-tier system, effective from 16 February 2016 (fn. 1). Fn. 2 cites larger negative rates in Switzerland (–0.75%), Sweden (–1.1%) and
  Denmark (–0.65%).
- 21 September 2016 p. 1: "QQE with Yield Curve Control": –0.1% short rate, 10-year JGB yields around zero, JGB holdings rising by "about
  80 trillion yen" a year, plus an "inflation-overshooting commitment" to expand the monetary base until CPI inflation stays above 2%.
- Derived: Japan's negative policy rate lasted from 16 February 2016 to 21 March 2024, about eight years; yield curve control ran from
  September 2016 to March 2024.

---

## India

Existing notes to use with this section (not re-read): `India_ES_2015-2020.md`, `India_ES_2020-2022.md` ("Monetary and financial response",
"Inflation"), `India_ES_2022-2024.md` ("Inflation", "Monetary policy", "Inflation and monetary policy") and `India_ES_2024-2026.md`
("Inflation and monetary policy", two sections). MO-IN-5 below adds the Survey passages most relevant to this chapter.

### MO-IN-1. RBI, Report of the Expert Committee to Revise and Strengthen the Monetary Policy Framework (Chairman: Urjit R. Patel), 21 January 2014
Landing page: https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=743 (title "Reports| Official Website of Reserve Bank of
India"; date "21 Jan 2014"; size of PDF "3958 kb"). PDF: https://rbidocs.rbi.org.in/rdocs//PublicationReport/Pdfs/ECOMRF210114_F.pdf
**not obtained** (curl exit 56, connection closed by the server with no HTTP response; see "Not read / not found"). Read instead from the
HTML chapters on www.rbi.org.in, which carry no page numbers, so items are cited by the report's own paragraph numbers: Chapter II
(https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?UrlPage=&ID=746), paras II.16–II.19 and II.37–II.38; Chapter VI
"Recommendations" (…&ID=750), recommendations 1–16. Chapter I (…&ID=745) was downloaded and only searched.
- Para II.16: the RBI adopted a "multiple indicator approach" in April 1998, looking at many quantity and rate variables. Para II.17: it
  worked fairly well in 1998-99 to 2008-09 (average real GDP growth 7.1%, average WPI and CPI inflation about 5.5%), but it lacked a clear
  nominal anchor and lost credibility as high inflation and weak growth coexisted.
- Para II.18: WPI and CPI-IW inflation averaged 8.0% and 8.8% under monetary targeting (1985-86 to 1997-98), 5.4% and 5.6% in 1998-99 to
  2008-09, then 7.2% and 10.5% between April 2009 and November 2013. Retail inflation had "persisted at double digit levels over the last six
  years"; supply bottlenecks and sharp rises in minimum support prices since 2007-08 contributed.
- Para II.38: the CPI-Combined inflation threshold above which inflation harms growth is estimated at 6.2%; with the output gap near zero
  (2003-04 Q3 to 2006-07 Q1), CPI inflation averaged about 4%. This gives "empirical support to a range of 4 to 6 per cent" for the target.
- Recommendation 1 (para II.25): "Inflation should be the nominal anchor"; recommendation 2 (II.36): headline CPI (combined), not WPI.
- Recommendation 3 (II.42): the target should be "set at 4 per cent with a band of +/- 2 per cent", wide because of supply and external
  shocks and the large weight of food, and to avoid deflation bias; two-year horizon.
- Recommendation 4 (II.43): a glide path from the current 10% to 8% within 12 months and 6% within 24 months before formally adopting 4%
  ± 2. Recommendation 5 (II.44): food and fuel are more than 57% of the CPI, so policy must respond to second-round effects.
- Recommendations 6–7 (II.47–II.48): the fiscal deficit to fall to 3.0% of GDP by 2016-17; administered prices, wages and interest rates
  impede transmission.
- Recommendations 8–15 (III.22–III.29): decisions vested in a monetary policy committee. The committee proposed five members (Governor as
  chair, the Deputy Governor and Executive Director for monetary policy, two external members), majority vote, meetings every two months,
  minutes after two weeks and a half-yearly inflation report. Failure means missing 4% ± 2 for three successive quarters, which triggers a
  public statement. (The 2016 law set a different composition; see MO-IN-3.)

### MO-IN-2. RBI, Report on Currency and Finance 2020-21, "Reviewing the Monetary Policy Framework" (press release of 26 February 2021)
Landing page: RBI press release 2020-2021/1159, https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=51187 (dated "Feb 26,
2021"). **The report itself was not obtained.** The RCF listing https://www.rbi.org.in/Scripts/AnnualPublications.aspx?head=Report%20on%20Currency%20and%20Finance
shows only the 2023-24 report; earlier years load through an ASP.NET form postback, which was not used, and RBI PDFs on rbidocs.rbi.org.in
fail with plain curl (see MO-IN-1). Read: the press release in full (HTML, no page numbers). The highlights are the report's own summary.
These are the contributors' views, not the RBI's, as the release says.
- The theme was chosen for the review of the inflation target due by March 2021. The study period runs from October 2016 to March 2020. The
  RCF was revived after a hiatus between 2014 and 2019.
- Over the review period headline CPI inflation averaged 3.9%, with lower volatility, "attesting to the success of FIT in terms of its
  primary mandate".
- Trend inflation fell from above 9% before FIT to 3.8–4.3% during FIT, which points to 4% as the right target. Threshold inflation, above
  which growth is clearly impaired, is 5–6%, which supports 6% as the upper limit; a lower limit above 2% would cause frequent undershoots,
  one below 2% would hurt growth. So 4% ± 2 "is appropriate for the next five years".
- The MPC architecture is in line with best practice, but the definition of failure, onboarding of members, forward guidance and the timing
  of minutes and transcripts need review. Transmission was full and quick in money markets, incomplete in bond markets, and improving in
  bank rates; external benchmarks would help.
- International: inflation-targeting EMEs have generally lowered their targets and narrowed their bands.

### MO-IN-3. The statutory framework: RBI Act as amended by the Finance Act 2016; the 4% target notified on 5 August 2016; retained in March 2021 and March 2026
Documents: (a) PIB, Ministry of Finance, "Statutory and Institutionalised framework for Monetary Policy; Central Government in consultation
with RBI announces the Inflation Target of Four Percent", 5 August 2016, https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=148405&reg=48&lang=2
(HTML), and the same release as a DEA PDF, http://dea.gov.in/files/press_release_documents/MonetaryPolicy05082016.pdf (3 pages; read
pp. 1–2); (b) RBI "Overview" page on the monetary policy framework, https://www.rbi.org.in/Scripts/FS_Overview.aspx?fn=2752 (title "Overview |
Official Website of Reserve Bank of India"; HTML). The 2026 Gazette notification itself, https://egazette.gov.in/WriteReadData/2026/271285.pdf,
**was not obtained** (curl exit 60 on two tries, a TLS certificate error; not bypassed). The March 2021 Gazette was not fetched; its date
comes from (b) and MO-IN-4.
- (a) p. 1: the Finance Act, 2016 amended the RBI Act. Its Preamble now says the primary objective is to "maintain price stability, while
  keeping in mind the objective of growth". The MPC has six members: three from the RBI (the Governor as chair, a Deputy Governor and one
  officer) and three appointed by the government for four years, not eligible for reappointment. It meets at least four times a year. The MPC
  provisions came into force on 27 June 2016. **This differs from the Patel committee's five-member design (MO-IN-1).**
- (a) p. 1: under section 45ZA, the government, in consultation with the RBI, sets the CPI target every five years. The target from 5 August
  2016 to 31 March 2021 was four per cent, with an upper tolerance level of six and a lower one of two.
- (a) p. 2: the band allows for short-run trade-offs, data and projection errors and farm-supply shocks, given food's large CPI weight.
  Failure means average inflation above 6% or below 2% "for any three consecutive quarters". The RBI must then report to the government
  the reasons, remedies and time to return.
- (b): on 31 March 2021 the government "retained the inflation target and the tolerance band" for 1 April 2021 to 31 March 2026. In its
  second review, on 25 March 2026, it retained them again for 1 April 2026 to 31 March 2031. The first MPC was constituted on 29 September
  2016.
- The accountability clause was triggered once: inflation stayed above 6% for five quarters (Q4 2021-22 to Q4 2022-23), and the MPC met on
  3 November 2022 to send a report to the government (MO-IN-4, para 10).

### MO-IN-4. RBI, "Review of Monetary Policy Framework – A Discussion Paper", 21 August 2025
Landing page: press release 2025-2026/951, https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=61067. Paper (HTML):
https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23171. No page numbers; cited by the paper's paragraph numbers. Read: paras 4–12,
27 and Table 2, 33–46 (searched), 56, 60–61. Data run to May 2025 (Table 2 note). The paper sets out questions; it is not a decision. The
decision was the March 2026 retention (MO-IN-3).
- Para 5: a Monetary Policy Framework Agreement with the government in 2015 came first, then the 2016 amendment; failure was defined as
  three consecutive quarters outside the band. Table 2 note: the amended Act came into force on 27 June 2016, the target was announced on
  5 August 2016, the MPC was constituted on 29 September 2016 and first met on 3–4 October 2016.
- Para 9: average inflation since FIT was 4.9%, against 6.8% before FIT in the current series. The 2014 glide path (MO-IN-1) was
  "overachieved". Inflation hovered around 4% in 2016–19, then breached the band in some quarters of 2020-21 and 2021-22.
- Para 10: after the Russia-Ukraine war, food, fuel and core inflation were all above target for the first time; "Inflation reached 7.8 per
  cent in April 2022, its peak for the FIT period". Inflation was above 6% for five quarters, Q4 2021-22 to Q4 2022-23.
- Para 11: the decline after 2022-23 is credited to government supply-side measures on food, monetary policy that prevented
  generalisation, and lower commodity prices. Nine years of FIT show "a hump-shaped performance": the first three and last three years on
  target, the middle three years high.
- Para 12: the ± 2 band gave the MPC flexibility: "During the pandemic, high prints of inflation were ignored" to support growth; after the
  war the focus shifted to inflation.
- Para 27 and Table 2: headline CPI inflation averaged 7.4% (core 6.6%) before FIT (April 2012 to September 2016) and 4.4% (core 5.0%) in
  the first FIT period (October 2016 to March 2021); the standard deviation fell from 2.3 to 1.6. **Compare MO-IN-2: 3.9% for October
  2016 to March 2020. The periods differ, since the 2020-21 pandemic spike is excluded there.**
- Paras 39–40: breaches of 6% came in Q4 2019-20 and Q2–Q3 2020-21 (6.7%, 6.9%, 6.4%, mainly food), then in Q4 2021-22 to Q4 2022-23
  (broad-based); Q1 2025-26 was slightly below 4%. Para 56: in 35 quarters of FIT, inflation was in 2–4% for 11, in 4–6% for 14, and above
  6% in 9 quarters during 2020–2022.
- Paras 44–45 (disagreement): some argued for a higher target (close to 6%, on fiscal and current-account thresholds), others for a lower
  one, as Indonesia (6% to 2.5%) and Brazil (8% to 2.5%) had done. Para 46: the paper leans to continuity.
- Para 60: food and energy are "more than half of the consumption basket", so supply shocks weigh unusually heavily. Monetary-fiscal
  coordination (supply-side measures plus tightening against second-round effects) is presented as the reason FIT worked.

### MO-IN-5. Economic Survey passages on inflation targeting and the 2022 episode (mostly from existing notes)
Source text: `Econ Subject/sources/text/es<YEAR>.txt`. Only ES 2016-17 Vol 2 was read afresh here (st. 386–388 = pp. 35–37; offset: printed
p. = st. − 351). Everything else is cited from existing notes by item label.
- Framework: the February 2015 agreement between the government and the RBI; CPI came in below the 6% target set for January 2016
  (ES15-14, `India_ES_2015-2020.md`). Codified at 4% ± 2 from 5 August 2016; MPC notified 29 September 2016 (ES16-13). **Do not use ES
  2018-19's dating of the MPC to February 2015 (ES18-2, flagged there as wrong).**
- ES 2016-17 Vol 2 (August 2017), p. 35, para 1.147: a structural shift in inflation dynamics and inflation running well below 4% mean
  inflation by March 2018 is likely to be under the target. p. 35, para 1.150: real policy rates, at 4.7% on current inflation, are the
  highest in the recent past and above comparable EMs.
- ES 2016-17 Vol 2, p. 36, para 1.151: the inflation-targeting-cum-MPC framework is new, so credibility matters. p. 37, paras 1.153–1.156:
  RBI estimates put the real neutral rate at 1.25–1.75%, so the neutral nominal rate is 5.25–5.75% against a 6.00% repo. With "Current
  inflation, at 1.5" per cent and capacity utilisation at 72.7%, the Survey concludes that the "scope for monetary easing is considerable".
  **The Survey here pushes for easing against the RBI's own caution, an early government–central bank tension inside the new framework.**
- Pandemic: CPI inflation was 6.6% in April–December 2020, above the band and driven by food (ES20-31, `India_ES_2020-2022.md`). The RBI
  says it deliberately looked through this (MO-IN-4, para 12).
- 2022 episode: CPI peaked at 7.8% in April 2022, WPI at 16.6% in May; retail inflation was above the band for ten months, January to
  November 2022 (ES22-16, ES22-17, `India_ES_2022-2024.md`). The Survey credits India's calibrated stimulus: India "chose not to
  overstimulate" (ES22-18).
- Tightening: the stance changed and the SDF was introduced in April 2022, followed by an off-cycle hike in May 2022. The repo rose from 4.0%
  to 6.25% by December 2022 (ES22-24, ES22-25) and to 6.5% in February 2023 (flag in ES22-25); ES23-9 gives 250 bps of hikes between May 2022 and February 2023. Inflation was 6.7% in 2022-23 and
  5.4% in 2023-24, helped by supply measures and rate rises (ES23-9).
- Low inflation, 2025: CPI averaged 4.6% in FY25 and 1.7% in April–December FY26, the lowest in the series; 0.3% in October 2025 (ES25-12,
  `India_ES_2024-2026.md`). FY26 headline CPI 2.1% (IN26-19, `India_2026.md`).
- 2026 energy shock: CPI on the new 2024 = 100 series rose from 2.7% (January 2026) to 4.4% (June, the first month above target in 16
  months) and 4.8% (August) (IN26-19). The repo was held at 5.25% in April, June and August (IN26-21, IN26-22, IN26-24), then raised 25 bp
  to 5.50% on 7 October 2026, with the stance set to "calibrated tightening" (IN26-25).

---

## Synthesis: how the view of monetary policy moved, 2000–2026

1. **2000s: the Great Moderation and the anchor.** Industrial-country inflation had settled at 2–3% since the early 1990s, against about 9%
   in the early 1980s, matching explicit or implicit targets (MO-IMF-1, p. 98). The IMF (2006) gave credit both to credible targets, which
   set inflation in the medium term, and to globalization, which shaved about ½ point off inflation in 1998–99 and flattened its response to
   domestic slack (pp. 106, 109, 123). It warned that globalization "cannot be relied upon" as slack disappeared (p. 123). In 2018 the IMF
   found that EM gains were mainly domestic: anchored expectations, not global factors (MO-IMF-3, p. 101). **The two IMF chapters weight
   globalization differently.**
2. **India before inflation targeting.** WPI/CPI-IW inflation averaged 5.4%/5.6% in 1998-99 to 2008-09 under the multiple indicator
   approach, then 7.2%/10.5% in April 2009 to November 2013, with retail inflation in double digits for six years (MO-IN-1, para II.18).
   Pre-FIT (2012–16) headline CPI averaged 7.4% (MO-IN-4, Table 2).
3. **After 2008: the zero lower bound, QE and negative rates.** Major AE policy rates sat near zero; real policy rates had not been so low for
   so long since the start of the postwar period (MO-BIS-2, pp. 63–64). The Fed's lift-off came only in December 2015, to about 0.35% (p. 64).
   The ECB's deposit rate went to –0.40% in March 2016 (p. 65). Japan's negative rate ran from 16 February 2016 to 21 March 2024, about eight
   years, and yield curve control from September 2016 (MO-CB-3). In 2020–22, central bank balance sheets grew by more than 20% of GDP in
   Japan, the UK and the euro area and about 18% in the US (MO-IMF-4, Box 2.1 p. 58). In the largest AEs 30–50% of marketable government
   debt became effectively overnight (MO-BIS-1, p. xv).
4. **QE effects and side effects: a disagreement.** The IMF (2024) says pandemic QE had sizable effects in containing distress and that QT
   has had minimal effects so far, about 12 bp on term premiums per standard-deviation shock (MO-IMF-4, p. 58). The BIS (2016) argued that
   returns were diminishing: the output effect of US asset purchases weakened after 2011, successive programmes moved yields less, and
   negative rates squeezed banks (Swiss banks raised mortgage rates) (MO-BIS-2, pp. 70–71). The BIS (2022) adds that policy reaches only
   about a third of US price sectors (MO-BIS-1, p. 60).
5. **The "missing (dis)inflation" of the 2010s.** The IMF (2013) explained stable inflation after the Great Recession by a flatter Phillips
   curve and better-anchored expectations: "the Phillips curve is considerably flatter today" (MO-IMF-2, p. 14). It concluded that
   accommodation carried little inflation risk if independence was preserved, while flagging housing bubbles and balance-sheet politics
   (pp. 14–15). The frameworks of 2020–21 built in this world: Fed average inflation targeting with make-up (MO-CB-1, 2020 st.), and the
   ECB's symmetric 2% target with forceful action near the lower bound (MO-CB-2, 2021).
6. **2020 response.** Massive monetary and fiscal support; the Fed moved to flexible average inflation targeting (`IMF_2020-2021.md`, WEO
   October 2020, Ch. 1 p. 5). Pandemic fiscal stimulus averaged about 12% of GDP in AEs and 4% in EMs (MO-IMF-4, p. 41, fn. 1). In mid-2021
   the IMF read price pressures as "transitory supply-demand mismatches" (`IMF_2020-2021.md`, WEO Update July 2021, p. 1). India's MPC
   looked through high pandemic prints (MO-IN-4, para 12).
7. **2021–23 surge: supply or demand?** Global inflation tripled by mid-2022; the median AE and EM peaked at about 8% in 2022, and forecasts
   underestimated it (MO-IMF-4, pp. 41, 43). By April 2022 three-quarters of economies had inflation above 5% (MO-BIS-1, p. x). **The IMF
   stresses supply bottlenecks meeting demand rotation; energy pass-through gave more than 2.5 points in Europe; it finds labour markets
   decisive only in the US after mid-2022 (MO-IMF-4, pp. 42, 48). The BIS puts strong demand from huge stimulus first, then the
   services-to-goods pivot, then bottlenecks (MO-BIS-1, p. x).** Both admit the miss (MO-BIS-1, p. x). India peaked at 7.8% in April 2022
   and breached the band for five quarters; all of food, fuel and core were above target (MO-IN-4, para 10).
8. **The great tightening and its cost.** Rate rises at a speed, degree and breadth "unprecedented in at least 40 years" (MO-IMF-5, p. 43).
   The IMF found a low sacrifice ratio: no wage-price spirals, expectations anchored, disinflation faster than forecast (MO-IMF-4, pp. 43,
   56). Tightening three quarters earlier would have cut peak inflation about 2 points for a 0.8-point loss of 2022 GDP (p. 53). Before the
   event the BIS had feared a costlier path: 1.5–3% lower GDP by 2025 in stylised scenarios, and a possible tipping point into a high-inflation
   regime (MO-BIS-1, pp. xi–xii). **Outcome: the IMF's benign reading was closer to what happened by 2024.** India's repo went from 4.0% to
   6.5% (250 bp) between May 2022 and February 2023 (MO-IN-5).
9. **Framework reviews, 2025.** The Fed dropped average-inflation make-up and the "shortfalls" language and added "prepared to act
   forcefully" (MO-CB-1, 2025 st. p. 2). The ECB kept 2% but redefined symmetry as forceful action against large, sustained deviations in
   either direction, expecting a more volatile environment (MO-CB-2, 2025). India's RBI discussion paper (August 2025) weighed headline
   against core and higher against lower targets (MO-IN-4, paras 44–46). The government retained 4% ± 2 for 2026–31 on 25 March 2026 (MO-IN-3).
10. **India's record under inflation targeting.** Average CPI inflation was 4.9% since FIT against 6.8% before, in the current series
    (MO-IN-4, para 9); 3.9% in October 2016 to March 2020 (MO-IN-2); 4.4% in October 2016 to March 2021 (MO-IN-4, Table 2). Trend inflation
    fell from above 9% to 3.8–4.3% (MO-IN-2). The record was hump-shaped (MO-IN-4, para 11), ending with a series-low 1.7% in April–December
    FY26 (MO-IN-5) before the 2026 energy shock.
11. **2025–26: independence and the energy shock.** The IMF called independence "paramount" as the dollar wobbled when an investigation into
    the Fed chair was opened (`IMF_2026.md`, WEO Update January 2026, pp. 2, 8–9). The BIS (June 2026) warns that the fiscal-monetary
    separation, "long a cornerstone" of independence, is under strain from high debt; losses on QE holdings invite criticism that can erode
    legitimacy (MO-BIS-3, pp. 28, 61–62). The Hormuz closure pushed Brent up 67% to $120 intraday, and global inflation rose by half a point
    within weeks (pp. 17–18). Central banks feared faster de-anchoring after 2021–23 (p. 1), but started from more slack and higher rates. By
    Q3 2026, 14 of 33 major central banks had hiked (`IMF_2026.md`, GFSR October 2026, Ch. 1 p. 1). India hiked to 5.50% on 7 October 2026
    (IN26-25).

---

## Not read / not found

- **WEO "The Great Tightening" placement:** the brief gave April 2024 Ch 2. The April 2024 Ch 2 is "Feeling the Pinch?" (MO-IMF-5); "The
  Great Tightening" is October 2024 Ch 2 (MO-IMF-4). Both were read.
- **WEO April 2006 and April 2013 full volumes** were not fetched. The 2013 chapter file prints its own 1–18 numbering, not the bound
  volume's page numbers. Boxes 3.1–3.3 of 2006 and Box 3.1 of 2013 were not read.
- **WEO October 2018 Ch 3 online annexes** (`ch3annex.pdf`) were not fetched.
- **BIS AER 2019** (the EME monetary frameworks chapter, https://www.bis.org/publications/aer-2019/monetary-policy-frameworks-emes-inflation-targeting-exchange-rate-financial-stability)
  was not read; the 2016 chapter was chosen instead (MO-BIS-2). The BIS 2022 chapter PDF (`inflation-look-under-hood.pdf`) was downloaded but
  the full report was used for pages. BIS 2022 Chapter I and BIS 2026 Chapter III (stablecoins) were not read.
- **ECB:** a guessed URL https://www.ecb.europa.eu/home/search/review/html/ecb.strategydocument202107~a8f6c8f5e5.en.html returned
  HTTP 404. The ECB's pre-2021 definition of its target is quoted only second-hand, from the 2014 Patel report (Chapter II, para II.37 area:
  "below 2 per cent" HICP). The 2003 review itself was not fetched. The overview documents and the 2025 assessment topic pages were not read.
- **Fed:** the 2012 original statement and the January 2021–2024 reaffirmed versions were downloaded but not compared. The dates when the
  funds rate first reached zero (2008) and returned to zero (March 2020) were not taken from any source read; only the December 2015
  lift-off is sourced (MO-BIS-2, p. 64). The 2025–26 political pressure on the Fed is sourced only through `IMF_2026.md`; no Fed or US
  government document on it was read.
- **Patel committee report PDF**, https://rbidocs.rbi.org.in/rdocs//PublicationReport/Pdfs/ECOMRF210114_F.pdf: curl exit 56 (connection
  closed, no HTTP status) on three tries, with and without the double slash. Read from the HTML chapters instead (no page numbers). Same
  pattern as recorded in `India_2026.md` for rbidocs. Not bypassed.
- **Report on Currency and Finance 2020-21 (full report)**: not obtained. The listing page needs an ASP.NET form postback to show 2021, and
  rbidocs PDFs fail with curl. Only the press release was read (MO-IN-2), so no chapter-level findings or page numbers.
- **Gazette notification of 25 March 2026**, https://egazette.gov.in/WriteReadData/2026/271285.pdf: curl exit 60 (TLS certificate
  problem), twice; not bypassed. Its content (4%, 2–6%, 1 April 2026 to 31 March 2031) is taken from the RBI Overview page (MO-IN-3), not
  from the Gazette. A web-search snippet giving the number S.O. 1580(E) was not verified and is not used. The 2016 and 2021 Gazette texts and
  the Finance Act 2016 text were not fetched; the 2016 facts come from the PIB/DEA release.
- **Economic Surveys:** only ES 2016-17 Vol 2 pp. 35–37 were read afresh. ES 2015-16 and 2022-23 passages are cited from existing notes
  (ES15-14, ES22-16 to ES22-25). The ES 2015-16 text extract is in two-column layout that mixes columns, so no quotes were taken from it.
  Two quote attempts from ES 2016-17 failed the check for the same reason and were dropped.
- **IMF 2020–23 inflation chapters** (for example WEO October 2022 or October 2023 chapters on expectations and wage-price spirals) were not
  read; the 2020–23 points rely on existing `IMF_*.md` notes as cited.
