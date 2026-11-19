"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallBlackHoleRouteDetectedViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.resource_id
    import capo_fms.types.routes
    import capo_fms.types.violation_target


class NetworkFirewallBlackHoleRouteDetectedViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The subnet that has an inactive state.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the route table ID.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""
    violating_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>Information about the route or routes that are in violation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallBlackHoleRouteDetectedViolation,
) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallBlackHoleRouteDetectedViolation:
    out: NetworkFirewallBlackHoleRouteDetectedViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallBlackHoleRouteDetectedViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["violating_routes"]
        )
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallBlackHoleRouteDetectedViolation:
    out: NetworkFirewallBlackHoleRouteDetectedViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["ViolatingRoutes"]
        )
    return out
