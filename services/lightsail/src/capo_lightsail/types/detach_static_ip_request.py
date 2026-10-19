"""Generated from Smithy shape ``com.amazonaws.lightsail#DetachStaticIpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DetachStaticIpRequest(TypedDict, closed=True):
    static_ip_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the static IP to detach from the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachStaticIpRequest) -> dict:
    out: dict = {}
    out["staticIpName"] = value["static_ip_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachStaticIpRequest:
    out: DetachStaticIpRequest = {}  # type: ignore[typeddict-item]
    if data.get("staticIpName") is not None:
        out["static_ip_name"] = data["staticIpName"]
    else:
        out["static_ip_name"] = ""
    return out
