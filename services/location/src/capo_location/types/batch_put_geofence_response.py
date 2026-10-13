"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_put_geofence_error_list
    import capo_location.types.batch_put_geofence_success_list


class BatchPutGeofenceResponse(TypedDict, closed=True):
    successes: "capo_location.types.batch_put_geofence_success_list.BatchPutGeofenceSuccessList"
    """<p>Contains each geofence that was successfully stored in a geofence collection.</p>"""
    errors: (
        "capo_location.types.batch_put_geofence_error_list.BatchPutGeofenceErrorList"
    )
    """<p>Contains additional error details for each geofence that failed to be stored in a geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_put_geofence_success_list

    out["Successes"] = (
        capo_location.types.batch_put_geofence_success_list.serialize_json(
            value["successes"]
        )
    )
    import capo_location.types.batch_put_geofence_error_list

    out["Errors"] = capo_location.types.batch_put_geofence_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceResponse:
    out: BatchPutGeofenceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Successes") is not None:
        import capo_location.types.batch_put_geofence_success_list

        out["successes"] = (
            capo_location.types.batch_put_geofence_success_list.deserialize_json(
                data["Successes"]
            )
        )
    else:
        raise DeserializationError("BatchPutGeofenceResponse.successes required")
    if data.get("Errors") is not None:
        import capo_location.types.batch_put_geofence_error_list

        out["errors"] = (
            capo_location.types.batch_put_geofence_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchPutGeofenceResponse.errors required")
    return out


def redact_sensitive(value: BatchPutGeofenceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "successes" in value:
        import capo_location.types.batch_put_geofence_success_list

        out["successes"] = (
            capo_location.types.batch_put_geofence_success_list.redact_sensitive(
                value["successes"]
            )
        )
    return out
