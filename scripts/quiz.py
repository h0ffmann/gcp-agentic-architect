#!/usr/bin/env python3
"""Question-bank runner for the Agentic Architect lab. Stdlib only.

  quiz.py --lesson 02 [--count 20]      questions tagged with a lesson
  quiz.py --section 3 [--count 20]      a top-level section (1–5) or objective (3.1)
  quiz.py --mock 1 --minutes 120        timed run of questions/mock-1.jsonl
  quiz.py --weak [--count 20]           Leitner: lowest boxes first, then due
  quiz.py --stats [--json]              accuracy per objective, weighted predicted score
  quiz.py --build-mock 1 [--size 60]    sample a weighted, disjoint mock from bank.jsonl
  quiz.py --export-anki                 questions/cards/bank.tsv (front TAB back)
  quiz.py --validate                    schema check of every bank, exit 1 on error
  quiz.py --self-test

Answers are read from stdin one per line (A, B, C, D, or "A,C" for multi-select), so a session
can be piped for testing. History goes to .tmp/quiz-history.jsonl, boxes to .tmp/leitner.json.
"""
import argparse
import datetime as dt
import json
import pathlib
import random
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
QDIR = ROOT / "questions"
TMP = ROOT / ".tmp"
HISTORY = TMP / "quiz-history.jsonl"
LEITNER = TMP / "leitner.json"

OBJECTIVES = ["1.1", "1.2", "2.1", "2.2", "3.1", "3.2", "3.3", "4.1", "4.2", "5.1", "5.2"]
WEIGHTS = {"1": 13, "2": 17, "3": 33, "4": 22, "5": 15}
BOX_DAYS = {1: 0, 2: 1, 3: 3, 4: 7, 5: 14}
REQUIRED = ("id", "section", "lesson", "stem", "options", "answer", "rationale",
            "difficulty", "source_url", "verified", "tags")


def validate(q, where=""):
    errs = []
    for k in REQUIRED:
        if k not in q:
            errs.append(f"missing {k}")
    if errs:
        return [f"{where}: {e}" for e in errs]
    if q["section"] not in OBJECTIVES:
        errs.append(f"unknown section {q['section']!r}")
    opts = q["options"]
    if not isinstance(opts, dict) or not (2 <= len(opts) <= 6):
        errs.append("options must be a dict of 2–6 entries")
    answers = q["answer"] if isinstance(q["answer"], list) else [q["answer"]]
    for a in answers:
        if a not in opts:
            errs.append(f"answer {a!r} not in options")
    if set(q["rationale"]) != set(opts):
        errs.append("rationale keys must match options")
    if q["verified"] not in ("v", "⚠"):
        errs.append("verified must be 'v' or '⚠'")
    if not isinstance(q["difficulty"], int) or not 1 <= q["difficulty"] <= 3:
        errs.append("difficulty must be 1..3")
    if not str(q["source_url"]).startswith("http"):
        errs.append("source_url must be a URL")
    return [f"{where}: {e}" for e in errs]


def load(path):
    qs, errs = [], []
    if not path.exists():
        return qs, [f"{path.name}: not found"]
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            q = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"{path.name}:{n}: {e}")
            continue
        errs += validate(q, f"{path.name}:{n}")
        qs.append(q)
    ids = [q["id"] for q in qs]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errs.append(f"{path.name}: duplicate ids {sorted(dupes)}")
    return qs, errs


def load_bank():
    qs, errs = load(QDIR / "bank.jsonl")
    if errs:
        sys.exit("\n".join(errs))
    return qs


def load_history():
    if not HISTORY.exists():
        return []
    return [json.loads(x) for x in HISTORY.read_text().splitlines() if x.strip()]


def load_boxes():
    return json.loads(LEITNER.read_text()) if LEITNER.exists() else {}


def save_boxes(boxes):
    TMP.mkdir(exist_ok=True)
    LEITNER.write_text(json.dumps(boxes, indent=1, sort_keys=True))


def record(qid, correct, mode, boxes, persist=True):
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    if persist:
        TMP.mkdir(exist_ok=True)
        with HISTORY.open("a") as f:
            f.write(json.dumps({"ts": now, "id": qid, "correct": correct, "mode": mode}) + "\n")
    cur = boxes.get(qid, {"box": 1, "last": now})
    cur["box"] = min(5, cur["box"] + 1) if correct else 1
    cur["last"] = now
    boxes[qid] = cur


def is_due(entry, now):
    last = dt.datetime.fromisoformat(entry["last"])
    return (now - last).days >= BOX_DAYS[entry["box"]]


def pick_weak(qs, boxes, count):
    now = dt.datetime.now(dt.timezone.utc)
    unseen = [q for q in qs if q["id"] not in boxes]
    seen = [q for q in qs if q["id"] in boxes]
    seen.sort(key=lambda q: (boxes[q["id"]]["box"], boxes[q["id"]]["last"]))
    due = [q for q in seen if is_due(boxes[q["id"]], now)]
    order = due + unseen + [q for q in seen if q not in due]
    return order[:count]


