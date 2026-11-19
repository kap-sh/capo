"""Generated from Smithy shape ``com.amazonaws.guardduty#ObservedFindingTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.observed_finding_type

ObservedFindingTypes: TypeAlias = list[
    "capo_guardduty.types.observed_finding_type.ObservedFindingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObservedFindingTypes) -> list:
    import capo_guardduty.types.observed_finding_type

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.observed_finding_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ObservedFindingTypes:
    import capo_guardduty.types.observed_finding_type

    out: ObservedFindingTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.observed_finding_type.deserialize_json(item))
    return out
