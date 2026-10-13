"""Generated from Smithy shape ``com.amazonaws.location#DevicePositionUpdateList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.device_position_update

DevicePositionUpdateList: TypeAlias = list[
    "capo_location.types.device_position_update.DevicePositionUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevicePositionUpdateList) -> list:
    import capo_location.types.device_position_update

    out: list = []
    for item in value:
        out.append(capo_location.types.device_position_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> DevicePositionUpdateList:
    import capo_location.types.device_position_update

    out: DevicePositionUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.device_position_update.deserialize_json(item))
    return out


def redact_sensitive(value: DevicePositionUpdateList) -> list[Any]:
    import capo_location.types.device_position_update

    return [
        capo_location.types.device_position_update.redact_sensitive(item)
        for item in value
    ]
