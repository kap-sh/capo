"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FallbackError``."""

from typing import Literal, TypeAlias, cast

FallbackError: TypeAlias = Literal[
    "CONNECTION_ERROR",
    "FIRST_BYTE_TIMEOUT",
    "UNROUTABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FallbackError) -> str:
    return value


def deserialize_json(data: str) -> FallbackError:
    return cast(FallbackError, data)
