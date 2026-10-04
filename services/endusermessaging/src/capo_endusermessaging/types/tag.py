"""Generated from Smithy shape ``com.amazonaws.endusermessaging#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.tag_key
    import capo_endusermessaging.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_endusermessaging.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    value: "capo_endusermessaging.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
