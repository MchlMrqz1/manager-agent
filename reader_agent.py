import json
from collections import Counter
from datetime import datetime
import re
import os

TRENDS_FILE = "trends.json"
KEYWORDS_FILE = "keywords.json"

def load_latest_trends():
    try:
        with open(TRENDS_FILE, "r") as f:
            history = json.load(f)

        if not history:
            print("No trend data found.")
            return

        latest = history[-1]
        timestamp = latest["timestamp"]
        titles = [t["title"] for t in latest["trends"]]

        print(f"\nLatest trends as of {timestamp}:\n")
        extract_keywords(titles, timestamp)

    except FileNotFoundError:
        print(f"File {TRENDS_FILE} not found.")
    except Exception as e:
        print(f"Error reading trends: {e}")

def extract_keywords(titles, timestamp):
    print("\n🔍 Extracted Keywords:\n")

    words = []
    for title in titles:
        clean = re.sub(r"[^\w\s]", "", title.lower())
        words.extend(clean.split())

    stop_words = {
        "the", "and", "in", "of", "to", "a", "on", "for", "is", "how",
        "with", "its", "new", "this", "by", "at", "from", "are", "as"
    }

    filtered = [word for word in words if word not in stop_words and len(word) > 2]
    counter = Counter(filtered)
    most_common = counter.most_common(10)

    for word, freq in most_common:
        print(f"{word}: {freq}")

    # Save to keywords.json
    entry = {
        "timestamp": timestamp,
        "keywords": [{"word": w, "count": c} for w, c in most_common]
    }

    if os.path.exists(KEYWORDS_FILE):
        with open(KEYWORDS_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(KEYWORDS_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print("\n✅ Keywords saved to keywords.json")

if __name__ == "__main__":
    load_latest_trends()
