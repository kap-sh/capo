"""Generated from Smithy shape ``com.amazonaws.ivschat#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.resource_arn
    import capo_ivschat.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ivschat.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to be untagged. The ARN must be URL-encoded.</p>"""
    tag_keys: "capo_ivschat.types.tag_key_list.TagKeyList"
    """<p>Array of tags to be removed. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
