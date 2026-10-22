"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayClusterAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_cluster_association_summary

GatewayClusterAssociationSummaryList: TypeAlias = list[
    "capo_ecs.types.gateway_cluster_association_summary.GatewayClusterAssociationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayClusterAssociationSummaryList) -> list:
    import capo_ecs.types.gateway_cluster_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.gateway_cluster_association_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayClusterAssociationSummaryList:
    import capo_ecs.types.gateway_cluster_association_summary

    out: GatewayClusterAssociationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.gateway_cluster_association_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
