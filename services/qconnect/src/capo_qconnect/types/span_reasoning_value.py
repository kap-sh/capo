"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanReasoningValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string


class SpanReasoningValue(TypedDict, closed=True):
    value: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The reasoning text content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanReasoningValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SpanReasoningValue:
    out: SpanReasoningValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out


def redact_sensitive(value: SpanReasoningValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
