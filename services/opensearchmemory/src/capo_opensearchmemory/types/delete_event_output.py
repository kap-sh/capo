"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#DeleteEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.event_id


class DeleteEventOutput(TypedDict, closed=True):
    event_id: "capo_opensearchmemory.types.event_id.EventId"
    """<p>The ID of the deleted event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEventOutput) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEventOutput:
    out: DeleteEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    return out
