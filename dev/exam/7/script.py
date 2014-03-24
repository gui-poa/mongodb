#mongoimport -d m101 -c albums --file albums.json 
#mongoimport -d m101 -c images --file images.json 
#db.images.find({tags:{$in:["kittens"]}}).count()
#db.albums.find({images:{$in:[10000]}})
#db.images.find({_id:10000})
import pymongo

def using_set():

   #connection = pymongo.Connection("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")	
    connection = pymongo.Connection("mongodb://localhost")
    db=connection.m101
    images = db.images


    try:
        # get the doc
        score = images.find({}).count()
        print "Total: ", score

        # update using set
	#scores.update({'student':1, 'type':'exam'},{'$set':{'examiner':'Jones'}})

        #score = scores.find_one({'student':1, 'type':'exam'})
        #print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

using_set();
