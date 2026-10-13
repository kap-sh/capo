"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceSuccessList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_put_geofence_success

BatchPutGeofenceSuccessList: TypeAlias = list[
    "capo_location.types.batch_put_geofence_success.BatchPutGeofenceSuccess"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceSuccessList) -> list:
    import capo_location.types.batch_put_geofence_success

    out: list = []
    for item in value:
        out.append(capo_location.types.batch_put_geofence_success.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutGeofenceSuccessList:
    import capo_location.types.batch_put_geofence_success

    out: BatchPutGeofenceSuccessList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.batch_put_geofence_success.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchPutGeofenceSuccessList) -> list[Any]:
    import capo_location.types.batch_put_geofence_success

    return [
        capo_location.types.batch_put_geofence_success.redact_sensitive(item)
        for item in value
    ]
