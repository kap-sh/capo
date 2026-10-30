"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#StopReason``."""

from typing import Literal, TypeAlias, cast

StopReason: TypeAlias = Literal[
    "stop",
    "length",
]


# --- restJson1 ser/de ---
def serialize_json(value: StopReason) -> str:
    return value


def deserialize_json(data: str) -> StopReason:
    return cast(StopReason, data)
