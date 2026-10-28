"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationInputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.external_bedrock_knowledge_base_config
    import capo_qconnect.types.uuid


class AssistantAssociationInputDataKnowledgeBaseIdMember(TypedDict, closed=True):
    knowledgeBaseId: "capo_qconnect.types.uuid.Uuid"


class AssistantAssociationInputDataExternalBedrockKnowledgeBaseConfigMember(
    TypedDict, closed=True
):
    externalBedrockKnowledgeBaseConfig: "capo_qconnect.types.external_bedrock_knowledge_base_config.ExternalBedrockKnowledgeBaseConfig"


AssistantAssociationInputData: TypeAlias = (
    AssistantAssociationInputDataKnowledgeBaseIdMember
    | AssistantAssociationInputDataExternalBedrockKnowledgeBaseConfigMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationInputData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssistantAssociationInputData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBaseId" in value:
        return {"knowledgeBaseId": value["knowledgeBaseId"]}
    elif "externalBedrockKnowledgeBaseConfig" in value:
        import capo_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": capo_qconnect.types.external_bedrock_knowledge_base_config.serialize_json(
                value["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationInputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationInputData:
    if data.get("knowledgeBaseId") is not None:
        return {"knowledgeBaseId": data["knowledgeBaseId"]}
    elif data.get("externalBedrockKnowledgeBaseConfig") is not None:
        import capo_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": capo_qconnect.types.external_bedrock_knowledge_base_config.deserialize_json(
                data["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AssistantAssociationInputData: no recognized variant key"
        )
