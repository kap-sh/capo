"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list
    import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails(TypedDict, closed=True):
    associate_carrier_ip_address: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether to associate a Carrier IP address with eth0 for a new network interface. You use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information, see <a href="https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip">Carrier IP address</a> in the <i>Wavelength Developer Guide</i>. </p>"""
    associate_public_ip_address: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Associates a public IPv4 address with eth0 for a new network interface. </p>"""
    delete_on_termination: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the network interface is deleted when the instance is terminated. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A description for the network interface. </p>"""
    device_index: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The device index for the network interface attachment. </p>"""
    groups: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The IDs of one or more security groups. </p>"""
    interface_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of network interface. </p>"""
    ipv4_prefix_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of IPv4 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv4Prefixes</code> option. </p>"""
    ipv4_prefixes: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesList"
    ]
    """<p> One or more IPv4 prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv4PrefixCount</code> option. </p>"""
    ipv6_address_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if you use <code>Ipv6Addresses</code>. </p>"""
    ipv6_addresses: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesList"
    ]
    """<p> One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you use <code>Ipv6AddressCount</code>. </p>"""
    ipv6_prefix_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of IPv6 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv6Prefix</code> option. </p>"""
    ipv6_prefixes: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesList"
    ]
    """<p> One or more IPv6 prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv6PrefixCount</code> option. </p>"""
    network_card_index: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index <code>0</code>. The default is network card index <code>0</code>. </p>"""
    network_interface_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the network interface. </p>"""
    private_ip_address: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The primary private IPv4 address of the network interface. </p>"""
    private_ip_addresses: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesList"
    ]
    """<p> One or more private IPv4 addresses. </p>"""
    secondary_private_ip_address_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p> The number of secondary private IPv4 addresses to assign to a network interface. </p>"""
    subnet_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the subnet for the network interface. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails) -> dict:
    out: dict = {}
    if "associate_carrier_ip_address" in value:
        out["AssociateCarrierIpAddress"] = value["associate_carrier_ip_address"]
    if "associate_public_ip_address" in value:
        out["AssociatePublicIpAddress"] = value["associate_public_ip_address"]
    if "delete_on_termination" in value:
        out["DeleteOnTermination"] = value["delete_on_termination"]
    if "description" in value:
        out["Description"] = value["description"]
    if "device_index" in value:
        out["DeviceIndex"] = value["device_index"]
    if "groups" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Groups"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["groups"]
        )
    if "interface_type" in value:
        out["InterfaceType"] = value["interface_type"]
    if "ipv4_prefix_count" in value:
        out["Ipv4PrefixCount"] = value["ipv4_prefix_count"]
    if "ipv4_prefixes" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list

        out["Ipv4Prefixes"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list.serialize_json(
                value["ipv4_prefixes"]
            )
        )
    if "ipv6_address_count" in value:
        out["Ipv6AddressCount"] = value["ipv6_address_count"]
    if "ipv6_addresses" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list

        out["Ipv6Addresses"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list.serialize_json(
                value["ipv6_addresses"]
            )
        )
    if "ipv6_prefix_count" in value:
        out["Ipv6PrefixCount"] = value["ipv6_prefix_count"]
    if "ipv6_prefixes" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list

        out["Ipv6Prefixes"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list.serialize_json(
                value["ipv6_prefixes"]
            )
        )
    if "network_card_index" in value:
        out["NetworkCardIndex"] = value["network_card_index"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "private_ip_addresses" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list

        out["PrivateIpAddresses"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list.serialize_json(
                value["private_ip_addresses"]
            )
        )
    if "secondary_private_ip_address_count" in value:
        out["SecondaryPrivateIpAddressCount"] = value[
            "secondary_private_ip_address_count"
        ]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails:
    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssociateCarrierIpAddress") is not None:
        out["associate_carrier_ip_address"] = data["AssociateCarrierIpAddress"]
    if data.get("AssociatePublicIpAddress") is not None:
        out["associate_public_ip_address"] = data["AssociatePublicIpAddress"]
    if data.get("DeleteOnTermination") is not None:
        out["delete_on_termination"] = data["DeleteOnTermination"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DeviceIndex") is not None:
        out["device_index"] = data["DeviceIndex"]
    if data.get("Groups") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["groups"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Groups"]
        )
    if data.get("InterfaceType") is not None:
        out["interface_type"] = data["InterfaceType"]
    if data.get("Ipv4PrefixCount") is not None:
        out["ipv4_prefix_count"] = data["Ipv4PrefixCount"]
    if data.get("Ipv4Prefixes") is not None:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list

        out["ipv4_prefixes"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv4_prefixes_list.deserialize_json(
                data["Ipv4Prefixes"]
            )
        )
    if data.get("Ipv6AddressCount") is not None:
        out["ipv6_address_count"] = data["Ipv6AddressCount"]
    if data.get("Ipv6Addresses") is not None:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list

        out["ipv6_addresses"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_addresses_list.deserialize_json(
                data["Ipv6Addresses"]
            )
        )
    if data.get("Ipv6PrefixCount") is not None:
        out["ipv6_prefix_count"] = data["Ipv6PrefixCount"]
    if data.get("Ipv6Prefixes") is not None:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list

        out["ipv6_prefixes"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_ipv6_prefixes_list.deserialize_json(
                data["Ipv6Prefixes"]
            )
        )
    if data.get("NetworkCardIndex") is not None:
        out["network_card_index"] = data["NetworkCardIndex"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if data.get("PrivateIpAddress") is not None:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if data.get("PrivateIpAddresses") is not None:
        import capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list

        out["private_ip_addresses"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_network_interface_set_private_ip_addresses_list.deserialize_json(
                data["PrivateIpAddresses"]
            )
        )
    if data.get("SecondaryPrivateIpAddressCount") is not None:
        out["secondary_private_ip_address_count"] = data[
            "SecondaryPrivateIpAddressCount"
        ]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    return out
