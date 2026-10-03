"""Generated from Smithy shape ``com.amazonaws.appstream#CreateUpdatedImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.name
    import capo_appstream.types.tags


class CreateUpdatedImageRequest(TypedDict, closed=True):
    existing_image_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the image to update.</p>"""
    new_image_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the new image. The name must be unique within the AWS account and Region.</p>"""
    new_image_description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description to display for the new image.</p>"""
    new_image_display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The name to display for the new image.</p>"""
    new_image_tags: NotRequired["capo_appstream.types.tags.Tags"]
    r"""<p>The tags to associate with the new image. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    dry_run: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Indicates whether to display the status of image update availability before WorkSpaces Applications initiates the process of creating a new updated image. If this value is set to <code>true</code>, WorkSpaces Applications displays whether image updates are available. If this value is set to <code>false</code>, WorkSpaces Applications initiates the process of creating a new updated image without displaying whether image updates are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedImageRequest) -> dict:
    out: dict = {}
    if "existing_image_name" in value:
        out["existingImageName"] = value["existing_image_name"]
    if "new_image_name" in value:
        out["newImageName"] = value["new_image_name"]
    if "new_image_description" in value:
        out["newImageDescription"] = value["new_image_description"]
    if "new_image_display_name" in value:
        out["newImageDisplayName"] = value["new_image_display_name"]
    if "new_image_tags" in value:
        import capo_appstream.types.tags

        out["newImageTags"] = capo_appstream.types.tags.serialize_aws_json_1_1(
            value["new_image_tags"]
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedImageRequest:
    out: CreateUpdatedImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("existingImageName") is not None:
        out["existing_image_name"] = data["existingImageName"]
    if data.get("newImageName") is not None:
        out["new_image_name"] = data["newImageName"]
    if data.get("newImageDescription") is not None:
        out["new_image_description"] = data["newImageDescription"]
    if data.get("newImageDisplayName") is not None:
        out["new_image_display_name"] = data["newImageDisplayName"]
    if data.get("newImageTags") is not None:
        import capo_appstream.types.tags

        out["new_image_tags"] = capo_appstream.types.tags.deserialize_aws_json_1_1(
            data["newImageTags"]
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
