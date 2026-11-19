"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeClassifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding_type_classification

FindingTypeClassifications: TypeAlias = list[
    "capo_guardduty.types.finding_type_classification.FindingTypeClassification"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeClassifications) -> list:
    import capo_guardduty.types.finding_type_classification

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.finding_type_classification.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingTypeClassifications:
    import capo_guardduty.types.finding_type_classification

    out: FindingTypeClassifications = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.finding_type_classification.deserialize_json(item)
        )
    return out
