"""Generated from Smithy shape ``com.amazonaws.connectcases#OperandOne``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_id


class _OperandOne_fieldId(TypedDict, closed=True):
    fieldId: "capo_connectcases.types.field_id.FieldId"


OperandOne: TypeAlias = _OperandOne_fieldId | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OperandOne) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"OperandOne: cannot serialize unknown variant {value.name!r}"
        )
    elif "fieldId" in value:
        return {"fieldId": value["fieldId"]}
    else:
        raise SerializationError("OperandOne: no variant present")


def deserialize_json(data: dict) -> OperandOne:
    if data.get("fieldId") is not None:
        return {"fieldId": data["fieldId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("OperandOne: no recognized variant key")
