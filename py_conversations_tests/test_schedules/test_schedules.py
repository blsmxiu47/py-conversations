from datetime import datetime

from dagster import build_schedule_context, validate_run_config

from py_conversations.graphs.collect_insert_googlenews import collect_insert_googlenews
from py_conversations.schedules.schedules import hourly_collect_googlenews


def test_configurable_job_schedule():
    context = build_schedule_context(scheduled_execution_time=datetime.now())
    run_request = hourly_collect_googlenews(context)
    assert validate_run_config(collect_insert_googlenews, run_request.run_config)