def parse_answer(raw):
    return sorted(a.strip().upper() for a in raw.replace(" ", ",").split(",") if a.strip())


def correct_set(q):
    a = q["answer"]
    return sorted(a if isinstance(a, list) else [a])


def run(qs, mode, minutes=None, boxes=None, out=sys.stdout, inp=sys.stdin, persist=True):
    boxes = boxes if boxes is not None else load_boxes()
    deadline = time.monotonic() + minutes * 60 if minutes else None
    score, results = 0, []
    for i, q in enumerate(qs, 1):
        if deadline and time.monotonic() > deadline:
            out.write(f"\nTime is up after {i - 1} questions.\n")
            break
        multi = isinstance(q["answer"], list)
        out.write(f"\n[{i}/{len(qs)}] ({q['section']}) {q['stem']}\n")
        for k in sorted(q["options"]):
            out.write(f"  {k}. {q['options'][k]}\n")
        out.write("select all that apply > " if multi else "answer > ")
        out.flush()
        raw = inp.readline()
        if not raw:
            out.write("\n(no more input)\n")
            break
        given = parse_answer(raw)
        ok = given == correct_set(q)
        score += ok
        results.append((q, ok))
        record(q["id"], ok, mode, boxes, persist)
        out.write(("correct" if ok else f"wrong — answer {','.join(correct_set(q))}") + "\n")
        for k in sorted(q["options"]):
            mark = "✓" if k in correct_set(q) else "✗"
            out.write(f"  {mark} {k}: {q['rationale'][k]}\n")
        if q["verified"] != "v":
            out.write(f"  ⚠ unverified — {q['source_url']}\n")
    if persist:
        save_boxes(boxes)
    n = len(results)
    if n:
        out.write(f"\nScore {score}/{n} = {100 * score // n}%\n")
    return score, n


def stats(qs, history, as_json=False, out=sys.stdout):
    by_id = {q["id"]: q for q in qs}
    latest = {}
    for h in history:
        latest[h["id"]] = h["correct"]
    acc = {o: [0, 0] for o in OBJECTIVES}
    for qid, ok in latest.items():
        q = by_id.get(qid)
        if q:
            acc[q["section"]][1] += 1
            acc[q["section"]][0] += ok
    per_obj = {o: (a / n if n else None) for o, (a, n) in acc.items()}
    per_sec = {}
    for s in WEIGHTS:
        objs = [o for o in OBJECTIVES if o.startswith(s)]
        tot = sum(acc[o][1] for o in objs)
        per_sec[s] = sum(acc[o][0] for o in objs) / tot if tot else None
    covered = [s for s in WEIGHTS if per_sec[s] is not None]
    wsum = sum(WEIGHTS[s] for s in covered)
    predicted = sum(WEIGHTS[s] * per_sec[s] for s in covered) / wsum if wsum else None
    counts = {s: sum(1 for q in qs if q["section"].startswith(s)) for s in WEIGHTS}
    total = len(qs)
    weakest = sorted((o for o in OBJECTIVES if per_obj[o] is not None), key=lambda o: per_obj[o])[:3]
    rep = {"answered": len(latest), "bank": total, "per_objective": per_obj, "per_section": per_sec,
           "predicted": predicted, "weakest": weakest, "coverage_gap": {
               s: {"have": counts[s], "target_share": WEIGHTS[s],
                   "actual_share": round(100 * counts[s] / total, 1) if total else 0} for s in WEIGHTS}}
    if as_json:
        out.write(json.dumps(rep, indent=2) + "\n")
        return rep
    out.write(f"bank {total} questions, {len(latest)} answered at least once\n")
    for o in OBJECTIVES:
        a, n = acc[o]
        out.write(f"  {o}  {'--' if not n else f'{100 * a // n:3d}%'}  ({n} answered)\n")
    for s in WEIGHTS:
        out.write(f"  section {s} ({WEIGHTS[s]:2d}%): {'--' if per_sec[s] is None else f'{100 * per_sec[s]:.0f}%'}"
                  f"   bank share {rep['coverage_gap'][s]['actual_share']}%\n")
    out.write("predicted (weighted over answered sections): " +
              ("--" if predicted is None else f"{100 * predicted:.0f}%") + "\n")
    if weakest:
        out.write("weakest objectives: " + ", ".join(weakest) + "\n")
    return rep


