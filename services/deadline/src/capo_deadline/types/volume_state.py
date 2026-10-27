"""Generated from Smithy shape ``com.amazonaws.deadline#VolumeState``."""

from typing import Literal, TypeAlias, cast

"""The state of a persistent volume."""
VolumeState: TypeAlias = Literal[
    "PENDING_CREATION",
    "PENDING_ATTACHMENT",
    "IN_USE",
    "AVAILABLE",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeState) -> str:
    return value


def deserialize_json(data: str) -> VolumeState:
    return cast(VolumeState, data)
