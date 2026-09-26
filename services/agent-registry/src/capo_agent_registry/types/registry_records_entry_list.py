"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryRecordsEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_records_entry

RegistryRecordsEntryList: TypeAlias = list[
    "capo_agent_registry.types.registry_records_entry.RegistryRecordsEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordsEntryList) -> list:
    import capo_agent_registry.types.registry_records_entry

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry.types.registry_records_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RegistryRecordsEntryList:
    import capo_agent_registry.types.registry_records_entry

    out: RegistryRecordsEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry.types.registry_records_entry.deserialize_json(item)
        )
    return out
