"""Generated from Smithy shape ``com.amazonaws.connectcases#Section``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.field_group


class _Section_fieldGroup(TypedDict, closed=True):
    fieldGroup: "capo_connectcases.types.field_group.FieldGroup"


Section: TypeAlias = _Section_fieldGroup | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Section) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Section: cannot serialize unknown variant {value.name!r}"
        )
    elif "fieldGroup" in value:
        import capo_connectcases.types.field_group

        return {
            "fieldGroup": capo_connectcases.types.field_group.serialize_json(
                value["fieldGroup"]
            )
        }
    else:
        raise SerializationError("Section: no variant present")


def deserialize_json(data: dict) -> Section:
    if data.get("fieldGroup") is not None:
        import capo_connectcases.types.field_group

        return {
            "fieldGroup": capo_connectcases.types.field_group.deserialize_json(
                data["fieldGroup"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Section: no recognized variant key")
