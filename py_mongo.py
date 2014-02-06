import pymongo

connection = pymongo.MongoClient("mongodb://guipoa:coursetest@ds027749.mongolab.com:27749/course")
db = connection.course

name = {"name":"guilherme"}

db.names.insert(name);

