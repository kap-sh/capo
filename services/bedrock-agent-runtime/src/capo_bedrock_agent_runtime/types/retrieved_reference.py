"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievedReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_result_content
    import capo_bedrock_agent_runtime.types.retrieval_result_location
    import capo_bedrock_agent_runtime.types.retrieval_result_metadata


class RetrievedReference(TypedDict, closed=True):
    content: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_content.RetrievalResultContent"
    ]
    """<p>Contains the cited text from the data source.</p>"""
    location: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_location.RetrievalResultLocation"
    ]
    """<p>Contains information about the location of the data source.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieval_result_metadata.RetrievalResultMetadata"
    ]
    """<p>Contains metadata attributes and their values for the file in the data source. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata">Metadata and filtering</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedReference) -> dict:
    out: dict = {}
    if "content" in value:
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
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievedReference:
    out: RetrievedReference = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_content.deserialize_json(
                data["content"]
            )
        )
    if data.get("location") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_location

        out["location"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_location.deserialize_json(
                data["location"]
            )
        )
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_result_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.retrieval_result_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
