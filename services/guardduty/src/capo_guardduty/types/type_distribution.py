"""Generated from Smithy shape ``com.amazonaws.guardduty#TypeDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.percentage
    import capo_guardduty.types.string


class TypeDistribution(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings of this type.</p>"""
    percentage: NotRequired["capo_guardduty.types.percentage.Percentage"]
    """<p>The percentage of findings that are of this type, from 0 to 100.</p>"""
    dominant_severity: NotRequired["capo_guardduty.types.string.String"]
    """<p>The most common severity among findings of this type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypeDistribution) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "count" in value:
        out["count"] = value["count"]
    if "percentage" in value:
        out["percentage"] = (
            "NaN"
            if value["percentage"] != value["percentage"]
            else "Infinity"
            if value["percentage"] == float("inf")
            else "-Infinity"
            if value["percentage"] == float("-inf")
            else value["percentage"]
        )
    if "dominant_severity" in value:
        out["dominantSeverity"] = value["dominant_severity"]
    return out


def deserialize_json(data: dict) -> TypeDistribution:
    out: TypeDistribution = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("percentage") is not None:
        out["percentage"] = float(data["percentage"])
    if data.get("dominantSeverity") is not None:
        out["dominant_severity"] = data["dominantSeverity"]
    return out
