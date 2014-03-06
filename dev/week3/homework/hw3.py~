import pymongo
import sys
connection = pymongo.MongoClient("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")
scores = connection.m101.grades

def find():
    query = {"type":"homework"}
    
    try:
        cursor = scores.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])   
    except:
        print "Erro: ",sys.exc_info()[0]
    
    last_student_id = 9999999999
    delete_id = 0

    for doc in cursor:
        if (last_student_id == doc['student_id']):
            print "_id",doc['_id'],"Estudante: ", doc['student_id'], "Score" ,doc['score']
            scores.remove({'_id':doc['_id']})
        last_student_id = doc['student_id']
            

find()
