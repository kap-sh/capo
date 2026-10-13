"""Generated from Smithy shape ``com.amazonaws.location#ListMapsResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_maps_response_entry

ListMapsResponseEntryList: TypeAlias = list[
    "capo_location.types.list_maps_response_entry.ListMapsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMapsResponseEntryList) -> list:
    import capo_location.types.list_maps_response_entry

    out: list = []
    for item in value:
        out.append(capo_location.types.list_maps_response_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListMapsResponseEntryList:
    import capo_location.types.list_maps_response_entry

    out: ListMapsResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.list_maps_response_entry.deserialize_json(item))
    return out


def redact_sensitive(value: ListMapsResponseEntryList) -> list[Any]:
    import capo_location.types.list_maps_response_entry

    return [
        capo_location.types.list_maps_response_entry.redact_sensitive(item)
        for item in value
    ]
