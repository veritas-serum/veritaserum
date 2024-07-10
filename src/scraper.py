import feedparser
from src.article import Article 

AUTHORIZED_TOPICS = [
    "WORLD",
    "NATION",
    "BUSINESS",
    "TECHNOLOGY",
    "ENTERTAINMENT",
    "SPORTS",
    "SCIENCE ",
]

class GoogleNewsScraper:
    def __init__(self):
        self.lang_suffix = "hl=fr&gl=FR&ceid=FR:fr"
        self.query_suffix_template = "search?q={query}"
        self.base_url = "https://news.google.com/rss"
        self.topic_url_template = self.base_url + "/" + "headlines/section/topic/{topic}"


    def top_news(self) -> list[Article]:
        url = self.base_url + self.lang_suffix
        articles = self.retrieve_articles(url)
        return articles
        

    def query(self, query: str) -> list[Article]:
        query_suffix = self.query_suffix_template.format(query=query)
        url = self.base_url + query_suffix + "&" + self.lang_suffix
        articles = self.retrieve_articles(url)
        return articles


    def top_news_from_topic(self, topic: str) -> list[Article]:
        # topic in WORLD NATION BUSINESS TECHNOLOGY ENTERTAINMENT SPORTS SCIENCE 
        assert topic in AUTHORIZED_TOPICS
        url = self.topic_url_template.format(topic = topic) + self.lang_suffix
        articles = self.retrieve_articles(url)
        return articles
    
    def retrieve_articles(self, url: str) -> list[Article]:
        response = feedparser.parse(url)
        import ipdb; ipdb.set_trace()

