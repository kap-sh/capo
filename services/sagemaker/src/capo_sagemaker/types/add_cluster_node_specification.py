"""Generated from Smithy shape ``com.amazonaws.sagemaker#AddClusterNodeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_add_increment_count
    import capo_sagemaker.types.cluster_availability_zones
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_types


class AddClusterNodeSpecification(TypedDict, closed=True):
    instance_group_name: (
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group to which you want to add nodes.</p>"""
    increment_target_count_by: (
        "capo_sagemaker.types.batch_add_increment_count.BatchAddIncrementCount"
    )
    """<p>The number of nodes to add to the specified instance group. The total number of nodes across all instance groups in a single request cannot exceed 50.</p>"""
    availability_zones: NotRequired[
        "capo_sagemaker.types.cluster_availability_zones.ClusterAvailabilityZones"
    ]
    """<p>The availability zones in which to add nodes. Use this to target node placement in specific availability zones within a flexible instance group.</p>"""
    instance_types: NotRequired[
        "capo_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types to use when adding nodes. Use this to target specific instance types within a flexible instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddClusterNodeSpecification) -> dict:
    out: dict = {}
    out["InstanceGroupName"] = value["instance_group_name"]
    out["IncrementTargetCountBy"] = value["increment_target_count_by"]
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


def deserialize_aws_json_1_1(data: dict) -> AddClusterNodeSpecification:
    out: AddClusterNodeSpecification = {}  # type: ignore[typeddict-item]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        out["instance_group_name"] = ""
    if data.get("IncrementTargetCountBy") is not None:
        out["increment_target_count_by"] = data["IncrementTargetCountBy"]
    else:
        out["increment_target_count_by"] = 0
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
