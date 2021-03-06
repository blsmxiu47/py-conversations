from dagster import repository

from py_conversations.graphs.collect_insert_googlenews import collect_insert_googlenews
from py_conversations.schedules.schedules import hourly_collect_googlenews


@repository
def py_conversations():
    """
    The repository definition for this py_conversations Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [collect_insert_googlenews]
    schedules = [hourly_collect_googlenews]

    return jobs + schedules
