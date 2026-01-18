from src.retrieval.query_router import classify_query
from src.retrieval.retrieve import retrieve
from src.llm.ollama_client import generate_answer

def answer_query(query: str) -> str:
    intent = classify_query(query)
    context_docs = retrieve(query, intent)

    context = "\n\n".join(context_docs)

    prompt = f"""
You are a financial analyst assistant.
Answer ONLY using the information below.

Context:
{context}

Question:
{query}

Answer with clear reasoning and numbers where available.
"""
    
    return generate_answer(prompt)