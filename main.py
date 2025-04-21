import requests
import time
from datetime import datetime
import json
import os

NEWS_API_KEY = "f48540aeefa8455ba1216a42ee88087b"
NEWS_API_URL = "https://newsapi.org/v2/everything"
TRENDS_FILE = "trends.json"

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
    trends = []

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for i, article in enumerate(articles, 1):
            title = article['title']
            url = article['url']
            published_at = article['publishedAt']

            log(f"Trend {i}: {title}")
            log(f"URL: {url}")

            trends.append({
                "title": title,
                "url": url,
                "published_at": published_at
            })

        save_trends(trends)
    else:
        log(f"Failed to fetch trends. Status code: {response.status_code}")

def save_trends(trends):
    timestamp = datetime.now().isoformat()
    data = {
        "timestamp": timestamp,
        "trends": trends
    }

    if os.path.exists(TRENDS_FILE):
        with open(TRENDS_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(data)

    with open(TRENDS_FILE, "w") as f:
        json.dump(history, f, indent=2)

    log("Saved trends to trends.json")

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
