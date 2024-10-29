from http.cookiejar import CookieJar
import urllib.request as urllib2

def doIt(uri: str):
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    page = opener.open(uri)
    page.addheaders = [('User-agent', 'Mozilla/5.0')]
    print(page.read())

if __name__ == "__main__":
    doIt('https://www.fbi.gov/history/famous-cases/osama-bin-laden')
