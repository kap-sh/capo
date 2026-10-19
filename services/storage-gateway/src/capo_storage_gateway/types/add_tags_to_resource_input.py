"""Generated from Smithy shape ``com.amazonaws.storagegateway#AddTagsToResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.resource_arn
    import capo_storage_gateway.types.tags


class AddTagsToResourceInput(TypedDict, closed=True):
    resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>"""
    tags: "capo_storage_gateway.types.tags.Tags"
    """<p>The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_storage_gateway.types.tags

    out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceInput:
    out: AddTagsToResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
