import requests


def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    if response.status_code != 200:
        print("Ollama Error:", response.text)
        return ""

    return response.json()["response"]