"""Generated from Smithy shape ``com.amazonaws.location#MultiLinearRings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.linear_rings

MultiLinearRings: TypeAlias = list["capo_location.types.linear_rings.LinearRings"]


# --- restJson1 ser/de ---
def serialize_json(value: MultiLinearRings) -> list:
    import capo_location.types.linear_rings

    out: list = []
    for item in value:
        out.append(capo_location.types.linear_rings.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiLinearRings:
    import capo_location.types.linear_rings

    out: MultiLinearRings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.linear_rings.deserialize_json(item))
    return out


def redact_sensitive(value: MultiLinearRings) -> list[Any]:
    import capo_location.types.linear_rings

    return [capo_location.types.linear_rings.redact_sensitive(item) for item in value]
