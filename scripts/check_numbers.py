"""Check every number tagged in the chapters against the data.

In the HTML a figure is tagged  <span class="n" data-d="phase3:key">5.4</span>.
"phase3" names data/clean/derived/phase3.json, which maps key -> {value, how}.
The figure passes if it equals the stored value rounded to the decimals shown.
Prose often states a fall as a positive number ("fell 10.2 percent"), so the
sign is ignored when the span has data-abs="1" or when the text has no sign.
Exit status 1 if anything fails, so a data refresh that moves a number is caught.
    python3 scripts/check_numbers.py
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r'<span class="n" data-d="([a-z0-9_]+):([A-Za-z0-9_]+)"([^>]*)>([^<]+)</span>')
cache, bad, n = {}, 0, 0
for page in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.html"))):
    html = open(page, encoding="utf-8").read()
    for f, key, attrs, shown in TAG.findall(html):
        n += 1
        if f not in cache:
            cache[f] = json.load(open(os.path.join(ROOT, "data", "clean", "derived", f + ".json")))
            cache[f] = cache[f].get("values", cache[f])
        rec = cache[f].get(key)
        txt = shown.strip().replace("−", "-").replace(",", "")
        if rec is None:
            print(f"MISSING  {os.path.basename(page)}  {f}:{key}  shown {shown}"); bad += 1; continue
        val = rec["value"] if isinstance(rec, dict) else rec
        dec = len(txt.split(".")[1]) if "." in txt else 0
        want = round(val, dec)
        got = float(txt)
        signless = 'data-abs="1"' in attrs or not txt.startswith("-")
        ok = abs(got - want) < 1e-9 or (signless and abs(abs(got) - abs(want)) < 1e-9)
        if not ok:
            print(f"MISMATCH {os.path.basename(page)}  {f}:{key}  shown {shown}  data {val} (rounds to {want})"); bad += 1
print(f"{n} tagged numbers checked, {bad} problem(s).")
sys.exit(1 if bad else 0)
