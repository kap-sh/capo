"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connection

GatewayConnectionList: TypeAlias = list[
    "capo_ecs.types.gateway_connection.GatewayConnection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectionList) -> list:
    import capo_ecs.types.gateway_connection

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_connection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayConnectionList:
    import capo_ecs.types.gateway_connection

    out: GatewayConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_connection.deserialize_aws_json_1_1(item))
    return out
