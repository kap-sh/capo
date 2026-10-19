"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingPlanForList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.integer


class RestoreTestingPlanForList(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The date and time that a restore testing plan was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    last_execution_time: NotRequired["datetime.datetime"]
    """<p>The last time a restore test was run with the specified restore testing plan. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastExecutionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    last_update_time: NotRequired["datetime.datetime"]
    """<p>The date and time that the restore testing plan was updated. This update is in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdateTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    restore_testing_plan_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifiesa restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The restore testing plan name.</p>"""
    schedule_expression: "str"
    """<p>A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, Backup will use the default expression <code>cron(0 5 ? * * *)</code>.</p>"""
    schedule_expression_timezone: NotRequired["str"]
    """<p>Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.</p>"""
    start_window_hours: "capo_backup.types.integer.integer"
    """<p>Defaults to 24 hours.</p> <p>A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingPlanForList) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_execution_time" in value:
        import capo_backup.types._prelude.timestamp

        out["LastExecutionTime"] = capo_backup.types._prelude.timestamp.serialize_json(
            value["last_execution_time"]
        )
    if "last_update_time" in value:
        import capo_backup.types._prelude.timestamp

        out["LastUpdateTime"] = capo_backup.types._prelude.timestamp.serialize_json(
            value["last_update_time"]
        )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["ScheduleExpression"] = value["schedule_expression"]
    if "schedule_expression_timezone" in value:
        out["ScheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    out["StartWindowHours"] = value.get("start_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingPlanForList:
    out: RestoreTestingPlanForList = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["creation_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastExecutionTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["last_execution_time"] = (
            capo_backup.types._prelude.timestamp.deserialize_json(
                data["LastExecutionTime"]
            )
        )
    if data.get("LastUpdateTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["last_update_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    if data.get("RestoreTestingPlanArn") is not None:
        out["restore_testing_plan_arn"] = data["RestoreTestingPlanArn"]
    else:
        out["restore_testing_plan_arn"] = ""
    if data.get("RestoreTestingPlanName") is not None:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        out["restore_testing_plan_name"] = ""
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        out["schedule_expression"] = ""
    if data.get("ScheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["ScheduleExpressionTimezone"]
    if data.get("StartWindowHours") is not None:
        out["start_window_hours"] = data["StartWindowHours"]
    else:
        out["start_window_hours"] = 0
    return out
