import json
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path("data")
DOC_PATH = DATA_DIR / "docs.jsonl"

SAMPLE_DOCS: List[Dict] = [
    {
        "id": "doc1",
        "title": "Vector Search Basics",
        "tags": ["retrieval", "dense", "embeddings"],
        "text": "Vector search uses embeddings to find semantically similar text. "
                "It often uses cosine similarity or dot product for ranking.",
    },
    {
        "id": "doc2",
        "title": "BM25 and Sparse Retrieval",
        "tags": ["retrieval", "sparse", "bm25"],
        "text": "BM25 is a classic lexical ranking function. "
                "It uses term frequency, inverse document frequency, and length normalization.",
    },
    {
        "id": "doc3",
        "title": "RAG Overview",
        "tags": ["rag", "generation", "retrieval"],
        "text": "Retrieval-Augmented Generation combines search and generation. "
                "Relevant documents are retrieved and inserted into the prompt.",
    },
    {
        "id": "doc4",
        "title": "HyDE (Hypothetical Document Embeddings)",
        "tags": ["hyde", "query-translation"],
        "text": "HyDE generates a hypothetical answer document, embeds it, and retrieves "
                "real documents similar to that hypothetical text.",
    },
    {
        "id": "doc5",
        "title": "Fusion and RRF",
        "tags": ["fusion", "retrieval"],
        "text": "Fusion combines rankings from multiple retrievers. "
                "Reciprocal Rank Fusion (RRF) merges lists without score calibration.",
    },
]

def ensure_docs():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DOC_PATH.exists():
        with DOC_PATH.open("w", encoding="utf-8") as f:
            for d in SAMPLE_DOCS:
                f.write(json.dumps(d) + "\n")

def load_docs():
    ensure_docs()
    docs = []
    with DOC_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            docs.append(json.loads(line))
    return docs