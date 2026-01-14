import json
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

docs_dir = Path("data/docs")
index_dir = Path("data/indexes")
index_dir.mkdir(parents=True, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

index_config = {
    "yearly" : "yearly_snapshots.json",
    "ratios" : "ratio_summaries.json",
    "trends" : "trend_summaries.json",
    "definitions" : "financial_definitions.json"
}

for index_name, filename in index_config.items():
    with open(docs_dir / filename, "r") as f:
        docs = json.load(f)

    texts = [d["content"] for d in docs]
    embeddings = model.encode(texts, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, str(index_dir / f"{index_name}.faiss"))

    with open(index_dir / f"{index_name}_meta.json", "w") as f:
        json.dump(docs, f, indent=2)
    
    print(f"Built {index_name} index with {len(texts)} documents")