"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageVersionState``."""

from typing import Literal, TypeAlias, cast

MicrovmImageVersionState: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageVersionState) -> str:
    return value


def deserialize_json(data: str) -> MicrovmImageVersionState:
    return cast(MicrovmImageVersionState, data)
