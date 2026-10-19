"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class DeleteClusterRequest(TypedDict, closed=True):
    cluster_name: "capo_memorydb.types.string.String"
    """<p>The name of the cluster to be deleted</p>"""
    multi_region_cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-Region cluster to be deleted.</p>"""
    final_snapshot_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "final_snapshot_name" in value:
        out["FinalSnapshotName"] = value["final_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("FinalSnapshotName") is not None:
        out["final_snapshot_name"] = data["FinalSnapshotName"]
    return out
