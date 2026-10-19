"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tag_key
    import capo_bedrock_runtime.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_bedrock_runtime.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: "capo_bedrock_runtime.types.tag_value.TagValue"
    """<p>The tag's value.</p>"""


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
