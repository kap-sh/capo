"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#SynchronizationStatus``."""

from typing import Literal, TypeAlias, cast

SynchronizationStatus: TypeAlias = Literal[
    "IN_SYNC",
    "OUT_OF_SYNC",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizationStatus) -> str:
    return value


def deserialize_json(data: str) -> SynchronizationStatus:
    return cast(SynchronizationStatus, data)
