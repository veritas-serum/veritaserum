import feedparser

def retrieve_urls(url: str) -> list[str]:
        response = feedparser.parse(url)
        return [entry['link'] for entry in response['entries']]
