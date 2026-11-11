"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_value_input

FieldValueInputList: TypeAlias = list[
    "capo_connectcases.types.field_value_input.FieldValueInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueInputList) -> list:
    import capo_connectcases.types.field_value_input

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_value_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldValueInputList:
    import capo_connectcases.types.field_value_input

    out: FieldValueInputList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connectcases.types.field_value_input.deserialize_json(item))
    return out
