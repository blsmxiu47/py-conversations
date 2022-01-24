from dagster import Any, String, Int
from py_conversations.graphs.collect_insert_tweets import collect_insert_tweets


def test_collect_insert_tweets():
    """
    TODO: this.*
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
