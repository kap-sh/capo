"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_specification
    import capo_ec2.types.group_id_string_list
    import capo_ec2.types.instance_ipv6_address_list
    import capo_ec2.types.integer
    import capo_ec2.types.ipv4_prefix_list_response
    import capo_ec2.types.ipv6_prefix_list_response
    import capo_ec2.types.launch_template_ena_srd_specification
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.private_ip_address_specification_list
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class LaunchTemplateInstanceNetworkInterfaceSpecification(TypedDict, closed=True):
    associate_carrier_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to associate a Carrier IP address with eth0 for a new network interface.</p> <p>Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see <a href="https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip">Carrier IP address</a> in the <i>Wavelength Developer Guide</i>.</p>"""
    associate_public_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to associate a public IPv4 address with eth0 for a new network interface.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the network interface.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The device index for the network interface attachment.</p>"""
    groups: NotRequired["capo_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>The IDs of one or more security groups.</p>"""
    interface_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of network interface.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses for the network interface.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses for the network interface.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The primary private IPv4 address of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>One or more private IPv4 addresses.</p>"""
    secondary_private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses for the network interface.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet for the network interface.</p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    ipv4_prefixes: NotRequired[
        "capo_ec2.types.ipv4_prefix_list_response.Ipv4PrefixListResponse"
    ]
    """<p>One or more IPv4 prefixes assigned to the network interface.</p>"""
    ipv4_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired[
        "capo_ec2.types.ipv6_prefix_list_response.Ipv6PrefixListResponse"
    ]
    """<p>One or more IPv6 prefixes assigned to the network interface.</p>"""
    ipv6_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigned to the network interface.</p>"""
    primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a>.</p>"""
    ena_srd_specification: NotRequired[
        "capo_ec2.types.launch_template_ena_srd_specification.LaunchTemplateEnaSrdSpecification"
    ]
    """<p>Contains the ENA Express settings for instances launched from your launch template.</p>"""
    connection_tracking_specification: NotRequired[
        "capo_ec2.types.connection_tracking_specification.ConnectionTrackingSpecification"
    ]
    """<p>A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts">Idle connection tracking timeout</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ena_queue_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of ENA queues created with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceNetworkInterfaceSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associate_carrier_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}AssociateCarrierIpAddress",
                "true" if value["associate_carrier_ip_address"] else "false",
            )
        )
    if "associate_public_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}AssociatePublicIpAddress",
                "true" if value["associate_public_ip_address"] else "false",
            )
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))
    if "groups" in value:
        import capo_ec2.types.group_id_string_list

        capo_ec2.types.group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "interface_type" in value:
        pairs.append((f"{key_prefix}InterfaceType", str(value["interface_type"])))
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.instance_ipv6_address_list

        capo_ec2.types.instance_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6AddressesSet"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "private_ip_addresses" in value:
        import capo_ec2.types.private_ip_address_specification_list

        capo_ec2.types.private_ip_address_specification_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddressesSet"
        )
    if "secondary_private_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryPrivateIpAddressCount",
                str(value["secondary_private_ip_address_count"]),
            )
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
    if "ipv4_prefixes" in value:
        import capo_ec2.types.ipv4_prefix_list_response

        capo_ec2.types.ipv4_prefix_list_response.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4PrefixSet"
        )
    if "ipv4_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv4PrefixCount", str(value["ipv4_prefix_count"])))
    if "ipv6_prefixes" in value:
        import capo_ec2.types.ipv6_prefix_list_response

        capo_ec2.types.ipv6_prefix_list_response.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6PrefixSet"
        )
    if "ipv6_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv6PrefixCount", str(value["ipv6_prefix_count"])))
    if "primary_ipv6" in value:
        pairs.append(
            (f"{key_prefix}PrimaryIpv6", "true" if value["primary_ipv6"] else "false")
        )
    if "ena_srd_specification" in value:
        import capo_ec2.types.launch_template_ena_srd_specification

        capo_ec2.types.launch_template_ena_srd_specification.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{key_prefix}EnaSrdSpecification"
        )
    if "connection_tracking_specification" in value:
        import capo_ec2.types.connection_tracking_specification

        capo_ec2.types.connection_tracking_specification.serialize_ec2_query(
            value["connection_tracking_specification"],
            pairs,
            f"{key_prefix}ConnectionTrackingSpecification",
        )
    if "ena_queue_count" in value:
        pairs.append((f"{key_prefix}EnaQueueCount", str(value["ena_queue_count"])))


