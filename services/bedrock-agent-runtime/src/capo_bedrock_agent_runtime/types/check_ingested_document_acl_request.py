"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CheckIngestedDocumentAclRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.user_context


class CheckIngestedDocumentAclRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier"
    """<p>The unique identifier of the knowledge base that contains the document.</p>"""
    data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId"
    """<p>The unique identifier of the data source that contains the document.</p>"""
    document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId"
    """<p>The unique identifier of the document to check access for.</p>"""
    user_context: "capo_bedrock_agent_runtime.types.user_context.UserContext"
    """<p>The context object containing identity information for access control filtering, including user ID and optional group memberships used to evaluate the document access control list (ACL).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckIngestedDocumentAclRequest) -> dict:
    out: dict = {}
    out["documentId"] = value["document_id"]
    import capo_bedrock_agent_runtime.types.user_context

    out["userContext"] = capo_bedrock_agent_runtime.types.user_context.serialize_json(
        value["user_context"]
    )
    return out


def deserialize_json(data: dict) -> CheckIngestedDocumentAclRequest:
    out: CheckIngestedDocumentAclRequest = {}  # type: ignore[typeddict-item]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    else:
        out["document_id"] = ""
    if data.get("userContext") is not None:
        import capo_bedrock_agent_runtime.types.user_context

        out["user_context"] = (
            capo_bedrock_agent_runtime.types.user_context.deserialize_json(
                data["userContext"]
            )
        )
    else:
        raise DeserializationError(
            "CheckIngestedDocumentAclRequest.user_context required"
        )
    return out


def redact_sensitive(value: CheckIngestedDocumentAclRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_context" in value:
        out["user_context"] = "*** Sensitive Data Redacted ***"
    return out
