from MyMongoDatabase import MyMongoDatabase
from connection import connectToTwitterAPI
import tweepy

try:
    myMongo = MyMongoDatabase('covid19') #nome do banco 
    api = connectToTwitterAPI()
    tweetsList = tweepy.Cursor(api.search, q='Coronavirus OR "corona virus" Covid 19 OR covid19 OR pandemia or epidemia').items(100) #qualquer texto
    for tweet in tweetsList:
        myMongo.insert(
            "tweets", {'author': tweet.author.screen_name, 'text': tweet.text})
except tweepy.TweepError:
    print('Problema na conexão com a API')

    
#client = pymongo.MongoClient("mongodb://klemeragm:<password>@cluster1-shard-00-00.laahq.mongodb.net:27017,cluster1-shard-00-01.laahq.mongodb.net:27017,cluster1-shard-00-02.laahq.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-xosvxq-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test
