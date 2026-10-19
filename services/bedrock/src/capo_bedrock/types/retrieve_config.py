"""Generated from Smithy shape ``com.amazonaws.bedrock#RetrieveConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.knowledge_base_id
    import capo_bedrock.types.knowledge_base_retrieval_configuration


class RetrieveConfig(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the knowledge base.</p>"""
    knowledge_base_retrieval_configuration: "capo_bedrock.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
    """<p>Contains configuration details for knowledge base retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveConfig) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    import capo_bedrock.types.knowledge_base_retrieval_configuration

    out["knowledgeBaseRetrievalConfiguration"] = (
        capo_bedrock.types.knowledge_base_retrieval_configuration.serialize_json(
            value["knowledge_base_retrieval_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RetrieveConfig:
    out: RetrieveConfig = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("knowledgeBaseRetrievalConfiguration") is not None:
        import capo_bedrock.types.knowledge_base_retrieval_configuration

        out["knowledge_base_retrieval_configuration"] = (
            capo_bedrock.types.knowledge_base_retrieval_configuration.deserialize_json(
                data["knowledgeBaseRetrievalConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RetrieveConfig.knowledge_base_retrieval_configuration required"
        )
    return out


def redact_sensitive(value: RetrieveConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledge_base_retrieval_configuration" in value:
        import capo_bedrock.types.knowledge_base_retrieval_configuration

        out["knowledge_base_retrieval_configuration"] = (
            capo_bedrock.types.knowledge_base_retrieval_configuration.redact_sensitive(
                value["knowledge_base_retrieval_configuration"]
            )
        )
    return out
