"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_gameliftstreams.types.arn.Arn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> of the Amazon GameLift Streams resource that you want to remove tags from.</p>"""
    tag_keys: "capo_gameliftstreams.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the specified Amazon GameLift Streams resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
