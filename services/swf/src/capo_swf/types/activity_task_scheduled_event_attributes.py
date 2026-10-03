"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskScheduledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.activity_id
    import capo_swf.types.activity_type
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.event_id
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class ActivityTaskScheduledEventAttributes(TypedDict, closed=True):
    activity_type: "capo_swf.types.activity_type.ActivityType"
    """<p>The type of the activity task.</p>"""
    activity_id: "capo_swf.types.activity_id.ActivityId"
    """<p>The unique ID of the activity task.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The input provided to the activity task.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn't sent to the activity.</p>"""
    schedule_to_start_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time the activity task can wait to be assigned to a worker.</p>"""
    schedule_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time for this activity task.</p>"""
    start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time a worker may take to process the activity task.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The task list in which the activity task has been scheduled.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> The priority to assign to the scheduled activity task. If set, this overrides any default priority value that was assigned when the activity type was registered.</p> <p>Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision that resulted in the scheduling of this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    heartbeat_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum time before which the worker processing this task must report progress by calling <a>RecordActivityTaskHeartbeat</a>. If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or return a result, it is ignored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskScheduledEventAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.activity_type

    out["activityType"] = capo_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    out["activityId"] = value["activity_id"]
    if "input" in value:
        out["input"] = value["input"]
    if "control" in value:
        out["control"] = value["control"]
    if "schedule_to_start_timeout" in value:
        out["scheduleToStartTimeout"] = value["schedule_to_start_timeout"]
    if "schedule_to_close_timeout" in value:
        out["scheduleToCloseTimeout"] = value["schedule_to_close_timeout"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    if "heartbeat_timeout" in value:
        out["heartbeatTimeout"] = value["heartbeat_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskScheduledEventAttributes:
    out: ActivityTaskScheduledEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("activityType") is not None:
        import capo_swf.types.activity_type

        out["activity_type"] = capo_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError(
            "ActivityTaskScheduledEventAttributes.activity_type required"
        )
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError(
            "ActivityTaskScheduledEventAttributes.activity_id required"
        )
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("scheduleToStartTimeout") is not None:
        out["schedule_to_start_timeout"] = data["scheduleToStartTimeout"]
    if data.get("scheduleToCloseTimeout") is not None:
        out["schedule_to_close_timeout"] = data["scheduleToCloseTimeout"]
    if data.get("startToCloseTimeout") is not None:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError(
            "ActivityTaskScheduledEventAttributes.task_list required"
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("heartbeatTimeout") is not None:
        out["heartbeat_timeout"] = data["heartbeatTimeout"]
    return out
