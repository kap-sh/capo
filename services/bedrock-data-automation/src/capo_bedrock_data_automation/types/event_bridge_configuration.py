"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EventBridgeConfiguration``."""

from typing_extensions import TypedDict


class EventBridgeConfiguration(TypedDict, closed=True):
    event_bridge_enabled: "bool"
    """Event bridge flag."""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeConfiguration) -> dict:
    out: dict = {}
    out["eventBridgeEnabled"] = value["event_bridge_enabled"]
    return out


def deserialize_json(data: dict) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("eventBridgeEnabled") is not None:
        out["event_bridge_enabled"] = data["eventBridgeEnabled"]
    else:
        out["event_bridge_enabled"] = False
    return out
