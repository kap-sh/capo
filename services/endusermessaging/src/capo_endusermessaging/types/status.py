"""Generated from Smithy shape ``com.amazonaws.endusermessaging#Status``."""

from typing import Literal, TypeAlias, cast

"""Brand profile lifecycle status. Exposed on brand profile API responses (Get, List, Create, Update)."""
Status: TypeAlias = Literal[
    "ACTIVE",
    "BLOCKED",
    "PAUSED",
    "CANCELLED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
