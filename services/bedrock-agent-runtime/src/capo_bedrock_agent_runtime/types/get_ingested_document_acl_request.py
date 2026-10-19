"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetIngestedDocumentAclRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier


class GetIngestedDocumentAclRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier"
    """<p>The unique identifier of the knowledge base that contains the document.</p>"""
    data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId"
    """<p>The unique identifier of the data source that contains the document.</p>"""
    document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId"
    """<p>The unique identifier of the document to retrieve the ingested access control list (ACL) for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestedDocumentAclRequest) -> dict:
    out: dict = {}
    out["documentId"] = value["document_id"]
    return out


def deserialize_json(data: dict) -> GetIngestedDocumentAclRequest:
    out: GetIngestedDocumentAclRequest = {}  # type: ignore[typeddict-item]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    else:
        out["document_id"] = ""
    return out
