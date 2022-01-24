from dagster import InputDefinition, OutputDefinition, graph, String, Int
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.get_tweets import get_tweets


@graph(
    name='collect_insert_tweets',
    # input_defs=[
    #     InputDefinition(name='topic', dagster_type=String, default_value='wildfires'),
    #     InputDefinition(name='last_id', dagster_type=Int, default_value=1485314390639333378),
    #     InputDefinition(name='limit', dagster_type=Int, default_value=1)
    # ]
)
def collect_insert_tweets(topic, last_id, limit):
    insert_items(get_tweets(topic, last_id, limit)) # TODO: insert_items takes a list, but we also need to In the last id from the last run and store the last id from this run
