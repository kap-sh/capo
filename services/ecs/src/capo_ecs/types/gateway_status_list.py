"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_status

GatewayStatusList: TypeAlias = list["capo_ecs.types.gateway_status.GatewayStatus"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayStatusList) -> list:
    import capo_ecs.types.gateway_status

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayStatusList:
    import capo_ecs.types.gateway_status

    out: GatewayStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_status.deserialize_aws_json_1_1(item))
    return out
