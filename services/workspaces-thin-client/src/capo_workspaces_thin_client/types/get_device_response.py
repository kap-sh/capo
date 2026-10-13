"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#GetDeviceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.device


class GetDeviceResponse(TypedDict, closed=True):
    device: NotRequired["capo_workspaces_thin_client.types.device.Device"]
    """<p>Describes an device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import capo_workspaces_thin_client.types.device

        out["device"] = capo_workspaces_thin_client.types.device.serialize_json(
            value["device"]
        )
    return out


def deserialize_json(data: dict) -> GetDeviceResponse:
    out: GetDeviceResponse = {}  # type: ignore[typeddict-item]
    if data.get("device") is not None:
        import capo_workspaces_thin_client.types.device

        out["device"] = capo_workspaces_thin_client.types.device.deserialize_json(
            data["device"]
        )
    return out


def redact_sensitive(value: GetDeviceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device" in value:
        import capo_workspaces_thin_client.types.device

        out["device"] = capo_workspaces_thin_client.types.device.redact_sensitive(
            value["device"]
        )
    return out
