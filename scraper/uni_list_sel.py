from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os


# Instantiate options
opts = Options()
# opts.add_argument(" — headless") # Uncomment if the headless version needed
# opts.binary_location = "<path to Chrome executable>"

# Set the location of the webdriver
chrome_driver = os.path.join(os.getcwd(), "chromedriver")

# Instantiate a webdriver
driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

# Load the HTML page
driver.get("https://www.timeshighereducation.com/world-university-rankings/2022/world-ranking")

# Parse processed webpage with BeautifulSoup
soup = BeautifulSoup(driver.page_source)
datatable = soup.find(id="datatable-1").find("tbody")
# print(datatable.prettify())
rows = datatable.find_all(role="row")
for row in rows:
    uni_name = row.find("a", class_="ranking-institution-title")
    location = row.find("div", class_="location")
    uni_rank = row.find("td", class_="rank sorting_1 sorting_2")
    print(f"{uni_name.text}, {location.text}, {uni_rank.text}")