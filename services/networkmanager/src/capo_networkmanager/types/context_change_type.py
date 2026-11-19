"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextChangeType``."""

from typing import Literal, TypeAlias, cast

ContextChangeType: TypeAlias = Literal[
    "ADDED",
    "REMOVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextChangeType) -> str:
    return value


def deserialize_json(data: str) -> ContextChangeType:
    return cast(ContextChangeType, data)
