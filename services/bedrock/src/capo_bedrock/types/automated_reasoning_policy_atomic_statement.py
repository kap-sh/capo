"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAtomicStatement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_statement_id
    import capo_bedrock.types.automated_reasoning_policy_statement_location
    import capo_bedrock.types.automated_reasoning_policy_statement_text


class AutomatedReasoningPolicyAtomicStatement(TypedDict, closed=True):
    id: "capo_bedrock.types.automated_reasoning_policy_statement_id.AutomatedReasoningPolicyStatementId"
    """<p>A unique identifier for this atomic statement within the fidelity report.</p>"""
    text: "capo_bedrock.types.automated_reasoning_policy_statement_text.AutomatedReasoningPolicyStatementText"
    """<p>The actual text content of the atomic statement as extracted from the source document.</p>"""
    location: "capo_bedrock.types.automated_reasoning_policy_statement_location.AutomatedReasoningPolicyStatementLocation"
    """<p>Information about where this statement appears in the source document, including line numbers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAtomicStatement) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["text"] = value["text"]
    import capo_bedrock.types.automated_reasoning_policy_statement_location

    out["location"] = (
        capo_bedrock.types.automated_reasoning_policy_statement_location.serialize_json(
            value["location"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAtomicStatement:
    out: AutomatedReasoningPolicyAtomicStatement = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAtomicStatement.id required"
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAtomicStatement.text required"
        )
    if data.get("location") is not None:
        import capo_bedrock.types.automated_reasoning_policy_statement_location

        out["location"] = (
            capo_bedrock.types.automated_reasoning_policy_statement_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAtomicStatement.location required"
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAtomicStatement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
