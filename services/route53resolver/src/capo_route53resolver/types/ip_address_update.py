"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.ip
    import capo_route53resolver.types.ipv6
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.subnet_id


class IpAddressUpdate(TypedDict, closed=True):
    ip_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p> <i>Only when removing an IP address from a Resolver endpoint</i>: The ID of the IP address that you want to remove. To get this ID, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html">GetResolverEndpoint</a>.</p>"""
    subnet_id: NotRequired["capo_route53resolver.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet that includes the IP address that you want to update. To get this ID, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html">GetResolverEndpoint</a>.</p> <p>We recommend using <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html">VPC Resolver on Outposts</a> to create endpoints on Outposts Racks.</p> <important> <p>Outposts subnets with <a href="https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html">Local Network Interface (LNI)</a> enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility">Subnet compatibility for Resolver endpoints</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important>"""
    ip: NotRequired["capo_route53resolver.types.ip.Ip"]
    """<p>The new IPv4 address.</p>"""
    ipv6: NotRequired["capo_route53resolver.types.ipv6.Ipv6"]
    """<p> The new IPv6 address. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressUpdate) -> dict:
    out: dict = {}
    if "ip_id" in value:
        out["IpId"] = value["ip_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressUpdate:
    out: IpAddressUpdate = {}  # type: ignore[typeddict-item]
    if data.get("IpId") is not None:
        out["ip_id"] = data["IpId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("Ip") is not None:
        out["ip"] = data["Ip"]
    if data.get("Ipv6") is not None:
        out["ipv6"] = data["Ipv6"]
    return out
