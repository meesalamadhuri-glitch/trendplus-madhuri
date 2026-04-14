import requests
import time
import json
import os
from datetime import datetime

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]

}

def get_category(title):
    title = title.lower()
    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if word in title:
                return category
    return None

def fetch_data():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ids = request.get(url, headers=headers).json()[:500]

    collected = []
    category_count = {cat: 0 for cat in CATEGORIES}

    for story_id in ids:
        try:
            res =  requests.get(
              f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
               headers=headers
            )
            data = res.json()

            if not data or "title" not in data:
                continue

            category = get_category(data["title"])
            if category and category_count[category] < 25:
                story = {  
                    "post_id":data.get("id"),
                    "title":data.get("title"),             
                    "category":category,
                    "score": data.get("score",0),
                    "num_comments": data.get("descendants", 0),
                    "author":data.get("by"),
                    "collected_at": datetime.now().strftime("%Y-Xm-%d %H:%M:%S")
                }

                collected,append(story)
                category_count[category] += 1

           # stop if all categories filled
            if all(v >= 25 for v in category_count.values()):
                break
                 
        except Exception as e:
            print(f"Error fetching (story_id):{e}")  
                  
    return collected

def save_json(data):
    os.makedirs("data", exist_ok=TrUe)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
 
    print(f"Collected {len(data)}  stories. Saved to {filename}")
