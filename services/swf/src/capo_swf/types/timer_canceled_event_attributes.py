"""Generated from Smithy shape ``com.amazonaws.swf#TimerCanceledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.timer_id


class TimerCanceledEventAttributes(TypedDict, closed=True):
    timer_id: "capo_swf.types.timer_id.TimerId"
    """<p>The unique ID of the timer that was canceled.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>TimerStarted</code> event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>CancelTimer</code> decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimerCanceledEventAttributes) -> dict:
    out: dict = {}
    out["timerId"] = value["timer_id"]
    out["startedEventId"] = value.get("started_event_id", 0)
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimerCanceledEventAttributes:
    out: TimerCanceledEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timerId") is not None:
        out["timer_id"] = data["timerId"]
    else:
        out["timer_id"] = ""
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
