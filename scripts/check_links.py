"""Check internal links, anchors, footnotes, glossary terms and data files.

  - every relative href points to an existing file, and #anchors exist on the target page
  - every footnote reference has a note, and every note is referenced
  - every <span class="term" data-term="k"> has a glossary entry
  - every data id used in WE.chart / WE.load calls has a data/js file
    python3 scripts/check_links.py
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = sorted(glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "chapters", "*.html")))
ids = {p: set(re.findall(r'\sid="([^"]+)"', open(p, encoding="utf-8").read())) for p in pages}
gloss = set(re.findall(r'^\s*"([a-z0-9-]+)":\s*\{', open(os.path.join(ROOT, "assets/js/glossary-data.js"), encoding="utf-8").read(), re.M))
# anchors generated at runtime
dynamic = {os.path.join(ROOT, "glossary.html"): gloss, os.path.join(ROOT, "index.html"): {"timeline"}}
bad = 0
def err(p, msg):
    global bad; bad += 1; print(f"{os.path.relpath(p, ROOT)}: {msg}")

for p in pages:
    src = open(p, encoding="utf-8").read()
    base = os.path.dirname(p)
    for h in re.findall(r'href="([^"]+)"', src):
        if re.match(r"(https?:|mailto:|\$\{|data:)", h):
            continue
        path, _, frag = h.partition("#")
        target = os.path.normpath(os.path.join(base, path)) if path else p
        if not os.path.exists(target):
            err(p, f"missing file {h}"); continue
        if frag and target.endswith(".html") and frag not in ids.get(target, set()) | dynamic.get(target, set()):
            err(p, f"missing anchor {h}")
    refs = set(re.findall(r'<sup class="fn"><a href="#(fn\d+)"', src))
    notes = set(re.findall(r'<li id="(fn\d+)"', src))
    for r in refs - notes: err(p, f"footnote {r} has no note")
    for r in notes - refs:
        if not re.match(r'\s*Data\.', src.split(f'<li id="{r}">')[1]):
            err(p, f"note {r} is never referenced")
    for t in re.findall(r'data-term="([^"]+)"', src):
        if t not in gloss: err(p, f"glossary term '{t}' not defined")
    for d in set(re.findall(r'(?:data|names):\s*"([a-z_]+/[A-Za-z0-9_]+)"', src)) | set(x for grp in re.findall(r'WE\.load\(\[([^\]]+)\]', src) for x in re.findall(r'"([^"]+)"', grp)):
        if d != "__inline" and not os.path.exists(os.path.join(ROOT, "data", "js", d + ".js")):
            err(p, f"data file data/js/{d}.js missing")
print(f"{len(pages)} pages checked, {bad} problem(s).")
sys.exit(1 if bad else 0)
