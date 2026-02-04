import os
from io import BytesIO
from huggingface_hub import InferenceClient
import requests

def generate_image(prompt: str) -> bytes:
    """
    Generate image using Stable Diffusion XL via free HF Inference.
    Returns bytes for Facebook API.
    """
    try:
        API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
        }

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": prompt,
        })
        
        return image_bytes
        
    except Exception as e:
        print(f"⚠️ Image generation failed: {e}")
        return None


# Test
if __name__ == "__main__":
    prompt = "A futuristic cityscape at sunset, vibrant colors, digital art"
    image_bytes = generate_image(prompt)
    
    if image_bytes:
        with open("test.jpg", "wb") as f:
            f.write(image_bytes)
        print("✅ Image generated and saved!")
    else:
        print("❌ Failed to generate image")