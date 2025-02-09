import requests
from bs4 import BeautifulSoup
import json
import time

# Base URL of YueduFeng
base_url = "https://www.gushi365.com/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to scrape story links from the homepage
def get_story_links():
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    story_links = []

    # Find all story links on the homepage
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.startswith("/"):
            story_links.append(base_url + href)

    return story_links

# Function to scrape individual story content
def scrape_story(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract story title
    title = soup.find("h1")
    title_text = title.text.strip() if title else "No Title"

    # Extract story content
    content_div = soup.find("div", class_="post-content")
    paragraphs = content_div.find_all("p") if content_div else []
    content_text = "\n".join(p.text.strip() for p in paragraphs)

    return {"title": title_text, "content": content_text}

# Main function to scrape multiple stories
def scrape_stories():
    story_links = get_story_links()
    stories = []

    for link in story_links:
        story = scrape_story(link)
        stories.append(story)
        time.sleep(1)  # Respectful delay between requests

    return stories

# Scrape stories and save to JSON
stories = scrape_stories()
output_file = "yuedufeng_stories.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(stories, file, ensure_ascii=False, indent=4)

print(f"Scraped {len(stories)} stories and saved to '{output_file}'")
