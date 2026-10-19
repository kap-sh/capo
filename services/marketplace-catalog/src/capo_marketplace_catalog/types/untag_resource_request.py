"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_arn
    import capo_marketplace_catalog.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>Required. The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>"""
    tag_keys: "capo_marketplace_catalog.types.tag_key_list.TagKeyList"
    """<p>Required. A list of key names of tags to be removed. Number of strings allowed: 0-256.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_marketplace_catalog.types.tag_key_list

    out["TagKeys"] = capo_marketplace_catalog.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_marketplace_catalog.types.tag_key_list

        out["tag_keys"] = capo_marketplace_catalog.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
