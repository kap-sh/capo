"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewayRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_route_status_list
    import capo_ecs.types.string


class ListGatewayRoutesRequest(TypedDict, closed=True):
    gateway: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>"""
    service: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of a service to filter the results by. Because services can span clusters, a service name isn't necessarily unique and can match multiple services.</p>"""
    service_container_port_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of a task definition container port to filter the results by.</p>"""
    status: NotRequired[
        "capo_ecs.types.gateway_route_status_list.GatewayRouteStatusList"
    ]
    """<p>The gateway route status to filter the results by.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of results that the operation returns in a single page. The default is 100.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewayRoutesRequest) -> dict:
    out: dict = {}
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "service" in value:
        out["service"] = value["service"]
    if "service_container_port_name" in value:
        out["serviceContainerPortName"] = value["service_container_port_name"]
    if "status" in value:
        import capo_ecs.types.gateway_route_status_list

        out["status"] = capo_ecs.types.gateway_route_status_list.serialize_aws_json_1_1(
            value["status"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewayRoutesRequest:
    out: ListGatewayRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("serviceContainerPortName") is not None:
        out["service_container_port_name"] = data["serviceContainerPortName"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_route_status_list

        out["status"] = (
            capo_ecs.types.gateway_route_status_list.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
