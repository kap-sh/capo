"""Generated from Smithy shape ``com.amazonaws.continuum#PerFindingResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.per_finding_result

PerFindingResults: TypeAlias = list[
    "capo_continuum.types.per_finding_result.PerFindingResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerFindingResults) -> list:
    import capo_continuum.types.per_finding_result

    out: list = []
    for item in value:
        out.append(capo_continuum.types.per_finding_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> PerFindingResults:
    import capo_continuum.types.per_finding_result

    out: PerFindingResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.per_finding_result.deserialize_json(item))
    return out
