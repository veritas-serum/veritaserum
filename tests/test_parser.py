import pytest 
from pathlib import Path 

from src.article import Article, parse_url

@pytest.mark.parametrize(
        "article_path",
        [
            "tests/data/00_test_article.json",
            "tests/data/01_test_article.json",
            "tests/data/02_test_article.json",
        ]
)
def test_parse_url(article_path: str):
    expected_article = Article.from_json(Path(article_path).read_text())
    parsed_article = parse_url(expected_article.url)
    
    assert expected_article.title == parsed_article.title
    assert expected_article.content == parsed_article.content