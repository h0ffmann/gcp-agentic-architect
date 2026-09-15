# 12 — Low-code: Gemini Enterprise, Agent Designer, CX Agent Studio, Agent Search, multimodal ingestion

**Exam objectives:** 1.1 · 1.2 · section weight 13%. Quiz: `just quiz --lesson 12`. Case: `just case 12`.

## On the exam

- **CX Agent Studio**: state-based flows — **pages**, **transition routes** (intent/condition), **event handlers** (no-match, no-input, errors), webhooks. Deterministic multi-step collection → this.
- **Gemini Enterprise Agent Designer**: instruction-driven agents in the Gemini Enterprise workspace; **system instructions and prompt templates** (few-shot, chain-of-thought) in the console.
- **Connecting data**: Gemini Enterprise data connectors / **Agent Search** with source ACLs; **multimodal ingestion** (video, audio, images) must be processed into a searchable store before agents can use it.
- Honest gap: nothing here runs locally; learn the console vocabulary and the decision "state machine (CX Agent Studio) vs instruction agent (Agent Designer)".

## Read (fetched 2026-09-15)

- [Exam guide 1.1–1.2](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) (v).
- [Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) — Agent Studio described as a low-code visual canvas (v; note the exam says *Agent Designer* and *CX Agent Studio*).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| CX Agent Studio | Pages, routes, event handlers, webhooks | console only | ⚠ |
| Gemini Enterprise Agent Designer | Instruction/prompt-template agents in Gemini Enterprise | console only | ⚠ |
| Agent Search | Enterprise search/grounding with ACLs | ex Vertex AI Search | ⚠ |

## Case — `cases/12-lowcode-flow`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

Honest gap in marola (no low-code surface). The case shows the state-machine shape only so the vocabulary sticks.

## Quiz

`just quiz --lesson 12` — questions tagged `lesson: "12"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/12.tsv` (front TAB back). Import into Anki as basic cards.
