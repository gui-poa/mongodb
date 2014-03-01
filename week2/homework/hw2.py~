import pymongo
import sys
connection = pymongo.MongoClient("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")
scores = connection.m101.scores

def find():
    print "find, reporting for duty"
    query = {"type":"exam",'score':{'$gt':95,'$lte':99}}
    selector = {"student":1,"score":1}
    
    try:
        cursor = scores.find(query,selector)
    except:
        print "Erro: ",sys.exc_info()[0]
    
    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity >= 10):
            break;
            

def find_one():
    query = {'student':10}
    try:
        doc = scores.find_one(query)
    except:
        print "Erro: ",sys.exc_info()[0]

    print doc

find()
