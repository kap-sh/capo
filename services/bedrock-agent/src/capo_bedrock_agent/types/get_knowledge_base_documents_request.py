"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetKnowledgeBaseDocumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.document_identifiers
    import capo_bedrock_agent.types.id


class GetKnowledgeBaseDocumentsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that is connected to the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that contains the documents.</p>"""
    document_identifiers: (
        "capo_bedrock_agent.types.document_identifiers.DocumentIdentifiers"
    )
    """<p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKnowledgeBaseDocumentsRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.document_identifiers

    out["documentIdentifiers"] = (
        capo_bedrock_agent.types.document_identifiers.serialize_json(
            value["document_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetKnowledgeBaseDocumentsRequest:
    out: GetKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("documentIdentifiers") is not None:
        import capo_bedrock_agent.types.document_identifiers

        out["document_identifiers"] = (
            capo_bedrock_agent.types.document_identifiers.deserialize_json(
                data["documentIdentifiers"]
            )
        )
    else:
        out["document_identifiers"] = []
    return out
