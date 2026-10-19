"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CreateClusterSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.tag_map


class CreateClusterSnapshotInput(TypedDict, closed=True):
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster of which you want to create a snapshot.</p>"""
    snapshot_name: "str"
    """<p>The name of the new elastic cluster snapshot.</p>"""
    tags: NotRequired["capo_docdb_elastic.types.tag_map.TagMap"]
    """<p>The tags to be assigned to the new elastic cluster snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterSnapshotInput) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    out["snapshotName"] = value["snapshot_name"]
    if "tags" in value:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateClusterSnapshotInput:
    out: CreateClusterSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("tags") is not None:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    return out
