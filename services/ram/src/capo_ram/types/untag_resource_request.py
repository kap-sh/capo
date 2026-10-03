"""Generated from Smithy shape ``com.amazonaws.ram#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.string
    import capo_ram.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_share_arn: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove tags from. The tags are removed from the resource share, not the resources in the resource share. You must specify either <code>resourceShareArn</code>, or <code>resourceArn</code>, but not both.</p>"""
    tag_keys: "capo_ram.types.tag_key_list.TagKeyList"
    """<p>Specifies a list of one or more tag keys that you want to remove.</p>"""
    resource_arn: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that you want to remove tags from. You must specify either <code>resourceArn</code>, or <code>resourceShareArn</code>, but not both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    import capo_ram.types.tag_key_list

    out["tagKeys"] = capo_ram.types.tag_key_list.serialize_json(value["tag_keys"])
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("tagKeys") is not None:
        import capo_ram.types.tag_key_list

        out["tag_keys"] = capo_ram.types.tag_key_list.deserialize_json(data["tagKeys"])
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out
