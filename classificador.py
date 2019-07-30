from TwitterSearch import *
import json

try:
    tweets = TwitterSearch(
        consumer_key='Xxxxx',
        consumer_secret='XXXX',
        access_token='XXXXX',
        access_token_secret='XXXXXXXX'
    )
    pesquisa = TwitterSearchOrder()
    pesquisa.set_keywords(['IBM'])
    pesquisa.set_language('pt')
    tweetss = []
    for tweet in tweets.search_tweets_iterable(pesquisa):
        with open('tweets.json', 'a') as arq:
            json.dump(tweet, arq, indent=4)
        #tweetss.append({
         #   tweet
        #    "usuario": tweet["user"]["screen_name"],
        #    "tweet": tweet['text']
        #})
       #print(tweet)
        #tweetss.append('usuario:{0} tweet:{1}'.format({tweet['user']['screen_name']},tweet['text']))


except TwitterSearchException as e:
    print(e)

