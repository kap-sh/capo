"""Generated from Smithy shape ``com.amazonaws.polly#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.amazon_resource_name
    import capo_polly.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_polly.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon Polly lexicon.</p>"""
    tag_keys: "capo_polly.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_polly.types.tag_key_list

    out["TagKeys"] = capo_polly.types.tag_key_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_polly.types.tag_key_list

        out["tag_keys"] = capo_polly.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
