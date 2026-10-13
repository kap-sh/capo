"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesErrorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_evaluate_geofences_error

BatchEvaluateGeofencesErrorList: TypeAlias = list[
    "capo_location.types.batch_evaluate_geofences_error.BatchEvaluateGeofencesError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesErrorList) -> list:
    import capo_location.types.batch_evaluate_geofences_error

    out: list = []
    for item in value:
        out.append(
            capo_location.types.batch_evaluate_geofences_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchEvaluateGeofencesErrorList:
    import capo_location.types.batch_evaluate_geofences_error

    out: BatchEvaluateGeofencesErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_location.types.batch_evaluate_geofences_error.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchEvaluateGeofencesErrorList) -> list[Any]:
    import capo_location.types.batch_evaluate_geofences_error

    return [
        capo_location.types.batch_evaluate_geofences_error.redact_sensitive(item)
        for item in value
    ]
