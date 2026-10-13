"""Generated from Smithy shape ``com.amazonaws.location#ListTrackersResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_trackers_response_entry

ListTrackersResponseEntryList: TypeAlias = list[
    "capo_location.types.list_trackers_response_entry.ListTrackersResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackersResponseEntryList) -> list:
    import capo_location.types.list_trackers_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.list_trackers_response_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListTrackersResponseEntryList:
    import capo_location.types.list_trackers_response_entry

    out: ListTrackersResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.list_trackers_response_entry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ListTrackersResponseEntryList) -> list[Any]:
    import capo_location.types.list_trackers_response_entry

    return [
        capo_location.types.list_trackers_response_entry.redact_sensitive(item)
        for item in value
    ]
