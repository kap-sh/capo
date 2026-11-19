"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_operation_id
    import capo_sagemaker.types.cluster_operation_status
    import capo_sagemaker.types.cluster_operation_type
    import capo_sagemaker.types.timestamp


class ClusterOperationSummary(TypedDict, closed=True):
    operation_id: NotRequired[
        "capo_sagemaker.types.cluster_operation_id.ClusterOperationId"
    ]
    """<p>The unique identifier (UUID) of the operation.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the HyperPod cluster associated with the operation.</p>"""
    type: NotRequired[
        "capo_sagemaker.types.cluster_operation_type.ClusterOperationType"
    ]
    """<p>The type of the operation. Valid values are <code>Scaling</code> or <code>DeepHealthCheck</code>.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.cluster_operation_status.ClusterOperationStatus"
    ]
    """<p>The current status of the operation. Valid values are <code>InProgress</code>, <code>Superseded</code>, or <code>Done</code>.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the operation was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationSummary) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "type" in value:
        import capo_sagemaker.types.cluster_operation_type

        out["Type"] = (
            capo_sagemaker.types.cluster_operation_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.cluster_operation_status

        out["Status"] = (
            capo_sagemaker.types.cluster_operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOperationSummary:
    out: ClusterOperationSummary = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("Type") is not None:
        import capo_sagemaker.types.cluster_operation_type

        out["type"] = (
            capo_sagemaker.types.cluster_operation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.cluster_operation_status

        out["status"] = (
            capo_sagemaker.types.cluster_operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
