"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseDocument``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.document_content
    import capo_bedrock_agent.types.document_metadata


class KnowledgeBaseDocument(TypedDict, closed=True):
    metadata: NotRequired["capo_bedrock_agent.types.document_metadata.DocumentMetadata"]
    """<p>Contains the metadata to associate with the document.</p>"""
    content: "capo_bedrock_agent.types.document_content.DocumentContent"
    """<p>Contains the content of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseDocument) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_bedrock_agent.types.document_metadata

        out["metadata"] = capo_bedrock_agent.types.document_metadata.serialize_json(
            value["metadata"]
        )
    import capo_bedrock_agent.types.document_content

    out["content"] = capo_bedrock_agent.types.document_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseDocument:
    out: KnowledgeBaseDocument = {}  # type: ignore[typeddict-item]
    if data.get("metadata") is not None:
        import capo_bedrock_agent.types.document_metadata

        out["metadata"] = capo_bedrock_agent.types.document_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("content") is not None:
        import capo_bedrock_agent.types.document_content

        out["content"] = capo_bedrock_agent.types.document_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("KnowledgeBaseDocument.content required")
    return out


def redact_sensitive(value: KnowledgeBaseDocument) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata" in value:
        import capo_bedrock_agent.types.document_metadata

        out["metadata"] = capo_bedrock_agent.types.document_metadata.redact_sensitive(
            value["metadata"]
        )
    if "content" in value:
        import capo_bedrock_agent.types.document_content

        out["content"] = capo_bedrock_agent.types.document_content.redact_sensitive(
            value["content"]
        )
    return out
