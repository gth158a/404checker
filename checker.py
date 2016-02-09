import requests
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import HTML

start = ""


def generatereport(tdata):
    # open an HTML file to show output in a browser
    HTMLFILE = 'report.html'
    f = open(HTMLFILE, 'w')


    htmlcode = HTML.table(tdata,
        header_row=['Status Code', 'Link Text', 'Address'])
    #print(htmlcode)
    f.write(htmlcode)
    f.write('<p>')
    #print('-'*79)
    f.close()


def checklinks(page):
    results = []

    try:
        html = urlopen(page)

    except HTTPError as e:
        print(e)

    else:
        base = urlparse(page) # this could be handy in case of a relative link

        soup = BeautifulSoup(html.read(), "lxml")
        links = soup.find("div", { "id" : "content" }).findAll("a", href=True)
        print("Number of links: " + str(len(links)))

        for link in links:
            page_name = link.get_text().strip(' \t\n\r') # trims spaces of link description
            q = urlparse(link.attrs['href'])

            # if internal link
            if  link.attrs['href'].startswith("../"):
                # build absolute address
                address = base.scheme + "://" + base.netloc + "/?" + q.query

            #if external
            else:
                address = q.geturl()
                if q.scheme == "mailto":
                    # avoid checking status of mailto protocol
                    status = "null"
                else:
                    status = requests.get(address).status_code

            results.append([str(status), page_name, address])
            #print(str(status) + " - " + page + " - " + address)

        generatereport(results)


checklinks(start)
