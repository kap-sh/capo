"""Generated from Smithy shape ``com.amazonaws.braket#DeviceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.device_arn
    import capo_braket.types.device_status
    import capo_braket.types.device_type


class DeviceSummary(TypedDict, closed=True):
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device.</p>"""
    device_name: "str"
    """<p>The name of the device.</p>"""
    provider_name: "str"
    """<p>The provider of the device.</p>"""
    device_type: "capo_braket.types.device_type.DeviceType"
    """<p>The type of the device.</p>"""
    device_status: "capo_braket.types.device_status.DeviceStatus"
    """<p>The status of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummary) -> dict:
    out: dict = {}
    out["deviceArn"] = value["device_arn"]
    out["deviceName"] = value["device_name"]
    out["providerName"] = value["provider_name"]
    out["deviceType"] = value["device_type"]
    out["deviceStatus"] = value["device_status"]
    return out


def deserialize_json(data: dict) -> DeviceSummary:
    out: DeviceSummary = {}  # type: ignore[typeddict-item]
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        out["device_arn"] = ""
    if data.get("deviceName") is not None:
        out["device_name"] = data["deviceName"]
    else:
        out["device_name"] = ""
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    else:
        out["provider_name"] = ""
    if data.get("deviceType") is not None:
        out["device_type"] = data["deviceType"]
    else:
        out["device_type"] = ""
    if data.get("deviceStatus") is not None:
        out["device_status"] = data["deviceStatus"]
    else:
        out["device_status"] = ""
    return out
