"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddressDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.ip_address
    import capo_global_accelerator.types.network_zone


class IpAddressDetail(TypedDict, closed=True):
    ip_address: NotRequired["capo_global_accelerator.types.ip_address.IpAddress"]
    """<p>The static IP address.</p>"""
    network_zone: NotRequired["capo_global_accelerator.types.network_zone.NetworkZone"]
    """<p>The network zone that the specified IP address is located on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressDetail) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "network_zone" in value:
        out["NetworkZone"] = value["network_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressDetail:
    out: IpAddressDetail = {}  # type: ignore[typeddict-item]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("NetworkZone") is not None:
        out["network_zone"] = data["NetworkZone"]
    return out
