"""Import curated India series from the author's Indian-economy book.

That book's dataset (data/csv/annual.csv) was built from the Economic Survey
Statistical Appendices and the RBI Handbook of Statistics; every value carries a
source_id resolved in data/csv/sources.csv (document, table, page). This script
copies a curated list into data/clean/india/ and data/js/india/, keeping the
source of each value.

Convention: Indian fiscal years run April-March. An FY is plotted at the calendar
year in which it starts (FY2008-09 -> 2008), which is also how the IMF WEO dates
India's rows.

    python3 scripts/import_india.py [path-to-indian-book]
"""
import csv, datetime, json, os, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# The Indian-economy project folder: give it as the first argument or in the INDIA_BOOK environment variable.
if len(sys.argv) > 1:
    SRC = Path(sys.argv[1])
elif os.environ.get("INDIA_BOOK"):
    SRC = Path(os.environ["INDIA_BOOK"])
else:
    sys.exit("usage: import_india.py <path to the Indian-economy project folder> (or set INDIA_BOOK)")

SERIES = [
    # growth and demand
    "gdp_real_growth", "gdpfc_growth_ae_first", "gdpfc_growth_2004", "gdpfc_growth_1999", "gfcf_gdp", "sav_total_gdp", "gcf_total_gdp",
    "exports_gs_gdp", "exports_gs_real_growth", "imports_gs_gdp",
    # external
    "cab_gdp", "bop_ca", "bop_trade_balance", "bop_invisibles", "bop_fi", "fdi_net", "fpi_net", "bop_ecb",
    "bop_nri", "bop_overall", "bop_software_net", "bop_services_net", "bop_transfers_net",
    "services_exports_gross", "exports_goods", "imports_goods", "oil_imports", "nonoil_imports",
    "fx_reserves", "import_cover_months", "inr_usd", "ext_debt_gdp", "ext_debt_short_share", "exports_to_us",
    "imports_from_china",
    # prices and money
    "wpi_inflation", "cpi_iw_inflation", "cpi_inflation", "cpi_food_inflation", "repo_end", "repo_high", "repo_low",
    "reverse_repo_end", "scb_credit_gdp",
    # fiscal
    "centre_fd_gdp", "centre_fd_be_gdp", "gg_fd_gdp", "gg_debt_gdp", "centre_subsidies_gdp",
    # markets
    "sensex_avg", "mcap_bse_gdp",
    # energy
    "enr_crude_import_share",
]


def fy_start(fy):  # "FY09" -> 2008
    return 2000 + int(fy[2:]) - 1 if int(fy[2:]) < 80 else 1900 + int(fy[2:]) - 1


def last_firm(pts, provisional):
    """Last year after which every year is provisional (so only a trailing run counts)."""
    years = [y for y, _ in pts]
    last = years[-1]
    for y in reversed(years):
        if y in provisional:
            last = y - 1
        else:
            break
    return last if last < years[-1] else None


def main():
    csvdir = SRC / "data" / "csv"
    dic = {r["series"]: r for r in csv.DictReader(open(csvdir / "data_dictionary.csv", encoding="utf-8"))}
    srcs = {r["source_id"]: r for r in csv.DictReader(open(csvdir / "sources.csv", encoding="utf-8"))}
    rows = defaultdict(list)
    for r in csv.DictReader(open(csvdir / "annual.csv", encoding="utf-8")):
        if r["series"] in SERIES and r["value"] not in ("", "NA"):
            rows[r["series"]].append(r)
    today = datetime.date.today().isoformat()
    out_c, out_j = ROOT / "data/clean/india", ROOT / "data/js/india"
    out_c.mkdir(parents=True, exist_ok=True); out_j.mkdir(parents=True, exist_ok=True)
    made = []
    for sid in SERIES:
        if sid not in rows:
            print("not found:", sid); continue
        d = dic.get(sid, {})
        # annual.csv keeps every vintage (one row per series, FY, base and Survey edition), in
        # chronological order of source. Use the latest row per FY within the series' main base
        # (the base covering the most years), falling back to another base only where it is absent.
        by_base = defaultdict(dict)
        for r in rows[sid]:
            by_base[r.get("base", "")][r["fy"]] = r          # later rows overwrite earlier ones
        main = max(by_base, key=lambda b: (len(by_base[b]), b))
        chosen = dict(by_base[main])
        for b, fys in by_base.items():
            for f, r in fys.items():
                chosen.setdefault(f, r)
        pts, status, cites, bases = [], {}, {}, {}
        for f in sorted(chosen, key=fy_start):
            r = chosen[f]
            y = fy_start(f)
            pts.append([y, round(float(r["value"]), 4)])
            if r["status"] not in ("A", ""):
                status[y] = r["status"]
            if r.get("base", "") != main:
                bases[y] = r.get("base", "")
            s = srcs.get(r["source_id"], {})
            cites[y] = "; ".join(x for x in (s.get("doc") or r["source_id"], s.get("table", ""), ("p. " + s["page"]) if s.get("page") else "") if x)
        provisional = [y for y, st in status.items() if st in ("P", "PE", "PA", "RE", "1RE", "2RE", "3RE", "BE", "AE", "E", "Q")]
        obj = {
            "id": "india/" + sid, "source": d.get("source") or "Economic Survey / RBI Handbook (via the author's Indian-economy dataset)",
            "code": "India dataset " + sid, "label": d.get("name", sid), "unit": d.get("unit", ""), "freq": "A",
            "vintage": d.get("vintage", ""), "url": "", "retrieved": today,
            "notes": ("Indian fiscal year (April–March), plotted at its start year. " + (d.get("description") or "")).strip(),
            "base": main, "other_base": bases, "status": status, "cites": cites,
            # Provisional/revised estimates are listed in "status" (not drawn as projections).
            "data": {"IND": pts},
        }
        s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
        (out_c / f"{sid}.json").write_text(s, encoding="utf-8")
        (out_j / f"{sid}.js").write_text(f'WE.register("india/{sid}",{s});\n', encoding="utf-8")
        made.append(sid)
    print(f"{len(made)} India series written from {SRC}")


if __name__ == "__main__":
    main()
