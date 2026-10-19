"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event_id


class DeleteEventOutput(TypedDict, closed=True):
    event_id: "capo_bedrock_agentcore.types.event_id.EventId"
    """<p>The identifier of the event that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventOutput) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> DeleteEventOutput:
    out: DeleteEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    return out
