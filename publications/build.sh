#!/usr/bin/env bash
# Build the course book: course/*.md → publications/book/book.md → pdf/book.{html,pdf}
# EN is the source. PT is generated (hook below) — reuse ww3-gpu's md→PDF pipeline when wiring CI.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p pdf publications/book
{
  cat publications/book/front-matter.md
  for f in course/[0-9][0-9]-*.md; do printf '\n\n'; cat "$f"; done
} > publications/book/book.md
pandoc publications/book/book.md -s --toc -o pdf/book.html --metadata title="Professional Agentic Architect — study book"
if command -v xelatex >/dev/null && pandoc publications/book/book.md --toc --pdf-engine=xelatex -o pdf/book.pdf 2>/dev/null; then
  echo "pdf: xelatex"
elif command -v wkhtmltopdf >/dev/null && wkhtmltopdf -q pdf/book.html pdf/book.pdf 2>/dev/null; then
  echo "pdf: wkhtmltopdf"
else
  echo "pdf: no working engine, HTML only"
fi
# PT generation: translate.sh not present — reuse ww3-gpu's md translation step (Prompt 6 follow-up).
ls -la pdf
