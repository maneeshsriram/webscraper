from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import csv
import time
import random as r
names = []
reviews = []
keywords = []
link = "https://www.flipkart.com/apple-iphone-se-black-64-gb/product-reviews/itm4d3d5718a5c95?pid=MOBFWQ6BR3MK7AUG&lid=LSTMOBFWQ6BR3MK7AUGGHSWQD&marketplace=FLIPKART"
link = link.replace("/p/", "/product-reviews/")
link = link+"&page={page_number}"
for i in range(1, 7):    # number of page number
    link = link.format(page_number=i)
    # request for webpage   , <Response [200]> only then web scraping
    page = requests.get(link)
    # add time delay so that website thinks that you are a human, also add random time delay
    sec = r.randint(2, 7)
    time.sleep(sec)
    # parse the webpage and convert it a tree so that we can traverse
    soup = bs4(page.content, 'html.parser')

    for a in soup.find_all('div', class_="col _2wzgFH K0kLPL"):

        name = a.find('p', class_='_2sc7ZR _2V5EHH')
        if(name != None):
            name = name.get_text()

        review = a.find('div', class_='t-ZTKy')
        if(review != None):
            review = review.get_text()

        keyword = a.find('p', class_='_2-N8zT')
        if(keyword != None):
            keyword = keyword.get_text()

        names.append(name)
        reviews.append(review)
        keywords.append(keyword)
df = pd.DataFrame({"names": names, "reviews": reviews, "keywords": keywords})
df.to_csv("C:/Users/manee/Desktop/flipkart_review.csv", index=False)
