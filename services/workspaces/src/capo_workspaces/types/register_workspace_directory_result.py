"""Generated from Smithy shape ``com.amazonaws.workspaces#RegisterWorkspaceDirectoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.workspace_directory_state


class RegisterWorkspaceDirectoryResult(TypedDict, closed=True):
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    state: NotRequired[
        "capo_workspaces.types.workspace_directory_state.WorkspaceDirectoryState"
    ]
    """<p>The registration status of the WorkSpace directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWorkspaceDirectoryResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "state" in value:
        import capo_workspaces.types.workspace_directory_state

        out["State"] = (
            capo_workspaces.types.workspace_directory_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWorkspaceDirectoryResult:
    out: RegisterWorkspaceDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspace_directory_state

        out["state"] = (
            capo_workspaces.types.workspace_directory_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegisterWorkspaceDirectoryResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "state" in value:
        import capo_workspaces.types.workspace_directory_state

        out["State"] = capo_workspaces.types.workspace_directory_state.serialize_cbor(
            value["state"]
        )
    return out


def deserialize_cbor(data: dict) -> RegisterWorkspaceDirectoryResult:
    out: RegisterWorkspaceDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspace_directory_state

        out["state"] = capo_workspaces.types.workspace_directory_state.deserialize_cbor(
            data["State"]
        )
    return out
