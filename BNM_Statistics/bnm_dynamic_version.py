from my_function import *

url = f"https://www.bnm.gov.my/-/monthly-highlights-and-statistics-in-{month}-2021"

domain = "https://www.bnm.gov.my"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

r = requests.get(url)


soup = BeautifulSoup(r.content, "lxml")

productlist = soup.find_all("table", class_="standard-table")


a = 0
for item in productlist:
    for link in item.find_all("tr"):
        if a > 20:     # limit range of files needed to be download for early testing. Remove when all is ok
            break
        else:
            bullet = link.find("td")
            if bullet == None:
                pass
            else:
                title = bullet.find_next_sibling("td")
                link = title.find_next_sibling("td").find("a", href=True)
                if link is not None:
                    link = link["href"]
                    url = domain + link
                bullet, title = bullet.text, title.text
                print(f"{(bullet)} {(title)}")
                print(url)
                filename = bullet + " " + title + ".xls"
                # retrieve(url, filename)
                """
                The  download part is still buggy for unknow reasons:
                    - Mainly files are being downloaded without any data in it (Okb files are created)
                    - (Merchant/Investment Banks: Statement of Assets) is also causes issues while downloading
                       even tried in a static version. Issue still persist 
                """
                a += 1
