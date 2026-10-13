"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#Tag``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.tag_key
    import capo_rolesanywhere.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_rolesanywhere.types.tag_key.TagKey"
    """<p>The tag key.</p>"""
    value: "capo_rolesanywhere.types.tag_value.TagValue"
    """<p>The tag value.</p>"""


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


def redact_sensitive(value: Tag) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
