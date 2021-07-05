from my_function import *
import datetime as datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--disable-extensions")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
options.add_argument("--headless")
today = date.today()
begin_time = datetime.datetime.now()

my_path = str(Path(__file__).parent)
driver = webdriver.Chrome(
    options=options, executable_path="C:\Program Files (x86)\chromedriver.exe"
)
user_query = input("Enter Topic:").replace(" ", "+")
url = f"https://www.nst.com.my/search?keywords={user_query}"


for page_navigation in range(50):
    number = 1
    driver.get(url)
    articles = driver.find_elements_by_class_name("article-teaser")

    print(url)

    for x, article in enumerate(articles, 1):

        try:
            driver.implicitly_wait(5)

            topic_path = f'//*[@id="main"]/div/div[2]/div[1]/div/div[{number}]/a/div[2]/div[1]/span[1]'
            topic = article.find_element_by_xpath(topic_path).text

            title_path = (
                f'//*[@id="main"]/div/div[2]/div[1]/div/div[{number}]/a/div[2]/h6'
            )
            title = article.find_element_by_xpath(title_path).text

            time_path = f'//*[@id="main"]/div/div[2]/div[1]/div/div[{number}]/a/div[2]/div[1]/span[2]'
            time = article.find_element_by_xpath(time_path).text
            # if "ago" in time:
            #     time = today.strftime("%m/%d/%Y")
            #     May 20, 2021 @ 11:25pm nst's time format
            # else:
            #     time = time.split("@")[0].rstrip()
            #     time = datetime.datetime.strptime(time, "%b %d, %Y").strftime(
            #         "%m/%d/%Y"
            #     )
            #     time = "time eror"

            link_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a'

            for a in driver.find_elements_by_xpath(link_path):
                links = a.get_attribute("href")

            essay = Asobi.get_article(links)
            score = analyzer.polarity_scores(essay)
            compound_score = score["compound"]
            pos_score = score["pos"]
            neg_score = score["neg"]
            print(
                f"{x}. {topic} -> {title} , {time} ,{pos_score}, {neg_score}, {compound_score}"
            )
            news_items = {
                "topic": topic,
                "title": title,
                "date": time,
                "link": links,
                "article": essay,
                "positive_score": pos_score,
                "negative_score": neg_score,
                "compound_score": compound_score,
            }
            collection.insert_one(news_items)

            # print(pos_score, neg_score, compound_score)
            number = number + 1
            driver.implicitly_wait(5)
        except:
            # Exception as e print(e)
            break
    try:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li/a'
    except:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li[2]/a'

    for a in driver.find_elements_by_xpath(next_page):
        url = a.get_attribute("href")
print("Time Taken : ", datetime.datetime.now() - begin_time)

driver.close()
driver.quit()
