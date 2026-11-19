"""Generated from Smithy shape ``com.amazonaws.guardduty#FoundationalDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_detector_feature

FoundationalDataSources: TypeAlias = list[
    "capo_guardduty.types.investigation_detector_feature.InvestigationDetectorFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: FoundationalDataSources) -> list:
    import capo_guardduty.types.investigation_detector_feature

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.investigation_detector_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FoundationalDataSources:
    import capo_guardduty.types.investigation_detector_feature

    out: FoundationalDataSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.investigation_detector_feature.deserialize_json(item)
        )
    return out
