import tweepy
import configparser

config = configparser.ConfigParser()
config.read("./credentials/config.ini_example") # 


def connectToTwitterAPI():
    consumer_key = config.get("TwitterAPI", "consumer_key")
    consumer_secret = config.get("TwitterAPI", "consumer_secret")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    return tweepy.API(auth)
