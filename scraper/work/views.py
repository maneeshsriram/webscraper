from selenium import webdriver
from django.shortcuts import render
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import random as r
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from django.http.response import HttpResponse
import csv
import json
from autoscraper import AutoScraper
from django.core.serializers import serialize




def ebay(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])

        link = link+"&pgn={page_number}"
        products = []
        prices = []
        rates = []
        hands = []
        shippings = []
        origins = []
        solds = []
        descriptions = []
        for i in range(1, pages+1):
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

        if str(page) == "<Response [200]>":
            df = pd.DataFrame({"Products": products, "Price": prices, "Rate": rates, "Usage": hands,
                            "Shipping": shippings, "Origins": origins, "Solds": solds, "Description": descriptions})
            df.to_csv("C:/Users/manee/Desktop/ebay.csv", index=False)
            

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="ebay.csv"'
            writer = csv.writer(response)
            writer.writerow(["Products", "Price", "Rate", "Usage", "Shipping", "Origins", "Solds", "Description"])
            for i in range(len(products)):
                writer.writerow(
                    [products[i], prices[i], rates[i], hands[i], shippings[i], origins[i], solds[i], descriptions[i]])
            return response

    return render(request, 'webpages/ebay.html')

def Jebay(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])

        link = link+"&pgn={page_number}"
        products = []
        prices = []
        rates = []
        hands = []
        shippings = []
        origins = []
        solds = []
        descriptions = []
        for i in range(1, pages+1):
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

                origin = a.find(
                    'span', class_='s-item__location s-item__itemLocation')
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

        if str(page) == "<Response [200]>":
            df = pd.DataFrame({"Products": products, "Price": prices, "Rate": rates, "Usage": hands,
                               "Shipping": shippings, "Origins": origins, "Solds": solds, "Description": descriptions})

            data = df.to_json(orient='records')
            response = HttpResponse(data, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="ebay.txt"'
            return response

    return render(request, 'webpages/ebay.html')



def flipkart(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])

        link = link+"&page={page_number}"
        products = []
        prices = []
        rates = []
        quantities = []
        des = []
        

        for i in range(1, pages+1):  # page number u can modify
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
            for a in soup.find_all('div', class_="_4ddWXP"):

                name = a.find('a', class_='s1Q9rs')
                if(name != None):
                    name = name.get_text()

                price = a.find('div', class_='_30jeq3')
                if(price != None):
                    price = price.get_text()

                rate = a.find('div', class_='_3LWZlK')
                if(rate != None):
                    rate = rate.get_text()

                quantity = a.find('div', class_='_3Djpdu')
                if(quantity != None):
                    quantity = quantity.get_text()

                products.append(name)
                prices.append(price)
                rates.append(rate)
                quantities.append(quantities)
            for a in soup.find_all('div', class_="_1xHGtK _373qXS"):
                    name = a.find('a', class_=['IRpwTa _2-ICcC', 'IRpwTa'])
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3')
                    if(price != None):
                        price = price.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()


                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    quantities.append(quantities)
            for a in soup.find_all('div', class_="_2kHMtA"):
                    name = a.find('div', class_="_4rR01T")
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3 _1_WHN1')
                    if(price != None):
                        price = price.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()

                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    quantities.append(quantities)

        if str(page) == "<Response [200]>":
            df = pd.DataFrame({"Products": products, "Price": prices,
                        "Rate": rates, })
            df.to_csv("C:/Users/manee/Desktop/flipkart.csv", index=False)
            df.to_json("C:/Users/manee/Desktop/flipkart.txt", orient='records')

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="flipkart.csv"'
            writer = csv.writer(response)
            writer.writerow(["Products", "Price", "Rates"])
            for i in range(len(products)):
                writer.writerow([products[i], prices[i], rates[i]])
            return response

    return render(request, 'webpages/flipkart.html')

