"""Generated from Smithy shape ``com.amazonaws.workspaces#PendingCreateStandbyWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.user_name
    import capo_workspaces.types.workspace_id
    import capo_workspaces.types.workspace_state


class PendingCreateStandbyWorkspacesRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_workspaces.types.user_name.UserName"]
    """<p>Describes the standby WorkSpace that was created.</p> <p>Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html"> DescribeWorkspaces</a> before the WorkSpace is created, the information returned can be incomplete. </p>"""
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory for the standby WorkSpace.</p>"""
    state: NotRequired["capo_workspaces.types.workspace_state.WorkspaceState"]
    """<p>The operational state of the standby WorkSpace.</p>"""
    workspace_id: NotRequired["capo_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the standby WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingCreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "state" in value:
        import capo_workspaces.types.workspace_state

        out["State"] = capo_workspaces.types.workspace_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingCreateStandbyWorkspacesRequest:
    out: PendingCreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("State") is not None:
        import capo_workspaces.types.workspace_state

        out["state"] = capo_workspaces.types.workspace_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    return out
