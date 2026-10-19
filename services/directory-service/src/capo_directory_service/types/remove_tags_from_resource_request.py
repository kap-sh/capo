"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveTagsFromResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.resource_id
    import capo_directory_service.types.tag_keys


class RemoveTagsFromResourceRequest(TypedDict, closed=True):
    resource_id: "capo_directory_service.types.resource_id.ResourceId"
    """<p>Identifier (ID) of the directory from which to remove the tag.</p>"""
    tag_keys: "capo_directory_service.types.tag_keys.TagKeys"
    """<p>The tag key (name) of the tag to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_directory_service.types.tag_keys

    out["TagKeys"] = capo_directory_service.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceRequest:
    out: RemoveTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagKeys") is not None:
        import capo_directory_service.types.tag_keys

        out["tag_keys"] = (
            capo_directory_service.types.tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
