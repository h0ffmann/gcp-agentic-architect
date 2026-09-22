# interviews/ — system-design interview questions with a hidden-rubric reviewer

Date: 2026-09-22. Status: approved in chat, implemented in the same PR.

## Why

Two agentic-RAG system-design interviews in the same week (healthcare consulting, both) covered
ground the MCQ bank does not: a whiteboard-style "here is a bad RAG, fix it" with follow-ups on
access control, PHI, loop termination and infra choice. The repo should hold that practice in the
same shape as everything else — local, sourced, checked by `just smoke` — without spoiling the
answers.

## What

- `interviews/NN-*.md` — five questions with a fixed skeleton: Setting · The system as found ·
  Constraints · Part A (improve without changing infra) · Part B (change infra) · Part C (FOSS
  stack vs Google Cloud Agent Runtime stack, an empty table) · Related lessons. No hints, no
  model answer. Product names in Part C headers carry `(v)`/`⚠` and a fetched URL.
- `interviews/README.md` — how to run one (45 min, write `interviews/answers/NN-YYYYMMDD.md`,
  ask for the `design-reviewer` agent). Explicitly off the study calendar.
- `.claude/agents/design-reviewer.md` — Claude Code subagent. Read-only tools. Holds every
  rubric. Scores 1–5 on seven axes, prints three strengths, three gaps phrased as the follow-up
  an interviewer would ask, a hire verdict, and what to redo. Never prints a rubric wholesale.
- `scripts/smoke.py` — `interviews` added to the layout; new check: every `interviews/NN-*.md`
  has a `## Rubric NN` block in the agent file, and vice versa.

## Not in scope

An ADK/Ollama reviewer case; a JSONL schema or runner; adding anything to `STUDY-CALENDAR.md`;
real interview content beyond what the candidate volunteered (anonymised: no names, no firms).
