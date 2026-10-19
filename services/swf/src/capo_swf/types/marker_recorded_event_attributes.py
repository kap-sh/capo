"""Generated from Smithy shape ``com.amazonaws.swf#MarkerRecordedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.marker_name


class MarkerRecordedEventAttributes(TypedDict, closed=True):
    marker_name: "capo_swf.types.marker_name.MarkerName"
    """<p>The name of the marker.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>The details of the marker.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>RecordMarker</code> decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarkerRecordedEventAttributes) -> dict:
    out: dict = {}
    out["markerName"] = value["marker_name"]
    if "details" in value:
        out["details"] = value["details"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MarkerRecordedEventAttributes:
    out: MarkerRecordedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("markerName") is not None:
        out["marker_name"] = data["markerName"]
    else:
        out["marker_name"] = ""
    if data.get("details") is not None:
        out["details"] = data["details"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
