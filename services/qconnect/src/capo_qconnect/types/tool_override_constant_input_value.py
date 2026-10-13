"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideConstantInputValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.tool_override_input_value_type


class ToolOverrideConstantInputValue(TypedDict, closed=True):
    type: (
        "capo_qconnect.types.tool_override_input_value_type.ToolOverrideInputValueType"
    )
    """<p>Override tool input value with constant values</p>"""
    value: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The constant input override value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideConstantInputValue) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ToolOverrideConstantInputValue:
    out: ToolOverrideConstantInputValue = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ToolOverrideConstantInputValue.type required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ToolOverrideConstantInputValue.value required")
    return out


def redact_sensitive(value: ToolOverrideConstantInputValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
