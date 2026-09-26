"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.subnet_id

SubnetIds: TypeAlias = list["capo_agent_registry_control.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return [item for item in data if item is not None]
