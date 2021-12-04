from autoscraper import AutoScraper
import pandas as pd

url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
column_name = ['stars']
wanted_list = ["APPLE iPhone SE (Black, 64 GB)"]

scraper = AutoScraper()
res = scraper.build(url, wanted_list)
result = scraper.get_result_similar(
    "https://www.flipkart.com/search?q=samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off", grouped=True)


# l = result.values()
# for old in l:
#     result[column_name[ind]] = result.pop(old)
print(result)

# df = pd.DataFrame.from_dict(result)
# df.to_csv("C:/Users/manee/Desktop/smart_scraper.csv", index=False)
