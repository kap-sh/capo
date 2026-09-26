"""Generated from Smithy shape ``com.amazonaws.agentregistry#DiscoverableFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry.types.filter_value

DiscoverableFilterValues: TypeAlias = list[
    "capo_agent_registry.types.filter_value.FilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoverableFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DiscoverableFilterValues:
    return [item for item in data if item is not None]
