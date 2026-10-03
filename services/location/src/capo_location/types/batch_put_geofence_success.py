"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceSuccess``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.id
    import capo_location.types.timestamp


class BatchPutGeofenceSuccess(TypedDict, closed=True):
    geofence_id: "capo_location.types.id.Id"
    """<p>The geofence successfully stored in a geofence collection.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was stored in a geofence collection in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceSuccess) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceSuccess:
    out: BatchPutGeofenceSuccess = {}  # type: ignore[typeddict-item]
    if data.get("GeofenceId") is not None:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.geofence_id required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.update_time required")
    return out
