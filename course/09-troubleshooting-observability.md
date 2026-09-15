# 09 — Troubleshooting and observability: loops, drift, tool latency, Cloud Trace / Logging

**Exam objectives:** 4.2 · section weight 22%. Quiz: `just quiz --lesson 09`. Case: `just case 09`.

## On the exam

- Symptoms → tools: **reasoning loop** (same tool call repeated) → iteration caps + traces; **tool latency** → Cloud Trace spans per call; **drift** (quality slowly falls) → continuous evaluation on production samples vs golden set; **hallucination** → grounding/retrieval evaluation + Model Armor is *not* the fix; **system failure** → Cloud Logging with the ReasoningEngine resource filter.
- Gateway 403 "Egress request is not authorized" → agent identity roles + authorization policy; find failing calls in Logging.
- Cost optimisation: cache, smaller model for sub-steps, cap loops, shorten context, batch offline work.
- Observability names: Google Cloud Observability = Cloud Logging + Cloud Trace (+ Topology view on Agent Platform).

## Read (fetched 2026-09-15)

- [Troubleshoot Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway) (v).
- [Agent Platform agents overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents) — Optimize pillar names Cloud Observability and Topology (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Cloud Trace | Spans per LLM/tool call; latency attribution | — | (v) named |
| Cloud Logging | Runtime logs under aiplatform.googleapis.com/ReasoningEngine | filter by location | (v) |

## Case — `cases/09-trace-triage`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola's `Telemetry` trait gets an OTLP-shaped span list; the case's loop and bottleneck detectors become a `just triage` recipe over `.tmp/traces.jsonl`.

## Quiz

`just quiz --lesson 09` — questions tagged `lesson: "09"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/09.tsv` (front TAB back). Import into Anki as basic cards.
