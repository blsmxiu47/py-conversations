from py_conversations.graphs.collect_googlenews import collect_googlenews


def test_collect_googlenews():
    """
    TODO: this.*
    """
    result = collect_googlenews.execute_in_process()

    assert result.success
