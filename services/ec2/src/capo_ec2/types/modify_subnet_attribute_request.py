"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySubnetAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.coip_pool_id
    import capo_ec2.types.hostname_type
    import capo_ec2.types.integer
    import capo_ec2.types.subnet_id


class ModifySubnetAttributeRequest(TypedDict, closed=True):
    assign_ipv6_address_on_creation: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Specify <code>true</code> to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives an IPv6 address). </p> <p>If you enable the IPv6 addressing feature for your subnet, your network interface or instance only receives an IPv6 address if it's created using version <code>2016-11-15</code> or later of the Amazon EC2 API.</p>"""
    map_public_ip_on_launch: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Specify <code>true</code> to indicate that network interfaces attached to instances created in the specified subnet should be assigned a public IPv4 address.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing page</a>.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    map_customer_owned_ip_on_launch: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Specify <code>true</code> to indicate that network interfaces attached to instances created in the specified subnet should be assigned a customer-owned IPv4 address.</p> <p>When this value is <code>true</code>, you must specify the customer-owned IP pool using <code>CustomerOwnedIpv4Pool</code>.</p>"""
    customer_owned_ipv4_pool: NotRequired["capo_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The customer-owned IPv4 address pool associated with the subnet.</p> <p>You must set this value when you specify <code>true</code> for <code>MapCustomerOwnedIpOnLaunch</code>.</p>"""
    enable_dns64: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.</p> <p>You must first configure a NAT gateway in a public subnet (separate from the subnet containing the IPv6-only workloads). For example, the subnet containing the NAT gateway should have a <code>0.0.0.0/0</code> route pointing to the internet gateway. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html#nat-gateway-nat64-dns64-walkthrough">Configure DNS64 and NAT64</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    private_dns_hostname_type_on_launch: NotRequired[
        "capo_ec2.types.hostname_type.HostnameType"
    ]
    """<p>The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name).</p>"""
    enable_resource_name_dns_a_record_on_launch: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record_on_launch: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p>"""
    enable_lni_at_device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> Indicates the device position for local network interfaces in this subnet. For example, <code>1</code> indicates local network interfaces in this subnet are the secondary network interface (eth1). A local network interface cannot be the primary network interface (eth0). </p>"""
    disable_lni_at_device_index: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p> Specify <code>true</code> to indicate that local network interfaces at the current position should be disabled. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySubnetAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "assign_ipv6_address_on_creation" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["assign_ipv6_address_on_creation"],
            pairs,
            f"{key_prefix}AssignIpv6AddressOnCreation",
        )
    if "map_public_ip_on_launch" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["map_public_ip_on_launch"], pairs, f"{key_prefix}MapPublicIpOnLaunch"
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "map_customer_owned_ip_on_launch" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["map_customer_owned_ip_on_launch"],
            pairs,
            f"{key_prefix}MapCustomerOwnedIpOnLaunch",
        )
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (
                f"{key_prefix}CustomerOwnedIpv4Pool",
                str(value["customer_owned_ipv4_pool"]),
            )
        )
    if "enable_dns64" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns64"], pairs, f"{key_prefix}EnableDns64"
        )
    if "private_dns_hostname_type_on_launch" in value:
        import capo_ec2.types.hostname_type

        capo_ec2.types.hostname_type.serialize_ec2_query(
            value["private_dns_hostname_type_on_launch"],
            pairs,
            f"{key_prefix}PrivateDnsHostnameTypeOnLaunch",
        )
    if "enable_resource_name_dns_a_record_on_launch" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_resource_name_dns_a_record_on_launch"],
            pairs,
            f"{key_prefix}EnableResourceNameDnsARecordOnLaunch",
        )
    if "enable_resource_name_dns_aaaa_record_on_launch" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_resource_name_dns_aaaa_record_on_launch"],
            pairs,
            f"{key_prefix}EnableResourceNameDnsAAAARecordOnLaunch",
        )
    if "enable_lni_at_device_index" in value:
        pairs.append(
            (
                f"{key_prefix}EnableLniAtDeviceIndex",
                str(value["enable_lni_at_device_index"]),
            )
        )
    if "disable_lni_at_device_index" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["disable_lni_at_device_index"],
            pairs,
            f"{key_prefix}DisableLniAtDeviceIndex",
        )


def deserialize_ec2_query(el: Element) -> ModifySubnetAttributeRequest:
    out: ModifySubnetAttributeRequest = {}  # type: ignore[typeddict-item]
    child_assign_ipv6_address_on_creation = el.find("AssignIpv6AddressOnCreation")
    if child_assign_ipv6_address_on_creation is not None:
        import capo_ec2.types.attribute_boolean_value

        out["assign_ipv6_address_on_creation"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_assign_ipv6_address_on_creation
            )
        )
    child_map_public_ip_on_launch = el.find("MapPublicIpOnLaunch")
    if child_map_public_ip_on_launch is not None:
        import capo_ec2.types.attribute_boolean_value

        out["map_public_ip_on_launch"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_map_public_ip_on_launch
            )
        )
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_map_customer_owned_ip_on_launch = el.find("MapCustomerOwnedIpOnLaunch")
    if child_map_customer_owned_ip_on_launch is not None:
        import capo_ec2.types.attribute_boolean_value

        out["map_customer_owned_ip_on_launch"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_map_customer_owned_ip_on_launch
            )
        )
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_enable_dns64 = el.find("EnableDns64")
    if child_enable_dns64 is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_dns64"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns64
            )
        )
    child_private_dns_hostname_type_on_launch = el.find(
        "PrivateDnsHostnameTypeOnLaunch"
    )
    if child_private_dns_hostname_type_on_launch is not None:
        import capo_ec2.types.hostname_type

        out["private_dns_hostname_type_on_launch"] = (
            capo_ec2.types.hostname_type.deserialize_ec2_query(
                child_private_dns_hostname_type_on_launch
            )
        )
    child_enable_resource_name_dns_a_record_on_launch = el.find(
        "EnableResourceNameDnsARecordOnLaunch"
    )
    if child_enable_resource_name_dns_a_record_on_launch is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_resource_name_dns_a_record_on_launch"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_resource_name_dns_a_record_on_launch
            )
        )
    child_enable_resource_name_dns_aaaa_record_on_launch = el.find(
        "EnableResourceNameDnsAAAARecordOnLaunch"
    )
    if child_enable_resource_name_dns_aaaa_record_on_launch is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_resource_name_dns_aaaa_record_on_launch"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_resource_name_dns_aaaa_record_on_launch
            )
        )
    child_enable_lni_at_device_index = el.find("EnableLniAtDeviceIndex")
    if child_enable_lni_at_device_index is not None:
        out["enable_lni_at_device_index"] = int(
            child_enable_lni_at_device_index.text or ""
        )
    child_disable_lni_at_device_index = el.find("DisableLniAtDeviceIndex")
    if child_disable_lni_at_device_index is not None:
        import capo_ec2.types.attribute_boolean_value

        out["disable_lni_at_device_index"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_disable_lni_at_device_index
            )
        )
    return out
