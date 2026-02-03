import torch
from diffusers import DiffusionPipeline
from PIL import Image

def setup_pipeline(model_name="stabilityai/stable-diffusion-xl-base-1.0", device="cuda"):
    """
    Setup the Diffusion pipeline for local image generation.
    """
    pipe = DiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        safety_checker=None,       # optional, disables NSFW check
    )
    pipe.to(device)
    return pipe

def generate_image( prompt: str) -> Image.Image:
    """
    Generate a PIL Image from a text prompt using the DiffusionPipeline.
    """
    try:
        pipe = setup_pipeline(device="cpu") 
        output = pipe(prompt)
        image = output.images[0]
        return image
    except Exception as e:
        print("⚠️ Error during image generation:", e)
        return None
