from my_functions import *

user_query = input("Enter Topic:").replace(" ", "+")
url = f"https://www.nst.com.my/search?keywords={user_query}"

"""
    Example user searches "palm oil", this will be converted into
    a url string : 
    https://www.nst.com.my/search?keywords=palm+oil
    
    some sites uses %20 instead of + which is the ASCII Value for 
    space
"""

for web_page in range(5):
    number = 1
    driver.get(url)
    """
    Navigates to a page given by the URL similar to a human
    """


    article_container = driver.find_elements_by_class_name("article-teaser")
    """
    "article-teaser" is the container that holds the titles of the 
    article and other specific information    
    """

    print(url)

    for article in article_container:
        time.sleep(1)
        title_path = f'//*[@id="main"]/div/div[2]/div[1]/div/div[{number}]/a/div[2]/h6'
        title = article.find_element_by_xpath(title_path).text

        """
        Gets the xpath of the title and identifies the text in that specific location
        
        <h6 class="field-title xh-highlight">
            Central banks of Malaysia, Indonesia expand ringgit-rupiah framework
        </h6>
        ∴ title = Central banks of Malaysia, Indonesia expand ringgit-rupiah framework
        """

        published_date_path = f'//*[@id="main"]/div/div[2]/div[1]/div/div[{number}]/a/div[2]/div[1]/span[2]'
        published_date = article.find_element_by_xpath(published_date_path).text

        article_link_path = f'//*[@id="main"]/div/div/div[1]/div/div[{number}]/a'

        for a in driver.find_elements_by_xpath(article_link_path):
            links = a.get_attribute("href")

        article = Asobi.get_article(links)
        time.sleep(1)
        if "ago" in published_date:
            published_date = today
        else:
            published_date = published_date.split("@")[0].rstrip()
            published_date = datetime.strptime(published_date, "%b %d, %Y").strftime(
                "%Y-%m-%d"
            )
        """
        converts various date format into YYYY-mm-dd (2020-12-20)
        """

        score = analyzer.polarity_scores(article)
        compound_score = score["compound"]
        pos_score = score["pos"]
        neg_score = score["neg"]

        news_items = {
            "title": title,
            "date": published_date,
            "link": links,
            "article": article,
            "positive_score": pos_score,
            "negative_score": neg_score,
            "compound_score": compound_score,
        }
        # collection.insert_one(news_items)

        print(f"{number}. {title} ,{published_date}")
        print(neg_score, pos_score, compound_score)
        time.sleep(1)

        number += 1
        if number > 20:
            break
    try:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li/a'
    except:
        next_page = f'//*[@id="main"]/div/div/div[1]/nav/ul/li[2]/a'

    for a in driver.find_elements_by_xpath(next_page):
        url = a.get_attribute("href")


driver.close()
driver.quit()
