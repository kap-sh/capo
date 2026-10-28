"""Generated from Smithy shape ``com.amazonaws.bedrock#RAGConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_precomputed_rag_source_config
    import capo_bedrock.types.knowledge_base_config


class RAGConfigKnowledgeBaseConfigMember(TypedDict, closed=True):
    knowledgeBaseConfig: "capo_bedrock.types.knowledge_base_config.KnowledgeBaseConfig"


class RAGConfigPrecomputedRagSourceConfigMember(TypedDict, closed=True):
    precomputedRagSourceConfig: "capo_bedrock.types.evaluation_precomputed_rag_source_config.EvaluationPrecomputedRagSourceConfig"


RAGConfig: TypeAlias = (
    RAGConfigKnowledgeBaseConfigMember
    | RAGConfigPrecomputedRagSourceConfigMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RAGConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RAGConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBaseConfig" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
