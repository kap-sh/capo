"""Generated from Smithy shape ``com.amazonaws.braket#GetDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.device_arn
    import capo_braket.types.device_queue_info_list
    import capo_braket.types.device_status
    import capo_braket.types.device_status_reason
    import capo_braket.types.device_type
    import capo_braket.types.json_value


class GetDeviceResponse(TypedDict, closed=True):
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device.</p>"""
    device_name: "str"
    """<p>The name of the device.</p>"""
    provider_name: "str"
    """<p>The name of the partner company for the device.</p>"""
    device_type: "capo_braket.types.device_type.DeviceType"
    """<p>The type of the device.</p>"""
    device_status: "capo_braket.types.device_status.DeviceStatus"
    """<p>The status of the device.</p>"""
    device_status_reason: NotRequired[
        "capo_braket.types.device_status_reason.DeviceStatusReason"
    ]
    """<p>The reason for the current status of the device, including status reason codes and timestamps.</p>"""
    device_capabilities: "capo_braket.types.json_value.JsonValue"
    """<p>Details about the capabilities of the device.</p>"""
    device_queue_info: NotRequired[
        "capo_braket.types.device_queue_info_list.DeviceQueueInfoList"
    ]
    """<p>The number of quantum tasks and hybrid jobs currently queued on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceResponse) -> dict:
    out: dict = {}
    out["deviceArn"] = value["device_arn"]
    out["deviceName"] = value["device_name"]
    out["providerName"] = value["provider_name"]
    out["deviceType"] = value["device_type"]
    out["deviceStatus"] = value["device_status"]
    if "device_status_reason" in value:
        import capo_braket.types.device_status_reason

        out["deviceStatusReason"] = (
            capo_braket.types.device_status_reason.serialize_json(
                value["device_status_reason"]
            )
        )
    out["deviceCapabilities"] = value["device_capabilities"]
    if "device_queue_info" in value:
        import capo_braket.types.device_queue_info_list

        out["deviceQueueInfo"] = (
            capo_braket.types.device_queue_info_list.serialize_json(
                value["device_queue_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeviceResponse:
    out: GetDeviceResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("deviceStatusReason") is not None:
        import capo_braket.types.device_status_reason

        out["device_status_reason"] = (
            capo_braket.types.device_status_reason.deserialize_json(
                data["deviceStatusReason"]
            )
        )
    if data.get("deviceCapabilities") is not None:
        out["device_capabilities"] = data["deviceCapabilities"]
    else:
        out["device_capabilities"] = ""
    if data.get("deviceQueueInfo") is not None:
        import capo_braket.types.device_queue_info_list

        out["device_queue_info"] = (
            capo_braket.types.device_queue_info_list.deserialize_json(
                data["deviceQueueInfo"]
            )
        )
    return out
