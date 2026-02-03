import os
from dotenv import load_dotenv
load_dotenv()  # Load .env automatically


BUCKET_NAME = os.environ.get("BUCKET_NAME")
FACEBOOK_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID")
FACEBOOK_TOKEN = os.environ.get("FACEBOOK_TOKEN")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

PROMPT_TEMPLATES = [
    "Create a funny meme about {}",
    "Draw a creative cartoon poster for {}",
    "Generate an exciting image of {} in a comic style"
]

ENTERTAINMENT_TOPICS = [
    "Spider-Man", "Stranger Things", "Avengers",
    "The Simpsons", "Game of Thrones", "Marvel Heroes",
    "DC Heroes", "Friends TV show"
]
