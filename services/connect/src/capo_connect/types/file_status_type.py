"""Generated from Smithy shape ``com.amazonaws.connect#FileStatusType``."""

from typing import Literal, TypeAlias, cast

FileStatusType: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "PROCESSING",
    "FAILED",
    "DRAFTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileStatusType) -> str:
    return value


def deserialize_json(data: str) -> FileStatusType:
    return cast(FileStatusType, data)
