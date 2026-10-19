"""Generated from Smithy shape ``com.amazonaws.sagemaker#NodeAdditionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_availability_zones
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_status
    import capo_sagemaker.types.cluster_instance_types
    import capo_sagemaker.types.cluster_node_logical_id


class NodeAdditionResult(TypedDict, closed=True):
    node_logical_id: "capo_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    """<p>A unique identifier assigned to the node that can be used to track its provisioning status through the <code>DescribeClusterNode</code> operation.</p>"""
    instance_group_name: (
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group to which the node was added.</p>"""
    status: "capo_sagemaker.types.cluster_instance_status.ClusterInstanceStatus"
    """<p>The current status of the node. Possible values include <code>Pending</code>, <code>Running</code>, <code>Failed</code>, <code>ShuttingDown</code>, <code>SystemUpdating</code>, <code>DeepHealthCheckInProgress</code>, and <code>NotFound</code>.</p>"""
    availability_zones: NotRequired[
        "capo_sagemaker.types.cluster_availability_zones.ClusterAvailabilityZones"
    ]
    """<p>The availability zones associated with the successfully added node.</p>"""
    instance_types: NotRequired[
        "capo_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types associated with the successfully added node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAdditionResult) -> dict:
    out: dict = {}
    out["NodeLogicalId"] = value["node_logical_id"]
    out["InstanceGroupName"] = value["instance_group_name"]
    import capo_sagemaker.types.cluster_instance_status

    out["Status"] = capo_sagemaker.types.cluster_instance_status.serialize_aws_json_1_1(
        value["status"]
    )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeAdditionResult:
    out: NodeAdditionResult = {}  # type: ignore[typeddict-item]
    if data.get("NodeLogicalId") is not None:
        out["node_logical_id"] = data["NodeLogicalId"]
    else:
        out["node_logical_id"] = ""
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        out["instance_group_name"] = ""
    if data.get("Status") is not None:
        import capo_sagemaker.types.cluster_instance_status

        out["status"] = (
            capo_sagemaker.types.cluster_instance_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_sagemaker.types.cluster_instance_status.ClusterInstanceStatus", ""
        )
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
    return out
