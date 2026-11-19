"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStoreAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_association

ContextStoreAssociationList: TypeAlias = list[
    "capo_networkmanager.types.context_store_association.ContextStoreAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextStoreAssociationList) -> list:
    import capo_networkmanager.types.context_store_association

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.context_store_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContextStoreAssociationList:
    import capo_networkmanager.types.context_store_association

    out: ContextStoreAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_networkmanager.types.context_store_association.deserialize_json(item)
        )
    return out
