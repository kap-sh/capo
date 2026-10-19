"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id
    import capo_codecommit.types.repository_name


class GetBlobInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the blob.</p>"""
    blob_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The ID of the blob, which is its SHA-1 pointer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["blobId"] = value["blob_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobInput:
    out: GetBlobInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("blobId") is not None:
        out["blob_id"] = data["blobId"]
    else:
        out["blob_id"] = ""
    return out
