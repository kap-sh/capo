"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationOutputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.knowledge_base_association_data


class AssistantAssociationOutputDataKnowledgeBaseAssociationMember(
    TypedDict, closed=True
):
    knowledgeBaseAssociation: (
        "capo_wisdom.types.knowledge_base_association_data.KnowledgeBaseAssociationData"
    )


AssistantAssociationOutputData: TypeAlias = (
    AssistantAssociationOutputDataKnowledgeBaseAssociationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationOutputData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssistantAssociationOutputData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBaseAssociation" in value:
        import capo_wisdom.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_wisdom.types.knowledge_base_association_data.serialize_json(
                value["knowledgeBaseAssociation"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationOutputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationOutputData:
    if data.get("knowledgeBaseAssociation") is not None:
        import capo_wisdom.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": capo_wisdom.types.knowledge_base_association_data.deserialize_json(
                data["knowledgeBaseAssociation"]
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
