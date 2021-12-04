from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup as bs4
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login")
time.sleep(15)
email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'
email = driver.find_element_by_xpath(email_xpath)
email.send_keys('chandku66099338')

next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div'
next_button = driver.find_element_by_xpath(next_xpath)
next_button.click()

time.sleep(3)

pass_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'
password = driver.find_element_by_xpath(pass_xpath)
password.send_keys('natsudragneel')

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
search.send_keys('cricket')
search.submit()

time.sleep(5)

prev_height = driver.execute_script('return document.body.scrollHeight')
for i in range(0, 6):   # scroll only twice.
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

