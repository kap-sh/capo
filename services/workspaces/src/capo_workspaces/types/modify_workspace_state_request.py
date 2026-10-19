"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.target_workspace_state
    import capo_workspaces.types.workspace_id


class ModifyWorkspaceStateRequest(TypedDict, closed=True):
    workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    workspace_state: "capo_workspaces.types.target_workspace_state.TargetWorkspaceState"
    """<p>The WorkSpace state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceStateRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    import capo_workspaces.types.target_workspace_state

    out["WorkspaceState"] = (
        capo_workspaces.types.target_workspace_state.serialize_aws_json_1_1(
            value["workspace_state"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceStateRequest:
    out: ModifyWorkspaceStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("WorkspaceState") is not None:
        import capo_workspaces.types.target_workspace_state

        out["workspace_state"] = (
            capo_workspaces.types.target_workspace_state.deserialize_aws_json_1_1(
                data["WorkspaceState"]
            )
        )
    else:
        import typing

        out["workspace_state"] = typing.cast(
            "capo_workspaces.types.target_workspace_state.TargetWorkspaceState", ""
        )
    return out
