"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallMissingExpectedRoutesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.expected_routes
    import capo_fms.types.resource_id
    import capo_fms.types.violation_target


class NetworkFirewallMissingExpectedRoutesViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The target of the violation.</p>"""
    expected_routes: NotRequired["capo_fms.types.expected_routes.ExpectedRoutes"]
    """<p>The expected routes.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallMissingExpectedRoutesViolation,
) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "expected_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedRoutes"] = capo_fms.types.expected_routes.serialize_aws_json_1_1(
            value["expected_routes"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallMissingExpectedRoutesViolation:
    out: NetworkFirewallMissingExpectedRoutesViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ExpectedRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_routes"] = (
            capo_fms.types.expected_routes.deserialize_aws_json_1_1(
                data["ExpectedRoutes"]
            )
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallMissingExpectedRoutesViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "expected_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedRoutes"] = capo_fms.types.expected_routes.serialize_cbor(
            value["expected_routes"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallMissingExpectedRoutesViolation:
    out: NetworkFirewallMissingExpectedRoutesViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ExpectedRoutes") is not None:
        import capo_fms.types.expected_routes

        out["expected_routes"] = capo_fms.types.expected_routes.deserialize_cbor(
            data["ExpectedRoutes"]
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out
