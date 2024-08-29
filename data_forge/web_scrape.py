from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_text(url: str):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Osama_bin_Laden"
    print(get_text(url))
