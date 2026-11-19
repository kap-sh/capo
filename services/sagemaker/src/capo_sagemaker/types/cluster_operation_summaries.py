"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_operation_summary

ClusterOperationSummaries: TypeAlias = list[
    "capo_sagemaker.types.cluster_operation_summary.ClusterOperationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationSummaries) -> list:
    import capo_sagemaker.types.cluster_operation_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_operation_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterOperationSummaries:
    import capo_sagemaker.types.cluster_operation_summary

    out: ClusterOperationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.cluster_operation_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
