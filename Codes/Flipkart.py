from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import csv
import time
import random as r
link="https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
link=link+"&page={page_number}"
products=[]
prices=[]
rates=[]
no_of_rates=[]
quantities=[]
des=[]
for i in range(1,2): # page number u can modify
    link=link.format(page_number=i)
    sec=r.randint(2,7)   # add time delay so that website thinks that you are a human, also add random time delay
    time.sleep(sec)
    page=requests.get(link)    #request for webpage   , <Response [200]> only then web scraping
    if str(page)!="<Response [200]>":
        print("ERROR",str(page)[11:14])          # if rqeuest denied by website then show error
        break
    soup=bs4(page.content,'html.parser') # parse the webpage and convert it a tree so that we can traverse
    for a in soup.find_all('div',class_="_4ddWXP"):
   
        name=a.find('a',class_='s1Q9rs')
        if(name!=None):
            name=name.get_text()

        price=a.find('div',class_='_30jeq3')
        if(price!=None):
            price=price.get_text()

        rate=a.find('div',class_='_3LWZlK')
        if(rate!=None):
            rate=rate.get_text()

        no_of_rate=a.find('span',class_='_2_R_DZ')
        if(no_of_rate!=None):
            no_of_rate=no_of_rate.get_text()

        quantity=a.find('div',class_='_3Djpdu')
        if(quantity!=None):
            quantity=quantity.get_text()



        products.append(name)
        prices.append(price)
        rates.append(rate)
        no_of_rates.append(no_of_rate)
        quantities.append(quantities)
    for a in soup.find_all('div',class_="_1xHGtK _373qXS"):

            name=a.find('a',class_=['IRpwTa _2-ICcC','IRpwTa'])
            if(name!=None):
                name=name.get_text()

            price=a.find('div',class_='_30jeq3')
            if(price!=None):
                price=price.get_text()

            de=a.find('div',class_='_3eWWd-')
            if(de!=None):
                de=de.get_text()

            rate=a.find('div',class_='_3LWZlK')
            if(rate!=None):
                rate=rate.get_text()

            no_of_rate=a.find('span',class_='_2_R_DZ')
            if(no_of_rate!=None):
                no_of_rate=no_of_rate.get_text()

            quantity=a.find('div',class_='_3Djpdu')
            if(quantity!=None):
                quantity=quantity.get_text()

            products.append(name)
            prices.append(price)
            rates.append(rate)
            des.append(de)
            no_of_rates.append(no_of_rate)
            quantities.append(quantities)
    for a in soup.find_all('div',class_="_2kHMtA"):
            name=a.find('div',class_="_4rR01T")
            if(name!=None):
                name=name.get_text()

            price=a.find('div',class_='_30jeq3 _1_WHN1')
            if(price!=None):
                price=price.get_text()

            de=a.find('div',class_='_3eWWd-')
            if(de!=None):
                de=de.get_text()

            rate=a.find('div',class_='_3LWZlK')
            if(rate!=None):
                rate=rate.get_text()

            no_of_rate=a.find('span',class_='_2_R_DZ')
            if(no_of_rate!=None):
                no_of_rate=no_of_rate.get_text()

            quantity=a.find('div',class_='_3Djpdu')
            if(quantity!=None):
                quantity=quantity.get_text()

            products.append(name)
            prices.append(price)
            rates.append(rate)
            des.append(de)
            no_of_rates.append(no_of_rate)
            quantities.append(quantities)
if str(page)=="<Response [200]>":
    df=pd.DataFrame({"Products":products,"Price":prices,"Rate":rates,"no_of_rates":no_of_rate,"Description":des})
    df.to_csv("C:/Users/manee/Desktop/flipkart.csv", index=False)
