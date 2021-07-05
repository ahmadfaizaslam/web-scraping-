import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster = MongoClient(
    'mongodb+srv://afaizaslam:faiz00aslam01@faizwebscraping.9kqkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster['Faiz']
collection = db["web_scraped_articles"]
# x = collection.delete_many({})
