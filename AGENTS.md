# AGENTS.md

Instructions for any AI coding agent working in this repository (Claude Code, Antigravity, or
otherwise). Read this before writing, modifying, or running anything. Humans should read it too.

## What this repo is

**gcp-agentic-architect** — one person's public exam lab for PR000340, *Google Cloud Certified –
Professional Agentic Architect* (beta, English): a self-paced course, runnable local cases, a
scenario-style question bank with a spaced-repetition runner, a verified awesome-list, and the
design docs for porting what the exam teaches into [marola](https://github.com/h0ffmann/marola)
without breaking its no-cloud default. Shape copied from
[ww3-gpu](https://github.com/h0ffmann/ww3-gpu) (lessons + cases + AWESOME list + Nix + PDF
pipeline); shared Nix tooling (lint, ai-jail, the PDF toolchain) comes from
[nix-config](https://github.com/h0ffmann/nix-config)'s labs as flake inputs.

The only file at bootstrap was `docs/PROMPT-SERIES_202609.md` (formerly `gt.md`) — the
seven-session prompt series that builds everything else. It is the plan of record; when this
file and it disagree, fix the one that is wrong in the same change.

## The exam, as verified on 2026-09-15 (dates matter — recheck if you are reading this later)

- Guide: <https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf>.
  FAQ: <https://support.google.com/cloud-certification/answer/18080541>.
- Five sections, weighted **13 / 17 / 33 / 22 / 15** (low-code · coding agents · custom agents ·
  evaluation & deployment · security & governance). Effort in this repo follows those weights.
- Hybrid: a 3-hour proctored multiple-choice exam (Pearson, window Sept 8–30, 2026, $120 beta)
  **and** hands-on labs in Google Skills (< 5 h), unlocked only for candidates who pass the MCQ,
  delivered late October–December. Results for the MCQ arrive late October. Both must pass.
- Consequence for planning: **until Sept 30 everything is the MCQ.** Console time is for
  recognising products, not for lab drills. Lab prep is a separate block after results.
- The in-scope tool list contains names newer than any model's training data (Antigravity,
  Agents CLI, Agent Runtime — formerly Agent Engine, Agent Search — formerly Vertex AI Search,
  Vector Search 1.0, Agent Gateway, Agent Identity, Skill Registry, Model Armor). Assume renames.

## Fetch, don't recall (hard rule)

Every product claim, quota, price, or API shape in this repo is either **fetched this session
and linked** or marked as unverified. Use ww3-gpu's markers, verbatim:

- `(v)` — verified against a source actually fetched while writing, with the URL and date.
- `⚠` — not verified; check before trusting. Never silently drop the marker to look tidy.

A lesson, question, or awesome-list entry without a source URL is a defect. Questions copied
from any paid course, exam-dump site, or NDA'd exam are forbidden — write scenario items from the
guide's bullets and the fetched docs. If a source 404s, drop the entry and say so in the commit.

## Local-first, cloud opt-in (hard rule)

Every runnable case under `cases/` runs with **no GCP account**: ADK local runner, Ollama or
open weights from Model Garden, a file-backed vector index, a local MCP server, two local ADK
agents talking A2A. A `--gcp` path may be documented, must be gated, and is *written-not-run*
unless a case says otherwise with a date.

**Never create, deploy, or enable a paid Google Cloud resource without explicit human
confirmation** — propose, state the expected cost, wait. Enforced two ways, deliberately
different (the marola lesson: they are not interchangeable):

1. `.claude/settings.json` `permissions.deny` refuses the literal prefixes `gcloud run deploy`,
   `gcloud ... create`, `terraform apply`, `adk deploy` before any hook runs; `GCP_ALLOW_DEPLOY=1`
   does nothing for those — the human runs the command directly.
2. `.claude/hooks/guard-gcloud.sh` (`PreToolUse` on `Bash`) catches every other shape (wrapped
   shell, absolute path, `cd infra && …`); only for those does `GCP_ALLOW_DEPLOY=1`, set after a
   human go-ahead, let one command through.

Cost ceiling for the whole lab is in `EXAM-BRIEF.md`; free tier and new-customer credits first.
Never hardcode a key, token, or project id; `.env` is gitignored and masked under ai-jail.

## Setup & commands

```bash
nix develop            # python, uv, gcloud, ollama, node + nix-config labs/lint and labs/agentic
just                   # list recipes
just smoke             # stdlib gate: layout, banks, scripts --self-test, gcloud guard, all cases
just quality           # ruff, shellcheck, actionlint, nixpkgs-fmt/statix/deadnix, just --fmt, self-tests
just check             # nix flake check (checks.smoke builds in the sandbox)
just case NN           # run lesson NN's case; prints expected output and the assertion
just quiz --lesson NN  # 20-question session; --section 3, --mock 1 --minutes 120, --weak, --stats
just book              # course/ -> build/agentic-architect-book.pdf (labs/publisher); book-nix = sandbox
just toolchain         # exact versions + nixpkgs rev, for the book's methods section
just jco               # Claude Code inside ai-jail (jcf fable, jcs sonnet), token from host gh
just pr                # push the branch, open/refresh its PR from the commits (uprd = body only)
```

`just smoke && just quality` green before a change is done (CI runs `just quality` in
`nix develop .#lint`). Scripts are stdlib-only Python with
`--self-test` and `--json`, cached under `.tmp/`, and never edit a curated document themselves
(the digest proposes, the human curates — MIP-0041/0043 pattern).

## Layout

```
docs/PROMPT-SERIES_202609.md   the prompt series that builds this repo (plan of record)
DESCRIPTION.md        one-paragraph project description (GitHub / LinkedIn)
EXAM-BRIEF.md         exam guide as a checklist + in-scope tools, one verified line each + cost plan
STUDY-CALENDAR.md     15 days to the MCQ, weighted 13/17/33/22/15; lab block after results
STUDY-LOG.md          one line per day: hours, quiz score, predicted score
AWESOME-AGENTIC-ARCHITECT_YYYYMM.md   curated, dated, every link fetched
course/NN-*.md        lessons; fixed skeleton: On the exam · Read · Verified today · Case ·
                      marola port · Quiz · Flashcards
cases/NN-*/           one runnable local case per lesson, one command, one assertion
questions/            bank.jsonl, mock-N.jsonl, cards/ (Anki TSV), schema.md
scripts/              quiz.py, awesome_digest.py, smoke.py, book_prep.py (stdlib, --self-test);
                      build_pdf.sh; pr.sh, uprd.sh, lib/ (from ww3-gpu)
marola/               MIP-0057 draft + docs/AGENTIC-ARCHITECT-MAPPING.md, upstreamed via marola's
                      mip / mip-tasks skills as stacked PRs; never edit marola from here
publications/         book/ (pandoc defaults, template, filters) + post-exam writeup; pdf/ on main
flake.nix · flake.lock  own tools + nix-config labs/{lint,agentic,publisher}; shells default/pubs/lint,
                      packages.book (mkPdf), checks.smoke. Shared tooling belongs in nix-config.
.github/              ci.yml, pubs.yml, pr-body.yml, dependabot.yml, PR template
.claude/ · .ai-jail   settings.json (deny prefixes, attribution off), hooks/guard-gcloud.sh, rules/;
                      the ai-jail policy (.env masked)
```

## Writing lessons and questions

- Weight before depth: Section 3 (custom agents) is a third of the exam and gets a third of the
  lessons, questions, and cases. Do not give Section 1 the treatment Section 3 gets.
- Questions are Google Professional scenario items: a company, a constraint, "what should you
  do?", one best answer, distractors that are real products used wrongly. Every option carries
  a rationale. Tag with the objective id (`1.1` … `5.2`); `quiz.py` fails on unknown ids.
- A question that only a bank statistic can catch is still a defect: the correct answer must not
  be the longest or the shortest option, one letter must not dominate the bank, and rationales
  must explain rather than dismiss. `quiz.py --validate` enforces all three; `--rebalance`
  redistributes answer letters after a batch. See `questions/schema.md`.
- "Verified today" tables are the point of a lesson, not decoration: product · what it does ·
  limits/quotas · pricing unit · marker · URL · date.
- The "marola port" sidebar names a trait, module, or MIP with a file:line, or says "honest gap".
  Low-code (Agent Designer, CX Agent Studio) is a known honest gap; say so, don't invent a shape.
- Flashcards are one line each, tab-separated, Anki-importable; no markdown inside.

## Session discipline

- One deliverable, one session, one branch, one PR — `/clear` and `/rename` to the branch name
  so usage maps to the PR. Sessions follow the prompt series' order; a session that starts writing
  Prompt 2 content inside Prompt 0 is doing it wrong.
- Commits carry exactly three trailers: `Tested:`, `Cost:`, `Co-Authored-By: Claude
  <noreply@anthropic.com>`. No session links, no "Generated with" banners, no PR-body attribution
  (`.claude/settings.json` turns it off — don't add it by hand).
- Comments: few, and only what the code cannot say — a why, a trap, or a pointer. Reasoning goes
  in the commit message or the lesson, never re-explained in the file.
- Stop and ask before anything that costs money or more than 30 minutes of compute.
- Do not "improve" the study calendar by adding material after D14. D15 is travel and flashcards.

## When something here turns out to be wrong

A product renamed, a price changed, a lab window moved, a link died: update this file,
`EXAM-BRIEF.md`, and the lesson in the same change, keep the old claim struck through with its
date if it was `(v)` at the time, and say in the commit what changed. This file is read by
non-Claude agents too — rules that matter stay stated here even if the detail lives in
`.claude/rules/*.md`.
