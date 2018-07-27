#!/usr/bin/python3
# Sentiment Analysis-Understanding and Extracting Feelings from Tweets 
# The Tweet API lets you access an app's functionality form your code
# Utilizes TextBlob for NLP tasks and produces a sentiment score from comments.

# Written by Kyle C. Seike, Security Analyst.
# Used to monitor Twitter sentiment for and/or against the work environment.
# For Twitter API, please visit https://apps.twitter.com (you will have to sign
# in with a Twitter Account to create and maintain Twitter Apps.

import tweepy
from textblob import TextBlob

consumer_key = '[twitter_consumer_key]'
consumer_secret = '[twitter_consumer_secret]’
# Owner ID: [owner_id]

access_token = '[access_token]'
access_token_secret = '[access_token_secret]'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('[twitter_search1]')
public_tweets1 = api.search('[twitter_search2]')
public_tweets2 = api.search('[twitter_search3]')
public_tweets3 = api.search('[twitter_search4]')
public_tweets4 = api.search('[twitter_search5]')
public_tweets5 = api.search('[twitter_search6]')
public_tweets6 = api.search('[twitter_search7]')

# public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets1:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets2:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets3:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets4:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets5:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

for tweet in public_tweets6:
    print(tweet.text.encode('UTF-8').decode('UTF-8'))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
