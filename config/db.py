from pymongo import MongoClient

client = MongoClient(host="mongodb://localhost:27017")

db = client['match']
collection = db['users']