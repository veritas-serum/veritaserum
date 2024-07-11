import pytest 
from pathlib import Path 

from src.article import Article, parse_url
from src.utils import normalized_ed

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
    dist_btw_titles = normalized_ed(expected_article.title, parsed_article.title)
    dist_btw_contents = normalized_ed(expected_article.content, parsed_article.content)

    assert dist_btw_titles <= 0.5
    assert dist_btw_contents <= 0.5
    