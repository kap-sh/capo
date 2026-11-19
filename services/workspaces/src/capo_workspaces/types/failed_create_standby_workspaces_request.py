"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedCreateStandbyWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.description
    import capo_workspaces.types.standby_workspace
    import capo_workspaces.types.workspace_error_code


class FailedCreateStandbyWorkspacesRequest(TypedDict, closed=True):
    standby_workspace_request: NotRequired[
        "capo_workspaces.types.standby_workspace.StandbyWorkspace"
    ]
    """<p>Information about the standby WorkSpace that could not be created.</p>"""
    error_code: NotRequired[
        "capo_workspaces.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code that is returned if the standby WorkSpace could not be created.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the standby WorkSpace could not be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    if "standby_workspace_request" in value:
        import capo_workspaces.types.standby_workspace

        out["StandbyWorkspaceRequest"] = (
            capo_workspaces.types.standby_workspace.serialize_aws_json_1_1(
                value["standby_workspace_request"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedCreateStandbyWorkspacesRequest:
    out: FailedCreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("StandbyWorkspaceRequest") is not None:
        import capo_workspaces.types.standby_workspace

        out["standby_workspace_request"] = (
            capo_workspaces.types.standby_workspace.deserialize_aws_json_1_1(
                data["StandbyWorkspaceRequest"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedCreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    if "standby_workspace_request" in value:
        import capo_workspaces.types.standby_workspace

        out["StandbyWorkspaceRequest"] = (
            capo_workspaces.types.standby_workspace.serialize_cbor(
                value["standby_workspace_request"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> FailedCreateStandbyWorkspacesRequest:
    out: FailedCreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("StandbyWorkspaceRequest") is not None:
        import capo_workspaces.types.standby_workspace

        out["standby_workspace_request"] = (
            capo_workspaces.types.standby_workspace.deserialize_cbor(
                data["StandbyWorkspaceRequest"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
