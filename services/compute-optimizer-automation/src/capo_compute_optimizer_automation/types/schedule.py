"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#Schedule``."""

from typing_extensions import NotRequired, TypedDict


class Schedule(TypedDict, closed=True):
    schedule_expression: NotRequired["str"]
    """<p>The expression that defines when the schedule runs. <code>cron</code> expression is supported. A <code>cron</code> expression consists of six fields separated by white spaces: (<code>minutes</code> <code>hours</code> <code>day_of_month</code> <code>month</code> <code>day_of_week</code> <code>year</code>)</p> <note> <p>You can schedule rules to run at most once per day. Your cron expression must use specific values (not wildcards) for the minutes and hours fields. For example: (<code>30 12 * * *</code>) runs daily at 12:30 PM UTC.</p> </note>"""
    schedule_expression_timezone: NotRequired["str"]
    """<p>The timezone to use when interpreting the schedule expression.</p>"""
    execution_window_in_minutes: NotRequired["int"]
    """<p>The time window in minutes during which the automation rule can start implementing recommended actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Schedule) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_timezone" in value:
        out["scheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    if "execution_window_in_minutes" in value:
        out["executionWindowInMinutes"] = value["execution_window_in_minutes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    if data.get("scheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["scheduleExpressionTimezone"]
    if data.get("executionWindowInMinutes") is not None:
        out["execution_window_in_minutes"] = data["executionWindowInMinutes"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Schedule) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["scheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_timezone" in value:
        out["scheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    if "execution_window_in_minutes" in value:
        out["executionWindowInMinutes"] = value["execution_window_in_minutes"]
    return out


def deserialize_cbor(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    if data.get("scheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["scheduleExpressionTimezone"]
    if data.get("executionWindowInMinutes") is not None:
        out["execution_window_in_minutes"] = data["executionWindowInMinutes"]
    return out
