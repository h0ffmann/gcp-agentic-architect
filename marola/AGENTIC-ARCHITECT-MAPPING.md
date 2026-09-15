# Agentic Architect (Google Cloud) → marola mapping

Same shape as `docs/AI-103-MAPPING.md`. Columns: guide bullet → what marola has today (file:line;
⚠ = verify the reference in the marola checkout before merging) → local shape to add → honest gap.
Exam weights: 13 / 17 / 33 / 22 / 15.

## 1. Low-code (13%)

| Bullet | marola today | Local shape | Gap |
|---|---|---|---|
| 1.1 pages/routes/event handlers (CX Agent Studio) | none | none | **honest gap** — console only |
| 1.1 system instructions, few-shot/CoT templates | prompt templates in the Recommender (⚠ path) | document as "prompt template" equivalents | partial |
| 1.2 connect enterprise data securely (Agent Search) | `knowledge/` store with file ACL-less access | none | gap |
| 1.2 multimodal ingestion | none | none | gap |

## 2. Coding agents (17%)

| Bullet | marola today | Local shape | Gap |
|---|---|---|---|
| 2.1 MCP servers, skills, tools for coding agents | `.claude/skills/*`, MCP tool server in `cli/` (⚠), MIP-0011/0013/0017 | table Antigravity vocabulary ↔ marola files | none |
| 2.1 secure sandboxes | ai-jail recipes (jco/jcf/jcs) from nix-config | — | none |
| 2.1 refactor / optimise / patch with evidence | `Tested:` trailer discipline, `just quality` | — | none |
| 2.2 skills, plugins, hooks, rules, subagents | `.claude/skills`, `.claude/hooks/guard-*.sh`, `.claude/rules/*.md`, `AGENTS.md` | — | none |
| 2.2 Agents CLI augmentation | none | none | gap (product-specific) |

## 3. Custom agents (33%)

| Bullet | marola today | Local shape | Gap |
|---|---|---|---|
| 3.1 model selection axes | Ollama local default; `azure/` opt-in `LlmClient` (⚠) | decision matrix in this doc | none |
| 3.1 ADK-style agents | Kyo Recommender pipeline = instruction + tools + runner (⚠) | `Session` events in ADK shape | small |
| 3.1 sessions & Memory Bank | `SightingStore`, `FileKnowledgeStore` (⚠) — not conversation sessions | `Session` + `MemoryStore` traits, file impls | **build** |
| 3.1 Agents CLI skills | — | — | gap |
| 3.2 RAG, vector retrieval, reranking | `knowledge/` (MIP-0055), benchmark ledger | `Reranker` step + retrieval@k metric | small |
| 3.2 Agent Identity (permissions) | ai-jail + settings deny rules + `.env` masking | document as identity boundary | none |
| 3.2 Agent Registry, MCP servers | `docs/AGENT-SKILLS.md`, MCP tool server | `tools/registry.json` allowlist enforced by the server | small |
| 3.3 MCP + A2A | MCP yes; A2A no | agent card endpoint + `just a2a-demo` | **build** |
| 3.3 parallel/sequential/graph, Runtime, policies | Recommender → Reviewer sequential chain; Kyo parallel effects (⚠) | note in doc; `deploy/agent-runtime.yaml` written-not-run | small |

## 4. Evaluation and deployment (22%)

| Bullet | marola today | Local shape | Gap |
|---|---|---|---|
| 4.1 test sets: golden data, prompts, edge cases | benchmark ledger, MIP-0040 validation set | `evalset/` JSON cases | **build** |
| 4.1 continuous evaluation in CI | `just benchmark` (⚠ CI wiring) | trajectory + response scoring in `just benchmark` | small |
| 4.1 framework choice (ADK evalset / eval service / autoraters) | MIP-0040 reviewer-judge = custom autorater | ledger column | none |
| 4.2 runtime choice | MIP-0008 Docker images = Cloud Run path | Runtime manifest written-not-run | small |
| 4.2 troubleshooting loops/latency/drift | `Telemetry` trait (⚠) | `just triage` over `.tmp/traces.jsonl` | small |
| 4.2 observability | Telemetry → logs | OTLP-shaped spans | small |

## 5. Security and governance (15%)

| Bullet | marola today | Local shape | Gap |
|---|---|---|---|
| 5.1 OAuth 2.0 agent-to-tool | `.env` secrets, no OAuth | document | gap (cloud-specific) |
| 5.1 PAB via Agent Identity | settings deny prefixes (non-overridable) | document as boundary | none |
| 5.1 Agent Gateway monitoring | `guard-*.sh` PreToolUse hooks + audit lines | `guard-gcloud.sh` | none |
| 5.1 governance: Registry + Model Armor | MIP-0039 deterministic fact guard, MIP-0022 safety footer | — | none |
| 5.2 guardrails + HITL | water-quality veto in code; cost gate | — | none |
| 5.2 identity propagation | ai-jail user/agent separation | audit line carries agent + user | small |

## Model-selection matrix (3.1)

| Constraint | marola choice | GCP equivalent |
|---|---|---|
| default, offline, no cost | Ollama open weights | Model Garden open weights on GKE |
| quality-critical review | opt-in cloud `LlmClient` (`azure/`, future `gcp/` Vertex Gemini) | Gemini via Vertex |
| routing/classification | small local model | SLM |
