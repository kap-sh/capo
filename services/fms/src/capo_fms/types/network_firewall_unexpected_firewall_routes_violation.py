"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallUnexpectedFirewallRoutesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.resource_id
    import capo_fms.types.routes


class NetworkFirewallUnexpectedFirewallRoutesViolation(TypedDict, closed=True):
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The subnet ID for the firewall.</p>"""
    violating_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The routes that are in violation.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the route table.</p>"""
    firewall_endpoint: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The endpoint of the firewall.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallUnexpectedFirewallRoutesViolation,
) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "firewall_endpoint" in value:
        out["FirewallEndpoint"] = value["firewall_endpoint"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallUnexpectedFirewallRoutesViolation:
    out: NetworkFirewallUnexpectedFirewallRoutesViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("FirewallEndpoint") is not None:
        out["firewall_endpoint"] = data["FirewallEndpoint"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallUnexpectedFirewallRoutesViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_cbor(
            value["violating_routes"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "firewall_endpoint" in value:
        out["FirewallEndpoint"] = value["firewall_endpoint"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallUnexpectedFirewallRoutesViolation:
    out: NetworkFirewallUnexpectedFirewallRoutesViolation = {}  # type: ignore[typeddict-item]
    if data.get("FirewallSubnetId") is not None:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if data.get("ViolatingRoutes") is not None:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_cbor(
            data["ViolatingRoutes"]
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    if data.get("FirewallEndpoint") is not None:
        out["firewall_endpoint"] = data["FirewallEndpoint"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out
