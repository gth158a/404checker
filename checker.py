import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer

site = "https://gradanalytics.georgetown.edu/"

try:
    html = urlopen(site)

except HTTPError as e:
    print(e)
# http = httplib2.Http()
# status, response = http.request('http://www.nytimes.com')
#


else:
    # for link in BeautifulSoup(html.read(), "lxml", parseOnlyThese=SoupStrainer('a')):
    #     if link.has_attr('href'):
    #         print(link['href'])
    soup = BeautifulSoup(html.read(), "lxml")

    #links = soup.findAll("a")

    # for link in links:
    #     if 'href' in link.attrs:
    #         print(link.get_text())
    #         print(link.attrs['href'])
# .find("div", {"id":"content"})

    # != "#main-content" or link.attrs['href'] != "#navigation_drawer"

    for link in soup.findAll("a", href=True):
#        if 'href' in link.attrs:
        print(link.get_text())
        if "http" in link.attrs['href']:
            print(link.attrs['href'])
            r = requests.get(link.attrs['href'])
            print(r.status_code)
        if  link.attrs['href'][0] == "/":
            print(site + link.attrs['href'])
            r = requests.get(site + link.attrs['href'][1:])
            print(r.status_code)





    # print(soup.title)