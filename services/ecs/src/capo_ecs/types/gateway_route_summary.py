"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_status
    import capo_ecs.types.string


class GatewayRouteSummary(TypedDict, closed=True):
    gateway_route_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway route.</p>"""
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service.</p>"""
    service_container_port_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The task definition container port name that the route targets on the service.</p>"""
    status: NotRequired["capo_ecs.types.gateway_route_status.GatewayRouteStatus"]
    """<p>The status of the gateway route.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteSummary) -> dict:
    out: dict = {}
    if "gateway_route_arn" in value:
        out["gatewayRouteArn"] = value["gateway_route_arn"]
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_container_port_name" in value:
        out["serviceContainerPortName"] = value["service_container_port_name"]
    if "status" in value:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayRouteSummary:
    out: GatewayRouteSummary = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRouteArn") is not None:
        out["gateway_route_arn"] = data["gatewayRouteArn"]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("serviceContainerPortName") is not None:
        out["service_container_port_name"] = data["serviceContainerPortName"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.deserialize_aws_json_1_1(
            data["status"]
        )
    return out
