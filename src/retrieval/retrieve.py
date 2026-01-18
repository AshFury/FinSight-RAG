import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index_dir = "data/indexes"

def load_index(name):
    index = faiss.read_index(f"{index_dir}/{name}.faiss")
    with open(f"{index_dir}/{name}_meta.json") as f:
        meta = json.load(f)
    return index, meta

def retrieve(query: str, index_name: str, k=3):
    index, meta = load_index(index_name)
    q_emb = model.encode([query])
    _, idxs = index.search(np.array(q_emb).astype("float32"), k)

    return [meta[i]["content"] for i in idxs[0]]