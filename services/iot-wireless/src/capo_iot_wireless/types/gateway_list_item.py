"""Generated from Smithy shape ``com.amazonaws.iotwireless#GatewayListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.downlink_frequency
    import capo_iot_wireless.types.wireless_gateway_id


class GatewayListItem(TypedDict, closed=True):
    gateway_id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the wireless gateways that you want to add to the list of gateways when sending downlink messages.</p>"""
    downlink_frequency: "capo_iot_wireless.types.downlink_frequency.DownlinkFrequency"
    """<p>The frequency to use for the gateways when sending a downlink message to the wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayListItem) -> dict:
    out: dict = {}
    out["GatewayId"] = value["gateway_id"]
    out["DownlinkFrequency"] = value["downlink_frequency"]
    return out


def deserialize_json(data: dict) -> GatewayListItem:
    out: GatewayListItem = {}  # type: ignore[typeddict-item]
    if data.get("GatewayId") is not None:
        out["gateway_id"] = data["GatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("DownlinkFrequency") is not None:
        out["downlink_frequency"] = data["DownlinkFrequency"]
    else:
        out["downlink_frequency"] = 0
    return out
