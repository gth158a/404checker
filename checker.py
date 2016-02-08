import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

start = "http://analytics.ncsu.edu/"
# "http://analytics.ncsu.edu/?page_id=1948"
# "https://gradanalytics.georgetown.edu/"

pages = set()  # pages collected in current site
pagesError = set()  # url of pages with issues
visitedPages = set()  # url of pages visited (promoted to site)


def checklinks(site):
    global visitedPages
    global pages
    global pagesError

    try:
        html = urlopen(site)

    except HTTPError as e:
        print(e)

    else:
        visitedPages.add(site)
        soup = BeautifulSoup(html.read(), "lxml")

        links = soup.find("div", { "class" : "primary" }).findAll("a", href=True)
        # numberlinks = len(links) # something that can be used for reporting later
        # print(len(links))

        for link in links:
            page = link.get_text().strip(' \t\n\r')

            if "http" in link.attrs['href']:
                address = link.attrs['href']

            # if internal link
            elif  link.attrs['href'].startswith("/"):
                address = site + link.attrs['href'][1:]

            else:
                address = link.attrs['href']


            if address not in pages:
                if address.startswith("mailto:"):
                    status = "null"
                else:
                    r = requests.get(address)
                    status = r.status_code
                pages.add(address)
                print(str(status) + " - " + page + " - " + address)
                if r.status_code != requests.codes.ok:
                    pagesError.add(address)
                else:
                    print("address: " + address)
                    print(len(visitedPages))
                    print("visited pages: " + str(visitedPages))
                    print("Pages Error: " + str(len(pagesError)))
                    if address not in visitedPages:
                        if address.startswith("http://analytics.ncsu.edu/") and not address.endswith(".pdf") and not address.endswith(".jpg"):
                            checklinks(address)

checklinks(start)






    # print(soup.title)