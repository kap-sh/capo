"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.workspace_id


class CreateWorkspaceResponse(TypedDict, closed=True):
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    workspace_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    out["WorkspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("WorkspaceArn") is not None:
        out["workspace_arn"] = data["WorkspaceArn"]
    else:
        out["workspace_arn"] = ""
    return out
