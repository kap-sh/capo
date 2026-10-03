"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateVpcCidrBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipv6_pool_ec2_id
    import capo_ec2.types.netmask_length
    import capo_ec2.types.string
    import capo_ec2.types.vpc_id


class AssociateVpcCidrBlockRequest(TypedDict, closed=True):
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>An IPv4 CIDR block to associate with the VPC.</p>"""
    ipv6_cidr_block_network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the CIDR block to this location.</p> <p> You must set <code>AmazonProvidedIpv6CidrBlock</code> to <code>true</code> to use this parameter.</p> <p> You can have one IPv6 CIDR block association per network border group.</p>"""
    ipv6_pool: NotRequired["capo_ec2.types.ipv6_pool_ec2_id.Ipv6PoolEc2Id"]
    """<p>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>An IPv6 CIDR block from the IPv6 address pool. You must also specify <code>Ipv6Pool</code> in the request.</p> <p>To let Amazon choose the IPv6 CIDR block for you, omit this parameter.</p>"""
    ipv4_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>Associate a CIDR allocated from an IPv4 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv4_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    ipv6_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>Associates a CIDR allocated from an IPv6 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    amazon_provided_ipv6_cidr_block: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses or the size of the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateVpcCidrBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr_block" in value:
        pairs.append((f"{key_prefix}CidrBlock", str(value["cidr_block"])))
    if "ipv6_cidr_block_network_border_group" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv6CidrBlockNetworkBorderGroup",
                str(value["ipv6_cidr_block_network_border_group"]),
            )
        )
    if "ipv6_pool" in value:
        pairs.append((f"{key_prefix}Ipv6Pool", str(value["ipv6_pool"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "ipv4_ipam_pool_id" in value:
        pairs.append((f"{key_prefix}Ipv4IpamPoolId", str(value["ipv4_ipam_pool_id"])))
    if "ipv4_netmask_length" in value:
        pairs.append(
            (f"{key_prefix}Ipv4NetmaskLength", str(value["ipv4_netmask_length"]))
        )
    if "ipv6_ipam_pool_id" in value:
        pairs.append((f"{key_prefix}Ipv6IpamPoolId", str(value["ipv6_ipam_pool_id"])))
    if "ipv6_netmask_length" in value:
        pairs.append(
            (f"{key_prefix}Ipv6NetmaskLength", str(value["ipv6_netmask_length"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "amazon_provided_ipv6_cidr_block" in value:
        pairs.append(
            (
                f"{key_prefix}AmazonProvidedIpv6CidrBlock",
                "true" if value["amazon_provided_ipv6_cidr_block"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> AssociateVpcCidrBlockRequest:
    out: AssociateVpcCidrBlockRequest = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_ipv6_cidr_block_network_border_group = el.find(
        "Ipv6CidrBlockNetworkBorderGroup"
    )
    if child_ipv6_cidr_block_network_border_group is not None:
        out["ipv6_cidr_block_network_border_group"] = str(
            child_ipv6_cidr_block_network_border_group.text or ""
        )
    child_ipv6_pool = el.find("Ipv6Pool")
    if child_ipv6_pool is not None:
        out["ipv6_pool"] = str(child_ipv6_pool.text or "")
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_ipv4_ipam_pool_id = el.find("Ipv4IpamPoolId")
    if child_ipv4_ipam_pool_id is not None:
        out["ipv4_ipam_pool_id"] = str(child_ipv4_ipam_pool_id.text or "")
    child_ipv4_netmask_length = el.find("Ipv4NetmaskLength")
    if child_ipv4_netmask_length is not None:
        out["ipv4_netmask_length"] = int(child_ipv4_netmask_length.text or "")
    child_ipv6_ipam_pool_id = el.find("Ipv6IpamPoolId")
    if child_ipv6_ipam_pool_id is not None:
        out["ipv6_ipam_pool_id"] = str(child_ipv6_ipam_pool_id.text or "")
    child_ipv6_netmask_length = el.find("Ipv6NetmaskLength")
    if child_ipv6_netmask_length is not None:
        out["ipv6_netmask_length"] = int(child_ipv6_netmask_length.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_amazon_provided_ipv6_cidr_block = el.find("amazonProvidedIpv6CidrBlock")
    if child_amazon_provided_ipv6_cidr_block is not None:
        out["amazon_provided_ipv6_cidr_block"] = (
            child_amazon_provided_ipv6_cidr_block.text or ""
        ).lower() == "true"
    return out
