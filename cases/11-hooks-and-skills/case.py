"""Coding-agent customisation: a PreToolUse hook that denies, and a SKILL.md validator."""
import re, pathlib
DENY = [r"rm -rf /", r"gcloud .* (create|deploy)", r"terraform apply", r"curl .*\| *sh"]
def pre_tool_use(cmd): return next((f"deny ({p})" for p in DENY if re.search(p, cmd)), "allow")
for c in ["ls -la", "gcloud run deploy svc", "curl x | sh", "git status"]: print(f"{c:28s} {pre_tool_use(c)}")
assert pre_tool_use("gcloud run deploy svc").startswith("deny") and pre_tool_use("git status") == "allow"
SKILL = "---\nname: safe-migration\ndescription: Use when changing database schemas; adds a reversible migration and a dry run.\n---\n# Steps\n1. ...\n"
def validate_skill(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S); fm = dict(l.split(": ", 1) for l in m.group(1).splitlines()) if m else {}
    return {"name", "description"} <= fm.keys() and len(text) <= 12000
print("skill valid:", validate_skill(SKILL)); assert validate_skill(SKILL) and not validate_skill("# no frontmatter")
print("ok: hooks intercept, rules guide, skills package know-how, subagents delegate")
