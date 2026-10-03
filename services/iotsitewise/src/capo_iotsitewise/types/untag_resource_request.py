"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.amazon_resource_name
    import capo_iotsitewise.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotsitewise.types.amazon_resource_name.AmazonResourceName"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource to untag.</p>"""
    tag_keys: "capo_iotsitewise.types.tag_key_list.TagKeyList"
    """<p>A list of keys for tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
