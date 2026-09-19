# STUDY-GUIDE — how to work through the course, step by step

[`STUDY-CALENDAR.md`](STUDY-CALENDAR.md) says *when*; this file says *how*. Written 2026-09-19
(D4) with only [`EXAM-BRIEF.md`](EXAM-BRIEF.md) done, so it also carries the catch-up order.

## The loop, once per lesson

Lessons are ~40 lines; the time goes into the linked docs and the questions.

1. Read `course/NN-*.md`. "On the exam" is the tells and the distractors.
2. Read the docs under "Read". Resolve or accept each ⚠ in the lesson as you go.
3. `just case NN`, then read the case source (~40 lines of stdlib Python).
4. `just quiz --lesson NN`. Every wrong answer gets one line in the wrong-answer log (below).
5. `just quiz --weak` for 20 minutes.
6. Import `questions/cards/NN.tsv` into Anki.
7. One line in [`STUDY-LOG.md`](STUDY-LOG.md) before the day ends, even if it says "0 h".

## Catch-up order (Sept 19 → Sept 30)

Three days behind the calendar on Sept 19. Mock days do not move, so lessons double up until
Tuesday.

| Date | Lessons | Note |
|---|---|---|
| Sat 19 | 01 model selection · 02 ADK · 03 sessions/memory | 01 and 02 are light |
| Sun 20 | 04 RAG · 05 MCP/Registry/Identity | |
| Mon 21 | 06 multi-agent/A2A · 07 evaluation | |
| Tue 22 | 08 runtimes · 09 troubleshooting | back on calendar; console recon only if time allows |
| Wed 23 | 10 security | |
| Thu 24 | 11 coding agents | |
| Fri 25 | 12 low-code | gate: section 1 quiz ≥ 85% |
| Sat 26 | **Mock 1** — `just quiz --mock 1 --minutes 120` | gate: `just quiz --stats` predicted ≥ 80% |
| Sun 27 | Sections 3 and 4 second pass, `--weak` sessions | |
| Mon 28 | marola port | the slack day: first thing dropped if anything slips |
| Tue 29 | **Mock 2**, flashcards | no new material |
| Wed 30 | **Exam** | reread lesson 00 and the wrong-answer log |

## Personal notes — which lessons need them

The `.tsv` flashcards cover facts. Hand-written notes are for the questions where two options
both look plausible. One page per topic, a table of "X vs Y: which constraint word picks which",
written from memory after the quiz, in your own words.

Write notes:

| Source | The discrimination to write down |
|---|---|
| Lesson 00 + EXAM-BRIEF "In-scope tools" | Rename map, old → current name (Agent Engine → Agent Runtime, Vertex AI Search → Agent Search, Vector Search 2.0 → Agent Retrieval). The exam wants the current name. |
| Lesson 10 (46 questions, densest set) | Agent Gateway vs Agent Identity/PAB vs Model Armor vs Sensitive Data Protection vs HITL; floor settings vs templates; inspect vs block; Model Armor fails open; IAP in dry-run first. |
| Lessons 03, 04 (objectives 3.1, 3.2) | Session state vs Memory Bank; Agent Search vs Agent Retrieval vs reranking. |
| Lessons 05, 06 | MCP vs A2A; Registry vs Gateway vs Identity; the multi-agent patterns. |
| Lesson 08 | Agent Runtime vs Cloud Run vs GKE, keyed on "least ops", "existing container pipeline", "node-level control". |
| Lesson 07 | Evalsets vs Gen AI eval service vs autoraters; which metric fits which situation. |
| Lesson 12 (43 questions for a 13% section) | Agent Designer vs CX Agent Studio vs Gemini Enterprise vs "just use ADK". |

Skip notes:

- Lesson 00 — five rules; reread on exam morning.
- Lessons 01, 02 — flashcards plus running the cases are enough.
- Lesson 09 — learned by doing the trace-triage case and the quiz.
- Lesson 11 — if you already use a coding agent daily, note only the Google Cloud parts:
  Antigravity, Claude on Agent Platform, Agents CLI, sandboxes on GKE.

## Wrong-answer log

One running file, one line per missed question:

```
picked X · answer was Y · the tell I missed was Z
```

Reread it on Sept 29 and on exam morning. It is worth more than the per-lesson notes. No real
exam content goes in it, ever (NDA) — bank questions only.
