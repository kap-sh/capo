"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Tag``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.tag_key
    import capo_chime_sdk_messaging.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_chime_sdk_messaging.types.tag_key.TagKey"
    """<p>The key in a tag.</p>"""
    value: "capo_chime_sdk_messaging.types.tag_value.TagValue"
    """<p>The value in a tag.</p>"""


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
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
