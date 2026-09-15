# STUDY-CALENDAR — 15 days to the MCQ (Sept 16 → Sept 30, 2026)

Full time. Weights 13/17/33/22/15 drive the order: Section 3 first, Section 1 last. The hands-on
labs are **not** in this window (they unlock only after passing the MCQ, late October), so every
day is multiple-choice preparation. Console time is for recognising products, not drills.

Daily shape (≈ 8 h): reading block · runnable case · 30-question quiz · 20-min `just quiz --weak`
review · one line in `STUDY-LOG.md`. No new material after D14.

| Day | Date | Focus | Sessions ([prompt series](docs/PROMPT-SERIES_202609.md)) | Done when |
|---|---|---|---|---|
| D1 | Tue 16 | Orientation, EXAM-BRIEF, toolchain, AWESOME list, question schema + 150 seed | Prompt 5 → 1 → 3 → 2 (outline only) | `just smoke` green; `just quiz --section 3` runs |
| D2 | Wed 17 | 3.1a — model selection, ADK fundamentals | Prompt 2: lessons 01, 02 | cases 01–02 run |
| D3 | Thu 18 | 3.1b — sessions, Memory Bank, Agents CLI skills | Prompt 2: lesson 03 | case 03 runs |
| D4 | Fri 19 | 3.2a — RAG, Vector Search, Agent Retrieval, reranking | Prompt 2: lesson 04 | case 04 runs |
| D5 | Sat 20 | 3.2b / 3.3 — MCP, Agent Registry, Identity; A2A, multi-agent, Agent Runtime | Prompt 2: lessons 05, 06 | cases 05–06 run |
| D6 | Sun 21 | 4.1 — evaluation: evalsets, Gen AI eval service, autoraters | Prompt 2: lesson 07 | case 07 runs |
| D7 | Mon 22 | 4.2 — Agent Runtime vs Cloud Run vs GKE, troubleshooting, observability; **console recon** (read-only: Agent Platform pages, Registry, Gateway screens) | Prompt 2: lessons 08, 09 | cases 08–09 run; recon notes in lesson 08 |
| D8 | Tue 23 | 5.1 / 5.2 — OAuth via Auth Manager, PAB, Agent Gateway, Model Armor, SDP, HITL | Prompt 2: lesson 10 | case 10 runs |
| D9 | Wed 24 | 2.1 / 2.2 — Antigravity, Claude Code on GCP, MCP config, sandboxes, Agents CLI | Prompt 2: lesson 11 | case 11 runs |
| D10 | Thu 25 | 1.1 / 1.2 — Gemini Enterprise, Agent Designer, CX Agent Studio, Agent Search, multimodal ingestion | Prompt 2: lesson 12 | quiz section 1 ≥ 85% |
| D11 | Fri 26 | **Mock exam 1** (60 q, 120 min, timed) then weak-spot review by objective | Prompt 2: lesson 13 (`--build-mock 1`) | `just quiz --stats` predicted ≥ 80% |
| D12 | Sat 27 | Section-3 and Section-4 second pass; every ⚠ in EXAM-BRIEF resolved or accepted | targeted `--weak` sessions | no unread ⚠ in Sections 3–4 |
| D13 | Sun 28 | **marola port** as active recall — MIP-0057 + mapping doc | Prompt 4a, 4b | marola `just build test quality` green, no GCP env |
| D14 | Mon 29 | **Mock exam 2**, flashcards, publications build, zip, first push | Prompt 2: lesson 14; Prompt 6 | tag `v0.1-beta-exam` |
| D15 | Tue 30 | Travel. Flashcards only. **Exam.** | — | — |

## After the MCQ

| Block | When | What |
|---|---|---|
| Result | late October | `publications/post-exam.md` filled (no question content — NDA) |
| Lab prep | on the results email, ≤ 2 weeks before the lab window | Google Skills learning-path labs mapped in AWESOME §2; the `cases/` `--gcp` paths; marola `gcp/` module as rehearsal; credits + ceiling set in EXAM-BRIEF |
| Labs | late Oct – Dec, < 5 h | on Google Skills |

## Rules

- A lesson slipping does not move the mock days; it moves into D12.
- Section 1 never borrows time from Section 3.
- `STUDY-LOG.md` gets its line before the day ends, even if it says "0 h".
