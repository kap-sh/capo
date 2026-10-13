"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.device_position_update_list
    import capo_location.types.resource_name


class BatchUpdateDevicePositionRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to update.</p>"""
    updates: "capo_location.types.device_position_update_list.DevicePositionUpdateList"
    """<p>Contains the position update details for each device, up to 10 devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionRequest) -> dict:
    out: dict = {}
    import capo_location.types.device_position_update_list

    out["Updates"] = capo_location.types.device_position_update_list.serialize_json(
        value["updates"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDevicePositionRequest:
    out: BatchUpdateDevicePositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Updates") is not None:
        import capo_location.types.device_position_update_list

        out["updates"] = (
            capo_location.types.device_position_update_list.deserialize_json(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateDevicePositionRequest.updates required")
    return out


def redact_sensitive(value: BatchUpdateDevicePositionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "updates" in value:
        import capo_location.types.device_position_update_list

        out["updates"] = (
            capo_location.types.device_position_update_list.redact_sensitive(
                value["updates"]
            )
        )
    return out
