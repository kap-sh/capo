"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ScheduleConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class ScheduleConfiguration(TypedDict, closed=True):
    cron_expression: NotRequired["str"]
    """<p>The schedule expression that determines when the workflow runs, as specified in the <code>schedule</code> parameter of the workflow's YAML definition. You can specify one of the following types of schedule expressions:</p> <ul> <li> <p>Apache Airflow cron expression – Five fields, such as <code>0 12 1 * *</code>.</p> </li> <li> <p>Apache Airflow schedule preset – <code>@hourly</code>, <code>@daily</code>, <code>@weekly</code>, <code>@monthly</code>, <code>@yearly</code>, or <code>@annually</code>.</p> </li> <li> <p>EventBridge Scheduler rate expression – For example, <code>rate(5 minutes)</code>. Supported units are minutes, hours, and days.</p> </li> <li> <p>EventBridge Scheduler cron expression – Six fields, such as <code>cron(0 12 * * ? *)</code>.</p> </li> </ul> <p>In a cron expression, specify either a day-of-month or a day-of-week, not both.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "cron_expression" in value:
        out["CronExpression"] = value["cron_expression"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CronExpression") is not None:
        out["cron_expression"] = data["CronExpression"]
    return out
