"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpDnsNameOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PublicIpDnsNameOptions(TypedDict, closed=True):
    dns_hostname_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The public hostname type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_ipv4_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.</p>"""
    public_ipv6_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.</p>"""
    public_dual_stack_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PublicIpDnsNameOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dns_hostname_type" in value:
        pairs.append((f"{key_prefix}DnsHostnameType", str(value["dns_hostname_type"])))
    if "public_ipv4_dns_name" in value:
        pairs.append(
            (f"{key_prefix}PublicIpv4DnsName", str(value["public_ipv4_dns_name"]))
        )
    if "public_ipv6_dns_name" in value:
        pairs.append(
            (f"{key_prefix}PublicIpv6DnsName", str(value["public_ipv6_dns_name"]))
        )
    if "public_dual_stack_dns_name" in value:
        pairs.append(
            (
                f"{key_prefix}PublicDualStackDnsName",
                str(value["public_dual_stack_dns_name"]),
            )
        )


def deserialize_ec2_query(el: Element) -> PublicIpDnsNameOptions:
    out: PublicIpDnsNameOptions = {}  # type: ignore[typeddict-item]
    child_dns_hostname_type = el.find("dnsHostnameType")
    if child_dns_hostname_type is not None:
        out["dns_hostname_type"] = str(child_dns_hostname_type.text or "")
    child_public_ipv4_dns_name = el.find("publicIpv4DnsName")
    if child_public_ipv4_dns_name is not None:
        out["public_ipv4_dns_name"] = str(child_public_ipv4_dns_name.text or "")
    child_public_ipv6_dns_name = el.find("publicIpv6DnsName")
    if child_public_ipv6_dns_name is not None:
        out["public_ipv6_dns_name"] = str(child_public_ipv6_dns_name.text or "")
    child_public_dual_stack_dns_name = el.find("publicDualStackDnsName")
    if child_public_dual_stack_dns_name is not None:
        out["public_dual_stack_dns_name"] = str(
            child_public_dual_stack_dns_name.text or ""
        )
    return out
