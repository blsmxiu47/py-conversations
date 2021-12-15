from dagster import graph
from dagster.core.definitions.input import InputDefinition
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.scrape_googlenews import scrape_googlenews


@graph(input_defs=[InputDefinition(name='collection_name')])
def collect_insert_googlenews(collection_name='googlenews'):
    insert_items(collection_name=collection_name, items=scrape_googlenews())


collect_insert_googlenews = collect_insert_googlenews.to_job()
