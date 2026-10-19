"""Generated from Smithy shape ``com.amazonaws.qconnect#AssociationConfigurationData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_association_configuration_data


class _AssociationConfigurationData_knowledgeBaseAssociationConfigurationData(
    TypedDict, closed=True
):
    knowledgeBaseAssociationConfigurationData: "capo_qconnect.types.knowledge_base_association_configuration_data.KnowledgeBaseAssociationConfigurationData"


AssociationConfigurationData: TypeAlias = (
    _AssociationConfigurationData_knowledgeBaseAssociationConfigurationData
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssociationConfigurationData) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AssociationConfigurationData: cannot serialize unknown variant {value.name!r}"
        )
    elif "knowledgeBaseAssociationConfigurationData" in value:
        import capo_qconnect.types.knowledge_base_association_configuration_data

        return {
            "knowledgeBaseAssociationConfigurationData": capo_qconnect.types.knowledge_base_association_configuration_data.serialize_json(
                value["knowledgeBaseAssociationConfigurationData"]
            )
        }
    else:
        raise SerializationError("AssociationConfigurationData: no variant present")


def deserialize_json(data: dict) -> AssociationConfigurationData:
    if data.get("knowledgeBaseAssociationConfigurationData") is not None:
        import capo_qconnect.types.knowledge_base_association_configuration_data

        return {
            "knowledgeBaseAssociationConfigurationData": capo_qconnect.types.knowledge_base_association_configuration_data.deserialize_json(
                data["knowledgeBaseAssociationConfigurationData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AssociationConfigurationData: no recognized variant key"
        )
