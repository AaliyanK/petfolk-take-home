#!/usr/bin/env python3
"""
verify_quotes.py

Checks that every verbatim span in a journey HTML file (wrapped in <span class="q">...</span>)
actually appears in the pet's source record. This is our own copy of the string match Petfolk runs.

Two checks per span:
  raw   : the span must appear exactly, character for character, in the source.
  loose : the span must appear when runs of whitespace (including newlines) are collapsed to
          one space on both sides. This is the assumption in ground-rules.md.

Usage:
  python verify_quotes.py <journey.html> <source.txt>
  python verify_quotes.py --all        # every journey in question-1/journeys against records/

Exit code 0 if every span passes at least the loose check, 1 otherwise.
"""
import sys, re, html, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
JOURNEYS = REPO / "question-1" / "journeys"
RECORDS = REPO / "records"

# journey file stem -> source record file
MAP = {
    "ikko": "z1_MRS-45.txt",
    "ikko3": "z2_16MRS-16.txt",
    "quorra": "z2_2-MRS-2.txt",
    "pobble": "z2_MRS.txt",
    "quorra2": "dl_MRS-_1_.txt",
}

SPAN_RE = re.compile(r'<span class="q">(.*?)</span>', re.DOTALL)

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def spans_from_html(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    out = []
    for m in SPAN_RE.finditer(text):
        raw = html.unescape(m.group(1))
        raw = re.sub(r"<[^>]+>", "", raw)   # drop any nested tags
        out.append(raw.strip())
    return out

def check(journey: pathlib.Path, source: pathlib.Path) -> bool:
    src = source.read_text(encoding="utf-8")
    src_loose = norm(src)
    spans = spans_from_html(journey)
    ok = True
    print(f"\n{journey.name}  vs  {source.name}   ({len(spans)} quoted spans)")
    for s in spans:
        raw_hit = s in src
        loose_hit = norm(s) in src_loose
        if raw_hit:
            tag = "raw  "
        elif loose_hit:
            tag = "loose"
        else:
            tag = "MISS "
            ok = False
        print(f"  [{tag}] {s[:96]}")
    return ok

def main():
    args = sys.argv[1:]
    all_ok = True
    if args == ["--all"]:
        for stem, rec in MAP.items():
            j = JOURNEYS / f"{stem}.html"
            r = RECORDS / rec
            if j.exists() and r.exists():
                all_ok &= check(j, r)
            elif j.exists():
                print(f"\n{j.name}: source {rec} not found in records/, skipped")
    elif len(args) == 2:
        all_ok = check(pathlib.Path(args[0]), pathlib.Path(args[1]))
    else:
        print(__doc__)
        sys.exit(2)
    print("\nRESULT:", "all spans verified" if all_ok else "FAILURES above")
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
