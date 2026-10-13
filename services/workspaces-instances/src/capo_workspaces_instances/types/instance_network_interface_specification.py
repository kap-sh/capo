"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceNetworkInterfaceSpecification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.connection_tracking_specification_request
    import capo_workspaces_instances.types.description
    import capo_workspaces_instances.types.ena_srd_specification_request
    import capo_workspaces_instances.types.interface_type_enum
    import capo_workspaces_instances.types.ipv4_address
    import capo_workspaces_instances.types.ipv4_prefixes
    import capo_workspaces_instances.types.ipv6_addresses
    import capo_workspaces_instances.types.ipv6_prefixes
    import capo_workspaces_instances.types.network_interface_id
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.private_ip_addresses
    import capo_workspaces_instances.types.security_group_ids
    import capo_workspaces_instances.types.subnet_id


class InstanceNetworkInterfaceSpecification(TypedDict, closed=True):
    associate_carrier_ip_address: NotRequired["bool"]
    """<p>Enables carrier IP address association.</p>"""
    associate_public_ip_address: NotRequired["bool"]
    """<p>Enables public IP address assignment.</p>"""
    connection_tracking_specification: NotRequired[
        "capo_workspaces_instances.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>Configures network connection tracking parameters.</p>"""
    description: NotRequired["capo_workspaces_instances.types.description.Description"]
    """<p>Descriptive text for the network interface.</p>"""
    device_index: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Unique index for the network interface.</p>"""
    ena_srd_specification: NotRequired[
        "capo_workspaces_instances.types.ena_srd_specification_request.EnaSrdSpecificationRequest"
    ]
    """<p>Configures Elastic Network Adapter Scalable Reliable Datagram settings.</p>"""
    interface_type: NotRequired[
        "capo_workspaces_instances.types.interface_type_enum.InterfaceTypeEnum"
    ]
    """<p>Specifies the type of network interface.</p>"""
    ipv4_prefixes: NotRequired[
        "capo_workspaces_instances.types.ipv4_prefixes.Ipv4Prefixes"
    ]
    """<p>IPv4 prefix configurations for the interface.</p>"""
    ipv4_prefix_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of IPv4 prefixes to assign.</p>"""
    ipv6_address_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of IPv6 addresses to assign.</p>"""
    ipv6_addresses: NotRequired[
        "capo_workspaces_instances.types.ipv6_addresses.Ipv6Addresses"
    ]
    """<p>Specific IPv6 addresses for the interface.</p>"""
    ipv6_prefixes: NotRequired[
        "capo_workspaces_instances.types.ipv6_prefixes.Ipv6Prefixes"
    ]
    """<p>IPv6 prefix configurations for the interface.</p>"""
    ipv6_prefix_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of IPv6 prefixes to assign.</p>"""
    network_card_index: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Index of the network card for multiple network interfaces.</p>"""
    network_interface_id: NotRequired[
        "capo_workspaces_instances.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>Unique identifier for the network interface.</p>"""
    primary_ipv6: NotRequired["bool"]
    """<p>Indicates the primary IPv6 configuration.</p>"""
    private_ip_address: NotRequired[
        "capo_workspaces_instances.types.ipv4_address.Ipv4Address"
    ]
    """<p>Primary private IP address for the interface.</p>"""
    private_ip_addresses: NotRequired[
        "capo_workspaces_instances.types.private_ip_addresses.PrivateIpAddresses"
    ]
    """<p>List of private IP addresses for the interface.</p>"""
    secondary_private_ip_address_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of additional private IP addresses to assign.</p>"""
    groups: NotRequired[
        "capo_workspaces_instances.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>Security groups associated with the network interface.</p>"""
    subnet_id: NotRequired["capo_workspaces_instances.types.subnet_id.SubnetId"]
    """<p>Subnet identifier for the network interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceNetworkInterfaceSpecification) -> dict:
    out: dict = {}
    if "associate_carrier_ip_address" in value:
        out["AssociateCarrierIpAddress"] = value["associate_carrier_ip_address"]
    if "associate_public_ip_address" in value:
        out["AssociatePublicIpAddress"] = value["associate_public_ip_address"]
    if "connection_tracking_specification" in value:
        import capo_workspaces_instances.types.connection_tracking_specification_request

        out["ConnectionTrackingSpecification"] = (
            capo_workspaces_instances.types.connection_tracking_specification_request.serialize_aws_json_1_0(
                value["connection_tracking_specification"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "device_index" in value:
        out["DeviceIndex"] = value["device_index"]
    if "ena_srd_specification" in value:
        import capo_workspaces_instances.types.ena_srd_specification_request

        out["EnaSrdSpecification"] = (
            capo_workspaces_instances.types.ena_srd_specification_request.serialize_aws_json_1_0(
                value["ena_srd_specification"]
            )
        )
    if "interface_type" in value:
        import capo_workspaces_instances.types.interface_type_enum

        out["InterfaceType"] = (
            capo_workspaces_instances.types.interface_type_enum.serialize_aws_json_1_0(
                value["interface_type"]
            )
        )
    if "ipv4_prefixes" in value:
        import capo_workspaces_instances.types.ipv4_prefixes

        out["Ipv4Prefixes"] = (
            capo_workspaces_instances.types.ipv4_prefixes.serialize_aws_json_1_0(
                value["ipv4_prefixes"]
            )
        )
    if "ipv4_prefix_count" in value:
        out["Ipv4PrefixCount"] = value["ipv4_prefix_count"]
    if "ipv6_address_count" in value:
        out["Ipv6AddressCount"] = value["ipv6_address_count"]
    if "ipv6_addresses" in value:
        import capo_workspaces_instances.types.ipv6_addresses

        out["Ipv6Addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.serialize_aws_json_1_0(
                value["ipv6_addresses"]
            )
        )
    if "ipv6_prefixes" in value:
        import capo_workspaces_instances.types.ipv6_prefixes

        out["Ipv6Prefixes"] = (
            capo_workspaces_instances.types.ipv6_prefixes.serialize_aws_json_1_0(
                value["ipv6_prefixes"]
            )
        )
    if "ipv6_prefix_count" in value:
        out["Ipv6PrefixCount"] = value["ipv6_prefix_count"]
    if "network_card_index" in value:
        out["NetworkCardIndex"] = value["network_card_index"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "primary_ipv6" in value:
        out["PrimaryIpv6"] = value["primary_ipv6"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "private_ip_addresses" in value:
        import capo_workspaces_instances.types.private_ip_addresses

        out["PrivateIpAddresses"] = (
            capo_workspaces_instances.types.private_ip_addresses.serialize_aws_json_1_0(
                value["private_ip_addresses"]
            )
        )
    if "secondary_private_ip_address_count" in value:
        out["SecondaryPrivateIpAddressCount"] = value[
            "secondary_private_ip_address_count"
        ]
    if "groups" in value:
        import capo_workspaces_instances.types.security_group_ids

        out["Groups"] = (
            capo_workspaces_instances.types.security_group_ids.serialize_aws_json_1_0(
                value["groups"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceNetworkInterfaceSpecification:
    out: InstanceNetworkInterfaceSpecification = {}  # type: ignore[typeddict-item]
    if data.get("AssociateCarrierIpAddress") is not None:
        out["associate_carrier_ip_address"] = data["AssociateCarrierIpAddress"]
    if data.get("AssociatePublicIpAddress") is not None:
        out["associate_public_ip_address"] = data["AssociatePublicIpAddress"]
    if data.get("ConnectionTrackingSpecification") is not None:
        import capo_workspaces_instances.types.connection_tracking_specification_request

        out["connection_tracking_specification"] = (
            capo_workspaces_instances.types.connection_tracking_specification_request.deserialize_aws_json_1_0(
                data["ConnectionTrackingSpecification"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DeviceIndex") is not None:
        out["device_index"] = data["DeviceIndex"]
    if data.get("EnaSrdSpecification") is not None:
        import capo_workspaces_instances.types.ena_srd_specification_request

        out["ena_srd_specification"] = (
            capo_workspaces_instances.types.ena_srd_specification_request.deserialize_aws_json_1_0(
                data["EnaSrdSpecification"]
            )
        )
    if data.get("InterfaceType") is not None:
        import capo_workspaces_instances.types.interface_type_enum

        out["interface_type"] = (
            capo_workspaces_instances.types.interface_type_enum.deserialize_aws_json_1_0(
                data["InterfaceType"]
            )
        )
    if data.get("Ipv4Prefixes") is not None:
        import capo_workspaces_instances.types.ipv4_prefixes

        out["ipv4_prefixes"] = (
            capo_workspaces_instances.types.ipv4_prefixes.deserialize_aws_json_1_0(
                data["Ipv4Prefixes"]
            )
        )
    if data.get("Ipv4PrefixCount") is not None:
        out["ipv4_prefix_count"] = data["Ipv4PrefixCount"]
    if data.get("Ipv6AddressCount") is not None:
        out["ipv6_address_count"] = data["Ipv6AddressCount"]
    if data.get("Ipv6Addresses") is not None:
        import capo_workspaces_instances.types.ipv6_addresses

        out["ipv6_addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.deserialize_aws_json_1_0(
                data["Ipv6Addresses"]
            )
        )
    if data.get("Ipv6Prefixes") is not None:
        import capo_workspaces_instances.types.ipv6_prefixes

        out["ipv6_prefixes"] = (
            capo_workspaces_instances.types.ipv6_prefixes.deserialize_aws_json_1_0(
                data["Ipv6Prefixes"]
            )
        )
    if data.get("Ipv6PrefixCount") is not None:
        out["ipv6_prefix_count"] = data["Ipv6PrefixCount"]
    if data.get("NetworkCardIndex") is not None:
        out["network_card_index"] = data["NetworkCardIndex"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if data.get("PrimaryIpv6") is not None:
        out["primary_ipv6"] = data["PrimaryIpv6"]
    if data.get("PrivateIpAddress") is not None:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if data.get("PrivateIpAddresses") is not None:
        import capo_workspaces_instances.types.private_ip_addresses

        out["private_ip_addresses"] = (
            capo_workspaces_instances.types.private_ip_addresses.deserialize_aws_json_1_0(
                data["PrivateIpAddresses"]
            )
        )
    if data.get("SecondaryPrivateIpAddressCount") is not None:
        out["secondary_private_ip_address_count"] = data[
            "SecondaryPrivateIpAddressCount"
        ]
    if data.get("Groups") is not None:
        import capo_workspaces_instances.types.security_group_ids

        out["groups"] = (
            capo_workspaces_instances.types.security_group_ids.deserialize_aws_json_1_0(
                data["Groups"]
            )
        )
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    return out


def redact_sensitive(value: InstanceNetworkInterfaceSpecification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ipv6_addresses" in value:
        import capo_workspaces_instances.types.ipv6_addresses

        out["ipv6_addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.redact_sensitive(
                value["ipv6_addresses"]
            )
        )
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    if "private_ip_addresses" in value:
        import capo_workspaces_instances.types.private_ip_addresses

        out["private_ip_addresses"] = (
            capo_workspaces_instances.types.private_ip_addresses.redact_sensitive(
                value["private_ip_addresses"]
            )
        )
    return out
