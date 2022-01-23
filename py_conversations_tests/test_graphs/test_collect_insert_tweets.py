from dagster import Any
from py_conversations.graphs.collect_insert_tweets import collect_insert_tweets


def test_collect_insert_tweets():
    """
    TODO: this.*
    """
    result = collect_insert_tweets.execute_in_process(
        run_config={
            'ops': {
                'get_tweets': {
                    'config': Any,
                    'outputs': [{
                        'last_id': {
                            'json': {
                                'path': str
                            }
                        }
                    }]
                }
            }
        }
    )

    assert result.success
