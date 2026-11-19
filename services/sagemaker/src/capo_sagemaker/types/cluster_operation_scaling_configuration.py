"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterOperationScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_operation_count


class ClusterOperationScalingConfiguration(TypedDict, closed=True):
    current_count: NotRequired[
        "capo_sagemaker.types.cluster_operation_count.ClusterOperationCount"
    ]
    """<p>The number of instances that were in the instance group at the time of the operation.</p>"""
    target_count: NotRequired[
        "capo_sagemaker.types.cluster_operation_count.ClusterOperationCount"
    ]
    """<p>The target number of instances for the instance group.</p>"""
    min_count: NotRequired[
        "capo_sagemaker.types.cluster_operation_count.ClusterOperationCount"
    ]
    """<p>The minimum number of instances that must be available in the instance group of a HyperPod cluster before it transitions to <code>InService</code> status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterOperationScalingConfiguration) -> dict:
    out: dict = {}
    if "current_count" in value:
        out["CurrentCount"] = value["current_count"]
    if "target_count" in value:
        out["TargetCount"] = value["target_count"]
    if "min_count" in value:
        out["MinCount"] = value["min_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterOperationScalingConfiguration:
    out: ClusterOperationScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CurrentCount") is not None:
        out["current_count"] = data["CurrentCount"]
    if data.get("TargetCount") is not None:
        out["target_count"] = data["TargetCount"]
    if data.get("MinCount") is not None:
        out["min_count"] = data["MinCount"]
    return out
