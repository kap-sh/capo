"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedLine``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_line_text


class AutomatedReasoningPolicyAnnotatedLine(TypedDict, closed=True):
    line_number: NotRequired["int"]
    """<p>The line number of this text within the source document.</p>"""
    line_text: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_line_text.AutomatedReasoningPolicyLineText"
    ]
    """<p>The actual text content of this line from the source document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedLine) -> dict:
    out: dict = {}
    if "line_number" in value:
        out["lineNumber"] = value["line_number"]
    if "line_text" in value:
        out["lineText"] = value["line_text"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedLine:
    out: AutomatedReasoningPolicyAnnotatedLine = {}  # type: ignore[typeddict-item]
    if data.get("lineNumber") is not None:
        out["line_number"] = data["lineNumber"]
    if data.get("lineText") is not None:
        out["line_text"] = data["lineText"]
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAnnotatedLine) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line_text" in value:
        out["line_text"] = "*** Sensitive Data Redacted ***"
    return out
