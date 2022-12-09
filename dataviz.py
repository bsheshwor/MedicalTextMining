import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.mydata
collection = db.datas

with open('datas.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)