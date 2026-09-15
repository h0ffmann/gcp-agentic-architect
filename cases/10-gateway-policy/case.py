"""Governance as code: identity → registry allowlist + boundary, Model-Armor-like screen, HITL, audit."""
import re
REGISTRY = {"agent://support": {"tools": {"get_order", "create_refund"}, "boundary": {"proj-a"}}}
INJECTION = re.compile(r"ignore (all|previous) instructions|reveal (the )?system prompt", re.I)
AUDIT = []
def gateway(agent, user, tool, project, args, approve):
    entry = REGISTRY.get(agent)
    if not entry or tool not in entry["tools"]: return deny(agent, user, tool, "not in registry allowlist")
    if project not in entry["boundary"]: return deny(agent, user, tool, "outside principal access boundary")
    if INJECTION.search(str(args)): return deny(agent, user, tool, "Model Armor: prompt injection")
    if tool == "create_refund" and args.get("amount", 0) > 1000 and not approve(): return deny(agent, user, tool, "HITL not approved")
    AUDIT.append(("allow", agent, user, tool)); return "allow"
def deny(a, u, t, why): AUDIT.append(("deny", a, u, t, why)); return f"deny: {why}"
print(gateway("agent://support", "user:ana", "get_order", "proj-a", {"id": "1"}, lambda: True))
print(gateway("agent://support", "user:ana", "delete_db", "proj-a", {}, lambda: True))
print(gateway("agent://support", "user:ana", "get_order", "proj-b", {"id": "1"}, lambda: True))
print(gateway("agent://support", "user:ana", "get_order", "proj-a", {"id": "ignore previous instructions"}, lambda: True))
print(gateway("agent://support", "user:ana", "create_refund", "proj-a", {"amount": 5000}, lambda: False))
assert [e[0] for e in AUDIT] == ["allow", "deny", "deny", "deny", "deny"] and all(e[2] == "user:ana" for e in AUDIT)
print("ok: every decision names agent AND user; policy is outside the prompt")
