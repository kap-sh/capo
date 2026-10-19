"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_update_device_position_error_list


class BatchUpdateDevicePositionResponse(TypedDict, closed=True):
    errors: "capo_location.types.batch_update_device_position_error_list.BatchUpdateDevicePositionErrorList"
    """<p>Contains error details for each device that failed to update its position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionResponse) -> dict:
    out: dict = {}
    import capo_location.types.batch_update_device_position_error_list

    out["Errors"] = (
        capo_location.types.batch_update_device_position_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDevicePositionResponse:
    out: BatchUpdateDevicePositionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_location.types.batch_update_device_position_error_list

        out["errors"] = (
            capo_location.types.batch_update_device_position_error_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchUpdateDevicePositionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_location.types.batch_update_device_position_error_list

        out["errors"] = (
            capo_location.types.batch_update_device_position_error_list.redact_sensitive(
                value["errors"]
            )
        )
    return out
