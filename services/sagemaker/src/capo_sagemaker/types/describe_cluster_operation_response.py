"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_operation_id
    import capo_sagemaker.types.cluster_operation_scaling_details_list
    import capo_sagemaker.types.cluster_operation_status
    import capo_sagemaker.types.cluster_operation_type
    import capo_sagemaker.types.deep_health_check_configurations
    import capo_sagemaker.types.timestamp


class DescribeClusterOperationResponse(TypedDict, closed=True):
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
    scaling_details: NotRequired[
        "capo_sagemaker.types.cluster_operation_scaling_details_list.ClusterOperationScalingDetailsList"
    ]
    """<p>The per-instance-group scaling details for the operation. This field is populated when the operation <code>Type</code> is <code>Scaling</code>.</p>"""
    deep_health_check_details: NotRequired[
        "capo_sagemaker.types.deep_health_check_configurations.DeepHealthCheckConfigurations"
    ]
    """<p>The deep health check details for the operation. This field is populated when the operation <code>Type</code> is <code>DeepHealthCheck</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterOperationResponse) -> dict:
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
    if "scaling_details" in value:
        import capo_sagemaker.types.cluster_operation_scaling_details_list

        out["ScalingDetails"] = (
            capo_sagemaker.types.cluster_operation_scaling_details_list.serialize_aws_json_1_1(
                value["scaling_details"]
            )
        )
    if "deep_health_check_details" in value:
        import capo_sagemaker.types.deep_health_check_configurations

        out["DeepHealthCheckDetails"] = (
            capo_sagemaker.types.deep_health_check_configurations.serialize_aws_json_1_1(
                value["deep_health_check_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterOperationResponse:
    out: DescribeClusterOperationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("ScalingDetails") is not None:
        import capo_sagemaker.types.cluster_operation_scaling_details_list

        out["scaling_details"] = (
            capo_sagemaker.types.cluster_operation_scaling_details_list.deserialize_aws_json_1_1(
                data["ScalingDetails"]
            )
        )
    if data.get("DeepHealthCheckDetails") is not None:
        import capo_sagemaker.types.deep_health_check_configurations

        out["deep_health_check_details"] = (
            capo_sagemaker.types.deep_health_check_configurations.deserialize_aws_json_1_1(
                data["DeepHealthCheckDetails"]
            )
        )
    return out
