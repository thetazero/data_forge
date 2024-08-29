from .prompt_maker import make_json_extract_prompt, column
from .open_ai import extract
from .web_scrape import get_text
from .parse_json import parse_json

import csv
import json
from typing import Any, NamedTuple, TypeVar


class DataForgeConfig(NamedTuple):
    answer_batch_size: int = 10


class ForgeResult(NamedTuple):
    raw_result: list[list[str]]
    parsed_result: list[dict[str, Any]]

    def to_csv(self, file_path: str):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(  # type: ignore
                file, fieldnames=self.parsed_result[0].keys())
            writer.writeheader()  # type: ignore
            for row in self.parsed_result:
                writer.writerow(row)  # type: ignore

    def to_json(self, file_path: str):
        with open(file_path, 'w') as file:
            json.dump(self.parsed_result, file, indent=4)


T = TypeVar('T')


def split_list(lst: list[T], n: int) -> list[list[T]]:
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def parse_raw_result(raw_result: list[str]) -> dict[str, Any]:
    data_list: list[dict[str, Any]] = [parse_json(data) for data in raw_result]
    all_data: dict[str, Any] = {}
    for data in data_list:
        all_data.update(data)
    return all_data


def forge(cols: list[column], urls: list[str], config: DataForgeConfig = DataForgeConfig()) -> ForgeResult:
    cols_list: list[list[column]] = split_list(cols, config.answer_batch_size)
    json_prompts: list[str] = [
        make_json_extract_prompt(cols) for cols in cols_list]

    raw_result: list[list[str]] = []
    for url in urls:
        raw_result.append(forge_url(json_prompts, url, config))

    parsed_res = [parse_raw_result(raw_res) for raw_res in raw_result]

    for i in range(len(parsed_res)):
        parsed_res[i]["url"] = urls[i]

    return ForgeResult(raw_result, parsed_res)


def forge_url(json_prompts: list[str], url: str, config: DataForgeConfig) -> list[str]:
    data = get_text(url)
    results: list[str] = []
    for prompt in json_prompts:
        results.append(extract(data, prompt))
    return results
