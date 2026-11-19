"""Generated from Smithy shape ``com.amazonaws.guardduty#ObservedFindingType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.severity_score
    import capo_guardduty.types.shared_resources


class ObservedFindingType(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings of this type.</p>"""
    severity_max: NotRequired["capo_guardduty.types.severity_score.SeverityScore"]
    """<p>The highest severity score among the findings of this type, from 0 to 10.</p>"""
    shared_resources: NotRequired[
        "capo_guardduty.types.shared_resources.SharedResources"
    ]
    """<p>The resources that the findings of this type share with the investigated activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObservedFindingType) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "count" in value:
        out["count"] = value["count"]
    if "severity_max" in value:
        out["severityMax"] = (
            "NaN"
            if value["severity_max"] != value["severity_max"]
            else "Infinity"
            if value["severity_max"] == float("inf")
            else "-Infinity"
            if value["severity_max"] == float("-inf")
            else value["severity_max"]
        )
    if "shared_resources" in value:
        import capo_guardduty.types.shared_resources

        out["sharedResources"] = capo_guardduty.types.shared_resources.serialize_json(
            value["shared_resources"]
        )
    return out


def deserialize_json(data: dict) -> ObservedFindingType:
    out: ObservedFindingType = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("severityMax") is not None:
        out["severity_max"] = float(data["severityMax"])
    if data.get("sharedResources") is not None:
        import capo_guardduty.types.shared_resources

        out["shared_resources"] = (
            capo_guardduty.types.shared_resources.deserialize_json(
                data["sharedResources"]
            )
        )
    return out
