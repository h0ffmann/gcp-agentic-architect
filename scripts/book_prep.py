#!/usr/bin/env python3
"""book_prep — copy course/NN-*.md into a build dir with stable chapter ids and in-book links.

    python3 scripts/book_prep.py course build/book
    python3 scripts/book_prep.py --self-test

- the first `# NN — Title` heading of NN-slug.md becomes `# Title {#ch-slug}` (the book numbers chapters)
- `](NN-slug.md)`   -> `](#ch-slug)`      (link to the chapter)
- `](NN-slug.md#a)` -> `](#a)`            (pandoc's auto id of that heading)
- `](../path)` and other repo-relative links -> the GitHub URL, so they work in a PDF
Exit 1 on a link to a lesson file that does not exist. Ported from h0ffmann/ww3-gpu.
"""
import pathlib
import re
import sys
import tempfile

REPO = "https://github.com/h0ffmann/gcp-agentic-architect/blob/main/"
LESSON = re.compile(r"\]\((?:\./)?(\d{2}-[a-z0-9-]+)\.md(#[A-Za-z0-9_-]+)?\)")
RELATIVE = re.compile(r"\]\(\.\./([^)#\s]+)(#[^)\s]*)?\)")


def slug(stem: str) -> str:
    return stem[3:]  # drop "NN-"


def prep(course: pathlib.Path, out: pathlib.Path) -> int:
    chapters = sorted(course.glob("[0-9][0-9]-*.md"))
    known = {p.stem for p in chapters}
    out.mkdir(parents=True, exist_ok=True)
    bad = []
    for path in chapters:
        text = path.read_text(encoding="utf-8")

        def fix(m: re.Match, path=path) -> str:
            target, anchor = m.group(1), m.group(2)
            if target not in known:
                bad.append(f"{path.name}: link to {target}.md, which is not a lesson")
                return m.group(0)
            return f"](#{anchor[1:]})" if anchor else f"](#ch-{slug(target)})"

        text = LESSON.sub(fix, text)
        text = RELATIVE.sub(lambda m: f"]({REPO}{m.group(1)}{m.group(2) or ''})", text)
        text = re.sub(r"^# (?:\d{2} — )?(.+?)\s*$", rf"# \1 {{#ch-{slug(path.stem)}}}", text, count=1, flags=re.M)
        (out / path.name).write_text(text, encoding="utf-8")
    for b in bad:
        print(f"book_prep: {b}", file=sys.stderr)
    return 1 if bad else 0


def self_test() -> None:
    src = pathlib.Path(tempfile.mkdtemp())
    out = pathlib.Path(tempfile.mkdtemp())
    (src / "00-orientation.md").write_text(
        "# 00 — Orientation\n\nSee [grids](03-grids.md), [dx](03-grids.md#resolution), [case](../cases/03-x/case.py).\n"
    )
    (src / "03-grids.md").write_text("# Grids\n\n## Resolution\n")
    (src / "README.md").write_text("# not a chapter\n")
    assert prep(src, out) == 0
    assert sorted(x.name for x in out.iterdir()) == ["00-orientation.md", "03-grids.md"]
    text = (out / "00-orientation.md").read_text()
    assert "# Orientation {#ch-orientation}" in text, text
    assert "[grids](#ch-grids)" in text, text
    assert "[dx](#resolution)" in text, text
    assert f"[case]({REPO}cases/03-x/case.py)" in text, text
    (src / "05-dangling.md").write_text("# D\n\n[x](09-missing.md)\n")
    assert prep(src, pathlib.Path(tempfile.mkdtemp())) == 1
    print("book_prep self-test ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        sys.exit(0)
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(prep(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])))
