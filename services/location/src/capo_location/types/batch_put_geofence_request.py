"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_put_geofence_request_entry_list
    import capo_location.types.resource_name


class BatchPutGeofenceRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the geofences.</p>"""
    entries: "capo_location.types.batch_put_geofence_request_entry_list.BatchPutGeofenceRequestEntryList"
    """<p>The batch of geofences to be stored in a geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceRequest) -> dict:
    out: dict = {}
    import capo_location.types.batch_put_geofence_request_entry_list

    out["Entries"] = (
        capo_location.types.batch_put_geofence_request_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceRequest:
    out: BatchPutGeofenceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_location.types.batch_put_geofence_request_entry_list

        out["entries"] = (
            capo_location.types.batch_put_geofence_request_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out


def redact_sensitive(value: BatchPutGeofenceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_location.types.batch_put_geofence_request_entry_list

        out["entries"] = (
            capo_location.types.batch_put_geofence_request_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out
