"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.domain_type
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipv4_pool_ec2_id
    import capo_ec2.types.public_ip_address
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class AllocateAddressRequest(TypedDict, closed=True):
    domain: NotRequired["capo_ec2.types.domain_type.DomainType"]
    """<p>The network (<code>vpc</code>).</p>"""
    address: NotRequired["capo_ec2.types.public_ip_address.PublicIpAddress"]
    """<p>The Elastic IP address to recover or an IPv4 address from an address pool.</p>"""
    public_ipv4_pool: NotRequired["capo_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To specify a specific address from the address pool, use the <code>Address</code> parameter instead.</p>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p> A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.</p>"""
    customer_owned_ipv4_pool: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of a customer-owned address pool. Use this parameter to let Amazon EC2 select an address from the address pool. Alternatively, specify a specific address from the address pool.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Elastic IP address.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPAM pool which has an Amazon-provided or BYOIP public IPv4 CIDR provisioned to it. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html">Allocate sequential Elastic IP addresses from an IPAM pool</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "domain" in value:
        import capo_ec2.types.domain_type

        capo_ec2.types.domain_type.serialize_ec2_query(
            value["domain"], pairs, f"{key_prefix}Domain"
        )
    if "address" in value:
        pairs.append((f"{key_prefix}Address", str(value["address"])))
    if "public_ipv4_pool" in value:
        pairs.append((f"{key_prefix}PublicIpv4Pool", str(value["public_ipv4_pool"])))
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerOwnedIpv4Pool",
                str(value["customer_owned_ipv4_pool"]),
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AllocateAddressRequest:
    out: AllocateAddressRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        import capo_ec2.types.domain_type

        out["domain"] = capo_ec2.types.domain_type.deserialize_ec2_query(child_domain)
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_public_ipv4_pool = el.find("PublicIpv4Pool")
    if child_public_ipv4_pool is not None:
        out["public_ipv4_pool"] = str(child_public_ipv4_pool.text or "")
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
