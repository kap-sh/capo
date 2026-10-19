"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateWorkspaceApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_application_id
    import capo_workspaces.types.workspace_id


class DisassociateWorkspaceApplicationRequest(TypedDict, closed=True):
    workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    application_id: (
        "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
    )
    """<p>The identifier of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateWorkspaceApplicationRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    out["ApplicationId"] = value["application_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateWorkspaceApplicationRequest:
    out: DisassociateWorkspaceApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    return out
