"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedCreateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.description
    import capo_workspaces.types.error_type
    import capo_workspaces.types.workspace_request


class FailedCreateWorkspaceRequest(TypedDict, closed=True):
    workspace_request: NotRequired[
        "capo_workspaces.types.workspace_request.WorkspaceRequest"
    ]
    """<p>Information about the WorkSpace.</p>"""
    error_code: NotRequired["capo_workspaces.types.error_type.ErrorType"]
    """<p>The error code that is returned if the WorkSpace cannot be created.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the WorkSpace cannot be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateWorkspaceRequest) -> dict:
    out: dict = {}
    if "workspace_request" in value:
        import capo_workspaces.types.workspace_request

        out["WorkspaceRequest"] = (
            capo_workspaces.types.workspace_request.serialize_aws_json_1_1(
                value["workspace_request"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedCreateWorkspaceRequest:
    out: FailedCreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceRequest") is not None:
        import capo_workspaces.types.workspace_request

        out["workspace_request"] = (
            capo_workspaces.types.workspace_request.deserialize_aws_json_1_1(
                data["WorkspaceRequest"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedCreateWorkspaceRequest) -> dict:
    out: dict = {}
    if "workspace_request" in value:
        import capo_workspaces.types.workspace_request

        out["WorkspaceRequest"] = (
            capo_workspaces.types.workspace_request.serialize_cbor(
                value["workspace_request"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> FailedCreateWorkspaceRequest:
    out: FailedCreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceRequest") is not None:
        import capo_workspaces.types.workspace_request

        out["workspace_request"] = (
            capo_workspaces.types.workspace_request.deserialize_cbor(
                data["WorkspaceRequest"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
