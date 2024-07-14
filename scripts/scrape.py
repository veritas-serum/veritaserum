import argparse
from pathlib import Path
from src.scraper import GoogleNewsScraper, AUTHORIZED_TOPICS

def cli_args():
    parser = argparse.ArgumentParser(
        "GoogleNews Scraper",
        "This script parses GoogleNews using Google News RSS feed."
    )
    parser.add_argument(
        "-f", 
        "--output-file", 
        help="Path where the scraped urls will be written.",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = cli_args()
    scraper = GoogleNewsScraper()
    urls = scraper.top_news()
    for topic in AUTHORIZED_TOPICS:
        urls += scraper.top_news_from_topic(topic)
    urls = list(set(urls))
    output_file = Path(args.output_file).open('a')

    for url in urls:
        output_file.write(url + "\n")