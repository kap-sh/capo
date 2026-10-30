"""Generated from Smithy shape ``com.amazonaws.continuum#AssociatedCollectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.associated_collector

AssociatedCollectors: TypeAlias = list[
    "capo_continuum.types.associated_collector.AssociatedCollector"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedCollectors) -> list:
    import capo_continuum.types.associated_collector

    out: list = []
    for item in value:
        out.append(capo_continuum.types.associated_collector.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedCollectors:
    import capo_continuum.types.associated_collector

    out: AssociatedCollectors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.associated_collector.deserialize_json(item))
    return out
