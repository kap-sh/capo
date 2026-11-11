"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldIdentifierUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_name


class FieldIdentifierUnionIdMember(TypedDict, closed=True):
    id: "capo_connectcases.types.field_id.FieldId"


class FieldIdentifierUnionNameMember(TypedDict, closed=True):
    name: "capo_connectcases.types.field_name.FieldName"


FieldIdentifierUnion: TypeAlias = (
    FieldIdentifierUnionIdMember | FieldIdentifierUnionNameMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldIdentifierUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FieldIdentifierUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "id" in value:
        return {"id": value["id"]}
    elif "name" in value:
        return {"name": value["name"]}
    else:
        raise SerializationError("FieldIdentifierUnion: no variant present")


def deserialize_json(data: dict) -> FieldIdentifierUnion:
    if data.get("id") is not None:
        return {"id": data["id"]}
    elif data.get("name") is not None:
        return {"name": data["name"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FieldIdentifierUnion: no recognized variant key")
