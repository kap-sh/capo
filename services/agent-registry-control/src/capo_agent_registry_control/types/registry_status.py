"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryStatus``."""

from typing import Literal, TypeAlias, cast

RegistryStatus: TypeAlias = Literal[
    "CREATING",
    "READY",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryStatus:
    return cast(RegistryStatus, data)
