import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

index_dir = "data/indexes"
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_index(name):
    index = faiss.read_index(f"{index_dir}/{name}.faiss")
    with open(f"{index_dir}/{name}_meta.json") as f:
        meta = json.load(f)
    return index, meta

index, meta = load_index("yearly")

query = "How did McDonald's revenue perform in 2010?"
query_embeddings = model.encode([query])

D, I = index.search(np.array(query_embeddings).astype("float32"), k=3)

print("Retrieved Documents:\n")
for idx in I[0]:
    print(meta[idx]["content"])
    print("-" * 60)