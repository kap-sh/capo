"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.batch_get_device_position_error_list
    import capo_location.types.device_position_list


class BatchGetDevicePositionResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_get_device_position_error_list.BatchGetDevicePositionErrorList"
    """<p>Contains error details for each device that failed to send its position to the tracker resource.</p>"""
    device_positions: "capo_location.types.device_position_list.DevicePositionList"
    """<p>Contains device position details such as the device ID, position, and timestamps for when the position was received and sampled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_get_device_position_error_list

    out["Errors"] = (
        capo_location.types.batch_get_device_position_error_list.serialize_json(
            value["errors"]
        )
    )
    import capo_location.types.device_position_list

    out["DevicePositions"] = capo_location.types.device_position_list.serialize_json(
        value["device_positions"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetDevicePositionResponse:
    out: BatchGetDevicePositionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_location.types.batch_get_device_position_error_list

        out["errors"] = (
            capo_location.types.batch_get_device_position_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetDevicePositionResponse.errors required")
    if data.get("DevicePositions") is not None:
        import capo_location.types.device_position_list

        out["device_positions"] = (
            capo_location.types.device_position_list.deserialize_json(
                data["DevicePositions"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDevicePositionResponse.device_positions required"
        )
    return out


def redact_sensitive(value: BatchGetDevicePositionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_positions" in value:
        import capo_location.types.device_position_list

        out["device_positions"] = (
            capo_location.types.device_position_list.redact_sensitive(
                value["device_positions"]
            )
        )
    return out
