"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding_reference

FindingReferences: TypeAlias = list[
    "capo_guardduty.types.finding_reference.FindingReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingReferences) -> list:
    import capo_guardduty.types.finding_reference

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.finding_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingReferences:
    import capo_guardduty.types.finding_reference

    out: FindingReferences = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.finding_reference.deserialize_json(item))
    return out
