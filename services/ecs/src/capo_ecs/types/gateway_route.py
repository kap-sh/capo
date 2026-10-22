"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_resources
    import capo_ecs.types.gateway_route_status
    import capo_ecs.types.string


class GatewayRoute(TypedDict, closed=True):
    gateway_route_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway route.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service associated with the route.</p>"""
    service_container_port_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The task definition container port name that the route targets on the service.</p>"""
    status: NotRequired["capo_ecs.types.gateway_route_status.GatewayRouteStatus"]
    """<p>The status of the gateway route.</p>"""
    service_url: NotRequired["capo_ecs.types.string.String"]
    """<p>The URL for accessing the service, including the <code>https://</code> scheme.</p>"""
    resources: NotRequired[
        "capo_ecs.types.gateway_route_resources.GatewayRouteResources"
    ]
    """<p>The service-specific infrastructure that the gateway manages for the route, keyed by gateway type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRoute) -> dict:
    out: dict = {}
    if "gateway_route_arn" in value:
        out["gatewayRouteArn"] = value["gateway_route_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "service_container_port_name" in value:
        out["serviceContainerPortName"] = value["service_container_port_name"]
    if "status" in value:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "service_url" in value:
        out["serviceUrl"] = value["service_url"]
    if "resources" in value:
        import capo_ecs.types.gateway_route_resources

        out["resources"] = (
            capo_ecs.types.gateway_route_resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayRoute:
    out: GatewayRoute = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRouteArn") is not None:
        out["gateway_route_arn"] = data["gatewayRouteArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("serviceContainerPortName") is not None:
        out["service_container_port_name"] = data["serviceContainerPortName"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("serviceUrl") is not None:
        out["service_url"] = data["serviceUrl"]
    if data.get("resources") is not None:
        import capo_ecs.types.gateway_route_resources

        out["resources"] = (
            capo_ecs.types.gateway_route_resources.deserialize_aws_json_1_1(
                data["resources"]
            )
        )
    return out
