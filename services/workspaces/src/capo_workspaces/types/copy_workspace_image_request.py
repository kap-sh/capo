"""Generated from Smithy shape ``com.amazonaws.workspaces#CopyWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.region
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_id
    import capo_workspaces.types.workspace_image_name


class CopyWorkspaceImageRequest(TypedDict, closed=True):
    name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the image.</p>"""
    description: NotRequired[
        "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    ]
    """<p>A description of the image.</p>"""
    source_image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the source image.</p>"""
    source_region: "capo_workspaces.types.region.Region"
    """<p>The identifier of the source Region.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["SourceImageId"] = value["source_image_id"]
    out["SourceRegion"] = value["source_region"]
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyWorkspaceImageRequest:
    out: CopyWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SourceImageId") is not None:
        out["source_image_id"] = data["SourceImageId"]
    else:
        out["source_image_id"] = ""
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    else:
        out["source_region"] = ""
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
