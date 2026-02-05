from prompt_generator import generate_prompt
from text_generator import generate_text
from image_generator import generate_image
from facebook_poster import post_to_facebook

def lambda_handler(event, context):
    """Main Lambda handler - generates and posts content"""
    
    print("🚀 Starting content generation...")
    
    # 1. Generate smart prompt based on day of week
    prompt_data = generate_prompt()
    print(f"[1] Category: {prompt_data['category']}")
    print(f"Topic: {prompt_data['topic']}\n")

    # 2. Generate engaging caption
    caption = generate_text(prompt_data['text_prompt'])
    print(f"[2] Generated Caption:\n{caption}\n")
    
    # 3. Add hashtags
    full_caption = f"{caption}\n\n{prompt_data['hashtags']}"
    print(f"[3] Final Caption with Hashtags:\n{full_caption}\n")

    # 4. Generate image
    print(f"[4] Generating image...")
    image_bytes = generate_image(prompt_data['image_prompt'])
    
    if image_bytes is None:
        print("❌ Image generation failed")
        return {"statusCode": 500, "error": "Image generation failed"}
    
    print("✅ Image generated successfully\n")

    # 5. Post to Facebook
    print("[5] Posting to Facebook...")
    result = post_to_facebook(image_bytes, full_caption)
    
    if "id" in result:
        print(f"✅ Posted successfully! Post ID: {result['id']}")
    else:
        print(f"⚠️ Facebook response: {result}")

    return {
        "statusCode": 200,
        "category": prompt_data['category'],
        "topic": prompt_data['topic'],
        "caption": full_caption,
        "facebook_result": result
    }

# For local testing
if __name__ == "__main__":
    result = lambda_handler({}, {})
    print("\n" + "="*50)
    print("FINAL RESULT:")
    print("="*50)
    print(result)