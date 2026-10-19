"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailManagedWordsConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_managed_words_type


class GuardrailManagedWordsConfig(TypedDict, closed=True):
    type: "capo_qconnect.types.guardrail_managed_words_type.GuardrailManagedWordsType"
    """<p>The managed word type to configure for the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordsConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> GuardrailManagedWordsConfig:
    out: GuardrailManagedWordsConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out


def redact_sensitive(value: GuardrailManagedWordsConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
