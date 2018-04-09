import pymongo

def connect():
    client = pymongo.MongoClient("localhost", 27017)
    db = client.api_mongo

    return db