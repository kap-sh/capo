"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskScheduledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class DecisionTaskScheduledEventAttributes(TypedDict, closed=True):
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The name of the task list in which the decision task was scheduled.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> A task priority that, if set, specifies the priority for this decision task. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration for this decision task. The task is considered timed out if it doesn't completed within this duration.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    schedule_to_start_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time the decision task can wait to be assigned to a worker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskScheduledEventAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    if "schedule_to_start_timeout" in value:
        out["scheduleToStartTimeout"] = value["schedule_to_start_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTaskScheduledEventAttributes:
    out: DecisionTaskScheduledEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError(
            "DecisionTaskScheduledEventAttributes.task_list required"
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("startToCloseTimeout") is not None:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    if data.get("scheduleToStartTimeout") is not None:
        out["schedule_to_start_timeout"] = data["scheduleToStartTimeout"]
    return out
