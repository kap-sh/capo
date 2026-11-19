"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallMissingExpectedRTViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id
    import capo_fms.types.violation_target


class NetworkFirewallMissingExpectedRTViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the Network Firewall or VPC resource that's in violation.</p>"""
    vpc: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the VPC associated with a violating subnet.</p>"""
    availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of a violating subnet. </p>"""
    current_route_table: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the current route table that's associated with the subnet, if one is available.</p>"""
    expected_route_table: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the route table that should be associated with the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallMissingExpectedRTViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "vpc" in value:
        out["VPC"] = value["vpc"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "current_route_table" in value:
        out["CurrentRouteTable"] = value["current_route_table"]
    if "expected_route_table" in value:
        out["ExpectedRouteTable"] = value["expected_route_table"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallMissingExpectedRTViolation:
    out: NetworkFirewallMissingExpectedRTViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("VPC") is not None:
        out["vpc"] = data["VPC"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("CurrentRouteTable") is not None:
        out["current_route_table"] = data["CurrentRouteTable"]
    if data.get("ExpectedRouteTable") is not None:
        out["expected_route_table"] = data["ExpectedRouteTable"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallMissingExpectedRTViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "vpc" in value:
        out["VPC"] = value["vpc"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "current_route_table" in value:
        out["CurrentRouteTable"] = value["current_route_table"]
    if "expected_route_table" in value:
        out["ExpectedRouteTable"] = value["expected_route_table"]
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallMissingExpectedRTViolation:
    out: NetworkFirewallMissingExpectedRTViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("VPC") is not None:
        out["vpc"] = data["VPC"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("CurrentRouteTable") is not None:
        out["current_route_table"] = data["CurrentRouteTable"]
    if data.get("ExpectedRouteTable") is not None:
        out["expected_route_table"] = data["ExpectedRouteTable"]
    return out
