from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

#https://gradanalytics.georgetown.edu
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://analytics.ncsu.edu/?"+pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    # re.compile("^(/[a-z]*/)"))
    for link in bsObj.findAll("a", href=True):
        #if 'href' in link.attrs:
        if link.attrs['href'] not in pages:
            # We have encountered a new page
            newPage = link.attrs['href']
            print("New Page")
            #print(newPage)
            pages.add(newPage)
            print("new Page: " + newPage)
            newLink = urlparse(newPage).query
            print(newLink)
            if not newLink.endswith('.pdf'):

                getLinks(newLink)

getLinks("")
print(len(pages))
print(pages)

#div.primary
#using urlparse.urljoin() for this