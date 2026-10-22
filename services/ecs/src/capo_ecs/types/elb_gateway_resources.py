"""Generated from Smithy shape ``com.amazonaws.ecs#ElbGatewayResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class ElbGatewayResources(TypedDict, closed=True):
    load_balancer_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    listener_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the listener on the load balancer.</p>"""
    security_group: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the security group attached to the load balancer.</p>"""
    gateway_route_arns: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The Amazon Resource Names (ARNs) of the gateway routes that use this load balancer for ingress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElbGatewayResources) -> dict:
    out: dict = {}
    if "load_balancer_arn" in value:
        out["loadBalancerArn"] = value["load_balancer_arn"]
    if "listener_arn" in value:
        out["listenerArn"] = value["listener_arn"]
    if "security_group" in value:
        out["securityGroup"] = value["security_group"]
    if "gateway_route_arns" in value:
        import capo_ecs.types.string_list

        out["gatewayRouteArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["gateway_route_arns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ElbGatewayResources:
    out: ElbGatewayResources = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancerArn") is not None:
        out["load_balancer_arn"] = data["loadBalancerArn"]
    if data.get("listenerArn") is not None:
        out["listener_arn"] = data["listenerArn"]
    if data.get("securityGroup") is not None:
        out["security_group"] = data["securityGroup"]
    if data.get("gatewayRouteArns") is not None:
        import capo_ecs.types.string_list

        out["gateway_route_arns"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["gatewayRouteArns"]
        )
    return out
