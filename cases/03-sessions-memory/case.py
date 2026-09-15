"""Sessions (events, scoped by user) → GenerateMemories → memories fetched in a later session."""
import re
class Sessions:
    def __init__(self): self.s = {}
    def create(self, user_id): sid = f"s{len(self.s)+1}"; self.s[sid] = {"user": user_id, "events": []}; return sid
    def append(self, sid, author, text): self.s[sid]["events"].append((author, text))
class MemoryBank:
    def __init__(self): self.m = {}
    def generate(self, session):  # extract stable facts; scope = user
        for a, t in session["events"]:
            if a == "user" and (m := re.search(r"i (?:prefer|like|am allergic to) (\w+)", t.lower())):
                self.m.setdefault(session["user"], set()).add(m.group(0))
    def fetch(self, user): return sorted(self.m.get(user, []))
S, M = Sessions(), MemoryBank()
s1 = S.create("u42"); S.append(s1, "user", "Hi, I prefer aisle seats"); S.append(s1, "agent", "noted"); S.append(s1, "user", "I am allergic to peanuts")
M.generate(S.s[s1])
s2 = S.create("u42"); s3 = S.create("u7")
print("u42 memories in new session:", M.fetch(S.s[s2]["user"])); print("u7 memories:", M.fetch("u7"))
assert M.fetch("u42") == ["i am allergic to peanuts", "i prefer aisle"] and M.fetch("u7") == []
print("ok: session = one conversation; memory = distilled, cross-session, per user")
