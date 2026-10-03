"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrievalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.retrieval_result_content
    import capo_bedrock_agent_runtime.types.retrieval_result_location
    import capo_bedrock_agent_runtime.types.retrieval_result_metadata


class KnowledgeBaseRetrievalResult(TypedDict, closed=True):
    content: "capo_bedrock_agent_runtime.types.retrieval_result_content.RetrievalResultContent"
    """<p>Contains information about the content of the chunk.</p>"""
    location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_location.RetrievalResultLocation"
    ]
    """<p>Contains information about the location of the data source.</p>"""
    score: NotRequired["float"]
    """<p>The level of relevance of the result to the query.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_metadata.RetrievalResultMetadata"
    ]
    """<p>Contains metadata attributes and their values for the file in the data source. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata">Metadata and filtering</a>.</p>"""
    document_id: NotRequired["capo_bedrock_agent_runtime.types.document_id.DocumentId"]
    """<p>The unique identifier of the document. Use with <code>GetDocumentContent</code> to retrieve the full document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalResult) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.retrieval_result_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.retrieval_result_content.serialize_json(
            value["content"]
        )
    )
    if "location" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_location.serialize_json(
                value["location"]
            )
        )
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalResult:
    out: KnowledgeBaseRetrievalResult = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseRetrievalResult.content required")
    if data.get("location") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_location.deserialize_json(
                data["location"]
            )
        )
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    return out
