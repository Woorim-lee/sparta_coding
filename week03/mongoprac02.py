
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

movie_name = db.movies.find_one({'name' : '월-E'})
target_point = movie_name['point']

movies = list(db.movies.find({'point' : target_point}))

for movie in movies:
    print(movie['name'], ":", movie['point'])