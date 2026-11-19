"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store

ContextStoreList: TypeAlias = list[
    "capo_networkmanager.types.context_store.ContextStore"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextStoreList) -> list:
    import capo_networkmanager.types.context_store

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.context_store.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContextStoreList:
    import capo_networkmanager.types.context_store

    out: ContextStoreList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.context_store.deserialize_json(item))
    return out
