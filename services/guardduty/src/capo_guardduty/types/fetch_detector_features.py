"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchDetectorFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_detector_feature_configuration

FetchDetectorFeatures: TypeAlias = list[
    "capo_guardduty.types.investigation_detector_feature_configuration.InvestigationDetectorFeatureConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchDetectorFeatures) -> list:
    import capo_guardduty.types.investigation_detector_feature_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.investigation_detector_feature_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FetchDetectorFeatures:
    import capo_guardduty.types.investigation_detector_feature_configuration

    out: FetchDetectorFeatures = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.investigation_detector_feature_configuration.deserialize_json(
                item
            )
        )
    return out
