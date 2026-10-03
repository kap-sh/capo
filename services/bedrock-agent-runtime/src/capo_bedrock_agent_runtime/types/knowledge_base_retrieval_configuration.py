"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseRetrievalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration
    import capo_bedrock_agent_runtime.types.managed_search_configuration


class KnowledgeBaseRetrievalConfiguration(TypedDict, closed=True):
    vector_search_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.KnowledgeBaseVectorSearchConfiguration"
    ]
    """<p>Contains details about how the results from the vector search should be returned. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>"""
    managed_search_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.managed_search_configuration.ManagedSearchConfiguration"
    ]
    """<p>Contains configurations for managed search. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalConfiguration) -> dict:
    out: dict = {}
    if "vector_search_configuration" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration

        out["vectorSearchConfiguration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.serialize_json(
                value["vector_search_configuration"]
            )
        )
    if "managed_search_configuration" in value:
        import capo_bedrock_agent_runtime.types.managed_search_configuration

        out["managedSearchConfiguration"] = (
            capo_bedrock_agent_runtime.types.managed_search_configuration.serialize_json(
                value["managed_search_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalConfiguration:
    out: KnowledgeBaseRetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vectorSearchConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration

        out["vector_search_configuration"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    if data.get("managedSearchConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.managed_search_configuration

        out["managed_search_configuration"] = (
            capo_bedrock_agent_runtime.types.managed_search_configuration.deserialize_json(
                data["managedSearchConfiguration"]
            )
        )
    return out
