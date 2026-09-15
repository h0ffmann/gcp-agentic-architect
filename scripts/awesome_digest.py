#!/usr/bin/env python3
"""Propose GitHub repos for the AWESOME list. Never edits the list. Stdlib only.

  awesome_digest.py [--json] [--refresh] [--self-test]
Caches GitHub search results in .tmp/awesome-cache.json; offline it reports from the cache.
"""
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / ".tmp" / "awesome-cache.json"
QUERIES = ["google adk agent", "agent2agent a2a", "antigravity skills", "agentic architect certification",
           "gemini enterprise agent platform", "model armor"]


def search(q):
    url = "https://api.github.com/search/repositories?sort=stars&per_page=10&q=" + urllib.parse.quote(q)
    with urllib.request.urlopen(url, timeout=15) as r:
        return [{"name": i["full_name"], "stars": i["stargazers_count"], "url": i["html_url"],
                 "desc": (i["description"] or "")[:120]} for i in json.load(r)["items"]]


def rank(results):
    seen, out = set(), []
    for q, items in results.items():
        for i in items:
            if i["name"] not in seen:
                seen.add(i["name"]); out.append(dict(i, query=q))
    return sorted(out, key=lambda i: -i["stars"])


def self_test():
    r = rank({"a": [{"name": "x/y", "stars": 5, "url": "u", "desc": ""}], "b": [{"name": "x/y", "stars": 5, "url": "u", "desc": ""}, {"name": "z/w", "stars": 9, "url": "u", "desc": ""}]})
    assert [i["name"] for i in r] == ["z/w", "x/y"]
    print("awesome_digest self-test ok")


def main(argv):
    if "--self-test" in argv:
        self_test(); return 0
    import urllib.parse  # noqa: F401  (used in search)
    results = json.loads(CACHE.read_text()) if CACHE.exists() and "--refresh" not in argv else {}
    if not results:
        try:
            results = {q: search(q) for q in QUERIES}
            CACHE.parent.mkdir(exist_ok=True); CACHE.write_text(json.dumps(results, indent=1))
        except Exception as e:  # offline: say so, exit 0
            print(f"no network and no cache ({e.__class__.__name__}); nothing to propose"); return 0
    ranked = rank(results)
    if "--json" in argv:
        print(json.dumps(ranked, indent=1)); return 0
    for i in ranked[:30]:
        print(f"{i['stars']:6d}  {i['name']:45s} {i['desc']}")
    return 0


if __name__ == "__main__":
    import urllib.parse
    sys.exit(main(sys.argv[1:]))
