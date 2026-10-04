"""Generated from Smithy shape ``com.amazonaws.deadline#IntStringListList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.nested_int_string_list

IntStringListList: TypeAlias = list[
    "capo_deadline.types.nested_int_string_list.NestedIntStringList"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntStringListList) -> list:
    import capo_deadline.types.nested_int_string_list

    out: list = []
    for item in value:
        out.append(capo_deadline.types.nested_int_string_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntStringListList:
    import capo_deadline.types.nested_int_string_list

    out: IntStringListList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.nested_int_string_list.deserialize_json(item))
    return out
