import requests
import math

API_KEY = "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"
URL = "https://openrouter.ai/api/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def embed(text: str) -> list[float]:
    payload = {
        "model": "sentence-transformers/all-minilm-l12-v2",
        "input": text,
        "encoding_format": "float"
    }

    response = requests.post(URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]

def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)

# --- TESTE RÁPIDO ---

text_1 = "Senior Python developer with experience in AI and machine learning"
text_2 = "Experienced backend engineer specialized in Python and artificial intelligence"
text_3 = "Graphic designer focused on branding and visual identity"

emb_1 = embed(text_1)
emb_2 = embed(text_2)
emb_3 = embed(text_3)

print("1 vs 2:", round(cosine_similarity(emb_1, emb_2), 4))
print("1 vs 3:", round(cosine_similarity(emb_1, emb_3), 4))
