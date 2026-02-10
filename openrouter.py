import requests

url = "https://openrouter.ai/api/v1/embeddings"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}

payload = {
    "model": "sentence-transformers/all-minilm-l12-v2",
    "input": "Your text string goes here",
    "encoding_format": "float"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code != 200:
    raise Exception(f"OpenRouter error {response.status_code}: {response.text}")

data = response.json()
embedding = data["data"][0]["embedding"]

print(f"Embedding size: {len(embedding)}")
