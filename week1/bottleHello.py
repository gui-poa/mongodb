import bottle
import pymongo

@bottle.route('/')
def index():
	connection = pymongo.MongoClient("mongodb://guipoa:coursetest@ds027749.mongolab.com:27749/course")
	db = connection.course

	name = db.names

	item = name.find_one()

	return '<b>Hello %s</b>' % item['name']

bottle.run(host='localhost', port=8082)
