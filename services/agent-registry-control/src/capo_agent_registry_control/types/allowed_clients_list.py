"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AllowedClientsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.allowed_client

AllowedClientsList: TypeAlias = list[
    "capo_agent_registry_control.types.allowed_client.AllowedClient"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedClientsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedClientsList:
    return [item for item in data if item is not None]
