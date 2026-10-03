"""Generated from Smithy shape ``com.amazonaws.storagegateway#NFSFileShareDefaults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.permission_id
    import capo_storage_gateway.types.permission_mode


class NFSFileShareDefaults(TypedDict, closed=True):
    file_mode: NotRequired["capo_storage_gateway.types.permission_mode.PermissionMode"]
    """<p>The Unix file mode in the form "nnnn". For example, <code>0666</code> represents the default file mode inside the file share. The default value is <code>0666</code>.</p>"""
    directory_mode: NotRequired[
        "capo_storage_gateway.types.permission_mode.PermissionMode"
    ]
    """<p>The Unix directory mode in the form "nnnn". For example, <code>0666</code> represents the default access mode for all directories inside the file share. The default value is <code>0777</code>.</p>"""
    group_id: NotRequired["capo_storage_gateway.types.permission_id.PermissionId"]
    """<p>The default group ID for the file share (unless the files have another group ID specified). The default value is <code>nfsnobody</code>.</p>"""
    owner_id: NotRequired["capo_storage_gateway.types.permission_id.PermissionId"]
    """<p>The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is <code>nfsnobody</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NFSFileShareDefaults) -> dict:
    out: dict = {}
    if "file_mode" in value:
        out["FileMode"] = value["file_mode"]
    if "directory_mode" in value:
        out["DirectoryMode"] = value["directory_mode"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NFSFileShareDefaults:
    out: NFSFileShareDefaults = {}  # type: ignore[typeddict-item]
    if data.get("FileMode") is not None:
        out["file_mode"] = data["FileMode"]
    if data.get("DirectoryMode") is not None:
        out["directory_mode"] = data["DirectoryMode"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    return out
