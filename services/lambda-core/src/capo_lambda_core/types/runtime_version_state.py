"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeVersionState``."""

from typing import Literal, TypeAlias, cast

"""The state of a runtime version."""
RuntimeVersionState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "FAILED",
    "DELETING",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionState) -> str:
    return value


def deserialize_json(data: str) -> RuntimeVersionState:
    return cast(RuntimeVersionState, data)