def deserialize_ec2_query(
    el: Element,
) -> LaunchTemplateInstanceNetworkInterfaceSpecification:
    out: LaunchTemplateInstanceNetworkInterfaceSpecification = {}  # type: ignore[typeddict-item]
    child_associate_carrier_ip_address = el.find("associateCarrierIpAddress")
    if child_associate_carrier_ip_address is not None:
        out["associate_carrier_ip_address"] = (
            child_associate_carrier_ip_address.text or ""
        ).lower() == "true"
    child_associate_public_ip_address = el.find("associatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    child_delete_on_termination = el.find("deleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_device_index = el.find("deviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_groups = el.find("groupSet")
    if child_groups is not None:
        import capo_ec2.types.group_id_string_list

        out["groups"] = capo_ec2.types.group_id_string_list.deserialize_ec2_query(
            child_groups
        )
    child_interface_type = el.find("interfaceType")
    if child_interface_type is not None:
        out["interface_type"] = str(child_interface_type.text or "")
    child_ipv6_address_count = el.find("ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    child_ipv6_addresses = el.find("ipv6AddressesSet")
    if child_ipv6_addresses is not None:
        import capo_ec2.types.instance_ipv6_address_list

        out["ipv6_addresses"] = (
            capo_ec2.types.instance_ipv6_address_list.deserialize_ec2_query(
                child_ipv6_addresses
            )
        )
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_private_ip_addresses = el.find("privateIpAddressesSet")
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
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_network_card_index = el.find("networkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_ipv4_prefixes = el.find("ipv4PrefixSet")
    if child_ipv4_prefixes is not None:
        import capo_ec2.types.ipv4_prefix_list_response

        out["ipv4_prefixes"] = (
            capo_ec2.types.ipv4_prefix_list_response.deserialize_ec2_query(
                child_ipv4_prefixes
            )
        )
    child_ipv4_prefix_count = el.find("ipv4PrefixCount")
    if child_ipv4_prefix_count is not None:
        out["ipv4_prefix_count"] = int(child_ipv4_prefix_count.text or "")
    child_ipv6_prefixes = el.find("ipv6PrefixSet")
    if child_ipv6_prefixes is not None:
        import capo_ec2.types.ipv6_prefix_list_response

        out["ipv6_prefixes"] = (
            capo_ec2.types.ipv6_prefix_list_response.deserialize_ec2_query(
                child_ipv6_prefixes
            )
        )
    child_ipv6_prefix_count = el.find("ipv6PrefixCount")
    if child_ipv6_prefix_count is not None:
        out["ipv6_prefix_count"] = int(child_ipv6_prefix_count.text or "")
    child_primary_ipv6 = el.find("primaryIpv6")
    if child_primary_ipv6 is not None:
        out["primary_ipv6"] = (child_primary_ipv6.text or "").lower() == "true"
    child_ena_srd_specification = el.find("enaSrdSpecification")
    if child_ena_srd_specification is not None:
        import capo_ec2.types.launch_template_ena_srd_specification

        out["ena_srd_specification"] = (
            capo_ec2.types.launch_template_ena_srd_specification.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_connection_tracking_specification = el.find("connectionTrackingSpecification")
    if child_connection_tracking_specification is not None:
        import capo_ec2.types.connection_tracking_specification

        out["connection_tracking_specification"] = (
            capo_ec2.types.connection_tracking_specification.deserialize_ec2_query(
                child_connection_tracking_specification
            )
        )
    child_ena_queue_count = el.find("enaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    return out
