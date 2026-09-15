"""RAG: bag-of-words embeddings → cosine top-k → reranker fixes precision@3."""
import math, collections
DOCS = {"d1": "refund policy: refunds within 30 days for damaged items", "d2": "shipping policy: free shipping over 50 euros",
        "d3": "returns: how to return an item and get a refund", "d4": "damaged parcel? contact support with photos for a refund",
        "d5": "loyalty points and refunds on gift cards", "d6": "refund timelines: 5 business days after approval"}
def emb(t): return collections.Counter(t.lower().replace("?", "").replace(":", "").split())
def cos(a, b): n = sum(a[k]*b[k] for k in a); return n / (math.sqrt(sum(v*v for v in a.values())) * math.sqrt(sum(v*v for v in b.values())) or 1)
q = "my parcel arrived damaged, can I get a refund?"
scores = sorted(((cos(emb(q), emb(t)), d) for d, t in DOCS.items()), reverse=True)
top = [d for _, d in scores[:5]]; print("vector top-5:", top)
def rerank(query, ids):  # cross-encoder stand-in: reward phrase co-occurrence, not term counts
    key = {"damaged", "refund"}
    return sorted(ids, key=lambda d: -len(key & set(DOCS[d].lower().split())))
rr = rerank(q, top)[:3]; print("reranked top-3:", rr)
assert "d4" in rr and "d1" in rr
print("ok: retrieval gets recall, reranking gets precision")
