from py_conversations.graphs.collect_googlenews import collect_googlenews


def test_collect_googlenews():
    """
    TODO: this.*
    """
    result = collect_googlenews.execute_in_process(
        run_config={
            'ops': {
                'insert_items': {
                    'inputs': {
                        'collection_name': 'googlenews',
                        'items': [{}, {}]
                    }
                }
            }
        }
    )

    assert result.success
