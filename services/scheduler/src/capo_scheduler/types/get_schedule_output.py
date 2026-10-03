"""Generated from Smithy shape ``com.amazonaws.scheduler#GetScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.action_after_completion
    import capo_scheduler.types.creation_date
    import capo_scheduler.types.description
    import capo_scheduler.types.end_date
    import capo_scheduler.types.flexible_time_window
    import capo_scheduler.types.kms_key_arn
    import capo_scheduler.types.last_modification_date
    import capo_scheduler.types.name
    import capo_scheduler.types.schedule_arn
    import capo_scheduler.types.schedule_expression
    import capo_scheduler.types.schedule_expression_timezone
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.schedule_state
    import capo_scheduler.types.start_date
    import capo_scheduler.types.target


class GetScheduleOutput(TypedDict, closed=True):
    arn: NotRequired["capo_scheduler.types.schedule_arn.ScheduleArn"]
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""
    group_name: NotRequired[
        "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group associated with this schedule.</p>"""
    name: NotRequired["capo_scheduler.types.name.Name"]
    """<p>The name of the schedule.</p>"""
    schedule_expression: NotRequired[
        "capo_scheduler.types.schedule_expression.ScheduleExpression"
    ]
    """<p> The expression that defines when the schedule runs. The following formats are supported. </p> <ul> <li> <p> <code>at</code> expression - <code>at(yyyy-mm-ddThh:mm:ss)</code> </p> </li> <li> <p> <code>rate</code> expression - <code>rate(value unit)</code> </p> </li> <li> <p> <code>cron</code> expression - <code>cron(fields)</code> </p> </li> </ul> <p> You can use <code>at</code> expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use <code>rate</code> and <code>cron</code> expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. </p> <p> A <code>cron</code> expression consists of six fields separated by white spaces: <code>(minutes hours day_of_month month day_of_week year)</code>. </p> <p> A <code>rate</code> expression consists of a <i>value</i> as a positive integer, and a <i>unit</i> with the following options: <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code> </p> <p> For more information and examples, see <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">Schedule types on EventBridge Scheduler</a> in the <i>EventBridge Scheduler User Guide</i>. </p>"""
    start_date: NotRequired["capo_scheduler.types.start_date.StartDate"]
    """<p>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the <code>StartDate</code> you specify. EventBridge Scheduler ignores <code>StartDate</code> for one-time schedules.</p>"""
    end_date: NotRequired["capo_scheduler.types.end_date.EndDate"]
    """<p>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the <code>EndDate</code> you specify. EventBridge Scheduler ignores <code>EndDate</code> for one-time schedules.</p>"""
    description: NotRequired["capo_scheduler.types.description.Description"]
    """<p>The description of the schedule.</p>"""
    schedule_expression_timezone: NotRequired[
        "capo_scheduler.types.schedule_expression_timezone.ScheduleExpressionTimezone"
    ]
    """<p>The timezone in which the scheduling expression is evaluated.</p>"""
    state: NotRequired["capo_scheduler.types.schedule_state.ScheduleState"]
    """<p>Specifies whether the schedule is enabled or disabled.</p>"""
    creation_date: NotRequired["capo_scheduler.types.creation_date.CreationDate"]
    """<p>The time at which the schedule was created.</p>"""
    last_modification_date: NotRequired[
        "capo_scheduler.types.last_modification_date.LastModificationDate"
    ]
    """<p>The time at which the schedule was last modified.</p>"""
    kms_key_arn: NotRequired["capo_scheduler.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN for a customer managed KMS Key that is be used to encrypt and decrypt your data.</p>"""
    target: NotRequired["capo_scheduler.types.target.Target"]
    """<p>The schedule target.</p>"""
    flexible_time_window: NotRequired[
        "capo_scheduler.types.flexible_time_window.FlexibleTimeWindow"
    ]
    """<p>Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.</p>"""
    action_after_completion: NotRequired[
        "capo_scheduler.types.action_after_completion.ActionAfterCompletion"
    ]
    """<p>Indicates the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScheduleOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "start_date" in value:
        import capo_scheduler.types.start_date

        out["StartDate"] = capo_scheduler.types.start_date.serialize_json(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_scheduler.types.end_date

        out["EndDate"] = capo_scheduler.types.end_date.serialize_json(value["end_date"])
    if "description" in value:
        out["Description"] = value["description"]
    if "schedule_expression_timezone" in value:
        out["ScheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    if "state" in value:
        out["State"] = value["state"]
    if "creation_date" in value:
        import capo_scheduler.types.creation_date

        out["CreationDate"] = capo_scheduler.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modification_date" in value:
        import capo_scheduler.types.last_modification_date

        out["LastModificationDate"] = (
            capo_scheduler.types.last_modification_date.serialize_json(
                value["last_modification_date"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "target" in value:
        import capo_scheduler.types.target

        out["Target"] = capo_scheduler.types.target.serialize_json(value["target"])
    if "flexible_time_window" in value:
        import capo_scheduler.types.flexible_time_window

        out["FlexibleTimeWindow"] = (
            capo_scheduler.types.flexible_time_window.serialize_json(
                value["flexible_time_window"]
            )
        )
    if "action_after_completion" in value:
        out["ActionAfterCompletion"] = value["action_after_completion"]
    return out


def deserialize_json(data: dict) -> GetScheduleOutput:
    out: GetScheduleOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("StartDate") is not None:
        import capo_scheduler.types.start_date

        out["start_date"] = capo_scheduler.types.start_date.deserialize_json(
            data["StartDate"]
        )
    if data.get("EndDate") is not None:
        import capo_scheduler.types.end_date

        out["end_date"] = capo_scheduler.types.end_date.deserialize_json(
            data["EndDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ScheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["ScheduleExpressionTimezone"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("CreationDate") is not None:
        import capo_scheduler.types.creation_date

        out["creation_date"] = capo_scheduler.types.creation_date.deserialize_json(
            data["CreationDate"]
        )
    if data.get("LastModificationDate") is not None:
        import capo_scheduler.types.last_modification_date

        out["last_modification_date"] = (
            capo_scheduler.types.last_modification_date.deserialize_json(
                data["LastModificationDate"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Target") is not None:
        import capo_scheduler.types.target

        out["target"] = capo_scheduler.types.target.deserialize_json(data["Target"])
    if data.get("FlexibleTimeWindow") is not None:
        import capo_scheduler.types.flexible_time_window

        out["flexible_time_window"] = (
            capo_scheduler.types.flexible_time_window.deserialize_json(
                data["FlexibleTimeWindow"]
            )
        )
    if data.get("ActionAfterCompletion") is not None:
        out["action_after_completion"] = data["ActionAfterCompletion"]
    return out
