"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CircuitBreakerMode``."""

from typing import Literal, TypeAlias, cast

CircuitBreakerMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CircuitBreakerMode) -> str:
    return value


def deserialize_json(data: str) -> CircuitBreakerMode:
    return cast(CircuitBreakerMode, data)
