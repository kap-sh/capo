"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListKnowledgeBaseDocumentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_document_details


class ListKnowledgeBaseDocumentsResponse(TypedDict, closed=True):
    document_details: "capo_bedrock_agent.types.knowledge_base_document_details.KnowledgeBaseDocumentDetails"
    """<p>A list of objects, each of which contains information about the documents that were retrieved.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBaseDocumentsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base_document_details

    out["documentDetails"] = (
        capo_bedrock_agent.types.knowledge_base_document_details.serialize_json(
            value["document_details"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBaseDocumentsResponse:
    out: ListKnowledgeBaseDocumentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("documentDetails") is not None:
        import capo_bedrock_agent.types.knowledge_base_document_details

        out["document_details"] = (
            capo_bedrock_agent.types.knowledge_base_document_details.deserialize_json(
                data["documentDetails"]
            )
        )
    else:
        out["document_details"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
