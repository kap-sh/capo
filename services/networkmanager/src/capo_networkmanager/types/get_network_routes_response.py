"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkRoutesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_network_function_group_identifier
    import capo_networkmanager.types.core_network_segment_edge_identifier
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.network_route_list
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.route_table_type


class GetNetworkRoutesResponse(TypedDict, closed=True):
    route_table_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the route table.</p>"""
    core_network_segment_edge: NotRequired[
        "capo_networkmanager.types.core_network_segment_edge_identifier.CoreNetworkSegmentEdgeIdentifier"
    ]
    """<p>Describes a core network segment edge.</p>"""
    core_network_network_function_group: NotRequired[
        "capo_networkmanager.types.core_network_network_function_group_identifier.CoreNetworkNetworkFunctionGroupIdentifier"
    ]
    """<p>Describes the network function group route table that the routes are from. This field is present only when you specify <code>CoreNetworkNetworkFunctionGroup</code> in <code>RouteTableIdentifier</code>.</p>"""
    route_table_type: NotRequired[
        "capo_networkmanager.types.route_table_type.RouteTableType"
    ]
    """<p>The route table type.</p>"""
    route_table_timestamp: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The route table creation time.</p>"""
    network_routes: NotRequired[
        "capo_networkmanager.types.network_route_list.NetworkRouteList"
    ]
    """<p>The network routes.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkRoutesResponse) -> dict:
    out: dict = {}
    if "route_table_arn" in value:
        out["RouteTableArn"] = value["route_table_arn"]
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
    if "route_table_type" in value:
        import capo_networkmanager.types.route_table_type

        out["RouteTableType"] = (
            capo_networkmanager.types.route_table_type.serialize_json(
                value["route_table_type"]
            )
        )
    if "route_table_timestamp" in value:
        import capo_networkmanager.types.date_time

        out["RouteTableTimestamp"] = capo_networkmanager.types.date_time.serialize_json(
            value["route_table_timestamp"]
        )
    if "network_routes" in value:
        import capo_networkmanager.types.network_route_list

        out["NetworkRoutes"] = (
            capo_networkmanager.types.network_route_list.serialize_json(
                value["network_routes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkRoutesResponse:
    out: GetNetworkRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("RouteTableArn") is not None:
        out["route_table_arn"] = data["RouteTableArn"]
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
    if data.get("RouteTableType") is not None:
        import capo_networkmanager.types.route_table_type

        out["route_table_type"] = (
            capo_networkmanager.types.route_table_type.deserialize_json(
                data["RouteTableType"]
            )
        )
    if data.get("RouteTableTimestamp") is not None:
        import capo_networkmanager.types.date_time

        out["route_table_timestamp"] = (
            capo_networkmanager.types.date_time.deserialize_json(
                data["RouteTableTimestamp"]
            )
        )
    if data.get("NetworkRoutes") is not None:
        import capo_networkmanager.types.network_route_list

        out["network_routes"] = (
            capo_networkmanager.types.network_route_list.deserialize_json(
                data["NetworkRoutes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
