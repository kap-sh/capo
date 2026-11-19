"""Generated from Smithy shape ``com.amazonaws.connecthealth#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

"""Lifecycle status of a Dataset. CREATING -> ACTIVE | CREATE_FAILED; ACTIVE | CREATE_FAILED | DELETE_FAILED -> DELETING -> DELETED | DELETE_FAILED."""
DatasetStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)
