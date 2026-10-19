"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionConfidenceThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_confidence_verdict_threshold


class SuppressionConfidenceThreshold(TypedDict, closed=True):
    confidence_verdict_threshold: "capo_sesv2.types.suppression_confidence_verdict_threshold.SuppressionConfidenceVerdictThreshold"
    """<p>The confidence level threshold for suppression decisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionConfidenceThreshold) -> dict:
    out: dict = {}
    import capo_sesv2.types.suppression_confidence_verdict_threshold

    out["ConfidenceVerdictThreshold"] = (
        capo_sesv2.types.suppression_confidence_verdict_threshold.serialize_json(
            value["confidence_verdict_threshold"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionConfidenceThreshold:
    out: SuppressionConfidenceThreshold = {}  # type: ignore[typeddict-item]
    if data.get("ConfidenceVerdictThreshold") is not None:
        import capo_sesv2.types.suppression_confidence_verdict_threshold

        out["confidence_verdict_threshold"] = (
            capo_sesv2.types.suppression_confidence_verdict_threshold.deserialize_json(
                data["ConfidenceVerdictThreshold"]
            )
        )
    else:
        import typing

        out["confidence_verdict_threshold"] = typing.cast(
            "capo_sesv2.types.suppression_confidence_verdict_threshold.SuppressionConfidenceVerdictThreshold",
            "",
        )
    return out
