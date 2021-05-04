from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
options.add_argument("--headless")
from selenium import webdriver


class Asobi:
    def get_article(links):
        url = links

        driver = webdriver.Chrome(
            options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
        )
        driver.get(url)

        # paragraphs = driver.find_element_by_class_name("field field-body")
        paragraphs = driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]'
        ).text
        return paragraphs
