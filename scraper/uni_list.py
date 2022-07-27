from multiprocessing.sharedctypes import Value
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#Get the top 10 universities from 
year = datetime.now().year
url = f"https://www.timeshighereducation.com/world-university-rankings/{year}/world-ranking"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

unis = []   #stored in uni name, rank, and location (named as country in personal thing)
ranks = requests.get("https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2022_0__e7070f0c2581be5fe6ab6392da206b36.json", headers=headers).json()
print(ranks.keys())

for d in ranks['data']:
    tup = (d['name'], d['rank'], d['location'])
    unis.append(tup)
    try:
        cur_rank = int(d['rank'])
    except ValueError:
        cur_rank = int(d['rank'][1::])
    if cur_rank >= 10:
        break
    
for uni in unis:
    print(uni)

