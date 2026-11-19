"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.context_change

ContextChangeList: TypeAlias = list[
    "capo_networkmanager.types.context_change.ContextChange"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextChangeList) -> list:
    import capo_networkmanager.types.context_change

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.context_change.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextChangeList:
    import capo_networkmanager.types.context_change

    out: ContextChangeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.context_change.deserialize_json(item))
    return out
