"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNatGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allocation_id
    import capo_ec2.types.allocation_id_list
    import capo_ec2.types.availability_mode
    import capo_ec2.types.availability_zone_addresses
    import capo_ec2.types.boolean
    import capo_ec2.types.connectivity_type
    import capo_ec2.types.ip_list
    import capo_ec2.types.private_ip_address_count
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.vpc_id


class CreateNatGatewayRequest(TypedDict, closed=True):
    availability_mode: NotRequired["capo_ec2.types.availability_mode.AvailabilityMode"]
    """<p>Specifies whether to create a zonal (single-AZ) or regional (multi-AZ) NAT gateway. Defaults to <code>zonal</code>.</p> <p>A zonal NAT gateway is a NAT Gateway that provides redundancy and scalability within a single availability zone. A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html">Regional NAT gateways for automatic multi-AZ expansion</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    allocation_id: NotRequired["capo_ec2.types.allocation_id.AllocationId"]
    """<p>[Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot specify an Elastic IP address with a private NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p> <p>Constraint: Maximum 64 ASCII characters.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to create the NAT gateway.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC where you want to create a regional NAT gateway.</p>"""
    availability_zone_addresses: NotRequired[
        "capo_ec2.types.availability_zone_addresses.AvailabilityZoneAddresses"
    ]
    """<p>For regional NAT gateways only: Specifies which Availability Zones you want the NAT gateway to support and the Elastic IP addresses (EIPs) to use in each AZ. The regional NAT gateway uses these EIPs to handle outbound NAT traffic from their respective AZs. If not specified, the NAT gateway will automatically expand to new AZs and associate EIPs upon detection of an elastic network interface. If you specify this parameter, auto-expansion is disabled and you must manually manage AZ coverage.</p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html">Regional NAT gateways for automatic multi-AZ expansion</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the NAT gateway.</p>"""
    connectivity_type: NotRequired["capo_ec2.types.connectivity_type.ConnectivityType"]
    """<p>Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.</p>"""
    secondary_allocation_ids: NotRequired[
        "capo_ec2.types.allocation_id_list.AllocationIdList"
    ]
    """<p>Secondary EIP allocation IDs. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html">Create a NAT gateway</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    secondary_private_ip_addresses: NotRequired["capo_ec2.types.ip_list.IpList"]
    """<p>Secondary private IPv4 addresses. For more information about secondary addresses, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html">Create a NAT gateway</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    secondary_private_ip_address_count: NotRequired[
        "capo_ec2.types.private_ip_address_count.PrivateIpAddressCount"
    ]
    """<p>[Private NAT gateway only] The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html">Create a NAT gateway</a> in the <i>Amazon VPC User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNatGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_mode" in value:
        import capo_ec2.types.availability_mode

        capo_ec2.types.availability_mode.serialize_ec2_query(
            value["availability_mode"], pairs, f"{key_prefix}AvailabilityMode"
        )
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "availability_zone_addresses" in value:
        import capo_ec2.types.availability_zone_addresses

        capo_ec2.types.availability_zone_addresses.serialize_ec2_query(
            value["availability_zone_addresses"],
            pairs,
            f"{key_prefix}AvailabilityZoneAddress",
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "connectivity_type" in value:
        import capo_ec2.types.connectivity_type

        capo_ec2.types.connectivity_type.serialize_ec2_query(
            value["connectivity_type"], pairs, f"{key_prefix}ConnectivityType"
        )
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "secondary_allocation_ids" in value:
        import capo_ec2.types.allocation_id_list

        capo_ec2.types.allocation_id_list.serialize_ec2_query(
            value["secondary_allocation_ids"],
            pairs,
            f"{key_prefix}SecondaryAllocationId",
        )
    if "secondary_private_ip_addresses" in value:
        import capo_ec2.types.ip_list

        capo_ec2.types.ip_list.serialize_ec2_query(
            value["secondary_private_ip_addresses"],
            pairs,
            f"{key_prefix}SecondaryPrivateIpAddress",
        )
    if "secondary_private_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryPrivateIpAddressCount",
                str(value["secondary_private_ip_address_count"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CreateNatGatewayRequest:
    out: CreateNatGatewayRequest = {}  # type: ignore[typeddict-item]
    child_availability_mode = el.find("AvailabilityMode")
    if child_availability_mode is not None:
        import capo_ec2.types.availability_mode

        out["availability_mode"] = (
            capo_ec2.types.availability_mode.deserialize_ec2_query(
                child_availability_mode
            )
        )
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_availability_zone_addresses = el.find("AvailabilityZoneAddress")
    if child_availability_zone_addresses is not None:
        import capo_ec2.types.availability_zone_addresses

        out["availability_zone_addresses"] = (
            capo_ec2.types.availability_zone_addresses.deserialize_ec2_query(
                child_availability_zone_addresses
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
    child_connectivity_type = el.find("ConnectivityType")
    if child_connectivity_type is not None:
        import capo_ec2.types.connectivity_type

        out["connectivity_type"] = (
            capo_ec2.types.connectivity_type.deserialize_ec2_query(
                child_connectivity_type
            )
        )
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_secondary_allocation_ids = el.find("SecondaryAllocationId")
    if child_secondary_allocation_ids is not None:
        import capo_ec2.types.allocation_id_list

        out["secondary_allocation_ids"] = (
            capo_ec2.types.allocation_id_list.deserialize_ec2_query(
                child_secondary_allocation_ids
            )
        )
    child_secondary_private_ip_addresses = el.find("SecondaryPrivateIpAddress")
    if child_secondary_private_ip_addresses is not None:
        import capo_ec2.types.ip_list

        out["secondary_private_ip_addresses"] = (
            capo_ec2.types.ip_list.deserialize_ec2_query(
                child_secondary_private_ip_addresses
            )
        )
    child_secondary_private_ip_address_count = el.find("SecondaryPrivateIpAddressCount")
    if child_secondary_private_ip_address_count is not None:
        out["secondary_private_ip_address_count"] = int(
            child_secondary_private_ip_address_count.text or ""
        )
    return out
