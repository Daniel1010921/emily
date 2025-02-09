import requests
from bs4 import BeautifulSoup

# Define the URL of the article
url = "https://today.line.me/tw/v2/article/5qQYq7"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract article title
    title = soup.find("h1")
    title_text = title.text.strip() if title else "Title not found"

    # Extract article content (paragraphs)
    paragraphs = soup.find_all("p")
    article_content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

    # Output extracted data
    extracted_data = {
        "title": title_text,
        "content": article_content
    }

    # Save extracted data to a JSON file
    import json
    with open("line_today_article.json", "w", encoding="utf-8") as file:
        json.dump(extracted_data, file, ensure_ascii=False, indent=4)

    print(f"Article extracted and saved to 'line_today_article.json'")
    print("Title:", title_text)
    print("\nArticle Content:\n", article_content[:500], "...")  # Displaying first 500 chars

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
