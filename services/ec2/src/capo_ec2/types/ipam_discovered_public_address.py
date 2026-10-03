"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredPublicAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_public_address_association_status
    import capo_ec2.types.ipam_public_address_aws_service
    import capo_ec2.types.ipam_public_address_security_group_list
    import capo_ec2.types.ipam_public_address_tags
    import capo_ec2.types.ipam_public_address_type
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamDiscoveredPublicAddress(TypedDict, closed=True):
    ipam_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    address_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region of the resource the IP address is assigned to.</p>"""
    address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address.</p>"""
    address_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the owner of the resource the IP address is assigned to.</p>"""
    address_allocation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The allocation ID of the resource the IP address is assigned to.</p>"""
    association_status: NotRequired[
        "capo_ec2.types.ipam_public_address_association_status.IpamPublicAddressAssociationStatus"
    ]
    """<p>The association status.</p>"""
    address_type: NotRequired[
        "capo_ec2.types.ipam_public_address_type.IpamPublicAddressType"
    ]
    """<p>The IP address type.</p>"""
    service: NotRequired[
        "capo_ec2.types.ipam_public_address_aws_service.IpamPublicAddressAwsService"
    ]
    """<p>The Amazon Web Services service associated with the IP address.</p>"""
    service_resource: NotRequired["capo_ec2.types.string.String"]
    """<p>The resource ARN or ID.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC that the resource with the assigned IP address is in.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet that the resource with the assigned IP address is in.</p>"""
    public_ipv4_pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the public IPv4 pool that the resource with the assigned IP address is from.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The network interface ID of the resource with the assigned IP address.</p>"""
    network_interface_description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the network interface that IP address is assigned to.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance ID of the instance the assigned IP address is assigned to.</p>"""
    tags: NotRequired["capo_ec2.types.ipam_public_address_tags.IpamPublicAddressTags"]
    """<p>Tags associated with the IP address.</p>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail">Local Zone availability</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.ipam_public_address_security_group_list.IpamPublicAddressSecurityGroupList"
    ]
    """<p>Security groups associated with the resource that the IP address is assigned to.</p>"""
    sample_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The last successful resource discovery time.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredPublicAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "address_region" in value:
        pairs.append((f"{key_prefix}AddressRegion", str(value["address_region"])))
    if "address" in value:
        pairs.append((f"{key_prefix}Address", str(value["address"])))
    if "address_owner_id" in value:
        pairs.append((f"{key_prefix}AddressOwnerId", str(value["address_owner_id"])))
    if "address_allocation_id" in value:
        pairs.append(
            (f"{key_prefix}AddressAllocationId", str(value["address_allocation_id"]))
        )
    if "association_status" in value:
        import capo_ec2.types.ipam_public_address_association_status

        capo_ec2.types.ipam_public_address_association_status.serialize_ec2_query(
            value["association_status"], pairs, f"{key_prefix}AssociationStatus"
        )
    if "address_type" in value:
        import capo_ec2.types.ipam_public_address_type

        capo_ec2.types.ipam_public_address_type.serialize_ec2_query(
            value["address_type"], pairs, f"{key_prefix}AddressType"
        )
    if "service" in value:
        import capo_ec2.types.ipam_public_address_aws_service

        capo_ec2.types.ipam_public_address_aws_service.serialize_ec2_query(
            value["service"], pairs, f"{key_prefix}Service"
        )
    if "service_resource" in value:
        pairs.append((f"{key_prefix}ServiceResource", str(value["service_resource"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "public_ipv4_pool_id" in value:
        pairs.append(
            (f"{key_prefix}PublicIpv4PoolId", str(value["public_ipv4_pool_id"]))
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "network_interface_description" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInterfaceDescription",
                str(value["network_interface_description"]),
            )
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "tags" in value:
        import capo_ec2.types.ipam_public_address_tags

        capo_ec2.types.ipam_public_address_tags.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "security_groups" in value:
        import capo_ec2.types.ipam_public_address_security_group_list

        capo_ec2.types.ipam_public_address_security_group_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroupSet"
        )
    if "sample_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["sample_time"], pairs, f"{key_prefix}SampleTime"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredPublicAddress:
    out: IpamDiscoveredPublicAddress = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery_id = el.find("ipamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_address_region = el.find("addressRegion")
    if child_address_region is not None:
        out["address_region"] = str(child_address_region.text or "")
    child_address = el.find("address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_address_owner_id = el.find("addressOwnerId")
    if child_address_owner_id is not None:
        out["address_owner_id"] = str(child_address_owner_id.text or "")
    child_address_allocation_id = el.find("addressAllocationId")
    if child_address_allocation_id is not None:
        out["address_allocation_id"] = str(child_address_allocation_id.text or "")
    child_association_status = el.find("associationStatus")
    if child_association_status is not None:
        import capo_ec2.types.ipam_public_address_association_status

        out["association_status"] = (
            capo_ec2.types.ipam_public_address_association_status.deserialize_ec2_query(
                child_association_status
            )
        )
    child_address_type = el.find("addressType")
    if child_address_type is not None:
        import capo_ec2.types.ipam_public_address_type

        out["address_type"] = (
            capo_ec2.types.ipam_public_address_type.deserialize_ec2_query(
                child_address_type
            )
        )
    child_service = el.find("service")
    if child_service is not None:
        import capo_ec2.types.ipam_public_address_aws_service

        out["service"] = (
            capo_ec2.types.ipam_public_address_aws_service.deserialize_ec2_query(
                child_service
            )
        )
    child_service_resource = el.find("serviceResource")
    if child_service_resource is not None:
        out["service_resource"] = str(child_service_resource.text or "")
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_public_ipv4_pool_id = el.find("publicIpv4PoolId")
    if child_public_ipv4_pool_id is not None:
        out["public_ipv4_pool_id"] = str(child_public_ipv4_pool_id.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_network_interface_description = el.find("networkInterfaceDescription")
    if child_network_interface_description is not None:
        out["network_interface_description"] = str(
            child_network_interface_description.text or ""
        )
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_tags = el.find("tags")
    if child_tags is not None:
        import capo_ec2.types.ipam_public_address_tags

        out["tags"] = capo_ec2.types.ipam_public_address_tags.deserialize_ec2_query(
            child_tags
        )
    child_network_border_group = el.find("networkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_security_groups = el.find("securityGroupSet")
    if child_security_groups is not None:
        import capo_ec2.types.ipam_public_address_security_group_list

        out["security_groups"] = (
            capo_ec2.types.ipam_public_address_security_group_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    child_sample_time = el.find("sampleTime")
    if child_sample_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["sample_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_sample_time
        )
    return out
