import json
from datetime import datetime

TRENDS_FILE = "trends.json"

def load_latest_trends():
    try:
        with open(TRENDS_FILE, "r") as f:
            history = json.load(f)

        if not history:
            print("No trend data found.")
            return

        latest = history[-1]
        timestamp = latest["timestamp"]
        trends = latest["trends"]

        print(f"Latest trends as of {timestamp}:\n")

        for i, trend in enumerate(trends, 1):
            print(f"{i}. {trend['title']}")
            print(f"   URL: {trend['url']}\n")

    except FileNotFoundError:
        print(f"File {TRENDS_FILE} not found.")
    except Exception as e:
        print(f"Error reading trends: {e}")

if __name__ == "__main__":
    load_latest_trends()
