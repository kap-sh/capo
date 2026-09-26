"""Generated from Smithy shape ``com.amazonaws.supportauthz#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.arn
    import capo_supportauthz.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_supportauthz.types.arn.Arn"
    """<p>The ARN of the resource to untag.</p>"""
    tag_keys: "capo_supportauthz.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
