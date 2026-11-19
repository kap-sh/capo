"""Generated from Smithy shape ``com.amazonaws.guardduty#RepresentativeFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.risk_level
    import capo_guardduty.types.string


class RepresentativeFinding(TypedDict, closed=True):
    resource_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the affected resource.</p>"""
    identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the affected resource.</p>"""
    finding_id: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>The ID of the representative finding.</p>"""
    finding_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings for the resource.</p>"""
    risk_level: NotRequired["capo_guardduty.types.risk_level.RiskLevel"]
    """<p>The assessed risk level of the resource. Possible values are <code>Info</code>, <code>Low</code>, <code>Medium</code>, <code>High</code>, and <code>Critical</code>.</p>"""
    risk_rationale: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The reason for the assessed risk level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepresentativeFinding) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    if "risk_level" in value:
        import capo_guardduty.types.risk_level

        out["riskLevel"] = capo_guardduty.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "risk_rationale" in value:
        out["riskRationale"] = value["risk_rationale"]
    return out


def deserialize_json(data: dict) -> RepresentativeFinding:
    out: RepresentativeFinding = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    if data.get("riskLevel") is not None:
        import capo_guardduty.types.risk_level

        out["risk_level"] = capo_guardduty.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("riskRationale") is not None:
        out["risk_rationale"] = data["riskRationale"]
    return out
