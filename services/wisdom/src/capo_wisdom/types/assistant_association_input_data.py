"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationInputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.uuid


class _AssistantAssociationInputData_knowledgeBaseId(TypedDict, closed=True):
    knowledgeBaseId: "capo_wisdom.types.uuid.Uuid"


AssistantAssociationInputData: TypeAlias = (
    _AssistantAssociationInputData_knowledgeBaseId | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationInputData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssistantAssociationInputData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "knowledgeBaseId" in value:
        return {"knowledgeBaseId": value["knowledgeBaseId"]}
    else:
        raise SerializationError("AssistantAssociationInputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationInputData:
    if data.get("knowledgeBaseId") is not None:
        return {"knowledgeBaseId": data["knowledgeBaseId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AssistantAssociationInputData: no recognized variant key"
        )
