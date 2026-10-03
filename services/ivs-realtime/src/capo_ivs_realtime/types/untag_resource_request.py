"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.resource_arn
    import capo_ivs_realtime.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ivs_realtime.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to be untagged. The ARN must be URL-encoded.</p>"""
    tag_keys: "capo_ivs_realtime.types.tag_key_list.TagKeyList"
    """<p>Array of tag keys (strings) for the tags to be removed. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
