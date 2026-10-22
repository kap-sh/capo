"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayResourceFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_resource_failure

GatewayResourceFailureList: TypeAlias = list[
    "capo_ecs.types.gateway_resource_failure.GatewayResourceFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayResourceFailureList) -> list:
    import capo_ecs.types.gateway_resource_failure

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_resource_failure.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayResourceFailureList:
    import capo_ecs.types.gateway_resource_failure

    out: GatewayResourceFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_resource_failure.deserialize_aws_json_1_1(item)
        )
    return out
