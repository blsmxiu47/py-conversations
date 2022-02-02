from datetime import datetime
import json

from dagster import op, In, Out
import tweepy

import settings
from py_conversations.utils import set_local_var

CONSUMER_KEY = settings.TWITTER_API_KEY
CONSUMER_SECRET = settings.TWITTER_API_SECRET_KEY
ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

@op(
    ins={
        'topic': In(str),
        'last_id': In(int),
        'limit': In(int)
    },
    out={
        'tweets': Out(list)
    }
)
def get_tweets(topic, last_id, limit=10):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    start_date = datetime.now().strftime('%Y-%m-%d')
    query = f'{topic} since:{start_date}'
    tweets = api.search_tweets(
        q=query,
        since_id=last_id,
        count=limit)
    tweets_list = [json.loads(json.dumps(status._json)) for status in tweets]

    last_id = tweets_list[-1]['id'] # set last id to be used as starting point for next run
    # store_local({
    #     'name': 'last_id',
    #     'type': int,
    #     'value': last_id
    # })
    set_local_var('LAST_ID', last_id)

    keys_to_extract = [
        'id', 
        'created_at', 
        'lang',
        'retweet_count',
        'text'
        ]
    user_keys_to_extract = [
        'id',
        'screen_name',
        'profile_image_url',
        'url']

    filtered_tweets = []
    for tweet in tweets_list:
        d = {key: tweet[key] for key in keys_to_extract}
        d.update([(f'user_{key}', tweet['user'][key]) \
            for key in user_keys_to_extract])
        filtered_tweets.append(d)
    
    return filtered_tweets
