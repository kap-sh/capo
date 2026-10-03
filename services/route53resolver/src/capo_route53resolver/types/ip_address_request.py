"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.ip
    import capo_route53resolver.types.ipv6
    import capo_route53resolver.types.subnet_id


class IpAddressRequest(TypedDict, closed=True):
    subnet_id: "capo_route53resolver.types.subnet_id.SubnetId"
    """<p>The ID of the subnet that contains the IP address. </p> <p>We recommend using <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html">VPC Resolver on Outposts</a> to create endpoints on Outposts Racks.</p> <important> <p>Outposts subnets with <a href="https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html">Local Network Interface (LNI)</a> enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility">Subnet compatibility for Resolver endpoints</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> </important>"""
    ip: NotRequired["capo_route53resolver.types.ip.Ip"]
    """<p>The IPv4 address that you want to use for DNS queries.</p>"""
    ipv6: NotRequired["capo_route53resolver.types.ipv6.Ipv6"]
    """<p> The IPv6 address that you want to use for DNS queries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressRequest) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressRequest:
    out: IpAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("IpAddressRequest.subnet_id required")
    if data.get("Ip") is not None:
        out["ip"] = data["Ip"]
    if data.get("Ipv6") is not None:
        out["ipv6"] = data["Ipv6"]
    return out
