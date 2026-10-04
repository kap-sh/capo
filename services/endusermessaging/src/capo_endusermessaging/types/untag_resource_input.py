"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_endusermessaging.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
