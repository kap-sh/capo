"""Generated from Smithy shape ``com.amazonaws.outposts#StartConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.asset_id
    import capo_outposts.types.device_serial_number
    import capo_outposts.types.network_interface_device_index
    import capo_outposts.types.wire_guard_public_key


class StartConnectionRequest(TypedDict, closed=True):
    device_serial_number: NotRequired[
        "capo_outposts.types.device_serial_number.DeviceSerialNumber"
    ]
    """<p> The serial number of the dongle. </p>"""
    asset_id: "capo_outposts.types.asset_id.AssetId"
    """<p> The ID of the Outpost server.</p>"""
    client_public_key: "capo_outposts.types.wire_guard_public_key.WireGuardPublicKey"
    """<p> The public key of the client. </p>"""
    network_interface_device_index: (
        "capo_outposts.types.network_interface_device_index.NetworkInterfaceDeviceIndex"
    )
    """<p> The device index of the network interface on the Outpost server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConnectionRequest) -> dict:
    out: dict = {}
    if "device_serial_number" in value:
        out["DeviceSerialNumber"] = value["device_serial_number"]
    out["AssetId"] = value["asset_id"]
    out["ClientPublicKey"] = value["client_public_key"]
    out["NetworkInterfaceDeviceIndex"] = value["network_interface_device_index"]
    return out


def deserialize_json(data: dict) -> StartConnectionRequest:
    out: StartConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceSerialNumber") is not None:
        out["device_serial_number"] = data["DeviceSerialNumber"]
    if data.get("AssetId") is not None:
        out["asset_id"] = data["AssetId"]
    else:
        out["asset_id"] = ""
    if data.get("ClientPublicKey") is not None:
        out["client_public_key"] = data["ClientPublicKey"]
    else:
        out["client_public_key"] = ""
    if data.get("NetworkInterfaceDeviceIndex") is not None:
        out["network_interface_device_index"] = data["NetworkInterfaceDeviceIndex"]
    else:
        out["network_interface_device_index"] = 0
    return out
