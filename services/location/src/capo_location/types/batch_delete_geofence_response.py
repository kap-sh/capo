"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteGeofenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_delete_geofence_error_list


class BatchDeleteGeofenceResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_delete_geofence_error_list.BatchDeleteGeofenceErrorList"
    """<p>Contains error details for each geofence that failed to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteGeofenceResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_delete_geofence_error_list

    out["Errors"] = capo_location.types.batch_delete_geofence_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteGeofenceResponse:
    out: BatchDeleteGeofenceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_location.types.batch_delete_geofence_error_list

        out["errors"] = (
            capo_location.types.batch_delete_geofence_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out
