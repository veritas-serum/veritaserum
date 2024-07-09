from src.article import Article 

class GoogleNewsScraper:
    def __init__(self):
        pass 

    def top_news(self) -> list[Article]:
        pass 

    def query(self, query: str) -> list[Article]:
        pass

    def top_news_from_topic(self, topic: str) -> list[Article]:
        # https://news.google.com/news/rss/headlines/section/topic/{topic}?hl=fr&gl=FR&ceid=FR:fr
        # topic in WORLD NATION BUSINESS TECHNOLOGY ENTERTAINMENT SPORTS SCIENCE HEALTH