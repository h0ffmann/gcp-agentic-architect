"""ADK-style evalset: expected tool trajectory + reference response; CI exit code on threshold."""
import json, sys, difflib
EVALSET = {"eval_set_id": "orders", "eval_cases": [
  {"eval_id": "refund-damaged", "user": "refund order ORD-1, it arrived damaged",
   "expected_tools": ["get_order", "create_refund"], "reference": "Refund created for ORD-1."},
  {"eval_id": "status", "user": "where is ORD-2?", "expected_tools": ["get_order"], "reference": "ORD-2 is shipped."}]}
def agent(user):                                     # the system under test
    if "refund" in user: return ["get_order", "create_refund"], "Refund created for ORD-1."
    return ["get_order"], "ORD-2 has shipped."
CONFIG = {"tool_trajectory_avg_score": 1.0, "response_match_score": 0.8}
rows = []
for c in EVALSET["eval_cases"]:
    tools, resp = agent(c["user"])
    traj = 1.0 if tools == c["expected_tools"] else 0.0
    match = difflib.SequenceMatcher(None, resp.lower(), c["reference"].lower()).ratio()
    rows.append((c["eval_id"], traj, round(match, 2))); print(rows[-1])
ok = all(t >= CONFIG["tool_trajectory_avg_score"] and m >= CONFIG["response_match_score"] for _, t, m in rows)
print("PASS" if ok else "FAIL"); assert ok
print("ok: trajectory is exact, response is fuzzy with a threshold, the run is gateable")
