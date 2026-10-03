"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.netmask_length
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.vpc_id


class CreateSubnetRequest(TypedDict, closed=True):
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the subnet.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone for the subnet.</p> <p>Default: Amazon Web Services selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.</p> <p>To create a subnet in a Local Zone, set this value to the Local Zone ID, for example <code>us-west-2-lax-1a</code>. For information about the Regions that support Local Zones, see <a href="https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html">Available Local Zones</a>.</p> <p>To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The AZ ID or the Local Zone ID of the subnet.</p>"""
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 network range for the subnet, in CIDR notation. For example, <code>10.0.0.0/24</code>. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</p> <p>This parameter is not supported for an IPv6 only subnet.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 network range for the subnet, in CIDR notation. This parameter is required for an IPv6 only subnet.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    ipv6_native: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to create an IPv6 only subnet.</p>"""
    ipv4_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv4 IPAM pool ID for the subnet.</p>"""
    ipv4_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv4 netmask length for the subnet.</p>"""
    ipv6_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv6 IPAM pool ID for the subnet.</p>"""
    ipv6_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv6 netmask length for the subnet.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSubnetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "cidr_block" in value:
        pairs.append((f"{key_prefix}CidrBlock", str(value["cidr_block"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "ipv6_native" in value:
        pairs.append(
            (f"{key_prefix}Ipv6Native", "true" if value["ipv6_native"] else "false")
        )
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
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateSubnetRequest:
    out: CreateSubnetRequest = {}  # type: ignore[typeddict-item]
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_ipv6_native = el.find("Ipv6Native")
    if child_ipv6_native is not None:
        out["ipv6_native"] = (child_ipv6_native.text or "").lower() == "true"
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
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
