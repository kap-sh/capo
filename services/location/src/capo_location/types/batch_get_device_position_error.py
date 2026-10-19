"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_item_error
    import capo_location.types.id


class BatchGetDevicePositionError(TypedDict, closed=True):
    device_id: "capo_location.types.id.Id"
    """<p>The ID of the device that didn't return a position.</p>"""
    error: "capo_location.types.batch_item_error.BatchItemError"
    """<p>Contains details related to the error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionError) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import capo_location.types.batch_item_error

    out["Error"] = capo_location.types.batch_item_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> BatchGetDevicePositionError:
    out: BatchGetDevicePositionError = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("Error") is not None:
        import capo_location.types.batch_item_error

        out["error"] = capo_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchGetDevicePositionError.error required")
    return out
