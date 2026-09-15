# 03 — Sessions, Memory Bank, managed sessions; Agents CLI skills

**Exam objectives:** 3.1 · section weight 33%. Quiz: `just quiz --lesson 03`. Case: `just case 03`.

## On the exam

- **Session** = one conversation's ordered events, scoped to a user id. **Memory Bank** = long-term facts *generated* from sessions (`GenerateMemories`) and fetched in later sessions, scoped by user (and optionally agent). The exam tests that you know which is which.
- Sessions and Memory Bank are Agent Runtime features (**Agent Platform Sessions / Memory Bank**); you can create a Runtime instance as a session store **without deploying code**.
- ADK wiring: `VertexAiSessionService` + a memory service; a callback such as `add_session_to_memory` triggers extraction at session end.
- Distractors: Firestore/Memorystore hand-rolled stores when "managed" is required; "bigger context window" as a substitute for cross-session memory.
- **Agents CLI**: scaffolds a project (`agents-cli-manifest.yaml`), installs skills into `~/.agents/skills` (Antigravity sees them), gives scaffold/eval/deploy skills and a Skill Registry skill; the guide names "plugins and agent vs human mode" — expect a question on human-in-the-loop vs autonomous execution of CLI workflows (⚠ exact semantics unverified).

## Read (fetched 2026-09-15)

- [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) — CreateSession → AppendEvent → ListEvents → GenerateMemories (v).
- [Sessions with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk) — Runtime instance as session store, no deploy needed (v).
- [Agents CLI community tutorial](https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d) (v as a secondary source; ⚠ official doc).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Agent Platform Sessions | Stores per-user conversation events; source of truth for context | needs an Agent Runtime instance | (v) |
| Memory Bank | Generates and serves long-term memories from sessions; scope keyed by user id | regions listed in docs | (v) |
| Agents CLI | scaffold/eval/deploy skills, manifest, Skill Registry access | Python 3.11+, Node, uv | ⚠ official |

## Case — `cases/03-sessions-memory`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

`Session` trait (lesson 02) + `MemoryStore` trait with a local `FileMemoryStore` that runs a deterministic fact extractor (reuse MIP-0039's fact guard vocabulary) at session close. Cloud impl in `gcp/` would be Memory Bank; written-not-run.

## Quiz

`just quiz --lesson 03` — questions tagged `lesson: "03"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/03.tsv` (front TAB back). Import into Anki as basic cards.
