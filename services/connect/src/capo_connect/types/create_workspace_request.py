"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map
    import capo_connect.types.workspace_description
    import capo_connect.types.workspace_name
    import capo_connect.types.workspace_theme
    import capo_connect.types.workspace_title


class CreateWorkspaceRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace. Must be unique within the instance and can contain 1-127 characters.</p>"""
    description: NotRequired[
        "capo_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace. Maximum length is 250 characters.</p>"""
    theme: NotRequired["capo_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration for the workspace, including colors and styling.</p>"""
    title: NotRequired["capo_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "theme" in value:
        import capo_connect.types.workspace_theme

        out["Theme"] = capo_connect.types.workspace_theme.serialize_json(value["theme"])
    if "title" in value:
        out["Title"] = value["title"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkspaceRequest:
    out: CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateWorkspaceRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Theme") is not None:
        import capo_connect.types.workspace_theme

        out["theme"] = capo_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
