from py_conversations.graphs.collect_insert_googlenews import collect_insert_googlenews


def test_collect_insert_googlenews():
    """
    TODO: this.*
    """
    result = collect_insert_googlenews.execute_in_process()

    assert result.success
