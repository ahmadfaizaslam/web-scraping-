from selenium import webdriver
import os
from my_function import *
import pandas as pd
from my_function import *
import datetime as datetime


my_path = os.path.dirname(os.path.realpath(__file__))

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-extensions")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
options.add_argument("--headless")
begin_time = datetime.datetime.now()


url = "https://www.nst.com.my/search?keywords=currency"


driver = webdriver.Chrome(
    options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
)


news_list = []

for page_navigation in range(6):
    number = 1
    driver.get(url)
    articles = driver.find_elements_by_class_name("article-teaser")
    driver.implicitly_wait(5)
    print(url)

    for x, article in enumerate(articles, 1):
        try:
            title_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a/div[2]/h6'
            title = article.find_element_by_xpath(title_path).text

            time_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a/div[2]/div[1]/span[2]'
            time = article.find_element_by_xpath(time_path).text

            topic_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a/div[2]/div[1]/span[1]'
            topic = article.find_element_by_xpath(topic_path).text

            link_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a'

            for a in driver.find_elements_by_xpath(link_path):
                links = a.get_attribute("href")

            essay = Asobi.get_article(links)
            news_items = {
                "topic": topic,
                "title": title,
                "article": essay,
                "date": time,
                "link": links
            }
            news_list.append(news_items)
            print(f"{x}. {topic} -> {title} , {time}")
            number = number + 1
        except:
            break
    try:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li/a'
    except:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li[2]/a'
    df = pd.DataFrame(news_list)
    for a in driver.find_elements_by_xpath(next_page):
        url = a.get_attribute("href")

    next_page = driver.find_element_by_link_text("Next »").click()
    driver.implicitly_wait(5)

df.to_excel(my_path + r"\\final.xlsx", engine="openpyxl", index=False)
print("Time Taken : ", datetime.datetime.now() - begin_time)
