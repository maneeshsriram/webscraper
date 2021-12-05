from autoscraper import AutoScraper
import pandas as pd

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'
wanted_list = [
    "Use urllib2 in combination with the brilliant BeautifulSoup library:"]

scraper = AutoScraper()
res = scraper.build(url, wanted_list)
result = scraper.get_result_similar(
    "https://stackoverflow.com/questions/2081586/web-scraping-with-python", grouped=True)
l = []
for i in result.keys():
    l.append(result[i])
