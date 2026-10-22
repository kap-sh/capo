"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.access_type
    import capo_ecs.types.gateway_connection_resources
    import capo_ecs.types.gateway_route_status
    import capo_ecs.types.string


class GatewayConnection(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    gateway_route_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway route for the connection.</p>"""
    port_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the service port that receives gateway-managed ingress traffic.</p>"""
    service_url: NotRequired["capo_ecs.types.string.String"]
    """<p>The URL that the gateway uses to route ingress traffic to the service.</p>"""
    access_type: NotRequired["capo_ecs.types.access_type.AccessType"]
    """<p>The access type of the gateway ingress path.</p> <p>Valid values:</p> <ul> <li> <p> <code>PUBLIC</code> - The ingress path is publicly accessible.</p> </li> <li> <p> <code>PRIVATE</code> - The ingress path is only accessible privately.</p> </li> </ul>"""
    status: NotRequired["capo_ecs.types.gateway_route_status.GatewayRouteStatus"]
    """<p>The status of the gateway route for the connection.</p>"""
    resources: NotRequired[
        "capo_ecs.types.gateway_connection_resources.GatewayConnectionResources"
    ]
    """<p>The gateway-managed infrastructure resources for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnection) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "gateway_route_arn" in value:
        out["gatewayRouteArn"] = value["gateway_route_arn"]
    if "port_name" in value:
        out["portName"] = value["port_name"]
    if "service_url" in value:
        out["serviceUrl"] = value["service_url"]
    if "access_type" in value:
        import capo_ecs.types.access_type

        out["accessType"] = capo_ecs.types.access_type.serialize_aws_json_1_1(
            value["access_type"]
        )
    if "status" in value:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "resources" in value:
        import capo_ecs.types.gateway_connection_resources

        out["resources"] = (
            capo_ecs.types.gateway_connection_resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnection:
    out: GatewayConnection = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("gatewayRouteArn") is not None:
        out["gateway_route_arn"] = data["gatewayRouteArn"]
    if data.get("portName") is not None:
        out["port_name"] = data["portName"]
    if data.get("serviceUrl") is not None:
        out["service_url"] = data["serviceUrl"]
    if data.get("accessType") is not None:
        import capo_ecs.types.access_type

        out["access_type"] = capo_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    if data.get("status") is not None:
        import capo_ecs.types.gateway_route_status

        out["status"] = capo_ecs.types.gateway_route_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("resources") is not None:
        import capo_ecs.types.gateway_connection_resources

        out["resources"] = (
            capo_ecs.types.gateway_connection_resources.deserialize_aws_json_1_1(
                data["resources"]
            )
        )
    return out
