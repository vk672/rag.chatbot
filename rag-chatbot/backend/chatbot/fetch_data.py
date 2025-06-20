import feedparser
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

def fetch_rss_entries():
    techcrunch_url = "https://techcrunch.com/feed/"
    feeds = [techcrunch_url]
    entries = []
    for url in feeds:
        feed = feedparser.parse(url)
        entries.extend(feed.entries)
    return entries

def fetch_article_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text() for p in paragraphs)
    except:
        return ""

def fetch_and_cache_articles():
    entries = fetch_rss_entries()
    articles = []
    for entry in entries:
        content = fetch_article_content(entry.link)
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "content": content
        })
    Path("data").mkdir(exist_ok=True)
    with open("data/cache.json", "w") as f:
        json.dump(articles, f, indent=2)
