from .prompt_maker import make_json_extract_prompt, column
from .open_ai import extract
from .web_scrape import get_text
from .parse_json import parse_json

from typing import Any, NamedTuple

class ForgeResult(NamedTuple):
    raw_result: list[str]
    parsed_result: list[dict[str, Any]]

    def to_csv(self):
        pass

    def to_json(self):
        pass


def forge(cols: list[column], urls: list[str]) -> ForgeResult:
    json_prompt = make_json_extract_prompt(cols)
    raw_result: list[str] = []
    for url in urls:
        raw_result.append(forge_url(json_prompt, url))

    parsed_res: list[dict[str, Any]] = [parse_json(data) for data in raw_result]

    for i in range(len(parsed_res)):
        parsed_res[i]["url"] = urls[i]

    return ForgeResult(raw_result, parsed_res)


def forge_url(json_prompt: str, url: str) -> str:
    data = get_text(url)
    return extract(data, json_prompt)
