# 02 — ADK fundamentals: agents, tools, runners, local run

**Exam objectives:** 3.1 · section weight 33%. Quiz: `just quiz --lesson 02`. Case: `just case 02`.

## On the exam

- ADK vocabulary the exam uses: **Agent** (instruction + model + tools), **tools** (Python functions, MCP tools, built-ins), **Runner** (drives a session, yields **events**), **session service** (in-memory locally, Vertex/Agent Runtime in production).
- Local loop: `adk web <agents_folder>` opens the dev UI on localhost:8000 with an **Eval tab**; `adk run` for the CLI. Nothing is billed until you deploy or call a hosted model.
- Deploy paths: `adk deploy docker`, `adk deploy cloud_run`, `adk deploy agent_engine` (Agent Runtime). The exam pairs each with a requirement (see lesson 08).
- ADK is **model-agnostic** and open source; the exam says "open-source libraries (e.g., ADK)". A distractor will propose a proprietary console product for code-first work.
- Multi-agent primitives (lesson 06): `SequentialAgent`, `ParallelAgent`, `LoopAgent`, LLM-driven transfer between sub-agents.

## Read (fetched 2026-09-15)

- [adk-docs](https://google.github.io/adk-docs/) · [adk-python README](https://github.com/google/adk-python) — commands and deploy targets (v).
- [Memory Bank quickstart with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/adk-quickstart) — shows the local-then-Runtime path (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| ADK | Open-source, code-first, model-agnostic framework (Python, Java) for agents and orchestration | `pip install google-adk`; `adk web` on :8000 | (v) adk-python |
| adk deploy | `docker --with_ui`, `cloud_run --with_ui`, `agent_engine` | env via `--env` or `.env` | (v) adk-python README |

## Case — `cases/02-adk-fundamentals`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola's Kyo pipeline is already agent = instruction + tools + runner. The MIP adds a `Session` trait so events are recorded the ADK way (author, function_call, function_response), which lessons 03 and 07 need. Local impl: `FileSessionStore` under `.tmp/`.

## Quiz

`just quiz --lesson 02` — questions tagged `lesson: "02"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/02.tsv` (front TAB back). Import into Anki as basic cards.
