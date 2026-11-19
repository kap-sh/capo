"""Generated from Smithy shape ``com.amazonaws.fms#FirewallSubnetMissingVPCEndpointViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id


class FirewallSubnetMissingVPCEndpointViolation(TypedDict, closed=True):
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the firewall that this VPC endpoint is associated with.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the VPC associated with the deleted VPC subnet.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The name of the Availability Zone of the deleted VPC subnet.</p>"""
    subnet_availability_zone_id: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The ID of the Availability Zone of the deleted VPC subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallSubnetMissingVPCEndpointViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallSubnetMissingVPCEndpointViolation:
    out: FirewallSubnetMissingVPCEndpointViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallSubnetMissingVPCEndpointViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    return out


def deserialize_cbor(data: dict) -> FirewallSubnetMissingVPCEndpointViolation:
    out: FirewallSubnetMissingVPCEndpointViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    return out
