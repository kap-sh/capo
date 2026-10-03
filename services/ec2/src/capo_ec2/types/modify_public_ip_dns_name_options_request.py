"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPublicIpDnsNameOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.public_ip_dns_option


class ModifyPublicIpDnsNameOptionsRequest(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>A network interface ID.</p>"""
    hostname_type: NotRequired["capo_ec2.types.public_ip_dns_option.PublicIpDnsOption"]
    """<p>The public hostname type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p> <ul> <li> <p> <code>public-dual-stack-dns-name</code>: A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.</p> </li> <li> <p> <code>public-ipv4-dns-name</code>: An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.</p> </li> <li> <p> <code>public-ipv6-dns-name</code>: An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. </p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyPublicIpDnsNameOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "hostname_type" in value:
        import capo_ec2.types.public_ip_dns_option

        capo_ec2.types.public_ip_dns_option.serialize_ec2_query(
            value["hostname_type"], pairs, f"{key_prefix}HostnameType"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyPublicIpDnsNameOptionsRequest:
    out: ModifyPublicIpDnsNameOptionsRequest = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_hostname_type = el.find("HostnameType")
    if child_hostname_type is not None:
        import capo_ec2.types.public_ip_dns_option

        out["hostname_type"] = (
            capo_ec2.types.public_ip_dns_option.deserialize_ec2_query(
                child_hostname_type
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
