#!/usr/bin/env bash
# build_pdf — course/*.md -> $OUT_DIR/agentic-architect-book.pdf (default OUT_DIR: build/).
# Runs inside `nix develop .#pubs` (pandoc, xelatex) or the Nix sandbox via `nix build .#book`.
# Pipeline ported from h0ffmann/ww3-gpu (scripts/build_pdf.sh book).
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out_dir="${OUT_DIR:-$root/build}"
prep="$out_dir/book"
mkdir -p "$out_dir"
rm -rf "$prep"

python3 "$root/scripts/book_prep.py" "$root/course" "$prep"
inputs=("$prep"/[0-9][0-9]-*.md) # glob expansion is sorted
cd "$root"
pandoc "$root/publications/book/front-matter.md" "${inputs[@]}" \
  --defaults "$root/publications/book/defaults.yaml" \
  --template "$root/publications/book/template.tex" \
  --resource-path "$root/course" \
  -o "$out_dir/agentic-architect-book.pdf"
echo "build_pdf: $out_dir/agentic-architect-book.pdf"
