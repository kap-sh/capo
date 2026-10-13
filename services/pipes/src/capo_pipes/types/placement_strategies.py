"""Generated from Smithy shape ``com.amazonaws.pipes#PlacementStrategies``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.placement_strategy

PlacementStrategies: TypeAlias = list[
    "capo_pipes.types.placement_strategy.PlacementStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlacementStrategies) -> list:
    import capo_pipes.types.placement_strategy

    out: list = []
    for item in value:
        out.append(capo_pipes.types.placement_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlacementStrategies:
    import capo_pipes.types.placement_strategy

    out: PlacementStrategies = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pipes.types.placement_strategy.deserialize_json(item))
    return out


def redact_sensitive(value: PlacementStrategies) -> list[Any]:
    import capo_pipes.types.placement_strategy

    return [
        capo_pipes.types.placement_strategy.redact_sensitive(item) for item in value
    ]
