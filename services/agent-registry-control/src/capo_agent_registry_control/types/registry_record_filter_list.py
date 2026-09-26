"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_record_filter

RegistryRecordFilterList: TypeAlias = list[
    "capo_agent_registry_control.types.registry_record_filter.RegistryRecordFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordFilterList) -> list:
    import capo_agent_registry_control.types.registry_record_filter

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.registry_record_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistryRecordFilterList:
    import capo_agent_registry_control.types.registry_record_filter

    out: RegistryRecordFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.registry_record_filter.deserialize_json(
                item
            )
        )
    return out
