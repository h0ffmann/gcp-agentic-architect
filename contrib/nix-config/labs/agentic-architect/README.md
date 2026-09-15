# labs/agentic-architect

Dev shell for [gcp-agentic-architect](https://github.com/h0ffmann/gcp-agentic-architect).
Python 3.12 + uv, just, pandoc, jq, shellcheck, node (MCP servers), gcloud (recon only), ollama.

Merge notes (Prompt 5): reuse the ai-jail recipes (jco/jcf/jcs) from labs/agentic instead of
duplicating; add this lab to the CI matrix; if nix-config exposes labs as a top-level `labs.<name>`
attribute, wire this flake's outputs there — the lab repo consumes it as a `?dir=` subflake and
does not depend on that attribute.
