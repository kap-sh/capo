"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationScalingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_operation_scaling_configuration
    import capo_sagemaker.types.cluster_operation_status


class ClusterOperationScalingDetails(TypedDict, closed=True):
    instance_group_name: NotRequired["str"]
    """<p>The name of the instance group being scaled.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.cluster_operation_status.ClusterOperationStatus"
    ]
    """<p>The status of the scaling operation for this instance group. Valid values are <code>InProgress</code>, <code>Superseded</code>, or <code>Done</code>.</p>"""
    original: NotRequired[
        "capo_sagemaker.types.cluster_operation_scaling_configuration.ClusterOperationScalingConfiguration"
    ]
    """<p>The scaling configuration of the instance group before the scaling operation was applied, including its current, target, and minimum instance counts.</p>"""
    desired: NotRequired[
        "capo_sagemaker.types.cluster_operation_scaling_configuration.ClusterOperationScalingConfiguration"
    ]
    """<p>The desired scaling configuration of the instance group for the scaling operation, including its target and minimum instance counts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationScalingDetails) -> dict:
    out: dict = {}
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "status" in value:
        import capo_sagemaker.types.cluster_operation_status

        out["Status"] = (
            capo_sagemaker.types.cluster_operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "original" in value:
        import capo_sagemaker.types.cluster_operation_scaling_configuration

        out["Original"] = (
            capo_sagemaker.types.cluster_operation_scaling_configuration.serialize_aws_json_1_1(
                value["original"]
            )
        )
    if "desired" in value:
        import capo_sagemaker.types.cluster_operation_scaling_configuration

        out["Desired"] = (
            capo_sagemaker.types.cluster_operation_scaling_configuration.serialize_aws_json_1_1(
                value["desired"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOperationScalingDetails:
    out: ClusterOperationScalingDetails = {}  # type: ignore[typeddict-item]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.cluster_operation_status

        out["status"] = (
            capo_sagemaker.types.cluster_operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Original") is not None:
        import capo_sagemaker.types.cluster_operation_scaling_configuration

        out["original"] = (
            capo_sagemaker.types.cluster_operation_scaling_configuration.deserialize_aws_json_1_1(
                data["Original"]
            )
        )
    if data.get("Desired") is not None:
        import capo_sagemaker.types.cluster_operation_scaling_configuration

        out["desired"] = (
            capo_sagemaker.types.cluster_operation_scaling_configuration.deserialize_aws_json_1_1(
                data["Desired"]
            )
        )
    return out
