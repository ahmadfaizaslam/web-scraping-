from pymongo import collection
from pymongo import MongoClient
from selenium import webdriver
from pathlib import Path
import datetime as datetime
import pandas as pd
import os
from selenium import webdriver
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
today = date.today()
####################################
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-extensions")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
options.add_argument("--headless")
####################################
cluster = MongoClient(
    "mongodb+srv://afaizaslam:faiz00aslam01@faizwebscraping.9kqkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = cluster["Faiz"]
collection = db["web_scraped_articles"]
####################################

####################################


class Asobi:
    def get_article(links):
        url = links

        driver = webdriver.Chrome(
            options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
        )
        driver.get(url)
        driver.implicitly_wait(5)
        # paragraphs = driver.find_element_by_class_name("field field-body")
        paragraphs = driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]'
        ).text
        driver.close()
        return paragraphs
