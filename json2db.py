import pymongo
import json
import CONFIG

def json_database(json_path):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient.mydata
    collection = db.datas

    with open(json_path) as file:
        file_data = json.load(file)

    collection.insert_many(file_data)

if __name__ == "__main__":
    json_database(CONFIG.JSON_PATH)