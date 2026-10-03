"""Generated from Smithy shape ``com.amazonaws.scheduler#CreateScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_scheduler.types.action_after_completion
    import capo_scheduler.types.client_token
    import capo_scheduler.types.description
    import capo_scheduler.types.end_date
    import capo_scheduler.types.flexible_time_window
    import capo_scheduler.types.kms_key_arn
    import capo_scheduler.types.name
    import capo_scheduler.types.schedule_expression
    import capo_scheduler.types.schedule_expression_timezone
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.schedule_state
    import capo_scheduler.types.start_date
    import capo_scheduler.types.target


class CreateScheduleInput(TypedDict, closed=True):
    name: "capo_scheduler.types.name.Name"
    """<p>The name of the schedule that you are creating.</p>"""
    group_name: NotRequired[
        "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</p>"""
    schedule_expression: "capo_scheduler.types.schedule_expression.ScheduleExpression"
    """<p> The expression that defines when the schedule runs. The following formats are supported. </p> <ul> <li> <p> <code>at</code> expression - <code>at(yyyy-mm-ddThh:mm:ss)</code> </p> </li> <li> <p> <code>rate</code> expression - <code>rate(value unit)</code> </p> </li> <li> <p> <code>cron</code> expression - <code>cron(fields)</code> </p> </li> </ul> <p> You can use <code>at</code> expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use <code>rate</code> and <code>cron</code> expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. </p> <p> A <code>cron</code> expression consists of six fields separated by white spaces: <code>(minutes hours day_of_month month day_of_week year)</code>. </p> <p> A <code>rate</code> expression consists of a <i>value</i> as a positive integer, and a <i>unit</i> with the following options: <code>minute</code> | <code>minutes</code> | <code>hour</code> | <code>hours</code> | <code>day</code> | <code>days</code> </p> <p> For more information and examples, see <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html">Schedule types on EventBridge Scheduler</a> in the <i>EventBridge Scheduler User Guide</i>. </p>"""
    start_date: NotRequired["capo_scheduler.types.start_date.StartDate"]
    """<p>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the <code>StartDate</code> you specify. EventBridge Scheduler ignores <code>StartDate</code> for one-time schedules.</p>"""
    end_date: NotRequired["capo_scheduler.types.end_date.EndDate"]
    """<p>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the <code>EndDate</code> you specify. EventBridge Scheduler ignores <code>EndDate</code> for one-time schedules.</p>"""
    description: NotRequired["capo_scheduler.types.description.Description"]
    """<p>The description you specify for the schedule.</p>"""
    schedule_expression_timezone: NotRequired[
        "capo_scheduler.types.schedule_expression_timezone.ScheduleExpressionTimezone"
    ]
    """<p>The timezone in which the scheduling expression is evaluated.</p>"""
    state: NotRequired["capo_scheduler.types.schedule_state.ScheduleState"]
    """<p>Specifies whether the schedule is enabled or disabled.</p>"""
    kms_key_arn: NotRequired["capo_scheduler.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.</p>"""
    target: "capo_scheduler.types.target.Target"
    """<p>The schedule's target.</p>"""
    flexible_time_window: "capo_scheduler.types.flexible_time_window.FlexibleTimeWindow"
    """<p>Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.</p>"""
    client_token: NotRequired["capo_scheduler.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>"""
    action_after_completion: NotRequired[
        "capo_scheduler.types.action_after_completion.ActionAfterCompletion"
    ]
    """<p>Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleInput) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
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
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    import capo_scheduler.types.target

    out["Target"] = capo_scheduler.types.target.serialize_json(value["target"])
    import capo_scheduler.types.flexible_time_window

    out["FlexibleTimeWindow"] = (
        capo_scheduler.types.flexible_time_window.serialize_json(
            value["flexible_time_window"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "action_after_completion" in value:
        out["ActionAfterCompletion"] = value["action_after_completion"]
    return out


def deserialize_json(data: dict) -> CreateScheduleInput:
    out: CreateScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        raise DeserializationError("CreateScheduleInput.schedule_expression required")
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
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Target") is not None:
        import capo_scheduler.types.target

        out["target"] = capo_scheduler.types.target.deserialize_json(data["Target"])
    else:
        raise DeserializationError("CreateScheduleInput.target required")
    if data.get("FlexibleTimeWindow") is not None:
        import capo_scheduler.types.flexible_time_window

        out["flexible_time_window"] = (
            capo_scheduler.types.flexible_time_window.deserialize_json(
                data["FlexibleTimeWindow"]
            )
        )
    else:
        raise DeserializationError("CreateScheduleInput.flexible_time_window required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ActionAfterCompletion") is not None:
        out["action_after_completion"] = data["ActionAfterCompletion"]
    return out
