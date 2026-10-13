"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateDeviceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device


class UpdateDeviceResponse(TypedDict, closed=True):
    device: NotRequired["capo_networkmanager.types.device.Device"]
    """<p>Information about the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import capo_networkmanager.types.device

        out["Device"] = capo_networkmanager.types.device.serialize_json(value["device"])
    return out


def deserialize_json(data: dict) -> UpdateDeviceResponse:
    out: UpdateDeviceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Device") is not None:
        import capo_networkmanager.types.device

        out["device"] = capo_networkmanager.types.device.deserialize_json(
            data["Device"]
        )
    return out


def redact_sensitive(value: UpdateDeviceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device" in value:
        import capo_networkmanager.types.device

        out["device"] = capo_networkmanager.types.device.redact_sensitive(
            value["device"]
        )
    return out
