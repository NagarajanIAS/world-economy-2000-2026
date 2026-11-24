"""Build data/js/hand/*.js from the hand-entered files in data/hand/*.json.

Each hand file has rows read from a cited report page. A row may instead name a series
("from": "weo/NGDP_RPCH G001 2009"); its value is filled from data/clean at build time.
Series rows (with "series": {"key": [values]}) are copied as they are.
    python3 scripts/build_hand.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent


def lookup(ref):
    path, area, year = ref.split()
    d = json.loads((ROOT / "data/clean" / f"{path}.json").read_text())["data"][area]
    return round(dict((str(k), v) for k, v in d)[year], 2)


out = ROOT / "data/js/hand"; out.mkdir(parents=True, exist_ok=True)
for f in sorted((ROOT / "data/hand").glob("*.json")):
    h = json.loads(f.read_text())
    for r in h.get("rows", []):
        if r.get("from"):
            r["value"] = lookup(r["from"])
    s = json.dumps(h, ensure_ascii=False, separators=(",", ":"))
    (out / f"{f.stem}.js").write_text(f'WE.register("{h["id"]}",{s});\n', encoding="utf-8")
    print("built", f.stem)
