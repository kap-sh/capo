"""Generated from Smithy shape ``com.amazonaws.scheduler#EventBridgeMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.event_bridge_metadata_key
    import capo_scheduler.types.event_bridge_metadata_value

EventBridgeMetadataMap: TypeAlias = dict[
    "capo_scheduler.types.event_bridge_metadata_key.EventBridgeMetadataKey",
    "capo_scheduler.types.event_bridge_metadata_value.EventBridgeMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EventBridgeMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EventBridgeMetadataMap:
    out: EventBridgeMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
