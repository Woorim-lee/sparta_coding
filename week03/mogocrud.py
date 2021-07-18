from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

all_users = list(db.users.find({}))


db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
user = db.users.find_one({'name': '덤블도어'})
print(user)