import requests
import time
from datetime import datetime

# Replace with your actual NewsAPI key
NEWS_API_KEY = "f48540aeefa8455ba1216a42ee88087b"
NEWS_API_URL = "https://newsapi.org/v2/everything"

def get_ai_music_trends():
    log("Searching for 'AI music' trends...")
    params = {
        "q": "AI music",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for i, article in enumerate(articles, 1):
            log(f"Trend {i}: {article['title']}")
            log(f"URL: {article['url']}")
    else:
        log(f"Failed to fetch trends. Status code: {response.status_code}")

def log(message):
    with open("log.txt", "a") as file:
        file.write(f"[{datetime.now()}] {message}\n")
    print(f"[{datetime.now()}] {message}")

def run_manager():
    log("===== 2nzAI Manager Agent Run Started =====")
    get_ai_music_trends()
    log("===== Run Complete =====\n")

if __name__ == "__main__":
    run_manager()
