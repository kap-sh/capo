"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionTag``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.session_tag_key
    import capo_quicksight.types.session_tag_value


class SessionTag(TypedDict, closed=True):
    key: "capo_quicksight.types.session_tag_key.SessionTagKey"
    """<p>The key for the tag.</p>"""
    value: "capo_quicksight.types.session_tag_value.SessionTagValue"
    """<p>The value that you want to assign the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionTag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SessionTag:
    out: SessionTag = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out


def redact_sensitive(value: SessionTag) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
