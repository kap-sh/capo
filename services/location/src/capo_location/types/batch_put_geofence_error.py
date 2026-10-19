"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_item_error
    import capo_location.types.id


class BatchPutGeofenceError(TypedDict, closed=True):
    geofence_id: "capo_location.types.id.Id"
    """<p>The geofence associated with the error message.</p>"""
    error: "capo_location.types.batch_item_error.BatchItemError"
    """<p>Contains details associated to the batch error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceError) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import capo_location.types.batch_item_error

    out["Error"] = capo_location.types.batch_item_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceError:
    out: BatchPutGeofenceError = {}  # type: ignore[typeddict-item]
    if data.get("GeofenceId") is not None:
        out["geofence_id"] = data["GeofenceId"]
    else:
        out["geofence_id"] = ""
    if data.get("Error") is not None:
        import capo_location.types.batch_item_error

        out["error"] = capo_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchPutGeofenceError.error required")
    return out
