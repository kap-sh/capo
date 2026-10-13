"""Generated from Smithy shape ``com.amazonaws.location#ListKeysResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_keys_response_entry

ListKeysResponseEntryList: TypeAlias = list[
    "capo_location.types.list_keys_response_entry.ListKeysResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponseEntryList) -> list:
    import capo_location.types.list_keys_response_entry

    out: list = []
    for item in value:
        out.append(capo_location.types.list_keys_response_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListKeysResponseEntryList:
    import capo_location.types.list_keys_response_entry

    out: ListKeysResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.list_keys_response_entry.deserialize_json(item))
    return out


def redact_sensitive(value: ListKeysResponseEntryList) -> list[Any]:
    import capo_location.types.list_keys_response_entry

    return [
        capo_location.types.list_keys_response_entry.redact_sensitive(item)
        for item in value
    ]
