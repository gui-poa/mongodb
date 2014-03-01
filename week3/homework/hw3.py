import pymongo
import sys
connection = pymongo.MongoClient("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")
students = connection.m101.students

def find():
    
    try:
        cursor = students.find()
    except:
        print "Erro: ",sys.exc_info()[0]
    
    hwGrade = -1
    newGrade = []
    newGradeHW = []

    for doc in cursor:
        for grade in doc['scores']:
            if grade['type'] == 'homework':
                if grade['score'] > hwGrade:
                    newGradeHW = {"type":"homework","score":grade['score']}
                    hwGrade = grade['score']         
            else:
                newGrade.append(grade)
            
        newGrade.append(newGradeHW)    
        
        #UPDATE
        students.update({'_id':doc['_id']},{'$set':{'scores':newGrade}})    
        newGrade = []
        newGradeHW = []
        hwGrade = -1
                
            

find()
