from urllib.request import urlopen
from bs4 import BeautifulSoup
from .cache import cache

def get_text(url: str):
    caller = 'get-text-v1'
    key = url
    cached_value = cache.get(caller, key)
    if cached_value:
        return cached_value


    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    result = soup.get_text()
    cache.set(caller, key, result)
    return result


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Osama_bin_Laden"
    print(get_text(url))
