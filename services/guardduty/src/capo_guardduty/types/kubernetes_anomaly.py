"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesAnomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class KubernetesAnomaly(TypedDict, closed=True):
    unusual_behavior: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the unusual behavior.</p>"""
    baseline_context: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the normal behavior that the activity was compared against.</p>"""
    anomaly_score: NotRequired["capo_guardduty.types.string.String"]
    """<p>The anomaly score of the behavior.</p>"""
    training_period: NotRequired["capo_guardduty.types.string.String"]
    """<p>The period over which the normal behavior was established.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesAnomaly) -> dict:
    out: dict = {}
    if "unusual_behavior" in value:
        out["unusualBehavior"] = value["unusual_behavior"]
    if "baseline_context" in value:
        out["baselineContext"] = value["baseline_context"]
    if "anomaly_score" in value:
        out["anomalyScore"] = value["anomaly_score"]
    if "training_period" in value:
        out["trainingPeriod"] = value["training_period"]
    return out


def deserialize_json(data: dict) -> KubernetesAnomaly:
    out: KubernetesAnomaly = {}  # type: ignore[typeddict-item]
    if data.get("unusualBehavior") is not None:
        out["unusual_behavior"] = data["unusualBehavior"]
    if data.get("baselineContext") is not None:
        out["baseline_context"] = data["baselineContext"]
    if data.get("anomalyScore") is not None:
        out["anomaly_score"] = data["anomalyScore"]
    if data.get("trainingPeriod") is not None:
        out["training_period"] = data["trainingPeriod"]
    return out
