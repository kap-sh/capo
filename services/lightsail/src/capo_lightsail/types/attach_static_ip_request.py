"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachStaticIpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class AttachStaticIpRequest(TypedDict, closed=True):
    static_ip_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the static IP.</p>"""
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The instance name to which you want to attach the static IP address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachStaticIpRequest) -> dict:
    out: dict = {}
    out["staticIpName"] = value["static_ip_name"]
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachStaticIpRequest:
    out: AttachStaticIpRequest = {}  # type: ignore[typeddict-item]
    if data.get("staticIpName") is not None:
        out["static_ip_name"] = data["staticIpName"]
    else:
        out["static_ip_name"] = ""
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    return out
