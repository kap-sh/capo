"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#BuildState``."""

from typing import Literal, TypeAlias, cast

BuildState: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BuildState) -> str:
    return value


def deserialize_json(data: str) -> BuildState:
    return cast(BuildState, data)
