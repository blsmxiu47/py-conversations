import os

from dagster import graph
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.get_tweets import get_tweets


@graph(
    name='collect_insert_tweets',
)
def collect_insert_tweets(topic, last_id, limit):
    insert_items(get_tweets(topic, last_id, limit))

collect_insert_tweets = collect_insert_tweets.to_job(
    config={
        'inputs': {
            'topic': { 'value': 'wildfires' },
            'last_id': { 'value': os.environ.get('LAST_ID')},
            'limit': {'value': 1 }
        }
    }
)
