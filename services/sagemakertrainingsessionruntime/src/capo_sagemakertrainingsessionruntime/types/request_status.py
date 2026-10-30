"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#RequestStatus``."""

from typing import Literal, TypeAlias, cast

RequestStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Skipped",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestStatus) -> str:
    return value


def deserialize_json(data: str) -> RequestStatus:
    return cast(RequestStatus, data)
