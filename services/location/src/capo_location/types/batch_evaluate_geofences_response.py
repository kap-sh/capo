"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_evaluate_geofences_error_list


class BatchEvaluateGeofencesResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_evaluate_geofences_error_list.BatchEvaluateGeofencesErrorList"
    """<p>Contains error details for each device that failed to evaluate its position against the given geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_evaluate_geofences_error_list

    out["Errors"] = (
        capo_location.types.batch_evaluate_geofences_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesResponse:
    out: BatchEvaluateGeofencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_location.types.batch_evaluate_geofences_error_list

        out["errors"] = (
            capo_location.types.batch_evaluate_geofences_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchEvaluateGeofencesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_location.types.batch_evaluate_geofences_error_list

        out["errors"] = (
            capo_location.types.batch_evaluate_geofences_error_list.redact_sensitive(
                value["errors"]
            )
        )
    return out
