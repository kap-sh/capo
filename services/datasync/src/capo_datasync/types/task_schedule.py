"""Generated from Smithy shape ``com.amazonaws.datasync#TaskSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.schedule_expression_cron
    import capo_datasync.types.schedule_status


class TaskSchedule(TypedDict, closed=True):
    schedule_expression: (
        "capo_datasync.types.schedule_expression_cron.ScheduleExpressionCron"
    )
    """<p>Specifies your task schedule by using a cron or rate expression.</p> <p>Use cron expressions for task schedules that run on a specific time and day. For example, the following cron expression creates a task schedule that runs at 8 AM on the first Wednesday of every month:</p> <p> <code>cron(0 8 * * 3#1)</code> </p> <p>Use rate expressions for task schedules that run on a regular interval. For example, the following rate expression creates a task schedule that runs every 12 hours:</p> <p> <code>rate(12 hours)</code> </p> <p>For information about cron and rate expression syntax, see the <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html"> <i>Amazon EventBridge User Guide</i> </a>.</p>"""
    status: NotRequired["capo_datasync.types.schedule_status.ScheduleStatus"]
    """<p>Specifies whether to enable or disable your task schedule. Your schedule is enabled by default, but there can be situations where you need to disable it. For example, you might need to pause a recurring transfer to fix an issue with your task or perform maintenance on your storage system.</p> <p>DataSync might disable your schedule automatically if your task fails repeatedly with the same error. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskScheduleDetails.html">TaskScheduleDetails</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSchedule) -> dict:
    out: dict = {}
    out["ScheduleExpression"] = value["schedule_expression"]
    if "status" in value:
        import capo_datasync.types.schedule_status

        out["Status"] = capo_datasync.types.schedule_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskSchedule:
    out: TaskSchedule = {}  # type: ignore[typeddict-item]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        raise DeserializationError("TaskSchedule.schedule_expression required")
    if data.get("Status") is not None:
        import capo_datasync.types.schedule_status

        out["status"] = capo_datasync.types.schedule_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
