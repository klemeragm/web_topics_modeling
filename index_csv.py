#pacotes para o csv
import pandas as pd
import re
from connection import consumer_key, consumer_secret,access_token, access_token_secret
import tweepy 
import oauth2 as auth

#CSV

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
df  = pd.DataFrame()
user = ' '

def obter_tweets(usuario, limite=20):
    i = 0
    resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
    tweets = [[0 for x in range(2)] for y in range(limite)] # lista de tweets inicialmente vazia com o nome do usuário
    for r in resultados:
        # utiliza expressão regular para remover a URL do tweet
        # http pega o início da url
        # \S+ pega os caracteres não brancos (o final da URL) 
        tweet = re.sub(r'http\S+', '', r.full_text)
        tweets[i][0] = tweet.replace('\n', ' ') # adiciona na lista
        tweets[i][1] = usuario
        i+=1
        
    return tweets # retorna a lista de tweets

def createDataFrame(user_tweets, dataframe):
    df = pd.DataFrame(data=user_tweets, columns=['tweet', 'user'])
    return pd.concat([dataframe, df])


while True:
    user=input('Digite o usuário, não precisa digitar @ \nPara parar digite 0 \n')
    if(user == '0'):
        break  
    user_tweets = obter_tweets(user, 100)
    df = createDataFrame(user_tweets, df)


df.to_csv('/web_topics_modeling/dataframes/mytweets.csv', index=False)