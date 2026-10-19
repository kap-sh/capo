"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_bus_name


class DeleteEventBusRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.event_bus_name.EventBusName"
    """<p>The name of the event bus to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventBusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventBusRequest:
    out: DeleteEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
