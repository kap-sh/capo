"""Generated from Smithy shape ``com.amazonaws.connect#Workspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.visibility
    import capo_connect.types.workspace_description
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_name
    import capo_connect.types.workspace_theme
    import capo_connect.types.workspace_title


class Workspace(TypedDict, closed=True):
    visibility: NotRequired["capo_connect.types.visibility.Visibility"]
    """<p>Controls who can access the workspace. Valid values are: <code>ALL</code> (all users), <code>ASSIGNED</code> (only assigned users and routing profiles), and <code>NONE</code> (not visible).</p>"""
    id: "capo_connect.types.workspace_id.WorkspaceId"
    """<p>The unique identifier of the workspace.</p>"""
    name: "capo_connect.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    description: NotRequired[
        "capo_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    theme: NotRequired["capo_connect.types.workspace_theme.WorkspaceTheme"]
    """<p>The theme configuration for the workspace, including colors and styling.</p>"""
    title: NotRequired["capo_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the workspace was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the workspace was last modified.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Workspace) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_connect.types.visibility

        out["Visibility"] = capo_connect.types.visibility.serialize_json(
            value["visibility"]
        )
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "theme" in value:
        import capo_connect.types.workspace_theme

        out["Theme"] = capo_connect.types.workspace_theme.serialize_json(value["theme"])
    if "title" in value:
        out["Title"] = value["title"]
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Workspace:
    out: Workspace = {}  # type: ignore[typeddict-item]
    if data.get("Visibility") is not None:
        import capo_connect.types.visibility

        out["visibility"] = capo_connect.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Theme") is not None:
        import capo_connect.types.workspace_theme

        out["theme"] = capo_connect.types.workspace_theme.deserialize_json(
            data["Theme"]
        )
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
