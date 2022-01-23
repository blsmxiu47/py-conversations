from py_conversations.ops.get_tweets import get_tweets

def test_get_tweets():
    response = get_tweets(topic='wildfires', last_id=1485314390639333378, limit=2)
    assert isinstance(response, tuple), "returned object should be of type 'tuple'"
    assert isinstance(response[0], list), "first tuple item should be of type 'list'"
    assert isinstance(response[0][0], dict), "tweets list items should be of type 'dict'"
    assert isinstance(response[1], int), "second tuple item should be of type 'int'"