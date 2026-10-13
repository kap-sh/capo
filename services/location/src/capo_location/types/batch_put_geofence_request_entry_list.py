"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceRequestEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_put_geofence_request_entry

BatchPutGeofenceRequestEntryList: TypeAlias = list[
    "capo_location.types.batch_put_geofence_request_entry.BatchPutGeofenceRequestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceRequestEntryList) -> list:
    import capo_location.types.batch_put_geofence_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_location.types.batch_put_geofence_request_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchPutGeofenceRequestEntryList:
    import capo_location.types.batch_put_geofence_request_entry

    out: BatchPutGeofenceRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.batch_put_geofence_request_entry.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchPutGeofenceRequestEntryList) -> list[Any]:
    import capo_location.types.batch_put_geofence_request_entry

    return [
        capo_location.types.batch_put_geofence_request_entry.redact_sensitive(item)
        for item in value
    ]
