import requests
from PIL import Image
from io import BytesIO
from config import NIM_IMAGE_API_URL, NIM_API_KEY

def generate_stable_diffusion_image(prompt: str) -> dict:
    invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-3-medium"

    headers = {
        "Authorization":  f"Bearer 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",
        "Accept": "application/json",
    }

    payload = {
        "prompt": prompt,
        "cfg_scale": 5,
        "aspect_ratio": "16:9",
        "seed": 0,
        "steps": 50,
        "negative_prompt": ""
    }

    response = requests.post(invoke_url, headers=headers, json=payload)
    response.raise_for_status()
    response_body = response.json()
    return response_body
