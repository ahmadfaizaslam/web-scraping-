from my_function import *

url = f"https://www.bnm.gov.my/-/monthly-highlights-and-statistics-in-{month}-2021"

domain = "https://www.bnm.gov.my"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

productlist = soup.find_all("table", class_="standard-table")


for item in productlist:
    for link in item.find_all("tr"):

        bullet = link.find("td")
        if bullet == None:
            pass
        else:
            title = bullet.find_next_sibling("td")
            link = title.find_next_sibling("td").find("a", href=True)
            if link is not None:
                link = link["href"]
                file_url = domain + link
                bullet, title = bullet.text, title.text
                print(f"{(bullet)} {(title)}")
                print(file_url)
                extension = file_url.split(".")[-1]
                title = title.replace(":", " ").replace("/", " ").replace("*", " ")
                filename = bullet + " " + title + "." + extension
                try:
                    retrieve(file_url, filename)
                except:
                    print(f"{filename} is not able to downloaded currently")
