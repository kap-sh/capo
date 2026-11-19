"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStoreAssociationState``."""

from typing import Literal, TypeAlias, cast

ContextStoreAssociationState: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATED",
    "DISASSOCIATING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextStoreAssociationState) -> str:
    return value


def deserialize_json(data: str) -> ContextStoreAssociationState:
    return cast(ContextStoreAssociationState, data)
