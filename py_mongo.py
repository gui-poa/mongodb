import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test
print "nome %s" % db.name


