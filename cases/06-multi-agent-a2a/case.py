"""A2A shape: two local agents publish agent cards; an orchestrator fans out in parallel, then sequences."""
import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
def agent_server(name, skill, handler):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a): pass
        def do_GET(self):
            body = json.dumps({"name": name, "skills": [{"id": skill}], "url": f"http://127.0.0.1:{self.server.server_port}"}).encode()
            self.send_response(200); self.end_headers(); self.wfile.write(body)
        def do_POST(self):
            task = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            out = json.dumps({"task": task["id"], "result": handler(task["input"])}).encode()
            self.send_response(200); self.end_headers(); self.wfile.write(out)
    s = HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=s.serve_forever, daemon=True).start(); return s
srv = [agent_server("inventory", "stock", lambda q: {"sku": q, "stock": 7}), agent_server("pricing", "price", lambda q: {"sku": q, "price": 19.9})]
cards = [json.loads(urllib.request.urlopen(f"http://127.0.0.1:{s.server_port}/.well-known/agent.json").read()) for s in srv]
print("discovered:", [(c["name"], c["skills"][0]["id"]) for c in cards])
def send(card, task):
    req = urllib.request.Request(card["url"] + "/tasks", json.dumps(task).encode(), {"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())["result"]
results = {}
ts = [threading.Thread(target=lambda c=c: results.update({c["name"]: send(c, {"id": c["name"], "input": "SKU-1"})})) for c in cards]
[t.start() for t in ts]; [t.join() for t in ts]                      # parallel fan-out
summary = f"SKU-1: {results['inventory']['stock']} in stock at {results['pricing']['price']}"   # sequential fan-in
print(summary); assert "7 in stock at 19.9" in summary
[s.shutdown() for s in srv]; print("ok: agent cards for discovery, tasks for delegation, parallel then sequential")
