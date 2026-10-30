"""Generated from Smithy shape ``com.amazonaws.artifact#InquirySupportMode``."""

from typing import Literal, TypeAlias, cast

InquirySupportMode: TypeAlias = Literal["AI_ONLY",]


# --- restJson1 ser/de ---
def serialize_json(value: InquirySupportMode) -> str:
    return value


def deserialize_json(data: str) -> InquirySupportMode:
    return cast(InquirySupportMode, data)
