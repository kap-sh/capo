"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_operation_id


class DescribeClusterOperationRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the HyperPod cluster associated with the operation.</p>"""
    operation_id: NotRequired[
        "capo_sagemaker.types.cluster_operation_id.ClusterOperationId"
    ]
    """<p>The unique identifier (UUID) of the operation to describe. This ID can be obtained from the <code>ListClusterOperations</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterOperationRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterOperationRequest:
    out: DescribeClusterOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    return out
