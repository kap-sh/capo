"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceStatus``."""

from typing import Literal, TypeAlias, cast

ReferenceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
    "APPROVED",
    "REJECTED",
    "PROCESSING",
    "FAILED",
    "DRAFTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceStatus) -> str:
    return value


def deserialize_json(data: str) -> ReferenceStatus:
    return cast(ReferenceStatus, data)
