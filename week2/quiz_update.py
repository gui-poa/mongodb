import pymongo

def using_set():

    print "updating record using set"
    # get a handle to the school database
    connection = pymongo.Connection("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")	
    db=connection.m101
    scores = db.scores


    try:
        # get the doc
        score = scores.find_one({'student':1, 'type':'exam'})
        print "before: ", score

        # update using set
	scores.update({'student':1, 'type':'exam'},{'$set':{'examiner':'Jones'}})

        score = scores.find_one({'student':1, 'type':'exam'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

using_set();
