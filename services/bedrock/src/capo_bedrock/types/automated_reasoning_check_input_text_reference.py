"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckInputTextReference``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_natural_language_statement_content


class AutomatedReasoningCheckInputTextReference(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock.types.automated_reasoning_natural_language_statement_content.AutomatedReasoningNaturalLanguageStatementContent"
    ]
    """<p>The specific text from the original input that this reference points to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckInputTextReference) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckInputTextReference:
    out: AutomatedReasoningCheckInputTextReference = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out


def redact_sensitive(
    value: AutomatedReasoningCheckInputTextReference,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
