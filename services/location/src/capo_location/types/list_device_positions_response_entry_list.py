"""Generated from Smithy shape ``com.amazonaws.location#ListDevicePositionsResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_device_positions_response_entry

ListDevicePositionsResponseEntryList: TypeAlias = list[
    "capo_location.types.list_device_positions_response_entry.ListDevicePositionsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicePositionsResponseEntryList) -> list:
    import capo_location.types.list_device_positions_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.list_device_positions_response_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListDevicePositionsResponseEntryList:
    import capo_location.types.list_device_positions_response_entry

    out: ListDevicePositionsResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.list_device_positions_response_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ListDevicePositionsResponseEntryList) -> list[Any]:
    import capo_location.types.list_device_positions_response_entry

    return [
        capo_location.types.list_device_positions_response_entry.redact_sensitive(item)
        for item in value
    ]
