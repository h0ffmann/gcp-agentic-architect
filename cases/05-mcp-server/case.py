"""MCP shape: JSON-RPC over stdio, tools/list + tools/call, client-side allowlist (a registry)."""
import json
import subprocess
import sys
SERVER = r'''
import json, sys
TOOLS = {"lookup_order": lambda a: {"order": a["id"], "status": "shipped"}, "delete_db": lambda a: {"deleted": True}}
for line in sys.stdin:
    req = json.loads(line); m, i = req["method"], req["id"]
    if m == "tools/list": res = {"tools": [{"name": n} for n in TOOLS]}
    elif m == "tools/call": res = TOOLS[req["params"]["name"]](req["params"]["arguments"])
    else: res = {"error": "unknown"}
    print(json.dumps({"jsonrpc": "2.0", "id": i, "result": res}), flush=True)
'''
p = subprocess.Popen([sys.executable, "-c", SERVER], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
ids = iter(range(1, 1_000))
def rpc(method, params=None):
    p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": next(ids), "method": method, "params": params or {}}) + "\n"); p.stdin.flush()
    return json.loads(p.stdout.readline())["result"]
REGISTRY_ALLOW = {"lookup_order"}   # what the registry/gateway lets this agent call
tools = [t["name"] for t in rpc("tools/list")["tools"]]; print("server offers:", tools)
usable = [t for t in tools if t in REGISTRY_ALLOW]; print("agent may use:", usable)
print(rpc("tools/call", {"name": "lookup_order", "arguments": {"id": "A1"}}))
assert "delete_db" in tools and "delete_db" not in usable
p.stdin.close(); p.wait()
print("ok: MCP exposes tools; policy decides which the agent may call")
