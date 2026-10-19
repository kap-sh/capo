"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateUpdatedWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_id
    import capo_workspaces.types.workspace_image_name


class CreateUpdatedWorkspaceImageRequest(TypedDict, closed=True):
    name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the new updated WorkSpace image.</p>"""
    description: (
        "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>A description of whether updates for the WorkSpace image are available.</p>"""
    source_image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the source WorkSpace image.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags that you want to add to the new updated WorkSpace image.</p> <note> <p>To add tags at the same time when you're creating the updated image, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["SourceImageId"] = value["source_image_id"]
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedWorkspaceImageRequest:
    out: CreateUpdatedWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("SourceImageId") is not None:
        out["source_image_id"] = data["SourceImageId"]
    else:
        out["source_image_id"] = ""
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
