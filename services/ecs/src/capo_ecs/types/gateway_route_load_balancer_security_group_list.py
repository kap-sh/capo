"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteLoadBalancerSecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_load_balancer_security_group

GatewayRouteLoadBalancerSecurityGroupList: TypeAlias = list[
    "capo_ecs.types.gateway_route_load_balancer_security_group.GatewayRouteLoadBalancerSecurityGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteLoadBalancerSecurityGroupList) -> list:
    import capo_ecs.types.gateway_route_load_balancer_security_group

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.gateway_route_load_balancer_security_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayRouteLoadBalancerSecurityGroupList:
    import capo_ecs.types.gateway_route_load_balancer_security_group

    out: GatewayRouteLoadBalancerSecurityGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_route_load_balancer_security_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
