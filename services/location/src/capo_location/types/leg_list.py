"""Generated from Smithy shape ``com.amazonaws.location#LegList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.leg

LegList: TypeAlias = list["capo_location.types.leg.Leg"]


# --- restJson1 ser/de ---
def serialize_json(value: LegList) -> list:
    import capo_location.types.leg

    out: list = []
    for item in value:
        out.append(capo_location.types.leg.serialize_json(item))
    return out


def deserialize_json(data: list) -> LegList:
    import capo_location.types.leg

    out: LegList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_location.types.leg.deserialize_json(item))
    return out


def redact_sensitive(value: LegList) -> list[Any]:
    import capo_location.types.leg

    return [capo_location.types.leg.redact_sensitive(item) for item in value]
