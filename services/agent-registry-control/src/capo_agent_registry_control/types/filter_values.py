"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.filter_value

FilterValues: TypeAlias = list[
    "capo_agent_registry_control.types.filter_value.FilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValues:
    return [item for item in data if item is not None]
