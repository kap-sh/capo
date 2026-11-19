"""Generated from Smithy shape ``com.amazonaws.elementalinference#ContextTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.context_type

ContextTypeList: TypeAlias = list[
    "capo_elementalinference.types.context_type.ContextType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextTypeList) -> list:
    import capo_elementalinference.types.context_type

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.context_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextTypeList:
    import capo_elementalinference.types.context_type

    out: ContextTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.context_type.deserialize_json(item))
    return out
