"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningInputTextReference``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content


class GuardrailAutomatedReasoningInputTextReference(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content.GuardrailAutomatedReasoningStatementNaturalLanguageContent"
    ]
    """<p>The specific text from the original input that this reference points to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningInputTextReference) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningInputTextReference:
    out: GuardrailAutomatedReasoningInputTextReference = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out


def redact_sensitive(
    value: GuardrailAutomatedReasoningInputTextReference,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
