"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateIpAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.ipv6
    import capo_route53resolver.types.resource_id


class UpdateIpAddress(TypedDict, closed=True):
    ip_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p> The ID of the IP address, specified by the <code>ResolverEndpointId</code>. </p>"""
    ipv6: "capo_route53resolver.types.ipv6.Ipv6"
    """<p> The IPv6 address that you want to use for DNS queries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIpAddress) -> dict:
    out: dict = {}
    out["IpId"] = value["ip_id"]
    out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIpAddress:
    out: UpdateIpAddress = {}  # type: ignore[typeddict-item]
    if data.get("IpId") is not None:
        out["ip_id"] = data["IpId"]
    else:
        out["ip_id"] = ""
    if data.get("Ipv6") is not None:
        out["ipv6"] = data["Ipv6"]
    else:
        out["ipv6"] = ""
    return out