def build_mock(qs, n, size=60, seed=None):
    used = set()
    for p in QDIR.glob("mock-*.jsonl"):
        if p.name != f"mock-{n}.jsonl":
            used |= {q["id"] for q in load(p)[0]}
    pool = [q for q in qs if q["id"] not in used]
    rnd = random.Random(seed if seed is not None else n)
    quota = {s: round(size * WEIGHTS[s] / 100) for s in WEIGHTS}
    drift = size - sum(quota.values())
    quota["3"] += drift
    chosen = []
    for s, k in quota.items():
        cand = [q for q in pool if q["section"].startswith(s)]
        if len(cand) < k:
            raise SystemExit(f"section {s}: need {k} unused questions, have {len(cand)}")
        chosen += rnd.sample(cand, k)
    rnd.shuffle(chosen)
    return chosen


def export_anki(qs, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for q in qs:
            front = q["stem"] + " " + " ".join(f"({k}) {v}" for k, v in sorted(q["options"].items()))
            back = "Answer " + ",".join(correct_set(q)) + ". " + q["rationale"][correct_set(q)[0]]
            f.write(front.replace("\t", " ") + "\t" + back.replace("\t", " ") + "\n")
    return len(qs)


def select(qs, lesson=None, section=None):
    if lesson:
        qs = [q for q in qs if q["lesson"] == lesson.zfill(2)]
    if section:
        qs = [q for q in qs if q["section"] == section or q["section"].startswith(section + ".")]
    return qs


def self_test():
    import io
    q = {"id": "t1", "section": "3.1", "lesson": "02", "stem": "s", "options": {"A": "a", "B": "b"},
         "answer": "B", "rationale": {"A": "x", "B": "y"}, "difficulty": 1,
         "source_url": "https://x", "verified": "v", "tags": []}
    assert validate(q) == []
    bad = dict(q, section="6.1", answer="C", verified="maybe")
    assert len(validate(bad)) == 3, validate(bad)
    assert parse_answer(" b, a ") == ["A", "B"]
    boxes = {}
    out = io.StringIO()
    run([q, dict(q, id="t2")], "test", boxes=boxes, out=out, inp=io.StringIO("B\nA\n"), persist=False)
    assert boxes["t1"]["box"] == 2 and boxes["t2"]["box"] == 1
    assert "Score 1/2" in out.getvalue()
    hist = [{"ts": "x", "id": "t1", "correct": True}, {"ts": "x", "id": "t2", "correct": False}]
    rep = stats([q, dict(q, id="t2")], hist, as_json=True, out=io.StringIO())
    assert rep["per_objective"]["3.1"] == 0.5 and abs(rep["predicted"] - 0.5) < 1e-9
    pool = [dict(q, id=f"p{i}", section=s) for i, s in enumerate(OBJECTIVES * 12)]
    m = build_mock(pool, 9, size=60, seed=1)
    assert len(m) == 60 and sum(x["section"].startswith("3") for x in m) == 20
    try:
        build_mock(pool[:5], 9, size=60)
        raise AssertionError("should refuse small pool")
    except SystemExit:
        pass
    print("quiz self-test ok")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lesson")
    ap.add_argument("--section")
    ap.add_argument("--mock", type=int)
    ap.add_argument("--minutes", type=int)
    ap.add_argument("--weak", action="store_true")
    ap.add_argument("--count", type=int, default=20)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--build-mock", type=int)
    ap.add_argument("--size", type=int, default=60)
    ap.add_argument("--export-anki", action="store_true")
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--seed", type=int)
    a = ap.parse_args(argv)

    if a.self_test:
        self_test()
        return 0
    if a.validate:
        errs = []
        for p in sorted(QDIR.glob("*.jsonl")):
            errs += load(p)[1]
        print("\n".join(errs) if errs else "banks ok")
        return 1 if errs else 0
    qs = load_bank()
    if a.stats:
        stats(qs, load_history(), a.json)
        return 0
    if a.build_mock:
        chosen = build_mock(qs, a.build_mock, a.size, a.seed)
        path = QDIR / f"mock-{a.build_mock}.jsonl"
        path.write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in chosen))
        print(f"wrote {path.relative_to(ROOT)} ({len(chosen)} questions)")
        return 0
    if a.export_anki:
        n = export_anki(qs, QDIR / "cards" / "bank.tsv")
        print(f"wrote questions/cards/bank.tsv ({n} cards)")
        return 0
    if a.mock:
        mq, errs = load(QDIR / f"mock-{a.mock}.jsonl")
        if errs:
            sys.exit("\n".join(errs))
        run(mq, f"mock-{a.mock}", a.minutes)
        return 0
    if a.weak:
        run(pick_weak(qs, load_boxes(), a.count), "weak")
        return 0
    sel = select(qs, a.lesson, a.section)
    if not sel:
        sys.exit("no questions match")
    rnd = random.Random(a.seed)
    rnd.shuffle(sel)
    run(sel[:a.count], f"lesson-{a.lesson}" if a.lesson else f"section-{a.section}", a.minutes)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
