"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionConditionThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.feature_status
    import capo_sesv2.types.suppression_confidence_threshold


class SuppressionConditionThreshold(TypedDict, closed=True):
    condition_threshold_enabled: "capo_sesv2.types.feature_status.FeatureStatus"
    """<p>Indicates whether Auto Validation is enabled for suppression. Set to <code>ENABLED</code> to enable the Auto Validation feature, or set to <code>DISABLED</code> to disable it.</p>"""
    overall_confidence_threshold: NotRequired[
        "capo_sesv2.types.suppression_confidence_threshold.SuppressionConfidenceThreshold"
    ]
    """<p>The overall confidence threshold used to determine suppression decisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionConditionThreshold) -> dict:
    out: dict = {}
    import capo_sesv2.types.feature_status

    out["ConditionThresholdEnabled"] = capo_sesv2.types.feature_status.serialize_json(
        value["condition_threshold_enabled"]
    )
    if "overall_confidence_threshold" in value:
        import capo_sesv2.types.suppression_confidence_threshold

        out["OverallConfidenceThreshold"] = (
            capo_sesv2.types.suppression_confidence_threshold.serialize_json(
                value["overall_confidence_threshold"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuppressionConditionThreshold:
    out: SuppressionConditionThreshold = {}  # type: ignore[typeddict-item]
    if data.get("ConditionThresholdEnabled") is not None:
        import capo_sesv2.types.feature_status

        out["condition_threshold_enabled"] = (
            capo_sesv2.types.feature_status.deserialize_json(
                data["ConditionThresholdEnabled"]
            )
        )
    else:
        import typing

        out["condition_threshold_enabled"] = typing.cast(
            "capo_sesv2.types.feature_status.FeatureStatus", ""
        )
    if data.get("OverallConfidenceThreshold") is not None:
        import capo_sesv2.types.suppression_confidence_threshold

        out["overall_confidence_threshold"] = (
            capo_sesv2.types.suppression_confidence_threshold.deserialize_json(
                data["OverallConfidenceThreshold"]
            )
        )
    return out
