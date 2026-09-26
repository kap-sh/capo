"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AllowedAudienceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.allowed_audience

AllowedAudienceList: TypeAlias = list[
    "capo_agent_registry_control.types.allowed_audience.AllowedAudience"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAudienceList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedAudienceList:
    return [item for item in data if item is not None]
