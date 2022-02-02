from datetime import datetime
import json
import pdb
from pprint import pprint

import tweepy

import settings

CONSUMER_KEY = settings.TWITTER_API_KEY
CONSUMER_SECRET = settings.TWITTER_API_SECRET_KEY
ACCESS_TOKEN = settings.TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.TWITTER_ACCESS_TOKEN_SECRET

def get_tweets(topic, last_id=None, limit=10):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    start_date = datetime.now().strftime('%Y-%m-%d')
    query = f'{topic} -filter:retweets since:{start_date}'
    tweets = api.search_tweets(
        q=query,
        since_id=last_id,
        count=limit)
    
    tweets_list = [
        json.loads(json.dumps(status._json)) for status in tweets]

    # set last id to be used as starting point for next run
    last_id = tweets_list[-1]['id']

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
    
    pprint(filtered_tweets[0])
    
    pdb.set_trace()
    return (tweets_list, last_id)

if __name__=='__main__':
    out_object = get_tweets('wildfires')
