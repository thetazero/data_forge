from .prompt_maker import make_json_extract_prompt, column
from .open_ai import extract
from .web_scrape import get_text
from .parse_json import parse_json

from typing import Any


def forge(cols: list[column], urls: list[str]):
    json_prompt = make_json_extract_prompt(cols)
    res: list[str] = []
    for url in urls:
        res.append(forge_url(json_prompt, url))

    print(res)
    parsed_res: list[dict[str, Any]] = [parse_json(data) for data in res]

    for i in range(len(parsed_res)):
        parsed_res[i]["url"] = urls[i]
    return parsed_res


def forge_url(json_prompt: str, url: str) -> str:
    data = get_text(url)
    return extract(data, json_prompt)
