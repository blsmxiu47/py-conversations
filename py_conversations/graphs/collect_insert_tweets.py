from dagster import InputDefinition, graph
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.get_tweets import get_tweets


@graph(
    name='collect_insert_tweets',
    input_defs=[
        InputDefinition('topic', str, default_value='wildfires'),
        InputDefinition('last_id', int, default_value=1485314390639333378),
        InputDefinition('limit', int, default_value=1)
    ]
)
def collect_insert_tweets(topic='wildfires', last_id=1485314390639333378, limit=1):
    insert_items(get_tweets(topic, last_id, limit)[0]) # TODO: insert_items takes a list, but we also need to In the last id from the last run and store the last id from this run
