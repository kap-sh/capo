"""Generated from Smithy shape ``com.amazonaws.guardduty#Baseline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type_classifications


class Baseline(TypedDict, closed=True):
    total_findings: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of findings.</p>"""
    baseline_findings: NotRequired[
        "capo_guardduty.types.finding_type_classifications.FindingTypeClassifications"
    ]
    """<p>The finding types that are consistent with normal behavior.</p>"""
    anomalous_findings: NotRequired[
        "capo_guardduty.types.finding_type_classifications.FindingTypeClassifications"
    ]
    """<p>The finding types that deviate from normal behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Baseline) -> dict:
    out: dict = {}
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    if "baseline_findings" in value:
        import capo_guardduty.types.finding_type_classifications

        out["baselineFindings"] = (
            capo_guardduty.types.finding_type_classifications.serialize_json(
                value["baseline_findings"]
            )
        )
    if "anomalous_findings" in value:
        import capo_guardduty.types.finding_type_classifications

        out["anomalousFindings"] = (
            capo_guardduty.types.finding_type_classifications.serialize_json(
                value["anomalous_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Baseline:
    out: Baseline = {}  # type: ignore[typeddict-item]
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    if data.get("baselineFindings") is not None:
        import capo_guardduty.types.finding_type_classifications

        out["baseline_findings"] = (
            capo_guardduty.types.finding_type_classifications.deserialize_json(
                data["baselineFindings"]
            )
        )
    if data.get("anomalousFindings") is not None:
        import capo_guardduty.types.finding_type_classifications

        out["anomalous_findings"] = (
            capo_guardduty.types.finding_type_classifications.deserialize_json(
                data["anomalousFindings"]
            )
        )
    return out
