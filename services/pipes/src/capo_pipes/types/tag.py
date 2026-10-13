"""Generated from Smithy shape ``com.amazonaws.pipes#Tag``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.tag_key
    import capo_pipes.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_pipes.types.tag_key.TagKey"
    """<p>A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.</p>"""
    value: "capo_pipes.types.tag_value.TagValue"
    """<p>The value for the specified tag key.</p>"""


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
        raise DeserializationError("Tag.key required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out


def redact_sensitive(value: Tag) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
