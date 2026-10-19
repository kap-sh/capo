"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessEffectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.device_model
    import capo_workmail.types.device_operating_system
    import capo_workmail.types.device_type
    import capo_workmail.types.device_user_agent
    import capo_workmail.types.organization_id


class GetMobileDeviceAccessEffectRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to simulate the access effect for.</p>"""
    device_type: NotRequired["capo_workmail.types.device_type.DeviceType"]
    """<p>Device type the simulated user will report.</p>"""
    device_model: NotRequired["capo_workmail.types.device_model.DeviceModel"]
    """<p>Device model the simulated user will report.</p>"""
    device_operating_system: NotRequired[
        "capo_workmail.types.device_operating_system.DeviceOperatingSystem"
    ]
    """<p>Device operating system the simulated user will report.</p>"""
    device_user_agent: NotRequired[
        "capo_workmail.types.device_user_agent.DeviceUserAgent"
    ]
    """<p>Device user agent the simulated user will report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessEffectRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "device_type" in value:
        out["DeviceType"] = value["device_type"]
    if "device_model" in value:
        out["DeviceModel"] = value["device_model"]
    if "device_operating_system" in value:
        out["DeviceOperatingSystem"] = value["device_operating_system"]
    if "device_user_agent" in value:
        out["DeviceUserAgent"] = value["device_user_agent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessEffectRequest:
    out: GetMobileDeviceAccessEffectRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DeviceType") is not None:
        out["device_type"] = data["DeviceType"]
    if data.get("DeviceModel") is not None:
        out["device_model"] = data["DeviceModel"]
    if data.get("DeviceOperatingSystem") is not None:
        out["device_operating_system"] = data["DeviceOperatingSystem"]
    if data.get("DeviceUserAgent") is not None:
        out["device_user_agent"] = data["DeviceUserAgent"]
    return out
