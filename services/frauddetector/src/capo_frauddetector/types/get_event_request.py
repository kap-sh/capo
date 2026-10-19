"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string


class GetEventRequest(TypedDict, closed=True):
    event_id: "capo_frauddetector.types.string.string"
    """<p>The ID of the event to retrieve.</p>"""
    event_type_name: "capo_frauddetector.types.string.string"
    """<p>The event type of the event to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventRequest:
    out: GetEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        out["event_type_name"] = ""
    return out
