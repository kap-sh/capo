"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordFilterName``."""

from typing import Literal, TypeAlias, cast

RegistryRecordFilterName: TypeAlias = Literal[
    "name",
    "status",
    "recordType",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordFilterName) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordFilterName:
    return cast(RegistryRecordFilterName, data)
