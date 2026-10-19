"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id


class PutFileOutput(TypedDict, closed=True):
    commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full SHA ID of the commit that contains this file change.</p>"""
    blob_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The ID of the blob, which is its SHA-1 pointer.</p>"""
    tree_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full SHA-1 pointer of the tree information for the commit that contains this file change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["blobId"] = value["blob_id"]
    out["treeId"] = value["tree_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileOutput:
    out: PutFileOutput = {}  # type: ignore[typeddict-item]
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    else:
        out["commit_id"] = ""
    if data.get("blobId") is not None:
        out["blob_id"] = data["blobId"]
    else:
        out["blob_id"] = ""
    if data.get("treeId") is not None:
        out["tree_id"] = data["treeId"]
    else:
        out["tree_id"] = ""
    return out
