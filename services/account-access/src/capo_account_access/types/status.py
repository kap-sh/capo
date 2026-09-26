"""Generated from Smithy shape ``com.amazonaws.accountaccess#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "ACTIVE",
    "DELETE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
