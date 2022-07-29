from multiprocessing.sharedctypes import Value
import os
import sys
sys.path.insert(0, os.getcwd()) 
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from server_obj import ServerObj

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
s = ServerObj()

#Check for existing uni database
db_name = "uni"
dbs = s.read_query(s.connection, "SHOW DATABASES;")
if db_name not in [db[0] for db in dbs]:
    print(f"{db_name} not found in database. Creating database...")
    s.edit_databases(f"CREATE DATABASE {db_name};")
    s.create_db_connection(db_name)
else:
    print(f"{db_name} found in database.")
    s.create_db_connection(db_name)

    """Creates the initial table"""
    # s.execute_query(s.db_connection, 
    # """ CREATE TABLE UniData (
    #     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(50) NOT NULL,
    #     country VARCHAR(40),
    #     ranking VARCHAR(6)); """)

    """Populates the table with the top 10 universities"""
    # pop_top10 = "INSERT INTO UniData (name, ranking, country) VALUES (%s, %s, %s)"
    # for uni in unis:
    #     s.execute_query(s.db_connection, pop_top10, uni)

    s.execute_query(s.db_connection, "DELETE FROM UniData WHERE id=4;")
    print(s.read_query(s.db_connection, "SELECT * FROM UniData;"))

    #Do whatever updates you'd like to do here

#       rank INT)
