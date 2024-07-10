import feedparser

AUTHORIZED_TOPICS = [
    "WORLD",
    "NATION",
    "BUSINESS",
    "TECHNOLOGY",
    "ENTERTAINMENT",
    "SPORTS",
    "SCIENCE",
]

class GoogleNewsScraper:
    def __init__(self):
        self.lang_suffix = "?hl=fr&gl=FR&ceid=FR:fr"
        self.query_suffix_template = "search?q={query}"
        self.base_url = "https://news.google.com/rss"
        self.topic_url_template = self.base_url + "/" + "headlines/section/topic/{topic}"


    def top_news(self) -> list[str]:
        url = self.base_url + self.lang_suffix
        retrieved_urls = self.retrieve_urls(url)
        return retrieved_urls
        

    def query(self, query: str) -> list[str]:
        query_suffix = self.query_suffix_template.format(query=query)
        url = self.base_url + query_suffix + "&" + self.lang_suffix
        retrieved_urls = self.retrieve_urls(url)
        return retrieved_urls


    def top_news_from_topic(self, topic: str) -> list[str]:
        # topic in WORLD NATION BUSINESS TECHNOLOGY ENTERTAINMENT SPORTS SCIENCE 
        assert topic in AUTHORIZED_TOPICS
        url = self.topic_url_template.format(topic = topic) + self.lang_suffix
        retrieved_urls = self.retrieve_urls(url)
        return retrieved_urls
    
    def retrieve_urls(self, url: str) -> list[str]:
        response = feedparser.parse(url)
        output_urls = []
        for entry in response['entries']:
            output_urls.append(entry['link'])
        return output_urls

