"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryRecordIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.record_identifier

RegistryRecordIdList: TypeAlias = list[
    "capo_agent_registry.types.record_identifier.RecordIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegistryRecordIdList:
    return [item for item in data if item is not None]
