"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class ActivityTypeConfiguration(TypedDict, closed=True):
    default_task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum duration for tasks of an activity type specified when registering the activity type. You can override this default when scheduling a task through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_heartbeat_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum time, in seconds, before which a worker processing a task must report progress by calling <a>RecordActivityTaskHeartbeat</a>.</p> <p>You can specify this value only when <i>registering</i> an activity type. The registered default value can be overridden when you schedule a task through the <code>ScheduleActivityTask</code> <a>Decision</a>. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an <code>UnknownResource</code> fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_list: NotRequired["capo_swf.types.task_list.TaskList"]
    """<p> The default task list specified for this activity type at registration. This default is used if a task list isn't provided when a task is scheduled through the <code>ScheduleActivityTask</code> <a>Decision</a>. You can override the default registered task list when scheduling a task through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p>"""
    default_task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> The default task priority for tasks of this activity type, specified at registration. If not set, then <code>0</code> is used as the default priority. This default can be overridden when scheduling an activity task.</p> <p>Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    default_task_schedule_to_start_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum duration, specified when registering the activity type, that a task of an activity type can wait before being assigned to a worker. You can override this default when scheduling a task through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_schedule_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum duration, specified when registering the activity type, for tasks of this activity type. You can override this default when scheduling a task through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTypeConfiguration) -> dict:
    out: dict = {}
    if "default_task_start_to_close_timeout" in value:
        out["defaultTaskStartToCloseTimeout"] = value[
            "default_task_start_to_close_timeout"
        ]
    if "default_task_heartbeat_timeout" in value:
        out["defaultTaskHeartbeatTimeout"] = value["default_task_heartbeat_timeout"]
    if "default_task_list" in value:
        import capo_swf.types.task_list

        out["defaultTaskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
            value["default_task_list"]
        )
    if "default_task_priority" in value:
        out["defaultTaskPriority"] = value["default_task_priority"]
    if "default_task_schedule_to_start_timeout" in value:
        out["defaultTaskScheduleToStartTimeout"] = value[
            "default_task_schedule_to_start_timeout"
        ]
    if "default_task_schedule_to_close_timeout" in value:
        out["defaultTaskScheduleToCloseTimeout"] = value[
            "default_task_schedule_to_close_timeout"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTypeConfiguration:
    out: ActivityTypeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("defaultTaskStartToCloseTimeout") is not None:
        out["default_task_start_to_close_timeout"] = data[
            "defaultTaskStartToCloseTimeout"
        ]
    if data.get("defaultTaskHeartbeatTimeout") is not None:
        out["default_task_heartbeat_timeout"] = data["defaultTaskHeartbeatTimeout"]
    if data.get("defaultTaskList") is not None:
        import capo_swf.types.task_list

        out["default_task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["defaultTaskList"]
        )
    if data.get("defaultTaskPriority") is not None:
        out["default_task_priority"] = data["defaultTaskPriority"]
    if data.get("defaultTaskScheduleToStartTimeout") is not None:
        out["default_task_schedule_to_start_timeout"] = data[
            "defaultTaskScheduleToStartTimeout"
        ]
    if data.get("defaultTaskScheduleToCloseTimeout") is not None:
        out["default_task_schedule_to_close_timeout"] = data[
            "defaultTaskScheduleToCloseTimeout"
        ]
    return out
