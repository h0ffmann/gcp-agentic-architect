#!/usr/bin/env python3
"""Repo smoke check: layout present, scripts pass --self-test, question banks parse.

Usage: smoke.py [--json] [--self-test]
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED = [
    "AGENTS.md", "README.md", "EXAM-BRIEF.md", "STUDY-CALENDAR.md", "STUDY-LOG.md", "gt.md",
    "justfile", "flake.nix", ".github/workflows/ci.yml",
    ".claude/settings.json", ".claude/hooks/guard-gcloud.sh",
    "course", "cases", "questions", "scripts", "marola", "publications",
]
LESSONS = 15
SECTIONS = {"1.1", "1.2", "2.1", "2.2", "3.1", "3.2", "3.3", "4.1", "4.2", "5.1", "5.2"}


def check_layout():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    lessons = sorted((ROOT / "course").glob("[0-9][0-9]-*.md"))
    if len(lessons) != LESSONS:
        missing.append(f"course/: expected {LESSONS} lessons, found {len(lessons)}")
    return missing


def check_banks():
    errors = []
    for bank in (ROOT / "questions").glob("*.jsonl"):
        for n, line in enumerate(bank.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                q = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"{bank.name}:{n}: {e}")
                continue
            if q.get("section") not in SECTIONS:
                errors.append(f"{bank.name}:{n}: unknown section {q.get('section')!r}")
    return errors


def check_scripts():
    errors = []
    for s in sorted((ROOT / "scripts").glob("*.py")):
        if s.name == "smoke.py":
            continue
        r = subprocess.run([sys.executable, str(s), "--self-test"], capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"{s.name}: self-test failed\n{r.stdout}{r.stderr}")
    return errors


def self_test():
    assert "3.1" in SECTIONS and "6.1" not in SECTIONS
    assert check_layout() == [], check_layout()
    print("smoke self-test ok")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    report = {"layout": check_layout(), "banks": check_banks(), "scripts": check_scripts()}
    ok = not any(report.values())
    if "--json" in argv:
        print(json.dumps({"ok": ok, **report}, indent=2))
    else:
        for k, v in report.items():
            print(f"{k}: {'ok' if not v else ''}")
            for e in v:
                print(f"  - {e}")
        print("smoke:", "ok" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
