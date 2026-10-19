"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshotInList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.status


class ClusterSnapshotInList(TypedDict, closed=True):
    snapshot_name: "str"
    """<p>The name of the elastic cluster snapshot.</p>"""
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster snapshot.</p>"""
    snapshot_creation_time: "str"
    """<p>The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshotInList) -> dict:
    out: dict = {}
    out["snapshotName"] = value["snapshot_name"]
    out["snapshotArn"] = value["snapshot_arn"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    out["snapshotCreationTime"] = value["snapshot_creation_time"]
    return out


def deserialize_json(data: dict) -> ClusterSnapshotInList:
    out: ClusterSnapshotInList = {}  # type: ignore[typeddict-item]
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("snapshotArn") is not None:
        out["snapshot_arn"] = data["snapshotArn"]
    else:
        out["snapshot_arn"] = ""
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("snapshotCreationTime") is not None:
        out["snapshot_creation_time"] = data["snapshotCreationTime"]
    else:
        out["snapshot_creation_time"] = ""
    return out
