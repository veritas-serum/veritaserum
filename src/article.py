from typing import Optional 
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

import article_parser


@dataclass_json
@dataclass
class Article:
    url: str # only this field is mandatory
    # title and content are instanciated by the url parser
    title: Optional[str] = None 
    content: Optional[str] = None
    # suggested_title is instanciated by the LLM
    suggested_title: Optional[str] = None 
    # a metadata dict that should be further thought of
    metadata: Optional[dict] = field(default_factory=dict)

def parse_url(url: str) -> Article:
    title, content = article_parser.parse(url=url, output='markdown', timeout=5)
    return Article(url=url, title=title, content=content)