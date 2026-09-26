"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#MatchValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.match_value_string

MatchValueStringList: TypeAlias = list[
    "capo_agent_registry_control.types.match_value_string.MatchValueString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchValueStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchValueStringList:
    return [item for item in data if item is not None]
