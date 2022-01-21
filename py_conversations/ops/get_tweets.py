from datetime import datetime
import json

from dagster import op, In, Out
import tweepy

import settings

CONSUMER_KEY = settings.TWITTER_API_KEY
CONSUMER_SECRET = settings.TWITTER_API_SECRET_KEY
ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

@op(
    ins={
        'topic': In(str),
        'last_id': In(int)
    },
    out=Out(tuple)
)
def get_tweets(topic, last_id=None):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    start_date = datetime.now().strftime('%Y-%m-%d')
    query = f'{topic} since:{start_date}'
    tweets = api.search_tweets(
        q=query,
        since_id=last_id)
    
    tweets_list = [json.loads(json.dumps(status._json)) for status in tweets]

    # set last id to be used as starting point for next run
    last_id = tweets_list[-1]['id']
    
    return (tweets_list, last_id)
