from django.shortcuts import render
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import random as r
import time
import os



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


    return render(request, 'webpages/ebay.html')


def flipkart(request):
    if request.method == "POST":
        link = request.POST['url']
        pages = int(request.POST['pages'])

        link = link+"&page={page_number}"
        products = []
        prices = []
        rates = []
        no_of_rates = []
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

                no_of_rate = a.find('span', class_='_2_R_DZ')
                if(no_of_rate != None):
                    no_of_rate = no_of_rate.get_text()

                quantity = a.find('div', class_='_3Djpdu')
                if(quantity != None):
                    quantity = quantity.get_text()

                products.append(name)
                prices.append(price)
                rates.append(rate)
                no_of_rates.append(no_of_rate)
                quantities.append(quantities)
            for a in soup.find_all('div', class_="_1xHGtK _373qXS"):
                    name = a.find('a', class_=['IRpwTa _2-ICcC', 'IRpwTa'])
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3')
                    if(price != None):
                        price = price.get_text()

                    de = a.find('div', class_='_3eWWd-')
                    if(de != None):
                        de = de.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()

                    no_of_rate = a.find('span', class_='_2_R_DZ')
                    if(no_of_rate != None):
                        no_of_rate = no_of_rate.get_text()

                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    des.append(de)
                    no_of_rates.append(no_of_rate)
                    quantities.append(quantities)
            for a in soup.find_all('div', class_="_2kHMtA"):
                    name = a.find('div', class_="_4rR01T")
                    if(name != None):
                        name = name.get_text()

                    price = a.find('div', class_='_30jeq3 _1_WHN1')
                    if(price != None):
                        price = price.get_text()

                    de = a.find('div', class_='_3eWWd-')
                    if(de != None):
                        de = de.get_text()

                    rate = a.find('div', class_='_3LWZlK')
                    if(rate != None):
                        rate = rate.get_text()

                    no_of_rate = a.find('span', class_='_2_R_DZ')
                    if(no_of_rate != None):
                        no_of_rate = no_of_rate.get_text()

                    quantity = a.find('div', class_='_3Djpdu')
                    if(quantity != None):
                        quantity = quantity.get_text()

                    products.append(name)
                    prices.append(price)
                    rates.append(rate)
                    des.append(de)
                    no_of_rates.append(no_of_rate)
                    quantities.append(quantities)

        if str(page) == "<Response [200]>":
            df = pd.DataFrame({"Products": products, "Price": prices,
                        "Rate": rates, "no_of_rates": no_of_rate, "Description": des})
            df.to_csv("C:/Users/manee/Desktop/flipkart.csv", index=False)

    return render(request, 'webpages/flipkart.html')


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

        print('Download Completed!')

    return render(request, 'webpages/gimages.html')
