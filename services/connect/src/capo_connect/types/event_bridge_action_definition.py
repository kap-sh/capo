"""Generated from Smithy shape ``com.amazonaws.connect#EventBridgeActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.event_bridge_action_name


class EventBridgeActionDefinition(TypedDict, closed=True):
    name: "capo_connect.types.event_bridge_action_name.EventBridgeActionName"
    """<p>The name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeActionDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> EventBridgeActionDefinition:
    out: EventBridgeActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
