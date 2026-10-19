"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_partition_names
    import capo_sagemaker.types.cluster_slurm_node_type


class ClusterSlurmConfig(TypedDict, closed=True):
    node_type: "capo_sagemaker.types.cluster_slurm_node_type.ClusterSlurmNodeType"
    """<p>The type of Slurm node for the instance group. Valid values are <code>Controller</code>, <code>Worker</code>, and <code>Login</code>.</p>"""
    partition_names: NotRequired[
        "capo_sagemaker.types.cluster_partition_names.ClusterPartitionNames"
    ]
    """<p>The list of Slurm partition names that the instance group belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSlurmConfig) -> dict:
    out: dict = {}
    import capo_sagemaker.types.cluster_slurm_node_type

    out["NodeType"] = (
        capo_sagemaker.types.cluster_slurm_node_type.serialize_aws_json_1_1(
            value["node_type"]
        )
    )
    if "partition_names" in value:
        import capo_sagemaker.types.cluster_partition_names

        out["PartitionNames"] = (
            capo_sagemaker.types.cluster_partition_names.serialize_aws_json_1_1(
                value["partition_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSlurmConfig:
    out: ClusterSlurmConfig = {}  # type: ignore[typeddict-item]
    if data.get("NodeType") is not None:
        import capo_sagemaker.types.cluster_slurm_node_type

        out["node_type"] = (
            capo_sagemaker.types.cluster_slurm_node_type.deserialize_aws_json_1_1(
                data["NodeType"]
            )
        )
    else:
        import typing

        out["node_type"] = typing.cast(
            "capo_sagemaker.types.cluster_slurm_node_type.ClusterSlurmNodeType", ""
        )
    if data.get("PartitionNames") is not None:
        import capo_sagemaker.types.cluster_partition_names

        out["partition_names"] = (
            capo_sagemaker.types.cluster_partition_names.deserialize_aws_json_1_1(
                data["PartitionNames"]
            )
        )
    return out
