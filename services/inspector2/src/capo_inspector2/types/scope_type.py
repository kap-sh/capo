"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeType``."""

from typing import Literal, TypeAlias, cast

ScopeType: TypeAlias = Literal[
    "TENANT",
    "SUBSCRIPTION",
    "ORGANIZATION",
    "PROJECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeType) -> str:
    return value


def deserialize_json(data: str) -> ScopeType:
    return cast(ScopeType, data)
