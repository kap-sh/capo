"""Generated from Smithy shape ``com.amazonaws.storagegateway#RemoveTagsFromResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.resource_arn
    import capo_storage_gateway.types.tag_keys


class RemoveTagsFromResourceInput(TypedDict, closed=True):
    resource_arn: "capo_storage_gateway.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource you want to remove the tags from.</p>"""
    tag_keys: "capo_storage_gateway.types.tag_keys.TagKeys"
    """<p>The keys of the tags you want to remove from the specified resource. A tag is composed of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_storage_gateway.types.tag_keys

    out["TagKeys"] = capo_storage_gateway.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceInput:
    out: RemoveTagsFromResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_storage_gateway.types.tag_keys

        out["tag_keys"] = capo_storage_gateway.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
