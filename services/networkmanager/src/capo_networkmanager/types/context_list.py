"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.context_entry

ContextList: TypeAlias = list["capo_networkmanager.types.context_entry.ContextEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextList) -> list:
    import capo_networkmanager.types.context_entry

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.context_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextList:
    import capo_networkmanager.types.context_entry

    out: ContextList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.context_entry.deserialize_json(item))
    return out
