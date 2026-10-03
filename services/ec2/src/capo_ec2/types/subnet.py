"""Generated from Smithy shape ``com.amazonaws.ec2#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_public_access_states
    import capo_ec2.types.boolean
    import capo_ec2.types.coip_pool_id
    import capo_ec2.types.integer
    import capo_ec2.types.private_dns_name_options_on_launch
    import capo_ec2.types.string
    import capo_ec2.types.subnet_ipv6_cidr_block_association_set
    import capo_ec2.types.subnet_state
    import capo_ec2.types.tag_list


class Subnet(TypedDict, closed=True):
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The AZ ID of the subnet.</p>"""
    enable_lni_at_device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> Indicates the device position for local network interfaces in this subnet. For example, <code>1</code> indicates local network interfaces in this subnet are the secondary network interface (eth1). </p>"""
    map_customer_owned_ip_on_launch: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface created in this subnet (including a network interface created by <a>RunInstances</a>) receives a customer-owned IPv4 address.</p>"""
    customer_owned_ipv4_pool: NotRequired["capo_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The customer-owned IPv4 address pool associated with the subnet.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the subnet.</p>"""
    assign_ipv6_address_on_creation: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface created in this subnet (including a network interface created by <a>RunInstances</a>) receives an IPv6 address.</p>"""
    ipv6_cidr_block_association_set: NotRequired[
        "capo_ec2.types.subnet_ipv6_cidr_block_association_set.SubnetIpv6CidrBlockAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR blocks associated with the subnet.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the subnet.</p>"""
    subnet_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the subnet.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    enable_dns64: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.</p>"""
    ipv6_native: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is an IPv6 only subnet.</p>"""
    private_dns_name_options_on_launch: NotRequired[
        "capo_ec2.types.private_dns_name_options_on_launch.PrivateDnsNameOptionsOnLaunch"
    ]
    """<p>The type of hostnames to assign to instances in the subnet at launch. An instance hostname is based on the IPv4 address or ID of the instance.</p>"""
    block_public_access_states: NotRequired[
        "capo_ec2.types.block_public_access_states.BlockPublicAccessStates"
    ]
    """<p>The state of VPC Block Public Access (BPA).</p>"""
    type: NotRequired["capo_ec2.types.string.String"]
    """<p>Indicates if this is a subnet used with Amazon Elastic VMware Service (EVS). Possible values are <code>Elastic VMware Service</code> or no value. For more information about Amazon EVS, see <a href="https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html"> <i>Amazon Elastic VMware Service API Reference</i> </a>.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    state: NotRequired["capo_ec2.types.subnet_state.SubnetState"]
    """<p>The current state of the subnet.</p> <ul> <li> <p> <code>failed</code>: The underlying infrastructure to support the subnet failed to provision as expected.</p> </li> <li> <p> <code>failed-insufficient-capacity</code>: The underlying infrastructure to support the subnet failed to provision due to a shortage of EC2 instance capacity.</p> </li> </ul>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC the subnet is in.</p>"""
    cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 CIDR block assigned to the subnet.</p>"""
    available_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of unused private IPv4 addresses in the subnet. The IPv4 addresses for any stopped instances are considered unavailable.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the subnet.</p>"""
    default_for_az: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default subnet for the Availability Zone.</p>"""
    map_public_ip_on_launch: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether instances launched in this subnet receive a public IPv4 address.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing page</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Subnet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "enable_lni_at_device_index" in value:
        pairs.append(
            (
                f"{key_prefix}EnableLniAtDeviceIndex",
                str(value["enable_lni_at_device_index"]),
            )
        )
    if "map_customer_owned_ip_on_launch" in value:
        pairs.append(
            (
                f"{key_prefix}MapCustomerOwnedIpOnLaunch",
                "true" if value["map_customer_owned_ip_on_launch"] else "false",
            )
        )
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerOwnedIpv4Pool",
                str(value["customer_owned_ipv4_pool"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "assign_ipv6_address_on_creation" in value:
        pairs.append(
            (
                f"{key_prefix}AssignIpv6AddressOnCreation",
                "true" if value["assign_ipv6_address_on_creation"] else "false",
            )
        )
    if "ipv6_cidr_block_association_set" in value:
        import capo_ec2.types.subnet_ipv6_cidr_block_association_set

        capo_ec2.types.subnet_ipv6_cidr_block_association_set.serialize_ec2_query(
            value["ipv6_cidr_block_association_set"],
            pairs,
            f"{key_prefix}Ipv6CidrBlockAssociationSet",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "subnet_arn" in value:
        pairs.append((f"{key_prefix}SubnetArn", str(value["subnet_arn"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "enable_dns64" in value:
        pairs.append(
            (f"{key_prefix}EnableDns64", "true" if value["enable_dns64"] else "false")
        )
    if "ipv6_native" in value:
        pairs.append(
            (f"{key_prefix}Ipv6Native", "true" if value["ipv6_native"] else "false")
        )
    if "private_dns_name_options_on_launch" in value:
        import capo_ec2.types.private_dns_name_options_on_launch

        capo_ec2.types.private_dns_name_options_on_launch.serialize_ec2_query(
            value["private_dns_name_options_on_launch"],
            pairs,
            f"{key_prefix}PrivateDnsNameOptionsOnLaunch",
        )
    if "block_public_access_states" in value:
        import capo_ec2.types.block_public_access_states

        capo_ec2.types.block_public_access_states.serialize_ec2_query(
            value["block_public_access_states"],
            pairs,
            f"{key_prefix}BlockPublicAccessStates",
        )
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "state" in value:
        import capo_ec2.types.subnet_state

        capo_ec2.types.subnet_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "cidr_block" in value:
        pairs.append((f"{key_prefix}CidrBlock", str(value["cidr_block"])))
    if "available_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}AvailableIpAddressCount",
                str(value["available_ip_address_count"]),
            )
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "default_for_az" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultForAz",
                "true" if value["default_for_az"] else "false",
            )
        )
    if "map_public_ip_on_launch" in value:
        pairs.append(
            (
                f"{key_prefix}MapPublicIpOnLaunch",
                "true" if value["map_public_ip_on_launch"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_enable_lni_at_device_index = el.find("enableLniAtDeviceIndex")
    if child_enable_lni_at_device_index is not None:
        out["enable_lni_at_device_index"] = int(
            child_enable_lni_at_device_index.text or ""
        )
    child_map_customer_owned_ip_on_launch = el.find("mapCustomerOwnedIpOnLaunch")
    if child_map_customer_owned_ip_on_launch is not None:
        out["map_customer_owned_ip_on_launch"] = (
            child_map_customer_owned_ip_on_launch.text or ""
        ).lower() == "true"
    child_customer_owned_ipv4_pool = el.find("customerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_assign_ipv6_address_on_creation = el.find("assignIpv6AddressOnCreation")
    if child_assign_ipv6_address_on_creation is not None:
        out["assign_ipv6_address_on_creation"] = (
            child_assign_ipv6_address_on_creation.text or ""
        ).lower() == "true"
    child_ipv6_cidr_block_association_set = el.find("ipv6CidrBlockAssociationSet")
    if child_ipv6_cidr_block_association_set is not None:
        import capo_ec2.types.subnet_ipv6_cidr_block_association_set

        out["ipv6_cidr_block_association_set"] = (
            capo_ec2.types.subnet_ipv6_cidr_block_association_set.deserialize_ec2_query(
                child_ipv6_cidr_block_association_set
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_subnet_arn = el.find("subnetArn")
    if child_subnet_arn is not None:
        out["subnet_arn"] = str(child_subnet_arn.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_enable_dns64 = el.find("enableDns64")
    if child_enable_dns64 is not None:
        out["enable_dns64"] = (child_enable_dns64.text or "").lower() == "true"
    child_ipv6_native = el.find("ipv6Native")
    if child_ipv6_native is not None:
        out["ipv6_native"] = (child_ipv6_native.text or "").lower() == "true"
    child_private_dns_name_options_on_launch = el.find("privateDnsNameOptionsOnLaunch")
    if child_private_dns_name_options_on_launch is not None:
        import capo_ec2.types.private_dns_name_options_on_launch

        out["private_dns_name_options_on_launch"] = (
            capo_ec2.types.private_dns_name_options_on_launch.deserialize_ec2_query(
                child_private_dns_name_options_on_launch
            )
        )
    child_block_public_access_states = el.find("blockPublicAccessStates")
    if child_block_public_access_states is not None:
        import capo_ec2.types.block_public_access_states

        out["block_public_access_states"] = (
            capo_ec2.types.block_public_access_states.deserialize_ec2_query(
                child_block_public_access_states
            )
        )
    child_type = el.find("type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.subnet_state

        out["state"] = capo_ec2.types.subnet_state.deserialize_ec2_query(child_state)
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_cidr_block = el.find("cidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_available_ip_address_count = el.find("availableIpAddressCount")
    if child_available_ip_address_count is not None:
        out["available_ip_address_count"] = int(
            child_available_ip_address_count.text or ""
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_default_for_az = el.find("defaultForAz")
    if child_default_for_az is not None:
        out["default_for_az"] = (child_default_for_az.text or "").lower() == "true"
    child_map_public_ip_on_launch = el.find("mapPublicIpOnLaunch")
    if child_map_public_ip_on_launch is not None:
        out["map_public_ip_on_launch"] = (
            child_map_public_ip_on_launch.text or ""
        ).lower() == "true"
    return out
