"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewayRoutesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_summary_list
    import capo_ecs.types.string


class ListGatewayRoutesResponse(TypedDict, closed=True):
    gateway_routes: NotRequired[
        "capo_ecs.types.gateway_route_summary_list.GatewayRouteSummaryList"
    ]
    """<p>The gateway routes that match the request.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future request to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewayRoutesResponse) -> dict:
    out: dict = {}
    if "gateway_routes" in value:
        import capo_ecs.types.gateway_route_summary_list

        out["gatewayRoutes"] = (
            capo_ecs.types.gateway_route_summary_list.serialize_aws_json_1_1(
                value["gateway_routes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewayRoutesResponse:
    out: ListGatewayRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRoutes") is not None:
        import capo_ecs.types.gateway_route_summary_list

        out["gateway_routes"] = (
            capo_ecs.types.gateway_route_summary_list.deserialize_aws_json_1_1(
                data["gatewayRoutes"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
