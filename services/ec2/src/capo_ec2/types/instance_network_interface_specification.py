"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_specification_request
    import capo_ec2.types.ena_srd_specification_request
    import capo_ec2.types.instance_ipv6_address_list
    import capo_ec2.types.integer
    import capo_ec2.types.ipv4_prefix_list
    import capo_ec2.types.ipv6_prefix_list
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.private_ip_address_specification_list
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.string


class InstanceNetworkInterfaceSpecification(TypedDict, closed=True):
    associate_public_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is <code>true</code>.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, the interface is deleted when the instance is terminated. You can specify <code>true</code> only if creating a new network interface when launching an instance.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The position of the network interface in the attachment order. A primary network interface has a device index of 0.</p> <p>If you specify a network interface when launching an instance, you must specify the device index.</p>"""
    groups: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p> <p>If you are creating a Spot Fleet, omit this parameter because you can’t specify a network interface ID in a launch specification.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a> request.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>The private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a> request.</p>"""
    secondary_private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses. You can’t specify this parameter and also specify a secondary private IP address using the <code>PrivateIpAddress</code> parameter.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet associated with the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    associate_carrier_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a carrier IP address to the network interface.</p> <p>You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see <a href="https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip">Carrier IP address</a> in the <i>Amazon Web Services Wavelength Developer Guide</i>.</p>"""
    interface_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of network interface.</p> <p>If you specify <code>efa-only</code>, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.</p> <p>Valid values: <code>interface</code> | <code>efa</code> | <code>efa-only</code> </p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.</p> <p>If you are using <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html">RequestSpotInstances</a> to create Spot Instances, omit this parameter because you can’t specify the network card index when using this API. To specify the network card index, use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a>.</p>"""
    ipv4_prefixes: NotRequired["capo_ec2.types.ipv4_prefix_list.Ipv4PrefixList"]
    """<p>The IPv4 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv4PrefixCount</code> option.</p>"""
    ipv4_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv4 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv4Prefix</code> option.</p>"""
    ipv6_prefixes: NotRequired["capo_ec2.types.ipv6_prefix_list.Ipv6PrefixList"]
    """<p>The IPv6 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv6PrefixCount</code> option.</p>"""
    ipv6_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv6Prefix</code> option.</p>"""
    primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a>.</p>"""
    ena_srd_specification: NotRequired[
        "capo_ec2.types.ena_srd_specification_request.EnaSrdSpecificationRequest"
    ]
    """<p>Specifies the ENA Express settings for the network interface that's attached to the instance.</p>"""
    connection_tracking_specification: NotRequired[
        "capo_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ena_queue_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterfaceSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
        import capo_ec2.types.security_group_id_string_list

        capo_ec2.types.security_group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.instance_ipv6_address_list

        capo_ec2.types.instance_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6Addresses"
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
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddresses"
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
    if "associate_carrier_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}AssociateCarrierIpAddress",
                "true" if value["associate_carrier_ip_address"] else "false",
            )
        )
    if "interface_type" in value:
        pairs.append((f"{key_prefix}InterfaceType", str(value["interface_type"])))
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
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
    if "primary_ipv6" in value:
        pairs.append(
            (f"{key_prefix}PrimaryIpv6", "true" if value["primary_ipv6"] else "false")
        )
    if "ena_srd_specification" in value:
        import capo_ec2.types.ena_srd_specification_request

        capo_ec2.types.ena_srd_specification_request.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{key_prefix}EnaSrdSpecification"
        )
    if "connection_tracking_specification" in value:
        import capo_ec2.types.connection_tracking_specification_request

        capo_ec2.types.connection_tracking_specification_request.serialize_ec2_query(
            value["connection_tracking_specification"],
            pairs,
            f"{key_prefix}ConnectionTrackingSpecification",
        )
    if "ena_queue_count" in value:
        pairs.append((f"{key_prefix}EnaQueueCount", str(value["ena_queue_count"])))


def deserialize_ec2_query(el: Element) -> InstanceNetworkInterfaceSpecification:
    out: InstanceNetworkInterfaceSpecification = {}  # type: ignore[typeddict-item]
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
    child_groups = el.find("SecurityGroupId")
    if child_groups is not None:
        import capo_ec2.types.security_group_id_string_list

        out["groups"] = (
            capo_ec2.types.security_group_id_string_list.deserialize_ec2_query(
                child_groups
            )
        )
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
    child_associate_carrier_ip_address = el.find("AssociateCarrierIpAddress")
    if child_associate_carrier_ip_address is not None:
        out["associate_carrier_ip_address"] = (
            child_associate_carrier_ip_address.text or ""
        ).lower() == "true"
    child_interface_type = el.find("InterfaceType")
    if child_interface_type is not None:
        out["interface_type"] = str(child_interface_type.text or "")
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
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
    child_primary_ipv6 = el.find("PrimaryIpv6")
    if child_primary_ipv6 is not None:
        out["primary_ipv6"] = (child_primary_ipv6.text or "").lower() == "true"
    child_ena_srd_specification = el.find("EnaSrdSpecification")
    if child_ena_srd_specification is not None:
        import capo_ec2.types.ena_srd_specification_request

        out["ena_srd_specification"] = (
            capo_ec2.types.ena_srd_specification_request.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_connection_tracking_specification = el.find("ConnectionTrackingSpecification")
    if child_connection_tracking_specification is not None:
        import capo_ec2.types.connection_tracking_specification_request

        out["connection_tracking_specification"] = (
            capo_ec2.types.connection_tracking_specification_request.deserialize_ec2_query(
                child_connection_tracking_specification
            )
        )
    child_ena_queue_count = el.find("EnaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    return out
