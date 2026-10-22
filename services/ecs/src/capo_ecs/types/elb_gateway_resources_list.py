"""Generated from Smithy shape ``com.amazonaws.ecs#ElbGatewayResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.elb_gateway_resources

ElbGatewayResourcesList: TypeAlias = list[
    "capo_ecs.types.elb_gateway_resources.ElbGatewayResources"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElbGatewayResourcesList) -> list:
    import capo_ecs.types.elb_gateway_resources

    out: list = []
    for item in value:
        out.append(capo_ecs.types.elb_gateway_resources.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ElbGatewayResourcesList:
    import capo_ecs.types.elb_gateway_resources

    out: ElbGatewayResourcesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.elb_gateway_resources.deserialize_aws_json_1_1(item))
    return out
