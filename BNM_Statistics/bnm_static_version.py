from my_function import *
from urllib.request import urlretrieve as retrieve

page_url = f"https://www.bnm.gov.my/-/monthly-highlights-and-statistics-in-{month}-2021"

url = "https://www.bnm.gov.my/documents/20124/4196742/1.1.xls"
# retrieve(url,"test.xls")

bnm_data = {
    "Reserve Money": "https://www.bnm.gov.my/documents/20124/4196742/1.1.xls",
    "Currency in Circulation by Denomination": "https://www.bnm.gov.my/documents/20124/4196742/1.2.xls",
    "Merchant/Investment Banks: Statement of Assets": "https://www.bnm.gov.my/documents/20124/4196742/1.7.4.xls",
}

for file_name, url in bnm_data.items():
    filename = file_name + ".xls"
    retrieve(url, filename)
