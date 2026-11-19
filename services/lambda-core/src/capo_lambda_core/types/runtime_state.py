"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeState``."""

from typing import Literal, TypeAlias, cast

"""The state of the runtime. The state is automatically managed by the service and indicates the current status of the runtime."""
RuntimeState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_DELETION",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeState) -> str:
    return value


def deserialize_json(data: str) -> RuntimeState:
    return cast(RuntimeState, data)
