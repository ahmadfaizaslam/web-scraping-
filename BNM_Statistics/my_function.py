import datetime
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve as retrieve

today = datetime.datetime.today()
# today = datetime.date(2021, 6, 29)

# print(today)
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


lastday = last_day_of_month(datetime.date(today.year, today.month, today.day))

if today != lastday:
    month = datetime.date(today.year, today.month - 2, today.day).strftime("%B")
else:
    month = datetime.date(today.year, today.month - 1, today.day).strftime("%B")

print(month)