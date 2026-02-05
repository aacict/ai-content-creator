import os
from dotenv import load_dotenv
load_dotenv()  # Load .env automatically


BUCKET_NAME = os.environ.get("BUCKET_NAME")
FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
FACEBOOK_TOKEN = os.environ.get("FACEBOOK_TOKEN")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# Content themes with variety
CONTENT_THEMES = {
    "relatable_humor": {
        "topics": [
            "Monday morning energy vs Friday afternoon energy",
            "Coffee before vs after",
            "My plans vs what actually happens",
            "How I think I look vs tagged photos",
            "Online shopping: expectation vs reality",
            "Gym motivation vs actual gym performance",
            "My diet plan vs 2am me",
            "Checking bank account after weekend",
            "Replying to texts: me vs everyone else",
            "Waking up for work vs waking up on weekend"
        ],
        "image_style": "split comparison meme, cartoon style, exaggerated expressions, bold vibrant colors, funny",
        "hashtags": "#Relatable #Funny #Memes #SoTrue #Mood #Comedy"
    },
    
    "nostalgia": {
        "topics": [
            "Remember when phones had physical keyboards",
            "The sound of dial-up internet connecting",
            "Rewinding VHS tapes before returning to Blockbuster",
            "Burning CDs for your crush",
            "Playing outside until the streetlights came on",
            "Waiting for your favorite song on the radio",
            "Using a paper map for road trips",
            "The excitement of getting AOL mail",
            "Saturday morning cartoons ritual",
            "MySpace top 8 drama"
        ],
        "image_style": "retro vintage poster, 90s aesthetic, nostalgic warm colors, grain texture, classic typography",
        "hashtags": "#Nostalgia #90sKids #Throwback #MemoryLane #GoodOldDays #Vintage"
    },
    
    "trending": {
        "topics": [
            "AI trying to write emails like a human",
            "Everyone suddenly starting a podcast in 2024",
            "Side hustle culture is out of control",
            "Trying to be productive vs endless scrolling",
            "ChatGPT doing your homework",
            "When the WiFi goes out and you remember books exist",
            "Influencer vs reality behind the scenes",
            "Working from home: pajamas on top, professional on camera",
            "Streaming services: paying for 5 to watch 1",
            "Gen Z teaching Millennials new slang"
        ],
        "image_style": "modern digital art, trendy aesthetic, meme format, contemporary colors, relatable humor",
        "hashtags": "#Trending #Viral #CurrentMood #2024 #Relatable #Modern"
    },
    
    "motivational": {
        "topics": [
            "Small progress is still progress",
            "It's okay to rest without feeling guilty",
            "Your journey is unique, stop comparing",
            "Celebrate tiny wins every day",
            "Done is better than perfect",
            "You're doing better than you think",
            "Self-care isn't selfish",
            "Growth happens outside comfort zones",
            "Mistakes are proof you're trying",
            "Your vibe attracts your tribe"
        ],
        "image_style": "soft pastel colors, minimalist design, calming aesthetic, inspirational typography, gentle illustrations",
        "hashtags": "#Motivation #SelfCare #Positivity #MentalHealth #Growth #Inspiration"
    },
    
    "fun_facts": {
        "topics": [
            "Octopuses have three hearts",
            "Honey never spoils - archaeologists found edible honey in ancient tombs",
            "Bananas are berries but strawberries aren't",
            "You can't hum while holding your nose",
            "A group of flamingos is called a flamboyance",
            "The inventor of the Pringles can is buried in one",
            "Sharks are older than trees",
            "There's a planet made entirely of diamonds",
            "Your brain uses 20% of your body's energy",
            "The shortest war lasted 38 minutes"
        ],
        "image_style": "colorful infographic style, fun illustrations, educational but entertaining, bold text, eye-catching design",
        "hashtags": "#DidYouKnow #FunFacts #Learning #Interesting #MindBlown #Education"
    },
    
    "pop_culture": {
        "topics": [
            "When your favorite character gets killed off",
            "Binge watching vs waiting weekly for episodes",
            "Movie theater popcorn hits different",
            "Finding out your comfort show got cancelled",
            "When the book was better than the movie",
            "Rewatching the same show for the 10th time",
            "Getting emotionally attached to fictional characters",
            "Post-series depression is real",
            "When a new season drops and you cancel all plans",
            "Soundtrack so good you Shazam during credits"
        ],
        "image_style": "pop art comic style, vibrant colors, dynamic composition, entertainment theme, bold graphics",
        "hashtags": "#PopCulture #Entertainment #TVShows #Movies #Binge #Streaming"
    }
}

# Weekly schedule for variety
WEEKLY_SCHEDULE = {
    0: "motivational",      # Monday - need that motivation
    1: "relatable_humor",   # Tuesday - mid-week humor
    2: "fun_facts",         # Wednesday - hump day learning
    3: "trending",          # Thursday - catch trends
    4: "nostalgia",         # Friday - wind down vibes
    5: "pop_culture",       # Saturday - entertainment
    6: "relatable_humor"    # Sunday - Sunday scaries humor
}