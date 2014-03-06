
import json
import urllib2
import pymongo

# connect to mongo
#connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the reddit database
#db=connection.reddit
#stories = db.stories
connection = pymongo.MongoClient("mongodb://guipoa:senhabanco@ds027779.mongolab.com:27779/m101")
stories = connection.m101.stories


# get the reddit home page
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert(item['data'])




