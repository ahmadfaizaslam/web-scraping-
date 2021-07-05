from newsapi import NewsApiClient
import pandas as pd
from pathlib import Path

my_path = str(Path(__file__).parent)
newsapi = NewsApiClient(api_key='79cad9c3302b4dd2942978caa4c47d03')

news = newsapi.get_everything(q='palm oil', language='en', page_size=50)
articles = news['articles']

for x, y in enumerate(articles):
    print(f' {x}  {y["title"]}')
df = pd.DataFrame(articles)

df.to_excel(my_path + r"\\newsapi.xlsx", engine="openpyxl", index=False)
