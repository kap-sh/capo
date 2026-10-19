"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.workspace_instance_id


class ListTagsForResourceRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        out["workspace_instance_id"] = ""
    return out
