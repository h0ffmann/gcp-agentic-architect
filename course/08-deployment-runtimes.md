# 08 — Deployment: Agent Runtime vs Cloud Run vs GKE, scaling, cost

**Exam objectives:** 4.2 · section weight 22%. Quiz: `just quiz --lesson 08`. Case: `just case 08`.

## On the exam

- **Agent Runtime**: fully managed, Sessions/Memory Bank/code-execution/Example Store built in, automatic Registry and Gateway integration, `adk deploy agent_engine`. Choose for least ops and managed state.
- **Cloud Run**: your container, HTTP, scale-to-zero, `adk deploy cloud_run`; state is your problem. Choose for existing container pipelines or custom runtimes.
- **GKE**: sidecars, GPU node pools, node-level network policy, also the coding-agent sandbox. Choose for control.
- Scaling/cost tells: bursty + idle → serverless; steady high throughput with GPUs → GKE; "no platform team" → Runtime.
- Console recon (D7): open Agent Platform → Runtime, Registry, Gateway, Security pages read-only; note the exact menu names in this file.

## Read (fetched 2026-09-15)

- [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime) · [Scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) (v).
- [adk-python README deploy section](https://github.com/google/adk-python) (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Agent Runtime | Managed; sessions, memory, code execution, Example Store; observability built in | resource type ReasoningEngine | (v) |
| Cloud Run | Serverless containers | ADK deploy target | (v) README |
| GKE | Kubernetes; sidecars, GPUs, network policy; sandboxes | ADK deploy target | (v) README |

## Case — `cases/08-runtime-choice`

Console recon notes go here (D7):

- Agent Platform menu: …
- Runtime page shows: …
- Registry page shows: …
- Gateway / Security page shows: …

## marola port

MIP-0008 Docker images = the Cloud Run path; add a `deploy/agent-runtime.yaml` manifest (written-not-run) next to the Dockerfile, and a decision note in the mapping doc.

## Quiz

`just quiz --lesson 08` — questions tagged `lesson: "08"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/08.tsv` (front TAB back). Import into Anki as basic cards.
