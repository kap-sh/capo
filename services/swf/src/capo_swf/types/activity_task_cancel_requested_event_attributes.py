"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskCancelRequestedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.activity_id
    import capo_swf.types.event_id


class ActivityTaskCancelRequestedEventAttributes(TypedDict, closed=True):
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>RequestCancelActivityTask</code> decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    activity_id: "capo_swf.types.activity_id.ActivityId"
    """<p>The unique ID of the task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskCancelRequestedEventAttributes) -> dict:
    out: dict = {}
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    out["activityId"] = value["activity_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskCancelRequestedEventAttributes:
    out: ActivityTaskCancelRequestedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        out["activity_id"] = ""
    return out
