"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudAutonomousVmClustersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_autonomous_vm_cluster_list


class ListCloudAutonomousVmClustersOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The pagination token to continue listing from.</p>"""
    cloud_autonomous_vm_clusters: (
        "capo_odb.types.cloud_autonomous_vm_cluster_list.CloudAutonomousVmClusterList"
    )
    """<p>The list of Autonomous VM clusters in the specified Cloud Exadata Infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudAutonomousVmClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.cloud_autonomous_vm_cluster_list

    out["cloudAutonomousVmClusters"] = (
        capo_odb.types.cloud_autonomous_vm_cluster_list.serialize_aws_json_1_0(
            value["cloud_autonomous_vm_clusters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudAutonomousVmClustersOutput:
    out: ListCloudAutonomousVmClustersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudAutonomousVmClusters") is not None:
        import capo_odb.types.cloud_autonomous_vm_cluster_list

        out["cloud_autonomous_vm_clusters"] = (
            capo_odb.types.cloud_autonomous_vm_cluster_list.deserialize_aws_json_1_0(
                data["cloudAutonomousVmClusters"]
            )
        )
    else:
        out["cloud_autonomous_vm_clusters"] = []
    return out
