# get current location
from pathlib import Path

my_path = str(Path(__file__).parent)


# get current date

from datetime import datetime
import time

today = (str(datetime.today())).split(" ", 1)[0]

# selenium
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--disable-extensions")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome(
    options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
)

# for scoring article sentiments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://afaizaslam:faiz00aslam01@mywebscraping.lghyy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = cluster["faiz"]
collection = db["web_scraped_articles"]


class Asobi:
    def get_article(links):
        url = links

        driver = webdriver.Chrome(
            options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
        )
        driver.get(url)
        time.sleep(3)
        # paragraphs = driver.find_element_by_class_name("field field-body")
        paragraphs = driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]'
        ).text
        driver.close()
        return paragraphs
