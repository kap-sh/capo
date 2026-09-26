"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.registry_identifier

RegistryIdList: TypeAlias = list[
    "capo_agent_registry.types.registry_identifier.RegistryIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegistryIdList:
    return [item for item in data if item is not None]
