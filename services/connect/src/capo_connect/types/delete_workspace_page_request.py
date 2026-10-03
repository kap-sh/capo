"""Generated from Smithy shape ``com.amazonaws.connect#DeleteWorkspacePageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.page
    import capo_connect.types.workspace_id


class DeleteWorkspacePageRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    page: "capo_connect.types.page.Page"
    """<p>The page identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspacePageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspacePageRequest:
    out: DeleteWorkspacePageRequest = {}  # type: ignore[typeddict-item]
    return out
