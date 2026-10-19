"""Generated from Smithy shape ``com.amazonaws.supplychain#SendDataIntegrationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.uuid


class SendDataIntegrationEventResponse(TypedDict, closed=True):
    event_id: "capo_supplychain.types.uuid.UUID"
    """<p>The unique event identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataIntegrationEventResponse) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> SendDataIntegrationEventResponse:
    out: SendDataIntegrationEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    return out
