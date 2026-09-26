"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageState``."""

from typing import Literal, TypeAlias, cast

MicrovmImageState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageState) -> str:
    return value


def deserialize_json(data: str) -> MicrovmImageState:
    return cast(MicrovmImageState, data)
