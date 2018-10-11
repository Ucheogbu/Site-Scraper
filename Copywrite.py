import requests
from bs4 import BeautifulSoup
import tkinter as tk


def get_url():
    # get the webPage to be scraped from user

    url = input(r'Type the url of the web page you want to scrape: ')
    return url


def check_url(url):
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

    return url


def get_site(url):
    # create a request object linked to the page to be scraped
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        return soup
    # catch any exception raised if web page cannot be assessed
    # maybe due to incorrect url, bad internet etc
    except Exception:
        print('Page not found, check the url given or check internet connection and try again')




def get_information(soup):
    lookup = input('what html element do you want to see: type a for links, img for images, p for paragraph'
                   'h1,h2, for headers, type all if you want to scrape everything on the page'
                   '  type complete if you want to see the complete html of the page: ')
    if lookup == "a":
        links = soup.find_all("a")
        for link in links:
            a = '<a href="%s">%s</a>'
            b = (link.get("href"), link.text)
            a1 = link.text
            a2 = (a % b)
            result = a1 + '\n' + a2 + '\n'
            print(result)
    elif lookup == "p":
        para = soup.find_all("p")
        for a in para:
            result = a.text + '\n'
            print(result)
    elif lookup == "h1":
        h = soup.find_all("h1")
        for a in h:
            result = a.text + '\n'
            print(result)
    elif lookup == "h2":
        hi = soup.find_all("h2")
        for a in hi:
            result = a.text + '\n'
            print(result)
    elif lookup == "img":
        imgs = soup.find_all("img")
        for img in imgs:
            img_source = img.get("href")
            img_text = img.text
            result = img_source + '\n' + img_text
            print(result)
    elif lookup == "all":
        links = soup.find_all("a")
        for link in links:
            a = '<a href="%s">%s</a>'
            b = (link.get("href"), link.text)
            a1 = link.text
            a2 = (a % b)
            result = a1 + '\n' + a2 + '\n'
            print(result)
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


def run_gui():
    t = tk.Tk()
    header = tk.Label(master=t, text='Copywrite')
    header.pack()

    t.mainloop()


def main():
        try:
            url = get_url()
            soup = get_site(url)
            get_information(soup)
        except Exception:
            main()


if __name__ == '__main__':
    main()

