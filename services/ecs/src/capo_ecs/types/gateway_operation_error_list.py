"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayOperationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_operation_error

GatewayOperationErrorList: TypeAlias = list[
    "capo_ecs.types.gateway_operation_error.GatewayOperationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayOperationErrorList) -> list:
    import capo_ecs.types.gateway_operation_error

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_operation_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayOperationErrorList:
    import capo_ecs.types.gateway_operation_error

    out: GatewayOperationErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_operation_error.deserialize_aws_json_1_1(item)
        )
    return out
