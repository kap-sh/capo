"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.associated_subnet_list
    import capo_ec2.types.boolean
    import capo_ec2.types.connection_tracking_configuration
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.ipv4_prefixes_list
    import capo_ec2.types.ipv6_prefixes_list
    import capo_ec2.types.network_interface_association
    import capo_ec2.types.network_interface_attachment
    import capo_ec2.types.network_interface_ipv6_addresses_list
    import capo_ec2.types.network_interface_private_ip_address_list
    import capo_ec2.types.network_interface_status
    import capo_ec2.types.network_interface_type
    import capo_ec2.types.operator_response
    import capo_ec2.types.public_ip_dns_name_options
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class NetworkInterface(TypedDict, closed=True):
    association: NotRequired[
        "capo_ec2.types.network_interface_association.NetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IP address (IPv4) associated with the network interface.</p>"""
    attachment: NotRequired[
        "capo_ec2.types.network_interface_attachment.NetworkInterfaceAttachment"
    ]
    """<p>The network interface attachment.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    connection_tracking_configuration: NotRequired[
        "capo_ec2.types.connection_tracking_configuration.ConnectionTrackingConfiguration"
    ]
    """<p>A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description.</p>"""
    groups: NotRequired["capo_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>Any security groups for the network interface.</p>"""
    interface_type: NotRequired[
        "capo_ec2.types.network_interface_type.NetworkInterfaceType"
    ]
    """<p>The type of network interface.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.network_interface_ipv6_addresses_list.NetworkInterfaceIpv6AddressesList"
    ]
    """<p>The IPv6 addresses associated with the network interface.</p>"""
    mac_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The MAC address.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the network interface.</p>"""
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The private hostname. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A public hostname. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_ip_dns_name_options: NotRequired[
        "capo_ec2.types.public_ip_dns_name_options.PublicIpDnsNameOptions"
    ]
    """<p>Public hostname type options. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.network_interface_private_ip_address_list.NetworkInterfacePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the network interface.</p>"""
    ipv4_prefixes: NotRequired["capo_ec2.types.ipv4_prefixes_list.Ipv4PrefixesList"]
    """<p>The IPv4 prefixes that are assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired["capo_ec2.types.ipv6_prefixes_list.Ipv6PrefixesList"]
    """<p>The IPv6 prefixes that are assigned to the network interface.</p>"""
    requester_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The alias or Amazon Web Services account ID of the principal or service that created the network interface.</p>"""
    requester_managed: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is being managed by Amazon Web Services.</p>"""
    source_dest_check: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "capo_ec2.types.network_interface_status.NetworkInterfaceStatus"
    ]
    """<p>The status of the network interface.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    tag_set: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the network interface.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    deny_all_igw_traffic: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is <code>true</code>, inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks.</p>"""
    ipv6_native: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is an IPv6 only network interface.</p>"""
    ipv6_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 globally unique address associated with the network interface.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the network interface.</p>"""
    associated_subnets: NotRequired[
        "capo_ec2.types.associated_subnet_list.AssociatedSubnetList"
    ]
    """<p>The subnets associated with this network interface.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association" in value:
        import capo_ec2.types.network_interface_association

        capo_ec2.types.network_interface_association.serialize_ec2_query(
            value["association"], pairs, f"{key_prefix}Association"
        )
    if "attachment" in value:
        import capo_ec2.types.network_interface_attachment

        capo_ec2.types.network_interface_attachment.serialize_ec2_query(
            value["attachment"], pairs, f"{key_prefix}Attachment"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "connection_tracking_configuration" in value:
        import capo_ec2.types.connection_tracking_configuration

        capo_ec2.types.connection_tracking_configuration.serialize_ec2_query(
            value["connection_tracking_configuration"],
            pairs,
            f"{key_prefix}ConnectionTrackingConfiguration",
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "interface_type" in value:
        import capo_ec2.types.network_interface_type

        capo_ec2.types.network_interface_type.serialize_ec2_query(
            value["interface_type"], pairs, f"{key_prefix}InterfaceType"
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.network_interface_ipv6_addresses_list

        capo_ec2.types.network_interface_ipv6_addresses_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6AddressesSet"
        )
    if "mac_address" in value:
        pairs.append((f"{key_prefix}MacAddress", str(value["mac_address"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "private_dns_name" in value:
        pairs.append((f"{key_prefix}PrivateDnsName", str(value["private_dns_name"])))
    if "public_dns_name" in value:
        pairs.append((f"{key_prefix}PublicDnsName", str(value["public_dns_name"])))
    if "public_ip_dns_name_options" in value:
        import capo_ec2.types.public_ip_dns_name_options

        capo_ec2.types.public_ip_dns_name_options.serialize_ec2_query(
            value["public_ip_dns_name_options"],
            pairs,
            f"{key_prefix}PublicIpDnsNameOptions",
        )
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "private_ip_addresses" in value:
        import capo_ec2.types.network_interface_private_ip_address_list

        capo_ec2.types.network_interface_private_ip_address_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddressesSet"
        )
    if "ipv4_prefixes" in value:
        import capo_ec2.types.ipv4_prefixes_list

        capo_ec2.types.ipv4_prefixes_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4PrefixSet"
        )
    if "ipv6_prefixes" in value:
        import capo_ec2.types.ipv6_prefixes_list

        capo_ec2.types.ipv6_prefixes_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6PrefixSet"
        )
    if "requester_id" in value:
        pairs.append((f"{key_prefix}RequesterId", str(value["requester_id"])))
    if "requester_managed" in value:
        pairs.append(
            (
                f"{key_prefix}RequesterManaged",
                "true" if value["requester_managed"] else "false",
            )
        )
    if "source_dest_check" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDestCheck",
                "true" if value["source_dest_check"] else "false",
            )
        )
    if "status" in value:
        import capo_ec2.types.network_interface_status

        capo_ec2.types.network_interface_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "tag_set" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tag_set"], pairs, f"{key_prefix}TagSet"
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "deny_all_igw_traffic" in value:
        pairs.append(
            (
                f"{key_prefix}DenyAllIgwTraffic",
                "true" if value["deny_all_igw_traffic"] else "false",
            )
        )
    if "ipv6_native" in value:
        pairs.append(
            (f"{key_prefix}Ipv6Native", "true" if value["ipv6_native"] else "false")
        )
    if "ipv6_address" in value:
        pairs.append((f"{key_prefix}Ipv6Address", str(value["ipv6_address"])))
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "associated_subnets" in value:
        import capo_ec2.types.associated_subnet_list

        capo_ec2.types.associated_subnet_list.serialize_ec2_query(
            value["associated_subnets"], pairs, f"{key_prefix}AssociatedSubnetSet"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    child_association = el.find("association")
    if child_association is not None:
        import capo_ec2.types.network_interface_association

        out["association"] = (
            capo_ec2.types.network_interface_association.deserialize_ec2_query(
                child_association
            )
        )
    child_attachment = el.find("attachment")
    if child_attachment is not None:
        import capo_ec2.types.network_interface_attachment

        out["attachment"] = (
            capo_ec2.types.network_interface_attachment.deserialize_ec2_query(
                child_attachment
            )
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_connection_tracking_configuration = el.find("connectionTrackingConfiguration")
    if child_connection_tracking_configuration is not None:
        import capo_ec2.types.connection_tracking_configuration

        out["connection_tracking_configuration"] = (
            capo_ec2.types.connection_tracking_configuration.deserialize_ec2_query(
                child_connection_tracking_configuration
            )
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_groups = el.find("groupSet")
    if child_groups is not None:
        import capo_ec2.types.group_identifier_list

        out["groups"] = capo_ec2.types.group_identifier_list.deserialize_ec2_query(
            child_groups
        )
    child_interface_type = el.find("interfaceType")
    if child_interface_type is not None:
        import capo_ec2.types.network_interface_type

        out["interface_type"] = (
            capo_ec2.types.network_interface_type.deserialize_ec2_query(
                child_interface_type
            )
        )
    child_ipv6_addresses = el.find("ipv6AddressesSet")
    if child_ipv6_addresses is not None:
        import capo_ec2.types.network_interface_ipv6_addresses_list

        out["ipv6_addresses"] = (
            capo_ec2.types.network_interface_ipv6_addresses_list.deserialize_ec2_query(
                child_ipv6_addresses
            )
        )
    child_mac_address = el.find("macAddress")
    if child_mac_address is not None:
        out["mac_address"] = str(child_mac_address.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_private_dns_name = el.find("privateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_public_dns_name = el.find("publicDnsName")
    if child_public_dns_name is not None:
        out["public_dns_name"] = str(child_public_dns_name.text or "")
    child_public_ip_dns_name_options = el.find("publicIpDnsNameOptions")
    if child_public_ip_dns_name_options is not None:
        import capo_ec2.types.public_ip_dns_name_options

        out["public_ip_dns_name_options"] = (
            capo_ec2.types.public_ip_dns_name_options.deserialize_ec2_query(
                child_public_ip_dns_name_options
            )
        )
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_private_ip_addresses = el.find("privateIpAddressesSet")
    if child_private_ip_addresses is not None:
        import capo_ec2.types.network_interface_private_ip_address_list

        out["private_ip_addresses"] = (
            capo_ec2.types.network_interface_private_ip_address_list.deserialize_ec2_query(
                child_private_ip_addresses
            )
        )
    child_ipv4_prefixes = el.find("ipv4PrefixSet")
    if child_ipv4_prefixes is not None:
        import capo_ec2.types.ipv4_prefixes_list

        out["ipv4_prefixes"] = capo_ec2.types.ipv4_prefixes_list.deserialize_ec2_query(
            child_ipv4_prefixes
        )
    child_ipv6_prefixes = el.find("ipv6PrefixSet")
    if child_ipv6_prefixes is not None:
        import capo_ec2.types.ipv6_prefixes_list

        out["ipv6_prefixes"] = capo_ec2.types.ipv6_prefixes_list.deserialize_ec2_query(
            child_ipv6_prefixes
        )
    child_requester_id = el.find("requesterId")
    if child_requester_id is not None:
        out["requester_id"] = str(child_requester_id.text or "")
    child_requester_managed = el.find("requesterManaged")
    if child_requester_managed is not None:
        out["requester_managed"] = (
            child_requester_managed.text or ""
        ).lower() == "true"
    child_source_dest_check = el.find("sourceDestCheck")
    if child_source_dest_check is not None:
        out["source_dest_check"] = (
            child_source_dest_check.text or ""
        ).lower() == "true"
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.network_interface_status

        out["status"] = capo_ec2.types.network_interface_status.deserialize_ec2_query(
            child_status
        )
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_tag_set = el.find("tagSet")
    if child_tag_set is not None:
        import capo_ec2.types.tag_list

        out["tag_set"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tag_set)
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_deny_all_igw_traffic = el.find("denyAllIgwTraffic")
    if child_deny_all_igw_traffic is not None:
        out["deny_all_igw_traffic"] = (
            child_deny_all_igw_traffic.text or ""
        ).lower() == "true"
    child_ipv6_native = el.find("ipv6Native")
    if child_ipv6_native is not None:
        out["ipv6_native"] = (child_ipv6_native.text or "").lower() == "true"
    child_ipv6_address = el.find("ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_associated_subnets = el.find("associatedSubnetSet")
    if child_associated_subnets is not None:
        import capo_ec2.types.associated_subnet_list

        out["associated_subnets"] = (
            capo_ec2.types.associated_subnet_list.deserialize_ec2_query(
                child_associated_subnets
            )
        )
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
