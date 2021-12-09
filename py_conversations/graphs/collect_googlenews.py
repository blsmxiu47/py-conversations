from dagster import graph


@graph
def collect_googlenews():
    ingest_data(scrape_googlenews())


collect_googlenews = collect_googlenews.to_job()