def Jflipkart(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])

        link = link+"&page={page_number}"
        products = []
        prices = []
        rates = []
        quantities = []
        des = []
        

        for i in range(1, pages+1):  # page number u can modify
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
            for a in soup.find_all('div', class_="_4ddWXP"):

                name = a.find('a', class_='s1Q9rs')
                if(name != None):
                    name = name.get_text()

                price = a.find('div', class_='_30jeq3')
                if(price != None):
                    price = price.get_text()

                rate = a.find('div', class_='_3LWZlK')
                if(rate != None):
                    rate = rate.get_text()

                quantity = a.find('div', class_='_3Djpdu')
                if(quantity != None):
                    quantity = quantity.get_text()

                products.append(name)
                prices.append(price)
                rates.append(rate)
                quantities.append(quantities)
            for a in soup.find_all('div', class_="_1xHGtK _373qXS"):
                    name = a.find('a', class_=['IRpwTa _2-ICcC', 'IRpwTa'])
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3')
                    if(price != None):
                        price = price.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()


                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    quantities.append(quantities)
            for a in soup.find_all('div', class_="_2kHMtA"):
                    name = a.find('div', class_="_4rR01T")
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3 _1_WHN1')
                    if(price != None):
                        price = price.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()

                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    quantities.append(quantities)

        if str(page) == "<Response [200]>":
            df = pd.DataFrame({"Products": products, "Price": prices,
                        "Rate": rates, })

            data = df.to_json(orient='records')
            response = HttpResponse(data, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="flipkart.txt"'
            return response


    return render(request, 'webpages/flipkart.html')



def flipkartReview(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])
        names = []
        reviews = []
        keywords = []
        link = link.replace("/p/", "/product-reviews/")
        link = link+"&page={page_number}"
        for i in range(1, pages+1):    # number of page number
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
        df.to_json("C:/Users/manee/Desktop/flipkart_review.csv.txt", orient='records')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="flipkart_Review.csv"'
        writer = csv.writer(response)
        writer.writerow(["names", "reviews", "keywords"])
        for i in range(len(names)):
            writer.writerow([names[i], reviews[i], keywords[i]])
        return response

    return render(request, 'webpages/flipkartReview.html')

