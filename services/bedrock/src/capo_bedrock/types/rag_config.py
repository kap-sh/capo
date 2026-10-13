"""Generated from Smithy shape ``com.amazonaws.bedrock#RAGConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_precomputed_rag_source_config
    import capo_bedrock.types.knowledge_base_config


class _RAGConfig_knowledgeBaseConfig(TypedDict, closed=True):
    knowledgeBaseConfig: "capo_bedrock.types.knowledge_base_config.KnowledgeBaseConfig"


class _RAGConfig_precomputedRagSourceConfig(TypedDict, closed=True):
    precomputedRagSourceConfig: "capo_bedrock.types.evaluation_precomputed_rag_source_config.EvaluationPrecomputedRagSourceConfig"


RAGConfig: TypeAlias = (
    _RAGConfig_knowledgeBaseConfig | _RAGConfig_precomputedRagSourceConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: RAGConfig) -> dict:
    if "knowledgeBaseConfig" in value:
        import capo_bedrock.types.knowledge_base_config

        return {
            "knowledgeBaseConfig": capo_bedrock.types.knowledge_base_config.serialize_json(
                value["knowledgeBaseConfig"]
            )
        }
    elif "precomputedRagSourceConfig" in value:
        import capo_bedrock.types.evaluation_precomputed_rag_source_config

        return {
            "precomputedRagSourceConfig": capo_bedrock.types.evaluation_precomputed_rag_source_config.serialize_json(
                value["precomputedRagSourceConfig"]
            )
        }
    else:
        raise SerializationError("RAGConfig: no variant present")


def deserialize_json(data: dict) -> RAGConfig:
    if data.get("knowledgeBaseConfig") is not None:
        import capo_bedrock.types.knowledge_base_config

        return {
            "knowledgeBaseConfig": capo_bedrock.types.knowledge_base_config.deserialize_json(
                data["knowledgeBaseConfig"]
            )
        }
    elif data.get("precomputedRagSourceConfig") is not None:
        import capo_bedrock.types.evaluation_precomputed_rag_source_config

        return {
            "precomputedRagSourceConfig": capo_bedrock.types.evaluation_precomputed_rag_source_config.deserialize_json(
                data["precomputedRagSourceConfig"]
            )
        }
    else:
        raise DeserializationError("RAGConfig: no recognized variant key")


def redact_sensitive(value: RAGConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledgeBaseConfig" in value:
        import capo_bedrock.types.knowledge_base_config

        out["knowledgeBaseConfig"] = (
            capo_bedrock.types.knowledge_base_config.redact_sensitive(
                value["knowledgeBaseConfig"]
            )
        )
    return out
