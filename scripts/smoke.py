#!/usr/bin/env python3
"""Repo smoke check: layout present, scripts pass --self-test, question banks parse,
interview questions keep their skeleton and each has a rubric in the design-reviewer agent.

Usage: smoke.py [--json] [--self-test]
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED = [
    "AGENTS.md", "README.md", "DESCRIPTION.md", "CONTRIBUTING.md", "LICENSE",
    "EXAM-BRIEF.md", "STUDY-CALENDAR.md", "STUDY-LOG.md", "docs/PROMPT-SERIES_202609.md",
    "justfile", "flake.nix", "flake.lock", ".ai-jail", ".github/workflows/ci.yml", ".github/workflows/pubs.yml",
    ".claude/settings.json", ".claude/hooks/guard-gcloud.sh",
    "course", "cases", "questions", "scripts", "marola", "publications/book/defaults.yaml",
    "interviews/README.md", ".claude/agents/design-reviewer.md", "past-problems/TEMPLATE.md",
]
LESSONS = 15
SECTIONS = {"1.1", "1.2", "2.1", "2.2", "3.1", "3.2", "3.3", "4.1", "4.2", "5.1", "5.2"}
INTERVIEW_HEADINGS = ["## Setting", "## The system as found", "## Constraints", "## Part A",
                      "## Part B", "## Part C", "## Related lessons"]


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
    # quiz.py owns the schema and the quality lint (stems, rationales, answer-letter and
    # option-length balance); run it here so one command covers the banks.
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "quiz.py"), "--validate"],
                       capture_output=True, text=True, check=False)
    if r.returncode != 0:
        errors += [line for line in (r.stdout + r.stderr).splitlines() if line.strip()]
    return errors


def check_interviews():
    """Every question has the fixed skeleton and a rubric in the reviewer agent, and vice versa."""
    errors = []
    questions = sorted((ROOT / "interviews").glob("[0-9][0-9]-*.md"))
    agent = (ROOT / ".claude/agents/design-reviewer.md").read_text()
    rubrics = set(re.findall(r"^## Rubric (\d\d) ", agent, re.M))
    for q in questions:
        text = q.read_text()
        for h in INTERVIEW_HEADINGS:
            if not re.search(rf"^{re.escape(h)}\b", text, re.M):
                errors.append(f"interviews/{q.name}: missing '{h}'")
        if re.search(r"^## (Answer|Solution|Rubric|Hints?)\b", text, re.M | re.I):
            errors.append(f"interviews/{q.name}: answers do not belong in a question file")
        if q.name[:2] not in rubrics:
            errors.append(f"interviews/{q.name}: no '## Rubric {q.name[:2]}' in design-reviewer.md")
    for nn in sorted(rubrics - {q.name[:2] for q in questions}):
        errors.append(f"design-reviewer.md: rubric {nn} has no interviews/{nn}-*.md")
    # past-problems/ is private by construction: the ignore rule, not discipline, keeps it off
    # GitHub. Checked literally so it also holds in the nix sandbox, where there is no .git.
    ignored = (ROOT / ".gitignore").read_text().splitlines()
    if "past-problems/*" not in ignored:
        errors.append(".gitignore: 'past-problems/*' rule missing — private designs would be pushed")
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
    assert check_interviews() == [], check_interviews()
    print("smoke self-test ok")


def main(argv):
    if "--self-test" in argv:
        self_test()
        return 0
    report = {"layout": check_layout(), "banks": check_banks(), "interviews": check_interviews(),
              "scripts": check_scripts()}
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
