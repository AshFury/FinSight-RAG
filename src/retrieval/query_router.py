def classify_query(query: str) -> str:
    q = query.lower()

    if any(k in q for k in ["trend", "growth", "over time", "increase", "decrease"]):
        return "trends"
    if any(k in q for k in ["ratio", "margin", "p/e", "valuation"]):
        return "ratios"
    if any(k in q for k in ["what is", "define", "meaning"]):
        return "definitions"
    return "yearly"