"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayClusterAssociationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_cluster_association_status

GatewayClusterAssociationStatusList: TypeAlias = list[
    "capo_ecs.types.gateway_cluster_association_status.GatewayClusterAssociationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayClusterAssociationStatusList) -> list:
    import capo_ecs.types.gateway_cluster_association_status

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.gateway_cluster_association_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayClusterAssociationStatusList:
    import capo_ecs.types.gateway_cluster_association_status

    out: GatewayClusterAssociationStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_cluster_association_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
