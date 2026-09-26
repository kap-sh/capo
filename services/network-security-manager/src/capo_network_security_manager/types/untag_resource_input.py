"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.arn
    import capo_network_security_manager.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_network_security_manager.types.arn.Arn"
    """<p>The ARN of the resource to remove tags from. The ARN must not include a <code>:DRAFT</code> qualifier.</p>"""
    tag_keys: "capo_network_security_manager.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
