"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_add_cluster_nodes_error_code
    import capo_sagemaker.types.batch_add_failure_count
    import capo_sagemaker.types.cluster_availability_zones
    import capo_sagemaker.types.cluster_instance_types
    import capo_sagemaker.types.instance_group_name
    import capo_sagemaker.types.string


class BatchAddClusterNodesError(TypedDict, closed=True):
    instance_group_name: "capo_sagemaker.types.instance_group_name.InstanceGroupName"
    """<p>The name of the instance group for which the error occurred.</p>"""
    error_code: "capo_sagemaker.types.batch_add_cluster_nodes_error_code.BatchAddClusterNodesErrorCode"
    """<p>The error code associated with the failure. Possible values include <code>InstanceGroupNotFound</code> and <code>InvalidInstanceGroupState</code>.</p>"""
    failed_count: "capo_sagemaker.types.batch_add_failure_count.BatchAddFailureCount"
    """<p>The number of nodes that failed to be added to the specified instance group.</p>"""
    availability_zones: NotRequired[
        "capo_sagemaker.types.cluster_availability_zones.ClusterAvailabilityZones"
    ]
    """<p>The availability zones associated with the failed node addition request.</p>"""
    instance_types: NotRequired[
        "capo_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types associated with the failed node addition request.</p>"""
    message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A descriptive message providing additional details about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAddClusterNodesError) -> dict:
    out: dict = {}
    out["InstanceGroupName"] = value["instance_group_name"]
    import capo_sagemaker.types.batch_add_cluster_nodes_error_code

    out["ErrorCode"] = (
        capo_sagemaker.types.batch_add_cluster_nodes_error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    )
    out["FailedCount"] = value["failed_count"]
    if "availability_zones" in value:
        import capo_sagemaker.types.cluster_availability_zones

        out["AvailabilityZones"] = (
            capo_sagemaker.types.cluster_availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "instance_types" in value:
        import capo_sagemaker.types.cluster_instance_types

        out["InstanceTypes"] = (
            capo_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["instance_types"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAddClusterNodesError:
    out: BatchAddClusterNodesError = {}  # type: ignore[typeddict-item]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        out["instance_group_name"] = ""
    if data.get("ErrorCode") is not None:
        import capo_sagemaker.types.batch_add_cluster_nodes_error_code

        out["error_code"] = (
            capo_sagemaker.types.batch_add_cluster_nodes_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_sagemaker.types.batch_add_cluster_nodes_error_code.BatchAddClusterNodesErrorCode",
            "",
        )
    if data.get("FailedCount") is not None:
        out["failed_count"] = data["FailedCount"]
    else:
        out["failed_count"] = 0
    if data.get("AvailabilityZones") is not None:
        import capo_sagemaker.types.cluster_availability_zones

        out["availability_zones"] = (
            capo_sagemaker.types.cluster_availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if data.get("InstanceTypes") is not None:
        import capo_sagemaker.types.cluster_instance_types

        out["instance_types"] = (
            capo_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["InstanceTypes"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
