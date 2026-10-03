"""Generated from Smithy shape ``com.amazonaws.connect#DeleteWorkspaceMediaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.media_type
    import capo_connect.types.workspace_id


class DeleteWorkspaceMediaRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    media_type: "capo_connect.types.media_type.MediaType"
    """<p>The type of media to delete. Valid values are: <code>IMAGE_LOGO_FAVICON</code> and <code>IMAGE_LOGO_HORIZONTAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceMediaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceMediaRequest:
    out: DeleteWorkspaceMediaRequest = {}  # type: ignore[typeddict-item]
    return out
