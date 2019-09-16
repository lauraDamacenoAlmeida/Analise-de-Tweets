from TwitterSearch import *
import json

try:
    tweets = TwitterSearch(
        consumer_key='YGBqN97q8zcEZPH9zH9lXHvQk',
        consumer_secret='VXpXDPwo65jKYapTd2B9THviHNiGfcoEvcePUfPjkLIRWwZ1QP',
        access_token='1126108868122226691-6JEaygzLY7PnCKdd01U5e5dcE0GWOY',
        access_token_secret='XyMTSPKBVtrIROuP7AvPPEY7BWIh7V0xGQdUx4Px052bP'
    )
    pesquisa = TwitterSearchOrder()
    pesquisa.set_keywords(['cacau show'])
    pesquisa.set_language('pt')
    tweetss = []

    limit = 3

    for tweet in tweets.search_tweets_iterable(pesquisa):

        tweetss.append(tweet)
               # tweet
        #    "usuario": tweet["user"]["screen_name"],
        #    "tweet": tweet['text']
            #)
       #print(tweet)
        #tweetss.append('usuario:{0} tweet:{1}'.format({tweet['user']['screen_name']},tweet['text']))
    #with open('teste.json', 'w') as arq:
     #   json.dump(tweetss, arq, indent=1)
    print(len(tweetss))
    print(tweetss[0])
    with open('teste.json', 'w') as arq:
        json.dump(tweetss, arq, indent=2)
except TwitterSearchException as e:
    print(e)
