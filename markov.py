from flask import Flask
import os
import twitter
import tweepy
from random import choice


def connect_twitter_api(twitter_handle):
    """Connect to Twitter API and authenticate."""
    # connect to Twitter API
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"]
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    #tweepy library to authenticate with OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    # get user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
    user_tweets_string = api.user_timeline(screen_name = twitter_handle, include_rts = True, count=20)


    return user_tweets_string


def make_markov_chain(user_tweets_string):
    """Takes in user tweets as one long string; outputs dictionary of Markov chains."""