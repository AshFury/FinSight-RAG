from src.app.rag_pipeline import answer_query

while True:
    q = input("\nAsk a questions (or 'exit):")
    if q.lower() == "exit":
        break

    print("\nAnswer:\n")
    print(answer_query(q))