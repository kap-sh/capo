"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextStoreState``."""

from typing import Literal, TypeAlias, cast

ContextStoreState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "UPDATING",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextStoreState) -> str:
    return value


def deserialize_json(data: str) -> ContextStoreState:
    return cast(ContextStoreState, data)
