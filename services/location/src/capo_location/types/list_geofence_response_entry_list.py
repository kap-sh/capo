"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceResponseEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.list_geofence_response_entry

ListGeofenceResponseEntryList: TypeAlias = list[
    "capo_location.types.list_geofence_response_entry.ListGeofenceResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceResponseEntryList) -> list:
    import capo_location.types.list_geofence_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.list_geofence_response_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListGeofenceResponseEntryList:
    import capo_location.types.list_geofence_response_entry

    out: ListGeofenceResponseEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.list_geofence_response_entry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ListGeofenceResponseEntryList) -> list[Any]:
    import capo_location.types.list_geofence_response_entry

    return [
        capo_location.types.list_geofence_response_entry.redact_sensitive(item)
        for item in value
    ]
