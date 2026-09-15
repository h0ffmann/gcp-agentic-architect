"""Agent Runtime vs Cloud Run vs GKE as a requirements table."""
def choose(r):
    if r.get("sidecar") or r.get("gpu_node_pool") or r.get("node_network_policy"): return "GKE"
    if r.get("managed_sessions_memory") and not r.get("custom_container"): return "Agent Runtime"
    if r.get("custom_container") or r.get("existing_http_service"): return "Cloud Run"
    return "Agent Runtime"
CASES = [({"managed_sessions_memory": True}, "Agent Runtime"), ({"custom_container": True, "existing_http_service": True}, "Cloud Run"),
         ({"gpu_node_pool": True, "sidecar": True}, "GKE"), ({}, "Agent Runtime")]
for req, want in CASES:
    got = choose(req); print(f"{str(req):60s} -> {got}"); assert got == want
print("ok: least ops = Runtime; own container = Cloud Run; node-level control = GKE")
