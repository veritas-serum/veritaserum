import feedparser


if __name__ == "__main__":
    top_news_url = "https://news.google.com/rss?hl=fr&gl=FR&ceid=FR:fr"
    response = feedparser.parse(top_news_url)

    
    print(response)