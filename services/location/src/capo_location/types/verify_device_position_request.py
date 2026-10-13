"""Generated from Smithy shape ``com.amazonaws.location#VerifyDevicePositionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.device_state
    import capo_location.types.distance_unit
    import capo_location.types.resource_name


class VerifyDevicePositionRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to be associated with verification request.</p>"""
    device_state: "capo_location.types.device_state.DeviceState"
    """<p>The device's state, including position, IP address, cell signals and Wi-Fi access points.</p>"""
    distance_unit: NotRequired["capo_location.types.distance_unit.DistanceUnit"]
    """<p>The distance unit for the verification request.</p> <p>Default Value: <code>Kilometers</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyDevicePositionRequest) -> dict:
    out: dict = {}
    import capo_location.types.device_state

    out["DeviceState"] = capo_location.types.device_state.serialize_json(
        value["device_state"]
    )
    if "distance_unit" in value:
        out["DistanceUnit"] = value["distance_unit"]
    return out


def deserialize_json(data: dict) -> VerifyDevicePositionRequest:
    out: VerifyDevicePositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceState") is not None:
        import capo_location.types.device_state

        out["device_state"] = capo_location.types.device_state.deserialize_json(
            data["DeviceState"]
        )
    else:
        raise DeserializationError("VerifyDevicePositionRequest.device_state required")
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    return out


def redact_sensitive(value: VerifyDevicePositionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_state" in value:
        import capo_location.types.device_state

        out["device_state"] = capo_location.types.device_state.redact_sensitive(
            value["device_state"]
        )
    return out
