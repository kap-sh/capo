"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationOutputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.external_bedrock_knowledge_base_config
    import capo_qconnect.types.knowledge_base_association_data


class _AssistantAssociationOutputData_knowledgeBaseAssociation(TypedDict, closed=True):
    knowledgeBaseAssociation: "capo_qconnect.types.knowledge_base_association_data.KnowledgeBaseAssociationData"


class _AssistantAssociationOutputData_externalBedrockKnowledgeBaseConfig(
    TypedDict, closed=True
):
    externalBedrockKnowledgeBaseConfig: "capo_qconnect.types.external_bedrock_knowledge_base_config.ExternalBedrockKnowledgeBaseConfig"


AssistantAssociationOutputData: TypeAlias = (
    _AssistantAssociationOutputData_knowledgeBaseAssociation
    | _AssistantAssociationOutputData_externalBedrockKnowledgeBaseConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationOutputData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssistantAssociationOutputData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBaseAssociation" in value:
        import capo_qconnect.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_qconnect.types.knowledge_base_association_data.serialize_json(
                value["knowledgeBaseAssociation"]
            )
        }
    elif "externalBedrockKnowledgeBaseConfig" in value:
        import capo_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": capo_qconnect.types.external_bedrock_knowledge_base_config.serialize_json(
                value["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationOutputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationOutputData:
    if data.get("knowledgeBaseAssociation") is not None:
        import capo_qconnect.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_qconnect.types.knowledge_base_association_data.deserialize_json(
                data["knowledgeBaseAssociation"]
            )
        }
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
            "AssistantAssociationOutputData: no recognized variant key"
        )
