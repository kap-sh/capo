"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.tag_key_list
    import capo_lambda_microvms.types.taggable_resource


class UntagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource"
    """<p>The ARN of the resource to remove tags from.</p>"""
    tag_keys: "capo_lambda_microvms.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
