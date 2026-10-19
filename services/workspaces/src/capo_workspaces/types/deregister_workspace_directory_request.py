"""Generated from Smithy shape ``com.amazonaws.workspaces#DeregisterWorkspaceDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id


class DeregisterWorkspaceDirectoryRequest(TypedDict, closed=True):
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory. If any WorkSpaces are registered to this directory, you must remove them before you deregister the directory, or you will receive an OperationNotSupportedException error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterWorkspaceDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterWorkspaceDirectoryRequest:
    out: DeregisterWorkspaceDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    return out
