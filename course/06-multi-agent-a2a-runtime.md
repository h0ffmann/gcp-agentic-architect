# 06 — Multi-agent: sequential / parallel / graph, A2A, handoffs, Agent Runtime, policies

**Exam objectives:** 3.3 · section weight 33%. Quiz: `just quiz --lesson 06`. Case: `just case 06`.

## On the exam

- Composition: independent subtasks → **parallel**; dependent steps → **sequential**; conditional branching and retries → **graph/loop**. Latency questions want parallel fan-out then sequential fan-in.
- **A2A** is for agent-to-agent delegation across teams/frameworks: agent cards for discovery, tasks for delegation. **MCP** is not the answer to "two agents from different vendors".
- Coordination products: Agent Identity (who), Agent Registry (what exists), Agent Runtime (where it runs), agent policies via Gateway (what it may do). A2A agents on Runtime register automatically; Runtime traffic goes through Gateway automatically.
- Cross-project tool calls from a Runtime agent: register the destination in the gateway project, Agent-to-Anywhere mode only.
- Distractor: Cloud Scheduler / Pub/Sub for request-time orchestration.

## Read (fetched 2026-09-15)

- [Agent Registry automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration) — A2A on Runtime (v).
- [Agent Gateway setup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway) — cross-project destinations (v).
- [a2a-protocol.org](https://a2a-protocol.org/latest/) (v link).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| A2A | Open standard: agents declare identity/capabilities (agent card) and exchange tasks | skills extracted into Registry | (v) |
| Agent Runtime | Managed hosting; routes through Gateway; egress + ingress modes | formerly Agent Engine | (v) |
| ADK workflow agents | SequentialAgent, ParallelAgent, LoopAgent | ⚠ exact class names re-check | ⚠ |

## Case — `cases/06-multi-agent-a2a`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

Recommender → Reviewer in marola is a two-agent sequential chain; the case's parallel fan-out maps to running the three ocean-data lookups concurrently in Kyo, and the A2A card is a `/.well-known/agent.json` on the MCP server. `cases/06` is the reference implementation.

## Quiz

`just quiz --lesson 06` — questions tagged `lesson: "06"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/06.tsv` (front TAB back). Import into Anki as basic cards.
