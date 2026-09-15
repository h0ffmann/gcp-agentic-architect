# 11 — Coding agents: Antigravity, Claude Code on Google Cloud, MCP config, sandboxes, Agents CLI

**Exam objectives:** 2.1 · 2.2 · section weight 17%. Quiz: `just quiz --lesson 11`. Case: `just case 11`.

## On the exam

- **Antigravity** (app, CLI `agy`, SDK): Gemini CLI's successor; keeps **Agent Skills, Hooks, Subagents, Extensions**; reads AGENTS.md / GEMINI.md as **rules**; skills are `SKILL.md` directories (`.agents/skills` project scope, global under `~/.gemini/…`); terminal auto-execution = Request Review vs Always Proceed; non-workspace file access off by default.
- Customisation vocabulary for 2.2: **skill** (packaged know-how, auto-selected by description), **rule** (standing instruction), **hook** (runs at lifecycle events, e.g. before a tool executes), **plugin/extension** (bundles), **subagent** (delegated worker). Expect "which one is this?" questions.
- **Claude Code on Google Cloud**: same MCP/skills model; the exam cares that coding agents get tools via MCP servers and run in **secure sandboxes** (GKE, Cloud Workstations, Antigravity sandbox) when code is untrusted.
- Use cases named: refactor, optimise runtimes, patch application-layer vulnerabilities — always with tests + scanner + review.
- **Agents CLI** augments Antigravity to build/scale/govern/optimise deployed agents.

## Read (fetched 2026-09-15)

- [Gemini CLI → Antigravity CLI transition (Google Developers Blog)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (v via tracked issue).
- [Codelab: Authoring Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills) (v).
- [antigravity.google/docs/cli](https://antigravity.google/docs/cli) — official; open on D9.

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Antigravity | App + CLI (agy) + SDK; skills/hooks/subagents/extensions; rules from AGENTS.md | consumer Gemini CLI ended 2026-06-18 | (v) |
| Claude Code on Google Cloud | Anthropic's coding agent used with Google Cloud (MCP, skills) | ⚠ setup doc | ⚠ |
| Cloud Workstations | Managed dev environments as sandboxes | — | ⚠ |

## Case — `cases/11-hooks-and-skills`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola's `.claude/` (hooks, rules, skills, settings) is the Section 2.2 material; MIP-0011/0013/0017 already document it. Port = a table in the mapping doc from Antigravity vocabulary to marola files.

## Quiz

`just quiz --lesson 11` — questions tagged `lesson: "11"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/11.tsv` (front TAB back). Import into Anki as basic cards.
