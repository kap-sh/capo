"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#Scheme``."""

from typing import Literal, TypeAlias, cast

Scheme: TypeAlias = Literal[
    "internet-facing",
    "internal",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scheme) -> str:
    return value


def deserialize_json(data: str) -> Scheme:
    return cast(Scheme, data)
