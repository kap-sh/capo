"""Generated from Smithy shape ``com.amazonaws.mgn#PropertiesToDelete``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.enriched_property_key

PropertiesToDelete: TypeAlias = list[
    "capo_mgn.types.enriched_property_key.EnrichedPropertyKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertiesToDelete) -> list:
    return list(value)


def deserialize_json(data: list) -> PropertiesToDelete:
    return [item for item in data if item is not None]
