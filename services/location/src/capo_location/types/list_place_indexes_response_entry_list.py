"""Generated from Smithy shape ``com.amazonaws.location#ListPlaceIndexesResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_place_indexes_response_entry

ListPlaceIndexesResponseEntryList: TypeAlias = list[
    "capo_location.types.list_place_indexes_response_entry.ListPlaceIndexesResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaceIndexesResponseEntryList) -> list:
    import capo_location.types.list_place_indexes_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.list_place_indexes_response_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListPlaceIndexesResponseEntryList:
    import capo_location.types.list_place_indexes_response_entry

    out: ListPlaceIndexesResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.list_place_indexes_response_entry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ListPlaceIndexesResponseEntryList) -> list[Any]:
    import capo_location.types.list_place_indexes_response_entry

    return [
        capo_location.types.list_place_indexes_response_entry.redact_sensitive(item)
        for item in value
    ]
