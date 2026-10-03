"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteKnowledgeBaseDocumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.document_identifiers
    import capo_bedrock_agent.types.id


class DeleteKnowledgeBaseDocumentsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that is connected to the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that contains the documents.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    document_identifiers: (
        "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers"
    )
    """<p>A list of objects, each of which contains information to identify a document to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKnowledgeBaseDocumentsRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agent.types.document_identifiers

    out["documentIdentifiers"] = (
        capo_bedrock_agent.types.document_identifiers.serialize_json(
            value["document_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteKnowledgeBaseDocumentsRequest:
    out: DeleteKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("documentIdentifiers") is not None:
        import capo_bedrock_agent.types.document_identifiers

        out["document_identifiers"] = (
            capo_bedrock_agent.types.document_identifiers.deserialize_json(
                data["documentIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteKnowledgeBaseDocumentsRequest.document_identifiers required"
        )
    return out
