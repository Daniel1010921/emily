from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Function to scrape a single story
def scrape_story(url):
    driver.get(url)
    time.sleep(3)  # Allow JavaScript to load

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract story title
    title = soup.select_one("h1").text.strip()

    # Extract story content (Now selecting <div class="mt-4"> instead of previous incorrect selector)
    paragraphs = soup.select("div.mt-4 p")
    if not paragraphs:
        paragraphs = soup.select("div[class*='content'] p")  # Alternative selector

    content = "\n".join([p.text.strip() for p in paragraphs])

    return {"title": title, "content": content}

# Load previously scraped story links
with open("storymami_story_links.json", "r", encoding="utf-8") as file:
    stories = json.load(file)

# Scrape all stories
story_data = []
for story in stories:
    print(f"Scraping: {story['url']}")
    story_details = scrape_story(story["url"])
    story_data.append(story_details)
    time.sleep(2)  # Avoid bot detection

# Save to JSON
output_file = "storymami_stories.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(story_data, file, ensure_ascii=False, indent=4)

print(f"Scraped {len(story_data)} stories and saved to '{output_file}'")

# Close WebDriver
driver.quit()
