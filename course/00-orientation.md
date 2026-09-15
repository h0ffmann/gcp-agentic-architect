# 00 — Orientation: how this exam is written and how to answer it

**Exam objectives:** all · section weight —. Quiz: `just quiz --lesson 00`. Case: `just case 00`.

## On the exam

- Google Professional exams are **scenario elimination**: a company, a constraint, "what should you do?", one best answer. Two options are usually wrong products; one is a right product used wrongly; one is right. Find the constraint word first (cost, least ops, data residency, latency, audit, no code).
- **Newer names win.** If two options describe the same thing under old and new names (Agent Engine / Agent Runtime, Vertex AI Search / Agent Search, Vector Search 2.0 / Agent Retrieval), the exam wants the current name.
- **Managed beats custom** unless the scenario says otherwise (custom container, sidecar, GPU, on-prem). "Least operational effort" → Agent Runtime; "existing container pipeline" → Cloud Run; "node-level control" → GKE.
- **Policy beats prompt.** Any option that enforces security through the system prompt is wrong when a policy product exists (Agent Identity/PAB, Agent Gateway, Model Armor, HITL).
- **Protocol split**: MCP = agent ↔ tools/servers; A2A = agent ↔ agent.
- 3 hours, beta-length pool. Budget ~2 min per question, flag and move on, never leave blanks (no negative marking on Google exams — verify in the Pearson instructions on the day).

## Read (fetched 2026-09-15)

- EXAM-BRIEF.md (this repo) — the guide as a checklist and the 28 tools.
- [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) — the four pillars; every product on the exam is placed here.
- [How beta exams work](https://support.google.com/cloud-certification/answer/9750304).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Exam | MCQ 3 h, Pearson, Sept 8–30; labs < 5 h on Google Skills after passing, late Oct–Dec | $120 beta; 1-year validity | (v) FAQ |
| Weights | 13 / 17 / 33 / 22 / 15 | Section 3 first | (v) guide |

## Case — `cases/—`

No case for the orientation; run `just smoke` instead.

## marola port

Not applicable. The orientation for marola is `marola/AGENTIC-ARCHITECT-MAPPING.md`.

## Quiz

`just quiz --lesson 00` — questions tagged `lesson: "00"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/00.tsv` (front TAB back). Import into Anki as basic cards.
