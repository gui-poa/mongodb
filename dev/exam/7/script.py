#mongoimport -d m101 -c albums --file albums.json 
#mongoimport -d m101 -c images --file images.json 
#db.images.find({tags:{$in:["kittens"]}}).count()
#db.albums.find({images:{$in:[10000]}})
#db.images.find({_id:10000})
#db.albums.ensureIndex({tags:1})
import pymongo
import sys
def using_set():

   #connection = pymongo.Connection("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")	
    connection = pymongo.Connection("mongodb://localhost")
    db=connection.m101
    images = db.images
    albums = db.albums

    try:
        # get the doc
	a=0
        cursor = images.find()
	for post in cursor:
		c = albums.find({"images":{"$in":[post['_id']]}}).count()
		if c == 0:
		   images.remove({"_id":post['_id']})
	
	#scores.update({'student':1, 'type':'exam'},{'$set':{'examiner':'Jones'}})

        #score = scores.find_one({'student':1, 'type':'exam'})
        #print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

using_set();
