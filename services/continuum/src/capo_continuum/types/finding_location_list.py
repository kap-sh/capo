"""Generated from Smithy shape ``com.amazonaws.continuum#FindingLocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_location

FindingLocationList: TypeAlias = list[
    "capo_continuum.types.finding_location.FindingLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingLocationList) -> list:
    import capo_continuum.types.finding_location

    out: list = []
    for item in value:
        out.append(capo_continuum.types.finding_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingLocationList:
    import capo_continuum.types.finding_location

    out: FindingLocationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.finding_location.deserialize_json(item))
    return out
