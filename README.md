# The World Economy 2000–2026

An interactive book on the world economy over a quarter of a century: what happened, why, and what the IMF and the World Bank said at the time. It has nine phase chapters, nine theme chapters and seven country lenses, each with a section on India. It also has three tools (Compare countries, World map, WDR shelf), a glossary, and a sources page.

## Reading it

Open `index.html` in a browser. Nothing else is needed: no server, no internet connection, no install. The pages load their libraries and data from this folder, and they work from `file://`.

- Press `/` to search, and `[` and `]` to move between chapters.
- Every chart has a year range, a data table and a CSV download. Hover a chart for values.
- Pages print cleanly, with charts, sources and notes.

`scripts/serve.py` starts an optional local server (`python3 scripts/serve.py 8778`) that turns off browser caching. It is useful only while editing.

## What is where

| Path | Contents |
|---|---|
| `index.html` | Home: the master timeline and the contents |
| `chapters/` | `phase-1` … `phase-9`, `theme-*`, `lens-*` |
| `explorer.html`, `map.html`, `wdr-shelf.html` | The three tools |
| `glossary.html`, `sources.html`, `about.html` | Reference pages. About covers method, vintages and what is not yet confirmed |
| `assets/js/` | `charts.js` (the one chart wrapper), `book.js` (navigation, search, popovers), `palette.js` (fixed colour per economy), `explorer.js`, `map.js`, `timeline.js`, and generated data (`book-data.js`, `glossary-data.js`, `sources-data.js`, `search-index.js`) |
| `assets/vendor/` | ECharts and MiniSearch, vendored |
| `assets/geo/world-110m.js` | Natural Earth 1:110m country boundaries (public domain) |
| `data/raw/` | Untouched downloads, with `fetch_log.csv` (URL, size, SHA-256, time of every download) |
| `data/clean/`, `data/js/` | Tidy series as JSON, and the same as script files that pages load |
| `data/hand/` | Figures typed from cited report pages |
| `sources/bibliography.csv` | Every report and data set used, with URL, access date and the chapters that use it |
| `sources/reading-notes/` | Notes on each report read, with page references |
| `sources/reports/wdr_wds/` | Raw World Bank API records behind the WDR shelf |
| `NOTES.md` | Access problems, unverified items, conflicting sources, claims removed, and method notes, chapter by chapter |
| `PROGRESS.md`, `PLAN.md` | Build log and the original plan |

## Rebuilding

The book is already built. These steps rebuild it from the sources. Run them from this folder, using the project's virtual environment (`.venv/bin/python`) or Python 3.

1. `scripts/fetch.py <job> …` downloads data into `data/raw/`. Jobs: `weo weo_meta wdi fred fred_missing ecb bis oecd shiller infl geo`. Always name the jobs you want. Other folders in `data/raw/` (WEO vintages, Penn World Table, OWID, UN population, World Bank commodity prices, NASA, Eurostat, ONS) were fetched outside these jobs; they are logged in `fetch_log.csv` too.
2. `scripts/build_data.py` cleans the downloads into `data/clean/` and `data/js/`. `scripts/build_hand.py` and `scripts/import_india.py` add hand-entered and Indian series.
3. `scripts/derive_<chapter>.py` computes the figures quoted in each chapter (`data/clean/derived/`).
4. `scripts/build_catalogue.py` builds the indicator list for the explorer and the map. `scripts/build_wdr_shelf.py` builds `wdr-shelf.html`.
5. `scripts/build_site_meta.py` builds `sources-data.js` and the search index.
6. Run the checks:
   - `scripts/check_numbers.py` compares every tagged number in the text with the data.
   - `scripts/check_links.py` checks internal links, anchors and footnote back-links.

## Conventions

- Nothing is written from memory. Every report title, date, figure and quotation was read from the source and is footnoted. Anything that could not be checked carries a visible `[unverified]` marker and is listed on the About page and in `NOTES.md`.
- Reports are paraphrased; quotations are short and attributed.
- IMF data are the October 2026 World Economic Outlook unless a chart says otherwise. Years after each economy's last actual year are marked as estimates or projections.
- India's fiscal years (April–March) are plotted at the year in which they start.

## Licence

Text and charts: CC BY 4.0, made with Claude (Anthropic) at the author's direction. Data, cited reports and bundled libraries keep their own terms. See `LICENSE.md` and the About page.
