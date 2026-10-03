"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteTableIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_network_function_group_identifier
    import capo_networkmanager.types.core_network_segment_edge_identifier
    import capo_networkmanager.types.transit_gateway_route_table_arn


class RouteTableIdentifier(TypedDict, closed=True):
    transit_gateway_route_table_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn"
    ]
    """<p>The ARN of the transit gateway route table for the attachment request. For example, <code>"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"</code>.</p>"""
    core_network_segment_edge: NotRequired[
        "capo_networkmanager.types.core_network_segment_edge_identifier.CoreNetworkSegmentEdgeIdentifier"
    ]
    """<p>The segment edge in a core network.</p>"""
    core_network_network_function_group: NotRequired[
        "capo_networkmanager.types.core_network_network_function_group_identifier.CoreNetworkNetworkFunctionGroupIdentifier"
    ]
    """<p>The route table identifier associated with the network function group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTableIdentifier) -> dict:
    out: dict = {}
    if "transit_gateway_route_table_arn" in value:
        out["TransitGatewayRouteTableArn"] = value["transit_gateway_route_table_arn"]
    if "core_network_segment_edge" in value:
        import capo_networkmanager.types.core_network_segment_edge_identifier

        out["CoreNetworkSegmentEdge"] = (
            capo_networkmanager.types.core_network_segment_edge_identifier.serialize_json(
                value["core_network_segment_edge"]
            )
        )
    if "core_network_network_function_group" in value:
        import capo_networkmanager.types.core_network_network_function_group_identifier

        out["CoreNetworkNetworkFunctionGroup"] = (
            capo_networkmanager.types.core_network_network_function_group_identifier.serialize_json(
                value["core_network_network_function_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTableIdentifier:
    out: RouteTableIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayRouteTableArn") is not None:
        out["transit_gateway_route_table_arn"] = data["TransitGatewayRouteTableArn"]
    if data.get("CoreNetworkSegmentEdge") is not None:
        import capo_networkmanager.types.core_network_segment_edge_identifier

        out["core_network_segment_edge"] = (
            capo_networkmanager.types.core_network_segment_edge_identifier.deserialize_json(
                data["CoreNetworkSegmentEdge"]
            )
        )
    if data.get("CoreNetworkNetworkFunctionGroup") is not None:
        import capo_networkmanager.types.core_network_network_function_group_identifier

        out["core_network_network_function_group"] = (
            capo_networkmanager.types.core_network_network_function_group_identifier.deserialize_json(
                data["CoreNetworkNetworkFunctionGroup"]
            )
        )
    return out
