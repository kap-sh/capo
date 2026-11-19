"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationScalingDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_operation_scaling_details

ClusterOperationScalingDetailsList: TypeAlias = list[
    "capo_sagemaker.types.cluster_operation_scaling_details.ClusterOperationScalingDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationScalingDetailsList) -> list:
    import capo_sagemaker.types.cluster_operation_scaling_details

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cluster_operation_scaling_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterOperationScalingDetailsList:
    import capo_sagemaker.types.cluster_operation_scaling_details

    out: ClusterOperationScalingDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.cluster_operation_scaling_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
