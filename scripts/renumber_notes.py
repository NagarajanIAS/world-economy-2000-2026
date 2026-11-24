"""Renumber a chapter's footnotes in order of first reference.

References look like <sup class="fn"><a href="#fn7" id="r7b">7</a></sup>; notes are
<li id="fn7">…<a class="back" href="#r7">↩</a></li> inside <ol class="footnotes">.
Unreferenced notes (the general data note) go to the end; notes marked "(Reserved.)"
are dropped. Run after adding or moving footnotes:
    python3 scripts/renumber_notes.py chapters/phase-3.html
"""
import re, sys

path = sys.argv[1]
src = open(path, encoding="utf-8").read()
head, rest = src.split('<ol class="footnotes">', 1)
body, tail = rest.split("</ol>", 1)

items = re.findall(r'(<li id="fn(\d+)">.*?</li>)', body, re.S)
notes = {n: li for li, n in items}
order = []
for n in re.findall(r'<sup class="fn"><a href="#fn(\d+)"', head):
    if n not in order:
        order.append(n)
extra = [n for n in notes if n not in order and "(Reserved.)" not in notes[n]]
missing = [n for n in order if n not in notes]
if missing:
    sys.exit(f"references without notes: {missing}")
new = {old: str(i) for i, old in enumerate(order + extra, 1)}

def ref(m):
    old, rid = m.group(1), m.group(2)
    return f'<sup class="fn"><a href="#fn{new[old]}" id="r{new[old]}{rid}">{new[old]}</a></sup>'

head = re.sub(r'<sup class="fn"><a href="#fn(\d+)" id="r\d+([a-z]?)">\d+</a></sup>', ref, head)

first = {}
for n, rid in re.findall(r'<sup class="fn"><a href="#fn(\d+)" id="(r\d+[a-z]?)"', head):
    first.setdefault(n, rid)

def renote(old):
    li = notes[old]
    li = li.replace(f'<li id="fn{old}">', f'<li id="fn{new[old]}">', 1)
    target = first.get(new[old], "notes")          # back-link to the first reference
    li = re.sub(r'class="back" href="#r?\w+"', f'class="back" href="#{target}"', li)
    # theme chapters write the back-link without class="back"
    return re.sub(r'<a href="#(?:r\d+[a-z]?|notes)">↩</a>', f'<a href="#{target}">↩</a>', li)

body = "\n" + "\n".join(renote(o) for o in order + extra) + "\n"
open(path, "w", encoding="utf-8").write(head + '<ol class="footnotes">' + body + "</ol>" + tail)
print(f"{len(order)} referenced notes renumbered, {len(extra)} unreferenced kept at the end")
