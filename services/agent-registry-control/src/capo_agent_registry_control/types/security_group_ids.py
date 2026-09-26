"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.security_group_identifier

SecurityGroupIds: TypeAlias = list[
    "capo_agent_registry_control.types.security_group_identifier.SecurityGroupIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return [item for item in data if item is not None]
