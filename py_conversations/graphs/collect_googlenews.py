from dagster import graph
from py_conversations.ops.ingest_data import ingest_data
from py_conversations.ops.scrape_googlenews import scrape_googlenews


@graph
def collect_googlenews():
    ingest_data(scrape_googlenews())


collect_googlenews = collect_googlenews.to_job()
