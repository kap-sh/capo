"""Generated from Smithy shape ``com.amazonaws.location#BatchEvaluateGeofencesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.device_position_update_list
    import capo_location.types.resource_name


class BatchEvaluateGeofencesRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The geofence collection used in evaluating the position of devices against its geofences.</p>"""
    device_position_updates: (
        "capo_location.types.device_position_update_list.DevicePositionUpdateList"
    )
    """<p>Contains device details for each device to be evaluated against the given geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEvaluateGeofencesRequest) -> dict:
    out: dict = {}
    import capo_location.types.device_position_update_list

    out["DevicePositionUpdates"] = (
        capo_location.types.device_position_update_list.serialize_json(
            value["device_position_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEvaluateGeofencesRequest:
    out: BatchEvaluateGeofencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DevicePositionUpdates") is not None:
        import capo_location.types.device_position_update_list

        out["device_position_updates"] = (
            capo_location.types.device_position_update_list.deserialize_json(
                data["DevicePositionUpdates"]
            )
        )
    else:
        out["device_position_updates"] = []
    return out


def redact_sensitive(value: BatchEvaluateGeofencesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_position_updates" in value:
        import capo_location.types.device_position_update_list

        out["device_position_updates"] = (
            capo_location.types.device_position_update_list.redact_sensitive(
                value["device_position_updates"]
            )
        )
    return out
