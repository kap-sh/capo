"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetDevicesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_list
    import capo_networkmanager.types.next_token


class GetDevicesResponse(TypedDict, closed=True):
    devices: NotRequired["capo_networkmanager.types.device_list.DeviceList"]
    """<p>The devices.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicesResponse) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_networkmanager.types.device_list

        out["Devices"] = capo_networkmanager.types.device_list.serialize_json(
            value["devices"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDevicesResponse:
    out: GetDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Devices") is not None:
        import capo_networkmanager.types.device_list

        out["devices"] = capo_networkmanager.types.device_list.deserialize_json(
            data["Devices"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetDevicesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "devices" in value:
        import capo_networkmanager.types.device_list

        out["devices"] = capo_networkmanager.types.device_list.redact_sensitive(
            value["devices"]
        )
    return out
