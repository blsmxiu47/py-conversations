from dagster import graph, Selector, Field
from py_conversations.ops.insert_items import insert_items
from py_conversations.ops.scrape_googlenews import scrape_googlenews


@graph
def collect_insert_googlenews(collection_name='googlenews'):
    insert_items(collection_name=collection_name, items=scrape_googlenews())


collect_insert_googlenews = collect_insert_googlenews.to_job(
    config={
        'ops': {
            'insert_items': {
                'inputs': {
                    Field(str, is_required=True, description='Name of DB collection into which items shall be inserted'),
                    Field(list, is_required=True, description='Items to be inserted into DB collection')
                }
            }
        }
    }
)