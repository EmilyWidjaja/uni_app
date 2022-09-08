from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import sys
sys.path.insert(0, os.getcwd()) 
from server_obj import ServerObj

# Instantiate options
opts = Options()
# opts.add_argument(" — headless") # Uncomment if the headless version needed
# opts.binary_location = "<path to Chrome executable>"

# Set the location of the webdriver
chrome_driver = os.path.join(os.getcwd(), "chromedriver")

# Instantiate a webdriver
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

# Load the HTML page
# driver.get("https://www.timeshighereducation.com/world-university-rankings/2022/world-ranking")


# Parse processed webpage with BeautifulSoup
# soup = BeautifulSoup(driver.page_source)
# datatable = soup.find(id="datatable-1").find("tbody")
# print(datatable.prettify())
# rows = datatable.find_all(role="row")
# for row in rows:
#     uni_name = row.find("a", class_="ranking-institution-title")
#     location = row.find("div", class_="location")
#     uni_rank = row.find("td", class_="rank sorting_1 sorting_2")
#     print(f"{uni_name.text}, {location.text}, {uni_rank.text}")

# Connecting to database to add new information
s = ServerObj()
db_name = "uni"
dbs = s.read_query(s.connection, "SHOW DATABASES;")
s.create_db_connection(db_name)
# add_url_column = """
#     ALTER TABLE UniData
#     ADD url VARCHAR(60);"""
# s.execute_query(s.db_connection, add_url_column)
update_url_entry = lambda url, uni : "UPDATE UniData SET url = '" + url + "'\nWHERE name = '" + uni + "';"

#Get uni information on currently available unis
curr_unis = []
true_unis = []
res = s.read_query(s.db_connection, "SELECT name FROM UniData;")
for r in res: curr_unis.append(s.clean_string(r[0])); true_unis.append(r[0])
print(true_unis)

# Getting URL information
driver.get("https://www.webometrics.info/en/WORLD")
soup = BeautifulSoup(driver.page_source)
datatable = soup.find("tbody")
# print(datatable.prettify())
rows = datatable.find_all("a", href=True)

#Adding to the table
count = 0
total = len(curr_unis) + 1
for row in rows:
    if row.text == "":
        continue
    uniName = s.clean_string(row.text)
    prop_name = s.get_most_similar(uniName, curr_unis)
    if prop_name == False:
            continue
    else:
        search_uni = true_unis[curr_unis.index(prop_name)]
        print(row['href'])
        print(row.text)
        print(update_url_entry(row['href'], search_uni))
        s.execute_query(s.db_connection, update_url_entry(row['href'], search_uni))
        print()
        count += 1
        if count == total:
            break

print("Total update: ", count)


#Updating the table with the new variables:


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

print(s.read_query(s.db_connection, "SELECT * FROM UniData;"))
driver.close()
    # Do whatever updates you'd like to do here
