"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessDeviceWithMulticastGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.wireless_device_id


class AssociateWirelessDeviceWithMulticastGroupRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
    wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessDeviceWithMulticastGroupRequest) -> dict:
    out: dict = {}
    out["WirelessDeviceId"] = value["wireless_device_id"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessDeviceWithMulticastGroupRequest:
    out: AssociateWirelessDeviceWithMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("WirelessDeviceId") is not None:
        out["wireless_device_id"] = data["WirelessDeviceId"]
    else:
        out["wireless_device_id"] = ""
    return out
