# FinSight-RAG
FinSight-RAG is a Retrieval-Augmented Generation (RAG) system that analyzes 20 years of McDonald’s financial statements (2002–2022) to generate explainable, evidence-backed financial insights using Large Language Models.

The system is designed to help users ask natural-language questions about a company’s financial performance, trends, and risk signals, while ensuring that all responses are grounded strictly in retrieved financial data.


🔍 Key Capabilities

Query historical financial performance using natural language
Analyze year-over-year trends and derived financial ratios
Identify potential financial risk signals with supporting evidence
Provide transparent explanations by citing specific years and metrics


🧠 How It Works

FinSight-RAG converts structured financial data into RAG-friendly documents and stores them in multiple vector indexes (raw financials, derived ratios, and trend summaries).
A query-intent classifier routes each user query to the most relevant indexes, and the LLM synthesizes insights using only retrieved context to minimize hallucinations.


🏗️ Architecture Highlights

Multi-index vector retrieval for context-aware reasoning
Financial ratio engineering and trend analysis from raw statements
Intent-aware query routing and context re-ranking
Structured, explainable LLM outputs with evidence references


🛠️ Tech Stack

Python, GPT-4 / Llama-3, LangChain, FAISS, FastAPI, Streamlit, Docker


📌 Dataset

McDonald’s Financial Statements (2002–2022) — Kaggle


🎯 Use Cases

Financial performance analysis
Risk and volatility assessment
Business trend explanation for non-technical stakeholders
Demonstrating real-world LLM-RAG system design in finance
