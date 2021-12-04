from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import random as r
import time
link = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=shoes&_sacat=0&LH_TitleDesc=0&_odkw=watch&_osacat=0"
link = link+"&pgn={page_number}"
products = []
prices = []
rates = []
hands = []
shippings = []
origins = []
solds = []
descriptions = []
for i in range(1, 3):
    link = link.format(page_number=i)
    # add time delay so that website thinks that you are a human, also add random time delay
    sec = r.randint(2, 7)
    time.sleep(sec)
    # request for webpage   , <Response [200]> only then web scraping
    page = requests.get(link)
    if str(page) != "<Response [200]>":
        # if rqeuest denied by website then show error
        print("ERROR", str(page)[11:14])
        break
    # parse the webpage and convert it a tree so that we can traverse
    soup = bs4(page.content, 'html.parser')

    for a in soup.find_all('li', class_="s-item"):

        name = a.find('h3', class_='s-item__title')
        if(name != None):
            name = name.get_text()

        price = a.find('span', class_='s-item__price')
        if(price != None):
            price = price.get_text()

        rate = a.find('span', class_='clipped')
        if(rate != None):
            rate = rate.get_text()

        hand = a.find('span', class_='SECONDARY_INFO')
        if(hand != None):
            hand = hand.get_text()

        shipping = a.find(
            'span', class_='s-item__shipping s-item__logisticsCost')
        if(shipping != None):
            shipping = shipping.get_text()

        origin = a.find('span', class_='s-item__location s-item__itemLocation')
        if(origin != None):
            origin = origin.get_text()

        sold = a.find('span', class_='BOLD')
        if(sold != None):
            sold = sold.get_text()

        des = a.find('div', class_='s-item__subtitle')
        if(des != None):
            des = des.get_text()

        products.append(name)
        prices.append(price)
        rates.append(rate)
        hands.append(hand)
        shippings.append(shipping)
        origins.append(origin)
        solds.append(sold)
        descriptions.append(des)
        
if str(page)=="<Response [200]>":
    df=pd.DataFrame({"Products":products,"Price":prices,"Rate":rates,"Usage":hands,"Shipping":shippings,"Origins":origins,"Solds":solds,"Description":descriptions})
    df.to_csv("C:/Users/manee/Desktop/ebay.csv", index=False)
