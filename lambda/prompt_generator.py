import random
from config import PROMPT_TEMPLATES, ENTERTAINMENT_TOPICS

def generate_prompt() -> str:
    topic = random.choice(ENTERTAINMENT_TOPICS)
    template = random.choice(PROMPT_TEMPLATES)
    return template.format(topic)
