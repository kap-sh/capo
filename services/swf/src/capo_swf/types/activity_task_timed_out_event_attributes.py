"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskTimedOutEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.activity_task_timeout_type
    import capo_swf.types.event_id
    import capo_swf.types.limited_data


class ActivityTaskTimedOutEventAttributes(TypedDict, closed=True):
    timeout_type: "capo_swf.types.activity_task_timeout_type.ActivityTaskTimeoutType"
    """<p>The type of the timeout that caused this event.</p>"""
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    details: NotRequired["capo_swf.types.limited_data.LimitedData"]
    """<p>Contains the content of the <code>details</code> parameter for the last call made by the activity to <code>RecordActivityTaskHeartbeat</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskTimedOutEventAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.activity_task_timeout_type

    out["timeoutType"] = (
        capo_swf.types.activity_task_timeout_type.serialize_aws_json_1_0(
            value["timeout_type"]
        )
    )
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskTimedOutEventAttributes:
    out: ActivityTaskTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timeoutType") is not None:
        import capo_swf.types.activity_task_timeout_type

        out["timeout_type"] = (
            capo_swf.types.activity_task_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    else:
        import typing

        out["timeout_type"] = typing.cast(
            "capo_swf.types.activity_task_timeout_type.ActivityTaskTimeoutType", ""
        )
    if data.get("scheduledEventId") is not None:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if data.get("details") is not None:
        out["details"] = data["details"]
    return out
