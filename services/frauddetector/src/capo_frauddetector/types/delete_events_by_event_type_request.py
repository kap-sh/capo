"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEventsByEventTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier


class DeleteEventsByEventTypeRequest(TypedDict, closed=True):
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventsByEventTypeRequest) -> dict:
    out: dict = {}
    out["eventTypeName"] = value["event_type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventsByEventTypeRequest:
    out: DeleteEventsByEventTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        out["event_type_name"] = ""
    return out
