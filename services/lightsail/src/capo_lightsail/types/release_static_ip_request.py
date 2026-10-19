"""Generated from Smithy shape ``com.amazonaws.lightsail#ReleaseStaticIpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class ReleaseStaticIpRequest(TypedDict, closed=True):
    static_ip_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the static IP to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseStaticIpRequest) -> dict:
    out: dict = {}
    out["staticIpName"] = value["static_ip_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseStaticIpRequest:
    out: ReleaseStaticIpRequest = {}  # type: ignore[typeddict-item]
    if data.get("staticIpName") is not None:
        out["static_ip_name"] = data["staticIpName"]
    else:
        out["static_ip_name"] = ""
    return out
