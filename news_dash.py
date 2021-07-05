import pandas as pd
from pymongo import collection
from pymongo import MongoClient

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

cluster = MongoClient(
    "mongodb+srv://afaizaslam:faiz00aslam01@faizwebscraping.9kqkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = cluster["Faiz"]
collection = db["web_scraped_articles"]

df = pd.DataFrame(list(collection.find()))
df["rating"] = [
    "possitive" if x > 0 else "negative" if x < 0 else "neutral"
    for x in df["compound_score"]
]
df = df.drop(columns=["_id"]).dropna()

print(df.info())
count = df.groupby("rating").count().reset_index()
# print(df.value_counts("rating"))
# print(df.describe)

app = dash.Dash(__name__)
fig = px.bar(count, x="rating", y="title")


app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for Python.
    """
        ),
        fig.show(),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
