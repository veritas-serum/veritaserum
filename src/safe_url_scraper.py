import httpx
import asyncio
from urllib.parse import urlparse, quote_plus
from typing import List, Dict
from collections import defaultdict
import random

USER_AGENTS: List[str] = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
]

async def load_url(client: httpx.AsyncClient, url: str) -> str:

    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    try:
        response = await client.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return f"Error: HTTP {e.response.status_code}"
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {url}: {e}")
        return f"Error: {str(e)}"

def safe_filename(url: str) -> str:
    return quote_plus(url)

async def process_domain(urls: List[str]):
    async with httpx.AsyncClient() as client:
        for url in urls:
            content = await load_url(client, url)
            filename = safe_filename(url)
            with open(f"{filename}.html", "w", encoding="utf-8") as f:
                f.write(content)
            await asyncio.sleep(random.uniform(2, 5))

async def scrape_urls(url_list: List[str]):
    # Group URLs by domain
    domain_urls: Dict[str, List[str]] = defaultdict(list)
    for url in url_list:
        domain = urlparse(url).netloc
        domain_urls[domain].append(url)

    # Create and run tasks for each domain
    tasks = [asyncio.create_task(process_domain(urls)) 
             for _, urls in domain_urls.items()]
    await asyncio.gather(*tasks)

# Example usage
url_list: List[str] = [
    'https://example.com',
    'https://example.org',
    'https://example.net',
    'https://example.com/page2',  # Same domain as the first URL
    'https://another-example.com',
    'https://yet-another-example.com'
]

async def main():
    await scrape_urls(url_list)
    print("Scraping completed.")

if __name__ == "__main__":
    asyncio.run(main())