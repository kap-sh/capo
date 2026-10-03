"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.ipv6_pool_ec2_id
    import capo_ec2.types.netmask_length
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.tenancy
    import capo_ec2.types.vpc_encryption_control_configuration


class CreateVpcRequest(TypedDict, closed=True):
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 network range for the VPC, in CIDR notation. For example, <code>10.0.0.0/16</code>. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</p>"""
    ipv6_pool: NotRequired["capo_ec2.types.ipv6_pool_ec2_id.Ipv6PoolEc2Id"]
    """<p>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR block from the IPv6 address pool. You must also specify <code>Ipv6Pool</code> in the request.</p> <p>To let Amazon choose the IPv6 CIDR block for you, omit this parameter.</p>"""
    ipv4_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    ipv4_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPv6 IPAM pool which will be used to allocate this VPC an IPv6 CIDR. IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv6 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href="https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_cidr_block_network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the address to this location.</p> <p> You must set <code>AmazonProvidedIpv6CidrBlock</code> to <code>true</code> to use this parameter.</p>"""
    vpc_encryption_control: NotRequired[
        "capo_ec2.types.vpc_encryption_control_configuration.VpcEncryptionControlConfiguration"
    ]
    """<p>Specifies the encryption control configuration to apply to the VPC during creation. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html">Enforce VPC encryption in transit</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the VPC.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy options for instances launched into the VPC. For <code>default</code>, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For <code>dedicated</code>, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of <code>dedicated</code> or <code>host</code> into a dedicated tenancy VPC. </p> <p> <b>Important:</b> The <code>host</code> value cannot be used with this parameter. Use the <code>default</code> or <code>dedicated</code> values only.</p> <p>Default: <code>default</code> </p>"""
    amazon_provided_ipv6_cidr_block: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr_block" in value:
        pairs.append((f"{key_prefix}CidrBlock", str(value["cidr_block"])))
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
    if "ipv6_cidr_block_network_border_group" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv6CidrBlockNetworkBorderGroup",
                str(value["ipv6_cidr_block_network_border_group"]),
            )
        )
    if "vpc_encryption_control" in value:
        import capo_ec2.types.vpc_encryption_control_configuration

        capo_ec2.types.vpc_encryption_control_configuration.serialize_ec2_query(
            value["vpc_encryption_control"], pairs, f"{key_prefix}VpcEncryptionControl"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_tenancy" in value:
        import capo_ec2.types.tenancy

        capo_ec2.types.tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{key_prefix}InstanceTenancy"
        )
    if "amazon_provided_ipv6_cidr_block" in value:
        pairs.append(
            (
                f"{key_prefix}AmazonProvidedIpv6CidrBlock",
                "true" if value["amazon_provided_ipv6_cidr_block"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> CreateVpcRequest:
    out: CreateVpcRequest = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
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
    child_ipv6_cidr_block_network_border_group = el.find(
        "Ipv6CidrBlockNetworkBorderGroup"
    )
    if child_ipv6_cidr_block_network_border_group is not None:
        out["ipv6_cidr_block_network_border_group"] = str(
            child_ipv6_cidr_block_network_border_group.text or ""
        )
    child_vpc_encryption_control = el.find("VpcEncryptionControl")
    if child_vpc_encryption_control is not None:
        import capo_ec2.types.vpc_encryption_control_configuration

        out["vpc_encryption_control"] = (
            capo_ec2.types.vpc_encryption_control_configuration.deserialize_ec2_query(
                child_vpc_encryption_control
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_tenancy = el.find("instanceTenancy")
    if child_instance_tenancy is not None:
        import capo_ec2.types.tenancy

        out["instance_tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_amazon_provided_ipv6_cidr_block = el.find("amazonProvidedIpv6CidrBlock")
    if child_amazon_provided_ipv6_cidr_block is not None:
        out["amazon_provided_ipv6_cidr_block"] = (
            child_amazon_provided_ipv6_cidr_block.text or ""
        ).lower() == "true"
    return out
