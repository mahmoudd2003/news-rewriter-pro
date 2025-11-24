import requests
from slugify import slugify
import os

def publish_to_wordpress(title, content):
    url = f"{os.getenv('WP_URL')}/wp-json/wp/v2/posts"

    auth = (os.getenv("WP_USER"), os.getenv("WP_APP_PASSWORD"))

    data = {
        "title": title,
        "content": content,
        "status": "draft"
    }

    r = requests.post(url, json=data, auth=auth)
    
    try:
        return r.json()
    except:
        return {"error": "Invalid response", "raw": r.text}
