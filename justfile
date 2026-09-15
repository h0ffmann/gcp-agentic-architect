# gcp-agentic-architect — task runner. Logic lives in scripts/ and cases/; `just` lists recipes.
# Toolchain: `nix develop` (flake.nix: python, uv, gcloud, ollama + nix-config's lint and agentic
# labs). Nothing here creates a Google Cloud resource; see AGENTS.md for the two gates.

set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list --unsorted

# ---------------------------------------------------------------------
# Study: lessons, cases, questions
# ---------------------------------------------------------------------

# Run lesson NN's local case (cases/NN-*/run.sh), e.g. `just case 04`.
case NN:
    @dir=$(ls -d cases/{{ NN }}-*/ 2>/dev/null | head -1); \
    [ -n "$dir" ] || { echo "no case for lesson {{ NN }}"; exit 1; }; \
    bash "$dir/run.sh"

# Run every case, one result line each.
cases:
    @for d in cases/*/; do printf '%-28s ' "$d"; bash "$d/run.sh" | tail -1; done

# Quiz runner: --lesson NN, --section 3, --mock 1 --minutes 120, --weak, --stats, --export-anki.
quiz *ARGS:
    python3 scripts/quiz.py {{ ARGS }}

# Awesome-list candidates from GitHub Search (cached in .tmp/; proposes, never edits the list).
digest *ARGS:
    python3 scripts/awesome_digest.py {{ ARGS }}

# ---------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------

# Fast gate, stdlib only: layout, question banks, scripts' --self-test, gcloud guard, every case.
smoke:
    python3 scripts/smoke.py
    bash .claude/hooks/guard-gcloud.sh --self-test
    @for d in cases/*/; do bash "$d/run.sh" >/dev/null; done && echo "cases: ok"

# Every linter, same as ci.yml. A missing tool fails — run inside `nix develop` (or `.#lint`).
quality:
    ruff check .
    shellcheck scripts/*.sh scripts/lib/*.sh .claude/hooks/*.sh cases/*/run.sh
    actionlint
    nixpkgs-fmt --check flake.nix
    statix check .
    deadnix --fail flake.nix
    just --fmt --check --unstable
    @for s in scripts/*.py; do python3 "$s" --self-test; done

# gcloud guard self-test: every deny line denied, every allow line allowed.
guard-test:
    bash .claude/hooks/guard-gcloud.sh --self-test

# nix flake check: devShells evaluate, checks.smoke builds in the sandbox.
check:
    nix flake check --print-build-logs

# Format flake.nix and this justfile.
fmt:
    nix fmt
    just --fmt --unstable

# ---------------------------------------------------------------------
# Toolchain (flake.nix; labs from h0ffmann/nix-config)
# ---------------------------------------------------------------------

# Enter the dev shell: python, uv, gcloud, ollama, node, lint tools, ai-jail.
dev:
    nix develop

# Bump every flake input (publisher pins nixpkgs; lint and agentic follow). `just lock lint` for one.
lock *inputs:
    nix flake update {{ inputs }}

# Exact tool versions and the pinned nixpkgs, for the book's methods section.
toolchain:
    @printf '%-10s %s\n' nixpkgs "$(jq -r .nodes.nixpkgs.locked.rev flake.lock)"
    @for t in python3 uv just jq node gcloud ollama ruff shellcheck actionlint gh ai-jail pandoc nix; do \
      if command -v "$t" >/dev/null; then printf '%-10s %s\n' "$t" "$($t --version 2>&1 | grep -m1 -E '[0-9]+\.[0-9]+')"; else printf '%-10s (absent)\n' "$t"; fi; done

# ---------------------------------------------------------------------
# Publications: markdown -> PDF (nix-config labs/publisher)
# ---------------------------------------------------------------------

# Study book from course/*.md -> build/agentic-architect-book.pdf (pandoc + xelatex shell).
book:
    nix develop .#pubs --command bash scripts/build_pdf.sh

# Same book, built in the Nix sandbox (what pubs.yml runs) -> result/agentic-architect-book.pdf.
book-nix:
    nix build .#book --print-build-logs && ls -l result/

# ---------------------------------------------------------------------
# Coding agents in ai-jail (nix-config labs/agentic; policy in .ai-jail)
# ---------------------------------------------------------------------

# Claude Code in the jail, from this directory, with the host's GitHub token forwarded.
jail-claude *args:
    jail-run claude {{ args }}

# jail-claude with --model opus.
jco *args: (jail-claude "--model" "opus" args)

# jail-claude with --model fable.
jcf *args: (jail-claude "--model" "fable" args)

# jail-claude with --model sonnet.
jcs *args: (jail-claude "--model" "sonnet" args)

# Print the sandbox invocation ai-jail would use for <cmd>, without running it.
jail-dry-run *cmd:
    jail-run --dry-run -- {{ cmd }}

# Say which GitHub credential the host has for the jail to borrow (never log in inside a jail).
gh-auth:
    @if src="$(gh-token --source)"; then echo "gh-auth: $src — jail-run forwards it as GH_TOKEN"; else echo "gh-auth: none — run: gh auth login   (on the host)"; exit 1; fi

# ---------------------------------------------------------------------
# Git and pull requests (scripts ported from h0ffmann/ww3-gpu and marola)
# ---------------------------------------------------------------------

# Last n commits, one line each.
log n="10":
    git log --oneline --decorate -n {{ n }}

# Push the branch and create (or refresh) its PR, body generated from the commits.
pr *args:
    scripts/pr.sh {{ args }}

# Rewrite a PR description from its commits: `just uprd`, `just uprd --dry-run`, `just uprd 12`.
uprd *args:
    scripts/uprd.sh {{ args }}

# git-clean zip of the tracked tree (no .tmp, no build/).
zip:
    @test -z "$(git status --porcelain)" || { echo "tree not clean"; exit 1; }
    git archive --format=zip -o "gcp-agentic-architect-$(date +%F).zip" HEAD
    @ls -la gcp-agentic-architect-*.zip
