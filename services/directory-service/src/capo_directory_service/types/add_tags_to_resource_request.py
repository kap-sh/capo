"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddTagsToResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.resource_id
    import capo_directory_service.types.tags


class AddTagsToResourceRequest(TypedDict, closed=True):
    resource_id: "capo_directory_service.types.resource_id.ResourceId"
    """<p>Identifier (ID) for the directory to which to add the tag.</p>"""
    tags: "capo_directory_service.types.tags.Tags"
    """<p>The tags to be assigned to the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_directory_service.types.tags

    out["Tags"] = capo_directory_service.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceRequest:
    out: AddTagsToResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Tags") is not None:
        import capo_directory_service.types.tags

        out["tags"] = capo_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
