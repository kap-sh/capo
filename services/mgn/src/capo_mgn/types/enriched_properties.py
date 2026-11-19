"""Generated from Smithy shape ``com.amazonaws.mgn#EnrichedProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.enriched_property_key

EnrichedProperties: TypeAlias = dict[
    "capo_mgn.types.enriched_property_key.EnrichedPropertyKey", "object"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnrichedProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EnrichedProperties:
    out: EnrichedProperties = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
