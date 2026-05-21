import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import faiss

class Retriever:
    def __init__(self, docs):
        self.docs = docs
        self.texts = [d["text"] for d in docs]

        # BM25
        tokenized = [t.lower().split() for t in self.texts]
        self.bm25 = BM25Okapi(tokenized)

        # Dense embeddings
        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.embed_model.encode(self.texts, convert_to_numpy=True)
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings)

    def search_bm25(self, query, k=3):
        tokenized = query.lower().split()
        scores = self.bm25.get_scores(tokenized)
        top_idx = np.argsort(scores)[::-1][:k]
        return [(self.docs[i], float(scores[i])) for i in top_idx]

    def search_dense(self, query, k=3):
        q_emb = self.embed_model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(q_emb)
        scores, idx = self.index.search(q_emb, k)
        return [(self.docs[i], float(scores[0][j])) for j, i in enumerate(idx[0])]

    def search_fusion(self, query, k=3):
        bm25_results = self.search_bm25(query, k=5)
        dense_results = self.search_dense(query, k=5)

        scores = {}
        for rank, (doc, _) in enumerate(bm25_results):
            scores[doc["id"]] = scores.get(doc["id"], 0) + (1 / (rank + 1))
        for rank, (doc, _) in enumerate(dense_results):
            scores[doc["id"]] = scores.get(doc["id"], 0) + (1 / (rank + 1))

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]
        return [next(d for d in self.docs if d["id"] == doc_id) for doc_id, _ in ranked]