"""Entry for make.fun bounty "Everyday Things, Two Lines, Longer Run".

Writes a two-line text to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output``
when the variable is unset, matching the grader container). Line 1
explains one everyday thing -- a traffic jam -- to a 10-year-old in a
single vivid sentence built on an analogy; line 2 says in one sentence
why the analogy works: what it maps and what it leaves out.

The text is a constant, so the program is deterministic: every run
writes exactly the same bytes. Before writing, the program checks the
text against the bounty gate (UTF-8 text of 1 to 400 characters, not
only white space, exactly two lines) and fails loudly if it ever
drifts out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "A traffic jam is a thousand people in cars, all trying to be first in "
    "a line nobody can see the front of.\n"
    "The line explains why you shuffle forward only when the car in front "
    "does and why one stop holds up everyone behind, but it leaves out that "
    "a real line ends at a counter where you get served and can step out "
    "any time, while a jam has no counter and no easy way out."
)

MAX_CHARS = 400


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("error: the entry is empty", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 2 or any(not ln.strip() for ln in lines):
        print("error: the entry must be exactly two non-empty lines", file=sys.stderr)
        return 1
    if "\r" in text:
        print("error: the entry must use plain newline line endings", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the entry is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(text, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != text:
        print("error: written text differs from the entry", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
