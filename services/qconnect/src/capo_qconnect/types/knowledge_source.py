"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_association_id_list


class _KnowledgeSource_assistantAssociationIds(TypedDict, closed=True):
    assistantAssociationIds: (
        "capo_qconnect.types.assistant_association_id_list.AssistantAssociationIdList"
    )


KnowledgeSource: TypeAlias = (
    _KnowledgeSource_assistantAssociationIds | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"KnowledgeSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "assistantAssociationIds" in value:
        import capo_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": capo_qconnect.types.assistant_association_id_list.serialize_json(
                value["assistantAssociationIds"]
            )
        }
    else:
        raise SerializationError("KnowledgeSource: no variant present")


def deserialize_json(data: dict) -> KnowledgeSource:
    if data.get("assistantAssociationIds") is not None:
        import capo_qconnect.types.assistant_association_id_list

        return {
            "assistantAssociationIds": capo_qconnect.types.assistant_association_id_list.deserialize_json(
                data["assistantAssociationIds"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("KnowledgeSource: no recognized variant key")