def JflipkartReview(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])
        names = []
        reviews = []
        keywords = []
        link = link.replace("/p/", "/product-reviews/")
        link = link+"&page={page_number}"
        for i in range(1, pages+1):    # number of page number
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
        data = df.to_json(orient='records')
        response = HttpResponse(data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="flipkartReview.txt"'
        return response

    return render(request, 'webpages/flipkartReview.html')



def twitter(request):
    if request.method == "POST":
        key = request.POST['keyword']
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(15)
        email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'
        email = driver.find_element_by_xpath(email_xpath)
        email.send_keys('ManeeshSriram')

        next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div'
        next_button = driver.find_element_by_xpath(next_xpath)
        next_button.click()

        time.sleep(3)

        pass_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'
        password = driver.find_element_by_xpath(pass_xpath)
        password.send_keys('automatepass')

        login_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button.click()


        time.sleep(3)

        explore_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div'
        explore = driver.find_element_by_xpath(explore_xpath)
        explore.click()

        time.sleep(3)

        search_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
        search = driver.find_element_by_xpath(search_xpath)
        search.send_keys(key)
        search.submit()

        time.sleep(5)

        prev_height = driver.execute_script('return document.body.scrollHeight')
        for i in range(0, 15):   # scroll only twice.
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(3)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == prev_height:
                break


        tweet_divs = driver.page_source
        obj = bs4(tweet_divs, "html.parser")


        names = []
        tweets = []
        comments = []
        retweets = []
        likes = []
        dates = []
        users = []
        # css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu
        container = obj.find_all(
            'div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
        for i in container:
            sub = i.find_all('span', class_='r-qvutc0')
            try:
                name = sub[1].get_text()
            except:
                name = None
            try:
                user = sub[2].get_text()
            except:
                user = None
            try:
                tweet = sub[4].get_text()
            except:
                tweet = None
            try:
                comment = sub[-6].get_text()
            except:
                comment = None
            try:
                retweet = sub[-4].get_text()
            except:
                retweet = None
            try:
                like = sub[-1].get_text()
            except:
                like = None

            names.append(name)
            tweets.append(tweet)
            comments.append(comment)
            retweets.append(retweet)
            likes.append(like)
            users.append(user)
        df = pd.DataFrame({"Name": names, "users": users, "tweets": tweets,
                        "comments": comments, "retweets": retweets, "likes": likes})
        df.to_csv("C:/Users/manee/Desktop/twitter.csv", index=False)
        df.to_json("C:/Users/manee/Desktop/twitter.txt", orient='records')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Twitter.csv"'
        writer = csv.writer(response)
        writer.writerow(["Name", "Users", "Tweets", "comments", "retweets", "likes"])
        for i in range(len(names)):
            writer.writerow([names[i], users[i], tweets[i], comments[i], retweets[i], likes[i]])
        return response


    return render(request, 'webpages/twitter.html')

def Jtwitter(request):
    if request.method == "POST":
        key = request.POST['keyword']
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://twitter.com/i/flow/login")
        time.sleep(15)
        email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'
        email = driver.find_element_by_xpath(email_xpath)
        email.send_keys('ManeeshSriram')

        next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div'
        next_button = driver.find_element_by_xpath(next_xpath)
        next_button.click()

        time.sleep(3)

        pass_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'
        password = driver.find_element_by_xpath(pass_xpath)
        password.send_keys('automatepass')

        login_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button.click()


        time.sleep(3)

        explore_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div'
        explore = driver.find_element_by_xpath(explore_xpath)
        explore.click()

        time.sleep(3)

        search_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
        search = driver.find_element_by_xpath(search_xpath)
        search.send_keys(key)
        search.submit()

        time.sleep(5)

        prev_height = driver.execute_script('return document.body.scrollHeight')
        for i in range(0, 15):   # scroll only twice.
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(3)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == prev_height:
                break


        tweet_divs = driver.page_source
        obj = bs4(tweet_divs, "html.parser")


        names = []
        tweets = []
        comments = []
        retweets = []
        likes = []
        dates = []
        users = []
        # css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu
        container = obj.find_all(
            'div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
        for i in container:
            sub = i.find_all('span', class_='r-qvutc0')
            try:
                name = sub[1].get_text()
            except:
                name = None
            try:
                user = sub[2].get_text()
            except:
                user = None
            try:
                tweet = sub[4].get_text()
            except:
                tweet = None
            try:
                comment = sub[-6].get_text()
            except:
                comment = None
            try:
                retweet = sub[-4].get_text()
            except:
                retweet = None
            try:
                like = sub[-1].get_text()
            except:
                like = None

            names.append(name)
            tweets.append(tweet)
            comments.append(comment)
            retweets.append(retweet)
            likes.append(like)
            users.append(user)
        df = pd.DataFrame({"Name": names, "users": users, "tweets": tweets,
                        "comments": comments, "retweets": retweets, "likes": likes})
        data = df.to_json(orient='records')
        response = HttpResponse(data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Twitter.txt"'
        return response


    return render(request, 'webpages/twitter.html')



def gimages(request):
    if request.method == "POST":
        Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
        data = request.POST['keyowrd']
        num_images = int(request.POST['images'])

        u_agnt = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        }  # write: 'my user agent' in browser to get your browser user agent details
        Image_Folder = 'Images_1'

        if not os.path.exists(Image_Folder):
            os.mkdir(Image_Folder)

        search_url = Google_Image + 'q=' + data  # 'q=' because its a query
        response = requests.get(search_url, headers=u_agnt)
        html = response.text  # To get actual result i.e. to read the html data in text mode

        b_soup = bs4(html, 'html.parser')
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

        count = 0
        imagelinks = []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= num_images):
                    break
            except KeyError:
                continue
        
        print(f'Found {len(imagelinks)} images')
        print('Start downloading...')

        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink)
            imagename = Image_Folder + '/' + data + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)

    return render(request, 'webpages/gimages.html')



def smart(request):
    if request.method == "POST":
        url = request.POST['url']
        key = request.POST['key']
        wanted_list = key.split(",")

        scraper = AutoScraper()
        res = scraper.build(url, wanted_list)
        result = scraper.get_result_similar(url, grouped=True)
        data = []
        for i in result.keys(): 
            data.append(result[i])
        response = HttpResponse(data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="smart.txt"'
        return response
    return render(request, 'webpages/smart.html')






