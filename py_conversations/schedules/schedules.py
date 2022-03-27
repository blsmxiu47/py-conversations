from datetime import datetime

from dagster import schedule
from dagster.core.definitions import RunRequest

from py_conversations.graphs.collect_insert_googlenews import collect_insert_googlenews
from py_conversations.graphs.collect_insert_tweets import collect_insert_tweets
import settings


env_vars = {
    'MONGO_USERNAME': settings.MONGO_USERNAME,
    'MONGO_PW': settings.MONGO_PW,
    'MONGO_CLUSTER_NAME': settings.MONGO_CLUSTER_NAME,
    'MONGO_DB_NAME': settings.MONGO_DB_NAME
}


@schedule(cron_schedule='0 * * * *', job=collect_insert_googlenews, environment_vars=env_vars, execution_timezone='US/Pacific')
def hourly_collect_googlenews(_context):
    now = datetime.now()
    return RunRequest(run_key=now.strftime('%m/%d/%Y %H:%M:%S'))


@schedule(cron_schedule='0 * * * *', job=collect_insert_tweets, environment_vars=env_vars, execution_timezone='US/Pacific')
def hourly_collect_tweets(_context):
    now = datetime.now()
    return RunRequest(run_key=now.strftime('%m/%d/%Y %H:%M:%S'))