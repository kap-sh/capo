"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspaceVisibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.visibility
    import capo_connect.types.workspace_id


class UpdateWorkspaceVisibilityRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    visibility: "capo_connect.types.visibility.Visibility"
    """<p>The visibility setting for the workspace. Valid values are: <code>ALL</code> (available to all users), <code>ASSIGNED</code> (available only to assigned users and routing profiles), and <code>NONE</code> (not visible to any users).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceVisibilityRequest) -> dict:
    out: dict = {}
    import capo_connect.types.visibility

    out["Visibility"] = capo_connect.types.visibility.serialize_json(
        value["visibility"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceVisibilityRequest:
    out: UpdateWorkspaceVisibilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Visibility") is not None:
        import capo_connect.types.visibility

        out["visibility"] = capo_connect.types.visibility.deserialize_json(
            data["Visibility"]
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceVisibilityRequest.visibility required"
        )
    return out
