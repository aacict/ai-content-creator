import os
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv

from prompt_generator import generate_prompt
from text_generator import generate_text
from image_generator import generate_image
from facebook_poster import post_to_facebook
# from utils import upload_to_s3
from config import BUCKET_NAME, FACEBOOK_PAGE_ID, FACEBOOK_TOKEN

# Load .env
load_dotenv()

# Safe test mode: don't post to Facebook unless explicitly enabled
POST_TO_FACEBOOK = os.getenv("POST_TO_FACEBOOK", "False").lower() == "true"

def main():
    print("=== Local Test: Entertainment Auto-Post ===\n")

    # 1. Generate daily prompt
    prompt = generate_prompt()
    print(f"[1] Generated Prompt:\n{prompt}\n")

    # 2. Generate AI text caption
    caption = generate_text(prompt)
    print(f"[2] Generated Caption:\n{caption}\n")

    # 3. Generate AI image
    print("[3] Generating Image...")
    image_bytes = generate_image(prompt)
    if image_bytes is None:
        print("⚠️ Image generation failed. Exiting test.")
        return

    # 4. Save image locally for inspection
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local_filename = f"test_image_{timestamp}.png"
    with open(local_filename, "wb") as f:
        f.write(image_bytes.getbuffer())
    print(f"[4] Image saved locally: {local_filename}\n")

    # 5. Upload image to S3 (optional)
    if BUCKET_NAME:
        try:
            s3_path = upload_to_s3(image_bytes, f"test_image_{timestamp}.png", BUCKET_NAME)
            print(f"[5] Image uploaded to S3: {s3_path}\n")
        except Exception as e:
            print(f"⚠️ Failed to upload to S3: {e}\n")

    # 6. Post to Facebook (mock by default)
    print("[6] Posting to Facebook (mock mode)")
    if POST_TO_FACEBOOK:
        result = post_to_facebook(image_bytes, caption)
    else:
        print(f"Mock post: {caption}")
        result = {"mock": True, "caption": caption}
    
    print(f"[6] Facebook Post Result:\n{result}\n")
    print("=== Test Completed Successfully ===")

if __name__ == "__main__":
    main()
