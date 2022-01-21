from dagster import graph
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.get_tweets import get_tweets


@graph
def collect_insert_tweets():
    insert_items(get_tweets())


collect_insert_tweets = collect_insert_tweets.to_job()
