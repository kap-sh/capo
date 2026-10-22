"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_status

GatewayRouteStatusList: TypeAlias = list[
    "capo_ecs.types.gateway_route_status.GatewayRouteStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteStatusList) -> list:
    import capo_ecs.types.gateway_route_status

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_route_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayRouteStatusList:
    import capo_ecs.types.gateway_route_status

    out: GatewayRouteStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_route_status.deserialize_aws_json_1_1(item))
    return out
