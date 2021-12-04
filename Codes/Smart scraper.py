from autoscraper import AutoScraper
import pandas as pd

url = 'https://github.com/krishnaik06?tab=repositories'
column_name=['stars','title']
wanted_list = ["39","Car-Price-Prediction"]

scraper = AutoScraper()
res= scraper.build(url, wanted_list)
result=scraper.get_result_similar("https://github.com/krishnaik06?tab=repositories",grouped=True)

ind=0
l=list(result.keys())
for old in l:
    result[column_name[ind]] = result.pop(old)
    ind=ind + 1
   
df = pd.DataFrame.from_dict(result)
df.to_csv("C:/Users/manee/Desktop/smart_scraper.csv", index=False)
