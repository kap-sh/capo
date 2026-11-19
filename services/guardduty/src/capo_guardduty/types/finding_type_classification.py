"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeClassification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.percentage


class FindingTypeClassification(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type.</p>"""
    classification: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The classification of the finding type.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings of this type.</p>"""
    percentage: NotRequired["capo_guardduty.types.percentage.Percentage"]
    """<p>The percentage of findings that are of this type, from 0 to 100.</p>"""
    description: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the classification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeClassification) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "classification" in value:
        out["classification"] = value["classification"]
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
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> FindingTypeClassification:
    out: FindingTypeClassification = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("classification") is not None:
        out["classification"] = data["classification"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("percentage") is not None:
        out["percentage"] = float(data["percentage"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
