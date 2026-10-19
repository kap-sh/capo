"""Generated from Smithy shape ``com.amazonaws.s3files#GetFileSystemPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_system_id


class GetFileSystemPolicyResponse(TypedDict, closed=True):
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the file system.</p>"""
    policy: "str"
    """<p>The JSON-formatted resource policy for the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFileSystemPolicyResponse) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetFileSystemPolicyResponse:
    out: GetFileSystemPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
