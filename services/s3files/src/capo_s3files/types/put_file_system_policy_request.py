"""Generated from Smithy shape ``com.amazonaws.s3files#PutFileSystemPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_system_id


class PutFileSystemPolicyRequest(TypedDict, closed=True):
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to apply the resource policy to.</p>"""
    policy: "str"
    """<p>The JSON-formatted resource policy to apply to the file system. The policy defines the permissions for accessing the file system. The policy must be a valid JSON document that follows IAM policy syntax.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFileSystemPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutFileSystemPolicyRequest:
    out: PutFileSystemPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
