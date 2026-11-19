"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationAccountAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.baseline
    import capo_guardduty.types.trend


class InvestigationAccountAnalysis(TypedDict, closed=True):
    trend: NotRequired["capo_guardduty.types.trend.Trend"]
    """<p>The trend of findings over time. Set when <code>AnalysisType</code> is <code>TREND</code>.</p>"""
    baseline: NotRequired["capo_guardduty.types.baseline.Baseline"]
    """<p>A comparison of findings against normal behavior. Set when <code>AnalysisType</code> is <code>BASELINE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationAccountAnalysis) -> dict:
    out: dict = {}
    if "trend" in value:
        import capo_guardduty.types.trend

        out["trend"] = capo_guardduty.types.trend.serialize_json(value["trend"])
    if "baseline" in value:
        import capo_guardduty.types.baseline

        out["baseline"] = capo_guardduty.types.baseline.serialize_json(
            value["baseline"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationAccountAnalysis:
    out: InvestigationAccountAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("trend") is not None:
        import capo_guardduty.types.trend

        out["trend"] = capo_guardduty.types.trend.deserialize_json(data["trend"])
    if data.get("baseline") is not None:
        import capo_guardduty.types.baseline

        out["baseline"] = capo_guardduty.types.baseline.deserialize_json(
            data["baseline"]
        )
    return out
