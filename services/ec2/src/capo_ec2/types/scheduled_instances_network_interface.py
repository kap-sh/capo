"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.private_ip_address_config_set
    import capo_ec2.types.scheduled_instances_ipv6_address_list
    import capo_ec2.types.scheduled_instances_security_group_id_set
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class ScheduledInstancesNetworkInterface(TypedDict, closed=True):
    associate_public_ip_address: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is <code>true</code>.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href="http://aws.amazon.com/vpc/pricing/">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to delete the interface when the instance is terminated.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the device for the network interface attachment.</p>"""
    groups: NotRequired[
        "capo_ec2.types.scheduled_instances_security_group_id_set.ScheduledInstancesSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.scheduled_instances_ipv6_address_list.ScheduledInstancesIpv6AddressList"
    ]
    """<p>The specific IPv6 addresses from the subnet range.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_address_configs: NotRequired[
        "capo_ec2.types.private_ip_address_config_set.PrivateIpAddressConfigSet"
    ]
    """<p>The private IPv4 addresses.</p>"""
    secondary_private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesNetworkInterface, pairs: list[tuple[str, str]], prefix: str
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
        import capo_ec2.types.scheduled_instances_security_group_id_set

        capo_ec2.types.scheduled_instances_security_group_id_set.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}Group"
        )
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.scheduled_instances_ipv6_address_list

        capo_ec2.types.scheduled_instances_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6Address"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "private_ip_address_configs" in value:
        import capo_ec2.types.private_ip_address_config_set

        capo_ec2.types.private_ip_address_config_set.serialize_ec2_query(
            value["private_ip_address_configs"],
            pairs,
            f"{key_prefix}PrivateIpAddressConfig",
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


def deserialize_ec2_query(el: Element) -> ScheduledInstancesNetworkInterface:
    out: ScheduledInstancesNetworkInterface = {}  # type: ignore[typeddict-item]
    child_associate_public_ip_address = el.find("AssociatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_groups = el.find("Group")
    if child_groups is not None:
        import capo_ec2.types.scheduled_instances_security_group_id_set

        out["groups"] = (
            capo_ec2.types.scheduled_instances_security_group_id_set.deserialize_ec2_query(
                child_groups
            )
        )
    child_ipv6_address_count = el.find("Ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    child_ipv6_addresses = el.find("Ipv6Address")
    if child_ipv6_addresses is not None:
        import capo_ec2.types.scheduled_instances_ipv6_address_list

        out["ipv6_addresses"] = (
            capo_ec2.types.scheduled_instances_ipv6_address_list.deserialize_ec2_query(
                child_ipv6_addresses
            )
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_private_ip_address_configs = el.find("PrivateIpAddressConfig")
    if child_private_ip_address_configs is not None:
        import capo_ec2.types.private_ip_address_config_set

        out["private_ip_address_configs"] = (
            capo_ec2.types.private_ip_address_config_set.deserialize_ec2_query(
                child_private_ip_address_configs
            )
        )
    child_secondary_private_ip_address_count = el.find("SecondaryPrivateIpAddressCount")
    if child_secondary_private_ip_address_count is not None:
        out["secondary_private_ip_address_count"] = int(
            child_secondary_private_ip_address_count.text or ""
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    return out
