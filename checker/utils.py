import hashlib

import requests
import ua_generator


def get_website_hash(website_url: str) -> str:
    website_url = website_url.lower()

    if not website_url.startswith("http"):
        website_url = "https://" + website_url

    ua = ua_generator.generate()

    website_content = requests.get(website_url, headers=ua.headers.get()).content
    website_hash = hashlib.sha256(website_content).hexdigest()

    return website_hash
