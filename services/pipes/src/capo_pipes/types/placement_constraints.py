"""Generated from Smithy shape ``com.amazonaws.pipes#PlacementConstraints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.placement_constraint

PlacementConstraints: TypeAlias = list[
    "capo_pipes.types.placement_constraint.PlacementConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlacementConstraints) -> list:
    import capo_pipes.types.placement_constraint

    out: list = []
    for item in value:
        out.append(capo_pipes.types.placement_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlacementConstraints:
    import capo_pipes.types.placement_constraint

    out: PlacementConstraints = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pipes.types.placement_constraint.deserialize_json(item))
    return out


def redact_sensitive(value: PlacementConstraints) -> list[Any]:
    import capo_pipes.types.placement_constraint

    return [
        capo_pipes.types.placement_constraint.redact_sensitive(item) for item in value
    ]
