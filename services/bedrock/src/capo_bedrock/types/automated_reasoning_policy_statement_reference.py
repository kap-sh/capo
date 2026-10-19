"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyStatementReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_document_id
    import capo_bedrock.types.automated_reasoning_policy_statement_id


class AutomatedReasoningPolicyStatementReference(TypedDict, closed=True):
    document_id: "capo_bedrock.types.automated_reasoning_policy_document_id.AutomatedReasoningPolicyDocumentId"
    """<p>The unique identifier of the document containing the referenced statement.</p>"""
    statement_id: "capo_bedrock.types.automated_reasoning_policy_statement_id.AutomatedReasoningPolicyStatementId"
    """<p>The unique identifier of the specific atomic statement being referenced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyStatementReference) -> dict:
    out: dict = {}
    out["documentId"] = value["document_id"]
    out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyStatementReference:
    out: AutomatedReasoningPolicyStatementReference = {}  # type: ignore[typeddict-item]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    else:
        out["document_id"] = ""
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    else:
        out["statement_id"] = ""
    return out
