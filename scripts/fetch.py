"""Download every series in registry.py into data/raw/<source>/.

Each download is appended to data/raw/fetch_log.csv (source, id, url, file,
bytes, sha256, retrieved_utc). Raw files are never edited by hand.

Usage: python3 scripts/fetch.py [weo|wdi|fred|ecb|bis|shiller|geo ...]
"""
import csv, datetime as dt, hashlib, json, re, sys, time, urllib.request, urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import registry as R

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
LOG = RAW / "fetch_log.csv"
UA = "world-economy-book-data-fetch/1.0"


def get(url, headers=None, tries=4, timeout=120):
    h = {"User-Agent": UA, **(headers or {})}
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 400, 401, 403):
                raise
            time.sleep(3 * (i + 1))
        except Exception:
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"failed after {tries} tries: {url}")


def save(source, sid, url, data, ext):
    d = RAW / source
    d.mkdir(parents=True, exist_ok=True)
    f = d / f"{re.sub(r'[^A-Za-z0-9_.-]', '_', sid)}.{ext}"
    f.write_bytes(data)
    new = not LOG.exists()
    with LOG.open("a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["source", "id", "url", "file", "bytes", "sha256", "retrieved_utc"])
        w.writerow([source, sid, url, str(f.relative_to(ROOT)), len(data),
                    hashlib.sha256(data).hexdigest(), dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")])
    return f


def log_fail(source, sid, url, err):
    with (RAW / "fetch_failures.txt").open("a") as fh:
        fh.write(f"{dt.datetime.utcnow():%Y-%m-%dT%H:%M:%SZ}\t{source}\t{sid}\t{url}\t{err}\n")
    print(f"  FAIL {source} {sid}: {err}")


SDMX = "https://api.imf.org/external/sdmx/2.1/data/IMF.RES,{flow}/{key}?startPeriod=1980"
CSVH = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}


def fetch_weo():
    for ind in R.WEO_INDICATORS:
        url = SDMX.format(flow="WEO", key=f".{ind}.A")
        try:
            save("imf_weo", ind, url, get(url, CSVH, timeout=300), "csv"); print("  weo", ind)
        except Exception as e:
            log_fail("imf_weo", ind, url, e)
        time.sleep(1)
    for v in R.WEO_VINTAGES:
        for ind in R.WEO_VINTAGE_INDICATORS:
            url = SDMX.format(flow=v, key=f".{ind}.A")
            try:
                save("imf_weo_vintage", f"{v}__{ind}", url, get(url, CSVH, timeout=300), "csv"); print("  vintage", v, ind)
            except Exception as e:
                log_fail("imf_weo_vintage", f"{v}__{ind}", url, e)


def fetch_weo_meta():
    url = "https://api.imf.org/external/sdmx/2.1/dataflow/IMF.RES/WEO/latest?references=all"
    try:
        save("imf_weo", "_structure", url, get(url, timeout=300), "xml"); print("  weo structure")
    except Exception as e:
        log_fail("imf_weo", "_structure", url, e)


def fetch_wdi():
    for ind in R.WDI_INDICATORS:
        url = f"https://api.worldbank.org/v2/country/all/indicator/{ind}?format=json&date=1990:2026&per_page=20000"
        try:
            data = get(url)
            js = json.loads(data)
            if not isinstance(js, list) or len(js) < 2 or js[1] is None:
                raise RuntimeError(f"no data: {data[:200]!r}")
            save("wdi", ind, url, data, "json"); print("  wdi", ind, js[0].get("total"))
        except Exception as e:
            log_fail("wdi", ind, url, e)
    url = "https://api.worldbank.org/v2/country?format=json&per_page=400"
    save("wdi", "_countries", url, get(url), "json")


def fetch_fred(only_missing=False):
    for s in R.FRED_SERIES:
        if only_missing and (RAW / "fred" / f"{s}.csv").exists():
            continue
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}"
        try:
            data = get(url)
            if not data.startswith(b"observation_date") and not data[:20].upper().startswith(b"DATE"):
                raise RuntimeError(f"unexpected: {data[:80]!r}")
            save("fred", s, url, data, "csv")
            page = get(f"https://fred.stlouisfed.org/series/{s}").decode("utf-8", "ignore")
            meta = {
                "title": (re.search(r"<title>(.*?)\s*\|", page, re.S) or [None, ""])[1].strip(),
                "units": (re.search(r'id="UNITS"[^>]*>\s*(.*?)\s*<', page, re.S) or re.search(r'class="series-meta-value-units"[^>]*>(.*?)<', page, re.S) or [None, ""])[1].strip(),
            }
            save("fred", s + "__meta", f"https://fred.stlouisfed.org/series/{s}", json.dumps(meta).encode(), "json")
            print("  fred", s, meta["title"][:70])
        except Exception as e:
            log_fail("fred", s, url, e)
        time.sleep(0.5)


def fetch_ecb():
    for name, (flow, key) in R.ECB_SERIES.items():
        url = f"https://data-api.ecb.europa.eu/service/data/{flow}/{key}?format=csvdata"
        try:
            save("ecb", name, url, get(url), "csv"); print("  ecb", name)
        except Exception as e:
            log_fail("ecb", name, url, e)


def fetch_bis():
    for ds in R.BIS_DATASETS:
        url = f"https://data.bis.org/static/bulk/{ds}_csv_flat.zip"
        try:
            save("bis", ds, url, get(url, timeout=600), "zip"); print("  bis", ds)
        except Exception as e:
            log_fail("bis", ds, url, e)


def fetch_shiller():
    try:
        save("shiller", "ie_data", R.SHILLER_URL, get(R.SHILLER_URL), "xls"); print("  shiller")
    except Exception as e:
        log_fail("shiller", "ie_data", R.SHILLER_URL, e)


def fetch_geo():
    try:
        save("geo", "ne_110m_admin_0_countries", R.NE_URL, get(R.NE_URL), "geojson"); print("  geo")
    except Exception as e:
        log_fail("geo", "ne_110m", R.NE_URL, e)


def fetch_oecd():
    url = R.OECD_QNA_URL.format(areas="+".join(R.OECD_QNA_AREAS))
    try:
        data = get(url, {"Accept": "application/vnd.sdmx.data+csv; charset=utf-8"})
        if not data.startswith(b"DATAFLOW"):
            raise RuntimeError(f"unexpected: {data[:80]!r}")
        save("oecd", "QNA_GDP", url, data, "csv"); print("  oecd QNA_GDP")
    except Exception as e:
        log_fail("oecd", "QNA_GDP", url, e)


EUROSTAT_HICP_URL = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr"
                     "?format=JSON&geo=EA&coicop18=TOTAL&unit=RCH_A")
ONS_CPI_URL = "https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/d7g7/mm23"


def fetch_infl():
    """Headline inflation after the ECB's old HICP series and the OECD UK series stopped (Phase 9)."""
    for src, sid, url, ext in [("eurostat", "EA_HICP_ANR", EUROSTAT_HICP_URL, "json"), ("ons", "UK_CPI_D7G7", ONS_CPI_URL, "csv")]:
        try:
            save(src, sid, url, get(url), ext); print(" ", src, sid)
        except Exception as e:
            log_fail(src, sid, url, e)


JOBS = {"fred_missing": lambda: fetch_fred(True), "oecd": fetch_oecd, "weo": fetch_weo, "weo_meta": fetch_weo_meta, "wdi": fetch_wdi, "fred": fetch_fred, "ecb": fetch_ecb,
        "bis": fetch_bis, "shiller": fetch_shiller, "geo": fetch_geo, "infl": fetch_infl}

if __name__ == "__main__":
    for j in (sys.argv[1:] or JOBS):
        print("==", j); JOBS[j]()
