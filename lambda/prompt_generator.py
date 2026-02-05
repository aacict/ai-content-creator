import random
from datetime import datetime
from config import CONTENT_THEMES, WEEKLY_SCHEDULE

def generate_prompt() -> dict:
    """
    Generate content prompt based on day of week for variety.
    Returns dict with topic, image_prompt, and metadata.
    """
    # Get day of week (0=Monday, 6=Sunday)
    day_of_week = datetime.now().weekday()
    
    # Get category based on schedule
    category = WEEKLY_SCHEDULE.get(day_of_week, "relatable_humor")
    theme = CONTENT_THEMES[category]
    
    # Pick random topic from category
    topic = random.choice(theme["topics"])
    
    # Create prompts
    text_prompt = create_text_prompt(topic, category)
    image_prompt = f"{topic}. {theme['image_style']}"
    
    return {
        "topic": topic,
        "category": category,
        "text_prompt": text_prompt,
        "image_prompt": image_prompt,
        "hashtags": theme["hashtags"]
    }

def create_text_prompt(topic: str, category: str) -> str:
    """Create engaging text generation prompt"""
    
    style_guides = {
        "relatable_humor": "Create a SHORT, funny Facebook caption (max 3 sentences) that's super relatable. Start with a hook like 'POV:', 'Not me...', or 'Why is this so accurate?'. Use conversational language. End with a question to drive comments.",
        
        "nostalgia": "Create a SHORT, nostalgic Facebook caption (max 3 sentences) that makes people feel warm and fuzzy. Start with 'Remember when...' or 'If you know, you know...'. Make it emotional but fun.",
        
        "trending": "Create a SHORT, witty Facebook caption (max 3 sentences) about current trends. Use gen-z/millennial humor. Start with something like 'Real talk:' or 'Not everyone...'. Keep it relevant and funny.",
        
        "motivational": "Create a SHORT, uplifting Facebook caption (max 3 sentences). Be genuine, not preachy. Start with 'Your daily reminder:' or 'Real talk:'. End with an emoji or gentle encouragement.",
        
        "fun_facts": "Create a SHORT, engaging Facebook caption (max 3 sentences) presenting this fact. Start with 'Wait, WHAT?' or 'Mind = blown 🤯'. Make learning fun. End with 'Did you know this?'",
        
        "pop_culture": "Create a SHORT, entertaining Facebook caption (max 3 sentences) about this pop culture moment. Use humor and emojis. Start with something relatable like 'We've all been there...'"
    }
    
    style = style_guides.get(category, style_guides["relatable_humor"])
    
    return f"""{style}
    Topic: {topic}
    Requirements:
    - Maximum 3 sentences
    - Use 2-3 emojis naturally
    - End with a question or call-to-action
    - NO hashtags (we add those separately)
    - Sound like a real person, not a brand
    """

# Test
if __name__ == "__main__":
    prompt = generate_prompt()
    print(f"Category: {prompt['category']}")
    print(f"Topic: {prompt['topic']}")
    print(f"\nText Prompt:\n{prompt['text_prompt']}")
    print(f"\nImage Prompt:\n{prompt['image_prompt']}")
    print(f"\nHashtags: {prompt['hashtags']}")