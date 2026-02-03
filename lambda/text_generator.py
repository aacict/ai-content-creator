import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

def generate_text(prompt: str, model: str = "zai-org/GLM-4.7-Flash:novita") -> str:
    payload = {
        "messages": [
            {"role": "system", "content": "You are a creative social media post generator."},
            {"role": "user", "content": prompt}
        ],
        "model": model
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        print("⚠️ HF API returned unexpected response:", data)
        return prompt
