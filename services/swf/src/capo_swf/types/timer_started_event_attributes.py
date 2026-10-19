"""Generated from Smithy shape ``com.amazonaws.swf#TimerStartedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds
    import capo_swf.types.event_id
    import capo_swf.types.timer_id


class TimerStartedEventAttributes(TypedDict, closed=True):
    timer_id: "capo_swf.types.timer_id.TimerId"
    """<p>The unique ID of the timer that was started.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent workflow tasks.</p>"""
    start_to_fire_timeout: "capo_swf.types.duration_in_seconds.DurationInSeconds"
    """<p>The duration of time after which the timer fires.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>StartTimer</code> decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimerStartedEventAttributes) -> dict:
    out: dict = {}
    out["timerId"] = value["timer_id"]
    if "control" in value:
        out["control"] = value["control"]
    out["startToFireTimeout"] = value["start_to_fire_timeout"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimerStartedEventAttributes:
    out: TimerStartedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("timerId") is not None:
        out["timer_id"] = data["timerId"]
    else:
        out["timer_id"] = ""
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("startToFireTimeout") is not None:
        out["start_to_fire_timeout"] = data["startToFireTimeout"]
    else:
        out["start_to_fire_timeout"] = ""
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
