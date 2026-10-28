"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieverConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration


class RetrieverConfigurationKnowledgeBaseMember(TypedDict, closed=True):
    knowledgeBase: "capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration.KnowledgeBaseRetrieverConfiguration"


RetrieverConfiguration: TypeAlias = (
    RetrieverConfigurationKnowledgeBaseMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetrieverConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBase" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration

        return {
            "knowledgeBase": capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration.serialize_json(
                value["knowledgeBase"]
            )
        }
    else:
        raise SerializationError("RetrieverConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrieverConfiguration:
    if data.get("knowledgeBase") is not None:
        import capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration

        return {
            "knowledgeBase": capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration.deserialize_json(
                data["knowledgeBase"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RetrieverConfiguration: no recognized variant key")


def redact_sensitive(value: RetrieverConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledgeBase" in value:
        import capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration

        out["knowledgeBase"] = (
            capo_bedrock_agent_runtime.types.knowledge_base_retriever_configuration.redact_sensitive(
                value["knowledgeBase"]
            )
        )
    return out
