"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectionAlbResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connection_alb_resources

GatewayConnectionAlbResourcesList: TypeAlias = list[
    "capo_ecs.types.gateway_connection_alb_resources.GatewayConnectionAlbResources"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectionAlbResourcesList) -> list:
    import capo_ecs.types.gateway_connection_alb_resources

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.gateway_connection_alb_resources.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayConnectionAlbResourcesList:
    import capo_ecs.types.gateway_connection_alb_resources

    out: GatewayConnectionAlbResourcesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_connection_alb_resources.deserialize_aws_json_1_1(
                item
            )
        )
    return out
