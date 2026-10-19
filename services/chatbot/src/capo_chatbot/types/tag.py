"""Generated from Smithy shape ``com.amazonaws.chatbot#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.tag_key
    import capo_chatbot.types.tag_value


class Tag(TypedDict, closed=True):
    tag_key: "capo_chatbot.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    tag_value: "capo_chatbot.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    out["TagValue"] = value["tag_value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("TagValue") is not None:
        out["tag_value"] = data["TagValue"]
    else:
        out["tag_value"] = ""
    return out
