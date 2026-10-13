"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanToolUseValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.json_document
    import capo_qconnect.types.name
    import capo_qconnect.types.uuid


class SpanToolUseValue(TypedDict, closed=True):
    tool_use_id: "capo_qconnect.types.uuid.Uuid"
    """<p>Unique ID for this tool invocation</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The tool name</p>"""
    arguments: "capo_qconnect.types.json_document.JSONDocument"
    """<p>The tool input arguments</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanToolUseValue) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    out["arguments"] = value["arguments"]
    return out


def deserialize_json(data: dict) -> SpanToolUseValue:
    out: SpanToolUseValue = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("SpanToolUseValue.tool_use_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpanToolUseValue.name required")
    if data.get("arguments") is not None:
        out["arguments"] = data["arguments"]
    else:
        raise DeserializationError("SpanToolUseValue.arguments required")
    return out


def redact_sensitive(value: SpanToolUseValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arguments" in value:
        out["arguments"] = "*** Sensitive Data Redacted ***"
    return out
