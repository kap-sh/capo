"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.tag_key
    import capo_kinesis_video.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_kinesis_video.types.tag_key.TagKey"
    """<p>The key of the tag that is associated with the specified signaling channel.</p>"""
    value: "capo_kinesis_video.types.tag_value.TagValue"
    """<p>The value of the tag that is associated with the specified signaling channel.</p>"""


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
