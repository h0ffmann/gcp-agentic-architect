# 01 — Model selection: LLM vs SLM, self-hosted vs SaaS, OSS vs proprietary

**Exam objectives:** 3.1 · section weight 33%. Quiz: `just quiz --lesson 01`. Case: `just case 01`.

## On the exam

- The exam's model question is never "which model is smartest". It is a constraint puzzle over **cost, security/residency, latency, and agent architecture** (guide 3.1).
- Tells: "data must not leave the VPC / on-prem" → self-hosted open weights (Model Garden) on GKE; "narrow task, high volume, low latency" → SLM; "broad reasoning, no ML ops team" → Gemini SaaS via Vertex; "many small routing decisions inside a multi-agent system" → SLM for routers/classifiers, LLM only for the planner.
- Model Garden is the catalogue (200+ models, Google, partner, open); it is where the exam expects you to find open weights.
- Cost levers named in docs: model size, context length, caching, batch vs online. A right answer often pairs a small model with a bigger one, not one model for everything.
- Distractor pattern: "fine-tune the largest model" when the constraint was latency or cost.

## Read (fetched 2026-09-15)

- [Agent Platform: agents overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents) — Model Garden described as 200+ foundation models (v).
- [Exam guide 3.1](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) — the exact wording of the selection axes (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Model Garden | Library of 200+ foundation models from Google, partners and OSS for discovery and experimentation | Build pillar | (v) agents overview |
| Gemini LLMs | Google's proprietary models via Vertex / Gemini API | current versions and prices not fetched | ⚠ |

## Case — `cases/01-model-selection`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola already runs local Ollama models by default and treats every cloud model as opt-in (`azure/` module pattern). The port is a documented decision matrix in `docs/AGENTIC-ARCHITECT-MAPPING.md` §3.1 mapping marola's `LlmClient` implementations to the four axes; no code.

## Quiz

`just quiz --lesson 01` — questions tagged `lesson: "01"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/01.tsv` (front TAB back). Import into Anki as basic cards.
