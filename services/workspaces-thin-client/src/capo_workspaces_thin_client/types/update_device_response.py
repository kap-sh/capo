"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateDeviceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.device_summary


class UpdateDeviceResponse(TypedDict, closed=True):
    device: NotRequired[
        "capo_workspaces_thin_client.types.device_summary.DeviceSummary"
    ]
    """<p>Describes a device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import capo_workspaces_thin_client.types.device_summary

        out["device"] = capo_workspaces_thin_client.types.device_summary.serialize_json(
            value["device"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDeviceResponse:
    out: UpdateDeviceResponse = {}  # type: ignore[typeddict-item]
    if data.get("device") is not None:
        import capo_workspaces_thin_client.types.device_summary

        out["device"] = (
            capo_workspaces_thin_client.types.device_summary.deserialize_json(
                data["device"]
            )
        )
    return out


def redact_sensitive(value: UpdateDeviceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device" in value:
        import capo_workspaces_thin_client.types.device_summary

        out["device"] = (
            capo_workspaces_thin_client.types.device_summary.redact_sensitive(
                value["device"]
            )
        )
    return out
