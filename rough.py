import re
from textblob import TextBlob


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def get_min_max(tweets):
    ids = []
    for tweet in tweets:
        # print tweet
        if type(tweet) is list:
            tweet = tweet[0]
        ids.append(tweet.id)
    min_id = min(ids)
    max_id = max(ids)
    return min_id, max_id


def get_tweets(term, count):
    all_tweets = []
    max_id = 843567375765159939000000
    print max_id
    loop_count = count / 100
    for i in range(loop_count):
        tweets = api.GetSearch(term=term, count=100)
        print 'Total number of tweets found - ' + str(len(tweets))
        try:
            min_id, max_id = get_min_max(tweets)
            all_tweets = all_tweets + tweets
        except:
            pass
    return all_tweets


def print_tweet(tweet):
    print '---- Printing tweet ----'
    print tweet.favorite_count
    print tweet.text
    print ' --------- x --------- '


#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import twitter
import json

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '113707618-Hcynv2DrvuSs7ZhDd4k3mjW3xrnIQspYqnX9fGZq'
ACCESS_SECRET = '4dEvHrT7l6pIZbegTef8cOxpC3RkyWuOXoJXmGbJrtTXS'
CONSUMER_KEY = 'cLMfRK5UwlxPEKSGtOHpIMCxO'
CONSUMER_SECRET = 'c5fr8Ezh8iTGK2LD8fcMucUl70Tr3lA0rh737UhGVvgCwhB0oP'

# Initiate the connection to Twitter Streaming API
#twitter_stream = TwitterStream(auth=oauth)
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)
print(api.VerifyCredentials())

# tweets = api.GetSearch(term='Yogi Adityanath', count = 10, max_id = 843567375765159939000000)
tweets = get_tweets('Yogi Adityanath', 200)
min_id, max_id = get_min_max(tweets)
print 'Total number of tweets fetched = ' + str(len(tweets))

print min_id
print max_id
