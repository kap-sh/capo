"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeValues``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_string_values_list


class _PredefinedAttributeValues_StringList(TypedDict, closed=True):
    StringList: "capo_connect.types.predefined_attribute_string_values_list.PredefinedAttributeStringValuesList"


PredefinedAttributeValues: TypeAlias = (
    _PredefinedAttributeValues_StringList | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeValues) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PredefinedAttributeValues: cannot serialize unknown variant {value.name!r}"
        )
    elif "StringList" in value:
        import capo_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": capo_connect.types.predefined_attribute_string_values_list.serialize_json(
                value["StringList"]
            )
        }
    else:
        raise SerializationError("PredefinedAttributeValues: no variant present")


def deserialize_json(data: dict) -> PredefinedAttributeValues:
    if data.get("StringList") is not None:
        import capo_connect.types.predefined_attribute_string_values_list

        return {
            "StringList": capo_connect.types.predefined_attribute_string_values_list.deserialize_json(
                data["StringList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "PredefinedAttributeValues: no recognized variant key"
        )
