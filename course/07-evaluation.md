# 07 — Evaluation: evalsets, golden data, Gen AI evaluation service, autoraters, CI

**Exam objectives:** 4.1 · section weight 22%. Quiz: `just quiz --lesson 07`. Case: `just case 07`.

## On the exam

- **ADK evaluation**: `.evalset.json` of eval cases (user turns, expected tool trajectory, reference response); `adk eval <agent> <evalset>` with an eval config; criteria include tool-trajectory match, `response_match_score` (default threshold 0.8), rubric-based response/tool-use quality, and `safety_v1`/trajectory-quality that delegate to the **Agent Platform Eval SDK** and need a project. `adk conformance` = regression against a golden baseline.
- **Gen AI evaluation service** (Agent Platform, Optimize pillar) = managed model-based metrics at scale; **custom autoraters** when the rubric is bespoke.
- Test-set design: golden data + prompts + **edge cases**; evaluate **response and retrieval** separately; continuous evaluation in CI and on production samples (drift).
- Question tells: "tool order" → trajectory; "helpfulness at scale without writing a scorer" → evaluation service; "regression gate on each PR" → evalset in CI; "quality dropped after data refresh" → retrieval evaluation.

## Read (fetched 2026-09-15)

- [ADK evaluate](https://google.github.io/adk-docs/evaluate/) · [criteria](https://google.github.io/adk-docs/evaluate/criteria/) (v).
- [adk_eval_starter](https://github.com/cuppibla/adk_eval_starter) — runnable workshop (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| ADK eval | evalset files, CLI + web Eval tab, criteria, conformance | `response_match_score` default 0.8 | (v) |
| Gen AI evaluation service | Managed evaluation on Agent Platform | preview per Runtime page | (v) mention |
| Custom autoraters | LLM-as-judge you write | — | ⚠ |

## Case — `cases/07-evalset`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

MIP-0040's reviewer-judge is a custom autorater; add an `evalset/` directory in marola's shape (`user`, `expected_tools`, `reference`) run by `just benchmark`, with trajectory exact-match and a fuzzy response threshold — the case is the runner.

## Quiz

`just quiz --lesson 07` — questions tagged `lesson: "07"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/07.tsv` (front TAB back). Import into Anki as basic cards.
