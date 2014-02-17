
import pymongo
import sys

# establish a connection to the database
#connection = pymongo.Connection("mongodb://localhost", safe=True)
connection = pymongo.MongoClient("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")



def insert():

    # get a handle to the school database
#    db=connection.school
    people = connection.m101.people

    print "insert, reporting for duty"

    doc = {"name":"Andrew Erlichson", "company":"10gen","interests":['running', 'cycling', 'photography']}

    try:
        people.insert(doc)   # first insert
#        del(doc['_id'])
        people.insert(doc)   # second insert

    except:
        print "Unexpected error:", sys.exc_info()[0]



insert()

