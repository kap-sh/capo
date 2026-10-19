"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskTimedOutEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.decision_task_timeout_type
    import capo_swf.types.event_id


class DecisionTaskTimedOutEventAttributes(TypedDict, closed=True):
    timeout_type: "capo_swf.types.decision_task_timeout_type.DecisionTaskTimeoutType"
    """<p>The type of timeout that expired before the decision task could be completed.</p>"""
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskScheduled</code> event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskStarted</code> event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskTimedOutEventAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.decision_task_timeout_type

    out["timeoutType"] = (
        capo_swf.types.decision_task_timeout_type.serialize_aws_json_1_0(
            value["timeout_type"]
        )
    )
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTaskTimedOutEventAttributes:
    out: DecisionTaskTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timeoutType") is not None:
        import capo_swf.types.decision_task_timeout_type

        out["timeout_type"] = (
            capo_swf.types.decision_task_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    else:
        import typing

        out["timeout_type"] = typing.cast(
            "capo_swf.types.decision_task_timeout_type.DecisionTaskTimeoutType", ""
        )
    if data.get("scheduledEventId") is not None:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    return out
