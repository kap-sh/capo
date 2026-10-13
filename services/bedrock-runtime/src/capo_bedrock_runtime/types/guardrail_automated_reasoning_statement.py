"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningStatement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_logic_content
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content


class GuardrailAutomatedReasoningStatement(TypedDict, closed=True):
    logic: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_logic_content.GuardrailAutomatedReasoningStatementLogicContent"
    ]
    """<p>The formal logical representation of the statement.</p>"""
    natural_language: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_natural_language_content.GuardrailAutomatedReasoningStatementNaturalLanguageContent"
    ]
    """<p>The natural language explanation of the logical statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningStatement) -> dict:
    out: dict = {}
    if "logic" in value:
        out["logic"] = value["logic"]
    if "natural_language" in value:
        out["naturalLanguage"] = value["natural_language"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningStatement:
    out: GuardrailAutomatedReasoningStatement = {}  # type: ignore[typeddict-item]
    if data.get("logic") is not None:
        out["logic"] = data["logic"]
    if data.get("naturalLanguage") is not None:
        out["natural_language"] = data["naturalLanguage"]
    return out


def redact_sensitive(value: GuardrailAutomatedReasoningStatement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logic" in value:
        out["logic"] = "*** Sensitive Data Redacted ***"
    if "natural_language" in value:
        out["natural_language"] = "*** Sensitive Data Redacted ***"
    return out
