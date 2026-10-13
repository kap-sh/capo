"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionErrorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_update_device_position_error

BatchUpdateDevicePositionErrorList: TypeAlias = list[
    "capo_location.types.batch_update_device_position_error.BatchUpdateDevicePositionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionErrorList) -> list:
    import capo_location.types.batch_update_device_position_error

    out: list = []
    for item in value:
        out.append(
            capo_location.types.batch_update_device_position_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDevicePositionErrorList:
    import capo_location.types.batch_update_device_position_error

    out: BatchUpdateDevicePositionErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.batch_update_device_position_error.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BatchUpdateDevicePositionErrorList) -> list[Any]:
    import capo_location.types.batch_update_device_position_error

    return [
        capo_location.types.batch_update_device_position_error.redact_sensitive(item)
        for item in value
    ]
