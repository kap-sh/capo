"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AllowedScopesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.allowed_scope_type

AllowedScopesType: TypeAlias = list[
    "capo_agent_registry_control.types.allowed_scope_type.AllowedScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedScopesType) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedScopesType:
    return [item for item in data if item is not None]
