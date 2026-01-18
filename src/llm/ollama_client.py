import requests

ollama_url = "http://localhost:11434/api/generate"
model = "llama3"

def generate_answer(prompt: str) -> str:
    payload = {
        "model" : model,
        "prompt" : prompt,
        "stream" : False
    }

    response = requests.post(ollama_url, json=payload)
    response.raise_for_status()

    return response.json()["response"].strip()