"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.workspace_name
    import capo_iotsitewise.types.workspace_status


class CreateWorkspaceResponse(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    workspace_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the workspace.</p>"""
    workspace_status: "capo_iotsitewise.types.workspace_status.WorkspaceStatus"
    """<p>The status of the workspace, which is <code>CREATING</code> when the operation returns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    out["workspaceArn"] = value["workspace_arn"]
    import capo_iotsitewise.types.workspace_status

    out["workspaceStatus"] = capo_iotsitewise.types.workspace_status.serialize_json(
        value["workspace_status"]
    )
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("workspaceArn") is not None:
        out["workspace_arn"] = data["workspaceArn"]
    else:
        out["workspace_arn"] = ""
    if data.get("workspaceStatus") is not None:
        import capo_iotsitewise.types.workspace_status

        out["workspace_status"] = (
            capo_iotsitewise.types.workspace_status.deserialize_json(
                data["workspaceStatus"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspaceResponse.workspace_status required")
    return out
