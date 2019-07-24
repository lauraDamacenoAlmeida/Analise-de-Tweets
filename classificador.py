from textblob import TextBlob as tb
import tweepy
import numpy as np

consumer_key = 'XXXXX'
consumer_secret = 'XXXXXX'
access_token = 'XXXXX'
access_token_secret = 'XXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
