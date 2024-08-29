from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from .cache import cache


def get_domain(url: str) -> str:
    return urlparse(url).netloc


def get_raw_text(url: str) -> str:
    caller = 'get-raw-text-v1'
    key = url
    cached_value = cache.get(caller, key)
    if cached_value:
        return cached_value

    page = urlopen(url)
    html = page.read().decode("utf-8")
    cache.set(caller, key, html)
    return html


def get_text(url: str) -> str:
    html = get_raw_text(url)
    soup = BeautifulSoup(html, "html.parser")
    return post_process(soup, get_domain(url))

def post_process(soup: BeautifulSoup, domain: str) -> str:
    procs = {
        "en.wikipedia.org": proc_wikipedia
    }
    if domain in procs:
        return procs[domain](soup)
    return soup.get_text()

def proc_wikipedia(soup: BeautifulSoup) -> str:
    div = soup.find("div", {"class": "mw-content-container"})
    if div:
        return div.get_text()
    return soup.get_text()
