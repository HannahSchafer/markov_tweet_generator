# encoding=utf8  
from __future__ import unicode_literals
from flask import Flask
import os
import twitter
import tweepy
from random import choice
import pickle

markov_cache = {}

# user sends in twitter_handle  - server gets it
# create a new function - takes in twitter handle, checks to see if twitter_handle is in markov_cache
# if TH in MC, then pull and use markov_chain from cache, pass to make_markov_tweet
# twitter_handle - key

#ELSE
# use make_markov_chain inside check cache, so that we can add new chain to the cache 
# also connct to twitter if twitter handle not in cache

def check_cache(twitter_handle):
    """Checks cache for twitter handle. If there, use cached mar_chain, else
        connect to API and make markov chain, cache markov chain."""

    if twitter_handle in markov_cache.keys():
        mar_chains = markov_cache[twitter_handle]
        return mar_chains

    else:
        user_tweets_string = connect_twitter_api(twitter_handle)
        mar_chains = make_markov_chain(user_tweets_string)

        # add new mar_chain to cache
        markov_cache[twitter_handle] = mar_chains

        return mar_chains



def connect_twitter_api(twitter_handle):
    """Connect to Twitter API and authenticate."""
    # connect to Twitter API
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"]
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    #tweepy library for OAuth authentification
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    # get user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
    user_tweet_info = (api.user_timeline(screen_name = twitter_handle, 
                       exclude_replies = True, include_rts = False, count=200))

   
    user_tweets_string = ""
    for status in user_tweet_info:
        user_tweets_string += " " + status.text

    # one time use pickle file dump to use for mocking API in tests.py:
    # twitter_data = user_tweets_string
    # pickle.dump( twitter_data, open( "twitter_data.pickle", "wb"))

    return user_tweets_string



def make_markov_chain(user_tweets_string):
    """Takes in user tweets as one string; outputs dictionary of Markov chains.
       Ex. key-val pair: {('I', 'love') : [mangoes, apples, mangoes, oranges]}"""

    
    mar_chains = {}

    words = user_tweets_string.split()

    # iterate through words; save word pairs in tuples as keys & connected
    # words in list as values
    for index in range(len(words) - 2):
        mar_key = (words[index], words[index + 1])
        mar_val = words[index + 2]

        mar_chains.setdefault(mar_key, []).append(mar_val)

    return mar_chains



def make_markov_tweet(mar_chains):
    """Takes in Markov chains dictionary and returns new generated tweet."""

    # choose at random a key pair of words to begin with from keys list
    mar_key = choice(mar_chains.keys())

    # start_words will begin the tweet
    start_words = [mar_key[0], mar_key[1]]

    # initialize chars to later restrict to 140 (tweet char limit)
    chars = 0

    # iterate through chain, add new word to starting string (limit 140 chars)
    while mar_key in mar_chains:
        new_word = choice(mar_chains[mar_key])
        if chars + len(new_word) > 140:
            break
        start_words.append(new_word)
        mar_key = (mar_key[1], new_word)
        chars = len(" ".join(start_words))

    return " ".join(start_words)





