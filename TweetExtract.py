from twitter import *
from pymongo import MongoClient
import json

oauthToken = ""
oauthSecret = ""
consumerKey = ""
consumerSecret = ""

twitter_stream = TwitterStream(auth=OAuth(oauthToken, oauthSecret, consumerKey, consumerSecret))

iterator = twitter_stream.statuses.filter(track='FlyEmirates,emirates airlines',language='en')

client = MongoClient()
db = client.flyemirates
tweetsdb = db.tweets

for tweet in iterator:
    print json.dumps(tweet, indent=1)
    tweetsdb.insert_one(json.loads(json.dumps(tweet)))
