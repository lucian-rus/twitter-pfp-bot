# https://gist.github.com/edsu/54e6f7d63df3866a87a15aed17b51eaf
#
# this file is based on the repo linked above, only having slight modifications regarding the get_tweet_data() function 

import sys
import json
import time
import logging
import twitter
import urllib.parse

from os import environ as e

# export your own twitter api keys here
e["CONSUMER_KEY"]        = "" 
e["CONSUMER_SECRET"]     = ""
e["ACCESS_TOKEN"]        = ""
e["ACCESS_TOKEN_SECRET"] = ""

t = twitter.Api(
    consumer_key        = e["CONSUMER_KEY"],
    consumer_secret     = e["CONSUMER_SECRET"],
    access_token_key    = e["ACCESS_TOKEN"],
    access_token_secret = e["ACCESS_TOKEN_SECRET"],
    sleep_on_rate_limit = True
)

# get tweet url 
def tweet_url(t):
    return "https://twitter.com/%s/status/%s" % (t.user.screen_name, t.id)

# get the tweet from which to scrape the replies
def get_tweets(filename):
    for line in open(filename):
        yield twitter.Status.NewFromJsonDict(json.loads(line))

# function that get replies from the tweet
def get_replies(tweet):
    user     = tweet.user.screen_name
    tweet_id = tweet.id
    max_id   = None

    while True:
        q = urllib.parse.urlencode({"q": "to:%s" % user})
        try:
            replies = t.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)
        except twitter.error.TwitterError as e:
            time.sleep(60)
            continue

        # get the replies in a recursive manner
        for reply in replies:
            if reply.in_reply_to_status_id == tweet_id:
                yield reply
                for reply_to_reply in get_replies(reply):
                    yield reply_to_reply
            max_id = reply.id
        if len(replies) != 100:
            break

# return tweet data 
def get_tweet_data():
    tweets_file = '..\\resources\\json\\tweets.json'
    
    data = []

    for tweet in get_tweets(tweets_file):
        for reply in get_replies(tweet):

            user  = reply.user.screen_name
            count = reply.favorite_count

            for i in reply.media:
                url = i.media_url

                api_data = (user, count, url)
                data.append(api_data)
    
    return data