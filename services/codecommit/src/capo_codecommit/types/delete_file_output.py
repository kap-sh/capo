"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteFileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id
    import capo_codecommit.types.path


class DeleteFileOutput(TypedDict, closed=True):
    commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full commit ID of the commit that contains the change that deletes the file.</p>"""
    blob_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The blob ID removed from the tree as part of deleting the file.</p>"""
    tree_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the delete file change.</p>"""
    file_path: "capo_codecommit.types.path.Path"
    """<p>The fully qualified path to the file to be deleted, including the full name and extension of that file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["blobId"] = value["blob_id"]
    out["treeId"] = value["tree_id"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileOutput:
    out: DeleteFileOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    return out
