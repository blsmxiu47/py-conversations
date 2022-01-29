from dagster import Any
from py_conversations.graphs.collect_insert_tweets import collect_insert_tweets


def test_collect_insert_tweets():
    """
    Tests the graph 'collect_insert_tweets'.
    Ops:
        get_tweets(topic, last_id, limit) --> insert_items
    Inputs:
        topic: topic or phrase with which to query Twitter API
        last_id: ID of last Tweet in most recent run of this graph to be used to decide starting point for this run's query
        limit: maximum count of tweets to return
    """
    result = collect_insert_tweets.execute_in_process(
        run_config={
            'inputs': {
                'topic': { 'value': 'wildfires' },
                'last_id': { 'value': 1485314390639333378 },
                'limit': {'value': 1 }
            },
            'ops': {
                'get_tweets': {
                    'config': Any
                }
            }
        }
    )

    assert result.success
