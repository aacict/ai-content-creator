from prompt_generator import generate_prompt
from text_generator import generate_text
from image_generator import generate_image
from facebook_poster import post_to_facebook

def lambda_handler(event, context):
    # 1. Generate daily prompt
    prompt = generate_prompt()
    print(f"[1] Generated Prompt:\n{prompt}\n")

    # 2. Generate text content
    caption = generate_text(prompt)
    print(f"[2] Generated Caption:\n{caption}\n")

    # 3. Generate image
    image_bytes = generate_image(prompt)
    if image_bytes is None:
        return {"error": "Image generation failed"}

    # 4. Upload image to S3 if we need those images

    # 5. Post to Facebook
    result = post_to_facebook(image_bytes, caption)

    return {
        "prompt": prompt,
        "caption": caption,
        "facebook_result": result
    }
