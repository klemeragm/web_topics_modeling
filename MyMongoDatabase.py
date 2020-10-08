import configparser
import pymongo
<<<<<<< HEAD

=======
from pymongo import MongoClient
>>>>>>> 95d5bba5a29031507e66ea42a40142bafc287ab7

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus
<<<<<<< HEAD
    
config = configparser.ConfigParser()
config.read("./credentials/config.ini")
myMongoCreds = {'username': quote_plus(config.get("MongoDB", "username")), 'password': quote_plus(
   config.get("MongoDB", "password"))}
myMongoUrl = ("mongodb://klemeragm:klemer123@cluster1-shard-00-00.laahq.mongodb.net:27017,cluster1-shard-00-01.laahq.mongodb.net:27017,cluster1-shard-00-02.laahq.mongodb.net:27017/covid19?ssl=true&replicaSet=atlas-xosvxq-shard-0&authSource=admin&retryWrites=true&w=majority") % (
   myMongoCreds['username'], myMongoCreds['password']) 


#myMongoUrl = 'mongodb+srv://%s:%s@cluster1.sofkp.gcp.mongodb.net'
#mongodb://klemeragm:<password>@cluster1-shard-00-00.laahq.mongodb.net:27017,cluster1-shard-00-01.laahq.mongodb.net:27017,cluster1-shard-00-02.laahq.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-xosvxq-shard-0&authSource=admin&retryWrites=true&w=majority
# 

=======

config = configparser.ConfigParser()
config.read("./credentials/config.ini")
myMongoCreds = {'username': quote_plus(config.get("MongoDB", "username")), 'password': quote_plus(
    config.get("MongoDB", "password"))}
   myMongoUrl = 'mongodb://klemeragm:<password>@cluster1-shard-00-00.laahq.mongodb.net:27017,cluster1-shard-00-01.laahq.mongodb.net:27017,cluster1-shard-00-02.laahq.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-xosvxq-shard-0&authSource=admin&retryWrites=true&w=majority' % (
    myMongoCreds['username'], myMongoCreds['password'])

 #mongoexport --uri mongodb+srv://klemeragm:<PASSWORD>@cluster1.laahq.mongodb.net/<DATABASE> --collection <COLLECTION> --type <FILETYPE> --out <FILENAME>
 
 
>>>>>>> 95d5bba5a29031507e66ea42a40142bafc287ab7
class MyMongoDatabase:
    def __init__(self, dbName):
        myMongoClient = pymongo.MongoClient(myMongoUrl)
        self.db = myMongoClient[dbName]

    def insert(self, collectionName, tweet):
        tweetsCollection = self.db[collectionName]
<<<<<<< HEAD
        tweetsCollection.insert_one(tweet)
=======
        tweetsCollection.insert_one(tweet)
        
    def output(self, colletionName, tweet):
        
>>>>>>> 95d5bba5a29031507e66ea42a40142bafc287ab7
