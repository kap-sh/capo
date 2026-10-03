"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_id
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import capo_bedrock_agent_runtime.types.resource_description


class KnowledgeBase(TypedDict, closed=True):
    knowledge_base_id: (
        "capo_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId"
    )
    """<p> The unique identifier for a knowledge base associated with the inline agent. </p>"""
    description: (
        "capo_bedrock_agent_runtime.types.resource_description.ResourceDescription"
    )
    """<p> The description of the knowledge base associated with the inline agent. </p>"""
    retrieval_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    ]
    """<p> The configurations to apply to the knowledge base during query. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBase) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["description"] = value["description"]
    if "retrieval_configuration" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrievalConfiguration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.serialize_json(
                value["retrieval_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBase:
    out: KnowledgeBase = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBase.knowledge_base_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("KnowledgeBase.description required")
    if data.get("retrievalConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration

        out["retrieval_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    return out
