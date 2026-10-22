"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connector

GatewayConnectorList: TypeAlias = list[
    "capo_ecs.types.gateway_connector.GatewayConnector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorList) -> list:
    import capo_ecs.types.gateway_connector

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_connector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayConnectorList:
    import capo_ecs.types.gateway_connector

    out: GatewayConnectorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_connector.deserialize_aws_json_1_1(item))
    return out
