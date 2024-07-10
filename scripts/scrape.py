from src.scraper import GoogleNewsScraper


if __name__ == "__main__":
    scraper = GoogleNewsScraper()
    articles = scraper.top_news()