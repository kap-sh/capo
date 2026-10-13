"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailWordConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_word_text


class GuardrailWordConfig(TypedDict, closed=True):
    text: "capo_qconnect.types.guardrail_word_text.GuardrailWordText"
    """<p>Text of the word configured for the AI Guardrail to block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordConfig) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> GuardrailWordConfig:
    out: GuardrailWordConfig = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError("GuardrailWordConfig.text required")
    return out


def redact_sensitive(value: GuardrailWordConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
