import requests
from bs4 import BeautifulSoup


# get the webpage to be scraped from user

url = input(r'Type the url of the web page you want to scrape: ')

# check if user typed something
while 1:
    if url == '':
        print('Url cannot be blank!! Type a url please!!! ')
        url = input(r'Type the url of the web page you want to scrape: ')
    elif url != '':
        break


if r'http://' in url:
    url = r"%s" % url
elif r'https://' in url:
    url = r"%s" % url
else:
    url = r"http://" + r"%s" % url

# create a request object linked to the page to be scraped

try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
# catch any exception raised if web page cannot be assessed
# maybe due to incorrect url, bad internet etc
except Exception:
    print('Page not found, check the url given or check internet connection')
    exit(1)

# get the tag the user wants to scrape
lookup = input('what html element do you want to see: type a for links, img for images, p for paragraph'
               'h1,h2, for headers, type all if you want to scrape everything on the page'
               '  type complete if you want to see the complete html of the page: ')
if lookup == "a":
    links = soup.find_all("a")
    for link in links:
        a = '<a href="%s">%s</a>'
        b = (link.get("href"), link.text)
        print(link.text)
        print(a % b)
        print('\n')
elif lookup == "p":
    para = soup.find_all("p")
    for a in para:
        print(a.text + '\n')
elif lookup == "h1":
    h = soup.find_all("h1")
    for a in h:
        print(a.text + '\n')
elif lookup == "h2":
    hi = soup.find_all("h2")
    for a in hi:
        print(a.text + '\n')
elif lookup == "img":
    imgs = soup.find_all("img")
    for img in imgs:
        img_source = img.get("href")
        img_text = img.text
        print(img_source + '\n' + img_text)
elif lookup == "all":
    links = soup.find_all("a")
    for link in links:
        a = '<a href="%s">%s</a>'
        b = (link.get("href"), link.text)
        print(link.text)
        print(a % b)
        print('\n')
    para = soup.find_all("p")
    for a in para:
        print(a.text + '\n')
    h = soup.find_all("h1")
    for a in h:
        print(a.text + '\n')
    hi = soup.find_all("h2")
    for a in hi:
        print(a.text + '\n')
    imgs = soup.find_all("img")
    for img in imgs:
        img_source = img.get("href")
        img_text = img.text
        print(img_source + '\n' + img_text)
elif lookup == "complete":
    print(soup.prettify())
