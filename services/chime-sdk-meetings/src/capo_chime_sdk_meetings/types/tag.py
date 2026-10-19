"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.tag_key
    import capo_chime_sdk_meetings.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_chime_sdk_meetings.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: "capo_chime_sdk_meetings.types.tag_value.TagValue"
    """<p>The tag's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
