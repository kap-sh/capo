"""Generated from Smithy shape ``com.amazonaws.ivs#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.resource_arn
    import capo_ivs.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ivs.types.resource_arn.ResourceArn"
    """<p>ARN of the resource for which tags are to be removed. The ARN must be URL-encoded.</p>"""
    tag_keys: "capo_ivs.types.tag_key_list.TagKeyList"
    """<p>Array of tag keys (strings) for the tags to be removed. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
