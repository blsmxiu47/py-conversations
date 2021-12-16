from datetime import datetime

from dagster import schedule
from dagster.core.definitions import RunRequest

from py_conversations.graphs.collect_insert_googlenews import collect_insert_googlenews


@schedule(cron_schedule='0 * * * *', job=collect_insert_googlenews, execution_timezone='US/Pacific')
def hourly_collect_googlenews(_context):
    now = datetime.now()
    return RunRequest(run_key=now.strftime('%m/%d/%Y, %H:%M:%S'))
