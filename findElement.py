#coding=utf-8
'''
@author: DMao
@time: 15.09.18    20:36

Webpage structure:
every page has article block (emoji, title, content, pic)
at bottom of every page there is a next button linking to next web page
the last web page has no next button

'''


import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin





class CrawedArticle():
    def __init__(self, emoji, content, title,img):
        self.emoji = emoji
        self.content = content
        self.title = title
        self.img = img




class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        article = []

        while url != "" :
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")




            for card in doc.select(".card"):  # select html all stuffs with class=card, css selector
                #print(card.select(".emoji")) # get in form of list

                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title_span = card.select(".card-title span") # crawl the class card-title all span elememts, return in list form
                title = title_span[1].text
                img = urljoin(url, card.select_one("img").attrs["src"])

                #print(title_span)
                #print(emoji)
                #print(content)
                #print(title)
                #print(img) # .attrs return a dic back
                crawled = CrawedArticle(emoji, content, title, img)
                article.append(crawled)

            next_button = doc.select_one(".navigation .btn")
            if next_button:
                next_href = next_button.attrs["href"] # button NEXT PAGE
                next_link = urljoin(url, next_href)
                print("next button: ", next_link)
                url = next_link
            else:
                url = "" # the last page has no next button

        return article

fetcher = ArticleFetcher()
articles = fetcher.fetch()

for article in articles:
    print(article.emoji + " " + article.title + " " + article.img)

