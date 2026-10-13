"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningLogicStatement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_logic_statement_content
    import capo_bedrock.types.automated_reasoning_natural_language_statement_content


class AutomatedReasoningLogicStatement(TypedDict, closed=True):
    logic: "capo_bedrock.types.automated_reasoning_logic_statement_content.AutomatedReasoningLogicStatementContent"
    """<p>The formal logic representation of the statement using mathematical notation and logical operators.</p>"""
    natural_language: NotRequired[
        "capo_bedrock.types.automated_reasoning_natural_language_statement_content.AutomatedReasoningNaturalLanguageStatementContent"
    ]
    """<p>The natural language representation of the logical statement, providing a human-readable interpretation of the formal logic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningLogicStatement) -> dict:
    out: dict = {}
    out["logic"] = value["logic"]
    if "natural_language" in value:
        out["naturalLanguage"] = value["natural_language"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningLogicStatement:
    out: AutomatedReasoningLogicStatement = {}  # type: ignore[typeddict-item]
    if data.get("logic") is not None:
        out["logic"] = data["logic"]
    else:
        raise DeserializationError("AutomatedReasoningLogicStatement.logic required")
    if data.get("naturalLanguage") is not None:
        out["natural_language"] = data["naturalLanguage"]
    return out


def redact_sensitive(value: AutomatedReasoningLogicStatement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logic" in value:
        out["logic"] = "*** Sensitive Data Redacted ***"
    if "natural_language" in value:
        out["natural_language"] = "*** Sensitive Data Redacted ***"
    return out
