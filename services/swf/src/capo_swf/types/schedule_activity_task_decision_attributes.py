"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleActivityTaskDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.activity_id
    import capo_swf.types.activity_type
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class ScheduleActivityTaskDecisionAttributes(TypedDict, closed=True):
    activity_type: "capo_swf.types.activity_type.ActivityType"
    """<p> The type of the activity task to schedule.</p>"""
    activity_id: "capo_swf.types.activity_id.ActivityId"
    r"""<p> The <code>activityId</code> of the activity task.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent workflow tasks. This data isn't sent to the activity.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The input provided to the activity task.</p>"""
    schedule_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration for this activity task.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A schedule-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-close timeout was specified at registration time then a fault is returned.</p> </note>"""
    task_list: NotRequired["capo_swf.types.task_list.TaskList"]
    r"""<p>If set, specifies the name of the task list in which to schedule the activity task. If not specified, the <code>defaultTaskList</code> registered with the activity type is used.</p> <note> <p>A task list for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default task list was specified at registration time then a fault is returned.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> If set, specifies the priority with which the activity task is to be assigned to a worker. This overrides the defaultTaskPriority specified when registering the activity type using <a>RegisterActivityType</a>. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    schedule_to_start_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> If set, specifies the maximum duration the activity task can wait to be assigned to a worker. This overrides the default schedule-to-start timeout specified when registering the activity type using <a>RegisterActivityType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A schedule-to-start timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default schedule-to-start timeout was specified at registration time then a fault is returned.</p> </note>"""
    start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the maximum duration a worker may take to process this activity task. This overrides the default start-to-close timeout specified when registering the activity type using <a>RegisterActivityType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A start-to-close timeout for this activity task must be specified either as a default for the activity type or through this field. If neither this field is set nor a default start-to-close timeout was specified at registration time then a fault is returned.</p> </note>"""
    heartbeat_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the maximum time before which a worker processing a task of this type must report progress by calling <a>RecordActivityTaskHeartbeat</a>. If the timeout is exceeded, the activity task is automatically timed out. If the worker subsequently attempts to record a heartbeat or returns a result, it is ignored. This overrides the default heartbeat timeout specified when registering the activity type using <a>RegisterActivityType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleActivityTaskDecisionAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.activity_type

    out["activityType"] = capo_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    out["activityId"] = value["activity_id"]
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "schedule_to_close_timeout" in value:
        out["scheduleToCloseTimeout"] = value["schedule_to_close_timeout"]
    if "task_list" in value:
        import capo_swf.types.task_list

        out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
            value["task_list"]
        )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    if "schedule_to_start_timeout" in value:
        out["scheduleToStartTimeout"] = value["schedule_to_start_timeout"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    if "heartbeat_timeout" in value:
        out["heartbeatTimeout"] = value["heartbeat_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleActivityTaskDecisionAttributes:
    out: ScheduleActivityTaskDecisionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("activityType") is not None:
        import capo_swf.types.activity_type

        out["activity_type"] = capo_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError(
            "ScheduleActivityTaskDecisionAttributes.activity_type required"
        )
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        raise DeserializationError(
            "ScheduleActivityTaskDecisionAttributes.activity_id required"
        )
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("scheduleToCloseTimeout") is not None:
        out["schedule_to_close_timeout"] = data["scheduleToCloseTimeout"]
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("scheduleToStartTimeout") is not None:
        out["schedule_to_start_timeout"] = data["scheduleToStartTimeout"]
    if data.get("startToCloseTimeout") is not None:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    if data.get("heartbeatTimeout") is not None:
        out["heartbeat_timeout"] = data["heartbeatTimeout"]
    return out
