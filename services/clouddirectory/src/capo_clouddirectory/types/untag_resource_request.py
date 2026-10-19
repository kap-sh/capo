"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.</p>"""
    tag_keys: "capo_clouddirectory.types.tag_key_list.TagKeyList"
    """<p>Keys of the tag that need to be removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_clouddirectory.types.tag_key_list

    out["TagKeys"] = capo_clouddirectory.types.tag_key_list.serialize_json(
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
        import capo_clouddirectory.types.tag_key_list

        out["tag_keys"] = capo_clouddirectory.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
