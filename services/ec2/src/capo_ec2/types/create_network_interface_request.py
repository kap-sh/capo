"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_specification_request
    import capo_ec2.types.instance_ipv6_address_list
    import capo_ec2.types.integer
    import capo_ec2.types.ipv4_prefix_list
    import capo_ec2.types.ipv6_prefix_list
    import capo_ec2.types.network_interface_creation_type
    import capo_ec2.types.operator_request
    import capo_ec2.types.private_ip_address_specification_list
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_specification_list


class CreateNetworkInterfaceRequest(TypedDict, closed=True):
    ipv4_prefixes: NotRequired["capo_ec2.types.ipv4_prefix_list.Ipv4PrefixList"]
    """<p>The IPv4 prefixes assigned to the network interface.</p> <p>You can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</p>"""
    ipv4_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface.</p> <p>You can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</p>"""
    ipv6_prefixes: NotRequired["capo_ec2.types.ipv6_prefix_list.Ipv6PrefixList"]
    """<p>The IPv6 prefixes assigned to the network interface.</p> <p>You can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</p>"""
    ipv6_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface.</p> <p>You can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</p>"""
    interface_type: NotRequired[
        "capo_ec2.types.network_interface_creation_type.NetworkInterfaceCreationType"
    ]
    """<p>The type of network interface. The default is <code>interface</code>.</p> <p>If you specify <code>efa-only</code>, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.</p> <p>The only supported values are <code>interface</code>, <code>efa</code>, <code>efa-only</code>, and <code>trunk</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new network interface.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    enable_primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If you’re creating a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    connection_tracking_specification: NotRequired[
        "capo_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A connection tracking specification for the network interface.</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to associate with the network interface.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the network interface.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in <code>privateIpAddresses</code> as primary (only one IP address can be designated as primary).</p>"""
    groups: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>The private IPv4 addresses.</p> <p>You can't specify private IPv4 addresses if you've specified one of the following: a count of private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.</p>"""
    secondary_private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using <code>privateIpAddresses</code>.</p> <p>You can't specify a count of private IPv4 addresses if you've specified one of the following: specific private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses from the IPv6 CIDR block range of your subnet.</p> <p>You can't specify IPv6 addresses using this parameter if you've specified one of the following: a count of IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range.</p> <p>You can't specify a count of IPv6 addresses using this parameter if you've specified one of the following: specific IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.</p> <p>If your subnet has the <code>AssignIpv6AddressOnCreation</code> attribute set, you can override that setting by specifying 0 as the IPv6 address count.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInterfaceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv4_prefixes" in value:
        import capo_ec2.types.ipv4_prefix_list

        capo_ec2.types.ipv4_prefix_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4Prefix"
        )
    if "ipv4_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv4PrefixCount", str(value["ipv4_prefix_count"])))
    if "ipv6_prefixes" in value:
        import capo_ec2.types.ipv6_prefix_list

        capo_ec2.types.ipv6_prefix_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6Prefix"
        )
    if "ipv6_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv6PrefixCount", str(value["ipv6_prefix_count"])))
    if "interface_type" in value:
        import capo_ec2.types.network_interface_creation_type

        capo_ec2.types.network_interface_creation_type.serialize_ec2_query(
            value["interface_type"], pairs, f"{key_prefix}InterfaceType"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "enable_primary_ipv6" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePrimaryIpv6",
                "true" if value["enable_primary_ipv6"] else "false",
            )
        )
    if "connection_tracking_specification" in value:
        import capo_ec2.types.connection_tracking_specification_request

        capo_ec2.types.connection_tracking_specification_request.serialize_ec2_query(
            value["connection_tracking_specification"],
            pairs,
            f"{key_prefix}ConnectionTrackingSpecification",
        )
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "groups" in value:
        import capo_ec2.types.security_group_id_string_list

        capo_ec2.types.security_group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "private_ip_addresses" in value:
        import capo_ec2.types.private_ip_address_specification_list

        capo_ec2.types.private_ip_address_specification_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddresses"
        )
    if "secondary_private_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryPrivateIpAddressCount",
                str(value["secondary_private_ip_address_count"]),
            )
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.instance_ipv6_address_list

        capo_ec2.types.instance_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6Addresses"
        )
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateNetworkInterfaceRequest:
    out: CreateNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_ipv4_prefixes = el.find("Ipv4Prefix")
    if child_ipv4_prefixes is not None:
        import capo_ec2.types.ipv4_prefix_list

        out["ipv4_prefixes"] = capo_ec2.types.ipv4_prefix_list.deserialize_ec2_query(
            child_ipv4_prefixes
        )
    child_ipv4_prefix_count = el.find("Ipv4PrefixCount")
    if child_ipv4_prefix_count is not None:
        out["ipv4_prefix_count"] = int(child_ipv4_prefix_count.text or "")
    child_ipv6_prefixes = el.find("Ipv6Prefix")
    if child_ipv6_prefixes is not None:
        import capo_ec2.types.ipv6_prefix_list

        out["ipv6_prefixes"] = capo_ec2.types.ipv6_prefix_list.deserialize_ec2_query(
            child_ipv6_prefixes
        )
    child_ipv6_prefix_count = el.find("Ipv6PrefixCount")
    if child_ipv6_prefix_count is not None:
        out["ipv6_prefix_count"] = int(child_ipv6_prefix_count.text or "")
    child_interface_type = el.find("InterfaceType")
    if child_interface_type is not None:
        import capo_ec2.types.network_interface_creation_type

        out["interface_type"] = (
            capo_ec2.types.network_interface_creation_type.deserialize_ec2_query(
                child_interface_type
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
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_enable_primary_ipv6 = el.find("EnablePrimaryIpv6")
    if child_enable_primary_ipv6 is not None:
        out["enable_primary_ipv6"] = (
            child_enable_primary_ipv6.text or ""
        ).lower() == "true"
    child_connection_tracking_specification = el.find("ConnectionTrackingSpecification")
    if child_connection_tracking_specification is not None:
        import capo_ec2.types.connection_tracking_specification_request

        out["connection_tracking_specification"] = (
            capo_ec2.types.connection_tracking_specification_request.deserialize_ec2_query(
                child_connection_tracking_specification
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_groups = el.find("SecurityGroupId")
    if child_groups is not None:
        import capo_ec2.types.security_group_id_string_list

        out["groups"] = (
            capo_ec2.types.security_group_id_string_list.deserialize_ec2_query(
                child_groups
            )
        )
    child_private_ip_addresses = el.find("privateIpAddresses")
    if child_private_ip_addresses is not None:
        import capo_ec2.types.private_ip_address_specification_list

        out["private_ip_addresses"] = (
            capo_ec2.types.private_ip_address_specification_list.deserialize_ec2_query(
                child_private_ip_addresses
            )
        )
    child_secondary_private_ip_address_count = el.find("secondaryPrivateIpAddressCount")
    if child_secondary_private_ip_address_count is not None:
        out["secondary_private_ip_address_count"] = int(
            child_secondary_private_ip_address_count.text or ""
        )
    child_ipv6_addresses = el.find("ipv6Addresses")
    if child_ipv6_addresses is not None:
        import capo_ec2.types.instance_ipv6_address_list

        out["ipv6_addresses"] = (
            capo_ec2.types.instance_ipv6_address_list.deserialize_ec2_query(
                child_ipv6_addresses
            )
        )
    child_ipv6_address_count = el.find("ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
