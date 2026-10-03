"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestKnowledgeBaseDocumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_documents


class IngestKnowledgeBaseDocumentsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to ingest the documents into.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    documents: (
        "capo_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments"
    )
    """<p>A list of objects, each of which contains information about the documents to add.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestKnowledgeBaseDocumentsRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agent.types.knowledge_base_documents

    out["documents"] = capo_bedrock_agent.types.knowledge_base_documents.serialize_json(
        value["documents"]
    )
    return out


def deserialize_json(data: dict) -> IngestKnowledgeBaseDocumentsRequest:
    out: IngestKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("documents") is not None:
        import capo_bedrock_agent.types.knowledge_base_documents

        out["documents"] = (
            capo_bedrock_agent.types.knowledge_base_documents.deserialize_json(
                data["documents"]
            )
        )
    else:
        raise DeserializationError(
            "IngestKnowledgeBaseDocumentsRequest.documents required"
        )
    return out
