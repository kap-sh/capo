"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspaceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.workspace_description
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_name
    import capo_connect.types.workspace_title


class UpdateWorkspaceMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    name: NotRequired["capo_connect.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    description: NotRequired[
        "capo_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    title: NotRequired["capo_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "title" in value:
        out["Title"] = value["title"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceMetadataRequest:
    out: UpdateWorkspaceMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    return out
