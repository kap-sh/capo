"""Generated from Smithy shape ``com.amazonaws.fms#FirewallSubnetIsOutOfScopeViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id


class FirewallSubnetIsOutOfScopeViolation(TypedDict, closed=True):
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the firewall subnet that violates the policy scope.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The VPC ID of the firewall subnet that violates the policy scope.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of the firewall subnet that violates the policy scope.</p>"""
    subnet_availability_zone_id: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone ID of the firewall subnet that violates the policy scope.</p>"""
    vpc_endpoint_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The VPC endpoint ID of the firewall subnet that violates the policy scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallSubnetIsOutOfScopeViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallSubnetIsOutOfScopeViolation:
    out: FirewallSubnetIsOutOfScopeViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallSubnetIsOutOfScopeViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_cbor(data: dict) -> FirewallSubnetIsOutOfScopeViolation:
    out: FirewallSubnetIsOutOfScopeViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("SubnetAvailabilityZoneId") is not None:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
