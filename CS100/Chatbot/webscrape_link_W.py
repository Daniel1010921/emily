import requests
from bs4 import BeautifulSoup
import json

# Base URL of the website
base_url = "https://www.storymami.com"
category_url = base_url + "/category/fairy-tales"  # Change to the actual category page

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(category_url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Extract story links
stories = []
for link in soup.find_all("a", href=True, title=True):
    story_url = link["href"]
    story_title = link["title"]
    
    # Extract image URL (if available)
    img_tag = link.find("img")
    image_url = base_url + img_tag["src"] if img_tag else "No Image"

    # Store extracted data
    stories.append({
        "title": story_title,
        "url": story_url,
        "image": image_url
    })

# Save to JSON
output_file = "storymami_story_links.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(stories, file, ensure_ascii=False, indent=4)

print(f"Scraped {len(stories)} story links and saved to '{output_file}'")
