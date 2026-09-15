# 10 — Security and governance: OAuth 2.0 / Auth Manager, PAB, Agent Gateway, Model Armor, SDP, HITL

**Exam objectives:** 5.1 · 5.2 · section weight 15%. Quiz: `just quiz --lesson 10`. Case: `just case 10`.

## On the exam

- **Agent Gateway** = policy enforcement point for all agent traffic; requires an authorization policy; IAP authenticates using IAM; **deploy IAP in dry-run first**; egress vs ingress modes; delegates content checks to **Model Armor**; can add natural-language context-aware controls.
- **Agent Identity + PAB**: per-agent principal; **principal access boundary** policies bound what the agent can ever reach; agent-to-tool **OAuth 2.0** flows are handled by the **auth manager**, which encrypts end-user credentials so the agent never sees them and the gateway decrypts at egress.
- **Model Armor**: prompt injection/jailbreak, responsible-AI filters, **Sensitive Data Protection**, image screening; **floor settings** (project-wide) vs **templates** (per request); inspect-only vs INSPECT_AND_BLOCK; 4 MB cap; document screening only in Gemini Enterprise; if unreachable the request proceeds unscreened; Gateway needs `roles/modelarmor.calloutUser` and `modelarmor.user`.
- **HITL** for consequential actions (money, deletion, external comms). **Identity propagation**: logs show agent and user.
- Distractor: "put the policy in the system prompt".

## Read (fetched 2026-09-15)

- [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) · [set up](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway) (v).
- [Agent Identity overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) (v).
- [Model Armor overview](https://docs.cloud.google.com/model-armor/overview) · [Gateway integration](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration) · [Agent Platform integration](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Agent Gateway | Enforcement point; IAP/IAM authorization policies; Registry lookups; Model Armor delegation | dry-run first | (v) |
| Agent Identity / PAB / auth manager | Per-agent principal; boundaries; OAuth handled outside agent code | — | (v) |
| Model Armor | Floor settings vs templates; inspect vs block; SDP inside; 4 MB; fails open | GA with Agent Platform | (v) |
| Sensitive Data Protection | DLP filters used by Model Armor | own doc ⚠ | (v) via MA |

## Case — `cases/10-gateway-policy`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

ai-jail + `.claude/settings.json` deny rules + `guard-*.sh` hooks are marola's gateway; MIP-0039's deterministic fact guard is its Model Armor; the water-quality veto is HITL. The case's five denials are the acceptance test for `docs/AGENTIC-ARCHITECT-MAPPING.md` §5.

## Quiz

`just quiz --lesson 10` — questions tagged `lesson: "10"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/10.tsv` (front TAB back). Import into Anki as basic cards.
