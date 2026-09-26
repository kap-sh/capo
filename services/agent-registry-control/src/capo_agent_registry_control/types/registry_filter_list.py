"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_filter

RegistryFilterList: TypeAlias = list[
    "capo_agent_registry_control.types.registry_filter.RegistryFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryFilterList) -> list:
    import capo_agent_registry_control.types.registry_filter

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.registry_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RegistryFilterList:
    import capo_agent_registry_control.types.registry_filter

    out: RegistryFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.registry_filter.deserialize_json(item)
        )
    return out
