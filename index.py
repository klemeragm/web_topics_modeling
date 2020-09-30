from MyMongoDatabase import MyMongoDatabase
from connection import connectToTwitterAPI
import tweepy

try:
    myMongo = MyMongoDatabase('modelartopicosweb')
    api = connectToTwitterAPI()
    tweetsList = tweepy.Cursor(api.search, q="qualquer texto").items(10)
    for tweet in tweetsList:
        myMongo.insert(
            "tweets", {'author': tweet.author.screen_name, 'text': tweet.text})
except tweepy.TweepError:
    print('Problema na conexão com a API')