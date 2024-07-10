from src.scraper import GoogleNewsScraper, AUTHORIZED_TOPICS


if __name__ == "__main__":
    scraper = GoogleNewsScraper()
    urls = scraper.top_news()
    for topic in AUTHORIZED_TOPICS:
        urls += scraper.top_news_from_topic(topic)