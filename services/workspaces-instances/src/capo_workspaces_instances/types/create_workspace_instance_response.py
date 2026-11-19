"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateWorkspaceInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.workspace_instance_id


class CreateWorkspaceInstanceResponse(TypedDict, closed=True):
    workspace_instance_id: NotRequired[
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    ]
    """<p>Unique identifier assigned to the newly created WorkSpaces Instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkspaceInstanceResponse:
    out: CreateWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_cbor(data: dict) -> CreateWorkspaceInstanceResponse:
    out: CreateWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    return out
