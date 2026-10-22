"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteAlbResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_alb_resources

GatewayRouteAlbResourcesList: TypeAlias = list[
    "capo_ecs.types.gateway_route_alb_resources.GatewayRouteAlbResources"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteAlbResourcesList) -> list:
    import capo_ecs.types.gateway_route_alb_resources

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.gateway_route_alb_resources.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayRouteAlbResourcesList:
    import capo_ecs.types.gateway_route_alb_resources

    out: GatewayRouteAlbResourcesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_route_alb_resources.deserialize_aws_json_1_1(item)
        )
    return out
