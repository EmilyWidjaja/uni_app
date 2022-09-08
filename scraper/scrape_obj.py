from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

class Scraper():
    def __init__(self, chrome_driver_path=os.path.join(os.getcwd(), "chromedriver")) -> None:
        opts = Options()
        chrome_driver = chrome_driver_path
        self.driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)
        return

    def get_page(self, url):
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source)
        return soup


class ScrapeSubjects(Scraper):
    def __init__(self, chrome_driver_path=os.path.join(os.getcwd(), "chromedriver")) -> None:
        super().__init__(chrome_driver_path)
        return
    
    def subject_finder(self):
        subject_syns = [""]




