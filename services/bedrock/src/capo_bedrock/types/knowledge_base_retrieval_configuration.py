"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseRetrievalConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.knowledge_base_vector_search_configuration


class KnowledgeBaseRetrievalConfiguration(TypedDict, closed=True):
    vector_search_configuration: "capo_bedrock.types.knowledge_base_vector_search_configuration.KnowledgeBaseVectorSearchConfiguration"
    """<p>Contains configuration details for returning the results from the vector search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseRetrievalConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock.types.knowledge_base_vector_search_configuration

    out["vectorSearchConfiguration"] = (
        capo_bedrock.types.knowledge_base_vector_search_configuration.serialize_json(
            value["vector_search_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseRetrievalConfiguration:
    out: KnowledgeBaseRetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vectorSearchConfiguration") is not None:
        import capo_bedrock.types.knowledge_base_vector_search_configuration

        out["vector_search_configuration"] = (
            capo_bedrock.types.knowledge_base_vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "KnowledgeBaseRetrievalConfiguration.vector_search_configuration required"
        )
    return out


def redact_sensitive(value: KnowledgeBaseRetrievalConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vector_search_configuration" in value:
        import capo_bedrock.types.knowledge_base_vector_search_configuration

        out["vector_search_configuration"] = (
            capo_bedrock.types.knowledge_base_vector_search_configuration.redact_sensitive(
                value["vector_search_configuration"]
            )
        )
    return out
