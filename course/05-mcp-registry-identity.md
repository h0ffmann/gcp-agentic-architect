# 05 — MCP, Agent Registry, Google Cloud MCP Servers, Agent Identity for tools

**Exam objectives:** 3.2 · section weight 33%. Quiz: `just quiz --lesson 05`. Case: `just case 05`.

## On the exam

- **MCP** connects an agent to tools/servers (JSON-RPC; `tools/list`, `tools/call`). **Google Cloud MCP Servers** are managed MCP endpoints for Google services; custom MCP servers wrap your APIs, managed databases, or third-party SaaS.
- **Agent Registry** is the organisation's catalog of agents, tools and MCP servers: automatic registration from Agent Runtime, manual registration for external hosts; Agent Gateway reads it to enforce access.
- **Agent Identity** gives each agent a unique attested identity (SPIFFE ID; mTLS + DPoP) instead of a shared service account; permissions are IAM roles on that principal; **legacy bucket roles cannot be granted**. Audit logs show agent and user.
- Question shapes: "agents share a service account, auditors unhappy" → Agent Identity; "third-party agent must be discoverable" → manual registration; "which tools may this agent call" → registry + gateway policy, never the prompt.

## Read (fetched 2026-09-15)

- [Agent Identity overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) (v).
- [Agent Registry automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration) (v).
- ⚠ [MCP spec](https://modelcontextprotocol.io).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Agent Identity | Per-agent managed identity, SPIFFE-based, bound tokens, auth manager for OAuth/API keys | no legacy bucket roles | (v) |
| Agent Registry | Central catalog; automatic from Runtime; manual for external; A2A skills extracted | Gateway depends on it | (v) |
| Google Cloud MCP Servers | Managed MCP servers for Google Cloud services | ⚠ list | ⚠ |

## Case — `cases/05-mcp-server`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola's CLI already exposes an MCP tool server. Port: a `tools/registry.json` allowlist read by the server (registry) and enforced by ai-jail deny rules (identity boundary). This is exactly the case's shape.

## Quiz

`just quiz --lesson 05` — questions tagged `lesson: "05"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/05.tsv` (front TAB back). Import into Anki as basic cards.
