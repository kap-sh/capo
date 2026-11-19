"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding_type_count

FindingTypeCounts: TypeAlias = list[
    "capo_guardduty.types.finding_type_count.FindingTypeCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeCounts) -> list:
    import capo_guardduty.types.finding_type_count

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.finding_type_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingTypeCounts:
    import capo_guardduty.types.finding_type_count

    out: FindingTypeCounts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.finding_type_count.deserialize_json(item))
    return out
