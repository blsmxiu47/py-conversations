from dagster import graph
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.get_tweets import get_tweets


@graph
def collect_insert_tweets():
    topic = 'wildfires' # tmp, this'll actually be coming from the dashboard user's settings or selection
    last_id = None # tmp
    insert_items(get_tweets(topic, last_id)[0]) # TODO: insert_items takes a list, but we also need to In the last id from the last run and store the last id from this run


collect_insert_tweets = collect_insert_tweets.to_job()
