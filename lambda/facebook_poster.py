import requests
from config import FACEBOOK_PAGE_ID, FACEBOOK_TOKEN

def post_to_facebook(image_bytes, caption: str) -> dict:
    url = f"https://graph.facebook.com/v24.0/{FACEBOOK_PAGE_ID}/photos"
    files = {"source": image_bytes}
    data = {"caption": caption, "access_token": FACEBOOK_TOKEN}
    r = requests.post(url, files=files, data=data, timeout=30)
    return r.json()
