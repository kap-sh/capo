"""Generated from Smithy shape ``com.amazonaws.qbusiness#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.tag_key
    import capo_qbusiness.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_qbusiness.types.tag_key.TagKey"
    """<p> The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.</p>"""
    value: "capo_qbusiness.types.tag_value.TagValue"
    """<p>The value associated with the tag. The value may be an empty string but it can't be null.</p>"""


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
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
