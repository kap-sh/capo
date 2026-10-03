"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_item_error
    import capo_location.types.id
    import capo_location.types.timestamp


class BatchEvaluateGeofencesError(TypedDict, closed=True):
    device_id: "capo_location.types.id.Id"
    """<p>The device associated with the position evaluation error.</p>"""
    sample_time: "capo_location.types.timestamp.Timestamp"
    """<p>Specifies a timestamp for when the error occurred in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    error: "capo_location.types.batch_item_error.BatchItemError"
    """<p>Contains details associated to the batch error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import capo_location.types.timestamp

    out["SampleTime"] = capo_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import capo_location.types.batch_item_error

    out["Error"] = capo_location.types.batch_item_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesError:
    out: BatchEvaluateGeofencesError = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.device_id required")
    if data.get("SampleTime") is not None:
        import capo_location.types.timestamp

        out["sample_time"] = capo_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.sample_time required")
    if data.get("Error") is not None:
        import capo_location.types.batch_item_error

        out["error"] = capo_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchEvaluateGeofencesError.error required")
    return out
