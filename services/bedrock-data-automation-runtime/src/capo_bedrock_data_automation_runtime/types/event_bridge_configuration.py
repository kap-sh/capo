"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#EventBridgeConfiguration``."""

from typing_extensions import TypedDict


class EventBridgeConfiguration(TypedDict, closed=True):
    event_bridge_enabled: "bool"
    """Event bridge flag."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBridgeConfiguration) -> dict:
    out: dict = {}
    out["eventBridgeEnabled"] = value["event_bridge_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("eventBridgeEnabled") is not None:
        out["event_bridge_enabled"] = data["eventBridgeEnabled"]
    else:
        out["event_bridge_enabled"] = False
    return out
