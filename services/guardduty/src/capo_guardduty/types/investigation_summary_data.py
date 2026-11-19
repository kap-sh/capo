"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationSummaryData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_analysis
    import capo_guardduty.types.countermeasures
    import capo_guardduty.types.key_observations
    import capo_guardduty.types.organization_analysis
    import capo_guardduty.types.recommendations
    import capo_guardduty.types.string
    import capo_guardduty.types.threat_assessment


class InvestigationSummaryData(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>For a <code>FINDING</code> investigation, the type of the finding that the investigation analyzed.</p>"""
    threat_assessment: NotRequired[
        "capo_guardduty.types.threat_assessment.ThreatAssessment"
    ]
    """<p>For a <code>FINDING</code> investigation, an assessment of the threat, including how the attack progressed.</p>"""
    countermeasures: NotRequired["capo_guardduty.types.countermeasures.Countermeasures"]
    """<p>For a <code>FINDING</code> investigation, actions that you can take to respond to the threat, grouped by defensive tactic.</p>"""
    account_analysis: NotRequired[
        "capo_guardduty.types.account_analysis.AccountAnalysis"
    ]
    """<p>For an <code>ACCOUNT</code> investigation, an analysis of the findings in the investigated account.</p>"""
    organization_analysis: NotRequired[
        "capo_guardduty.types.organization_analysis.OrganizationAnalysis"
    ]
    """<p>For an <code>ORGANIZATION</code> investigation, an analysis of the findings across the organization.</p>"""
    key_observations: NotRequired[
        "capo_guardduty.types.key_observations.KeyObservations"
    ]
    """<p>The key observations of the investigation.</p>"""
    recommendations: NotRequired["capo_guardduty.types.recommendations.Recommendations"]
    """<p>For an <code>ACCOUNT</code> or <code>ORGANIZATION</code> investigation, the recommended actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationSummaryData) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "threat_assessment" in value:
        import capo_guardduty.types.threat_assessment

        out["threatAssessment"] = capo_guardduty.types.threat_assessment.serialize_json(
            value["threat_assessment"]
        )
    if "countermeasures" in value:
        import capo_guardduty.types.countermeasures

        out["countermeasures"] = capo_guardduty.types.countermeasures.serialize_json(
            value["countermeasures"]
        )
    if "account_analysis" in value:
        import capo_guardduty.types.account_analysis

        out["accountAnalysis"] = capo_guardduty.types.account_analysis.serialize_json(
            value["account_analysis"]
        )
    if "organization_analysis" in value:
        import capo_guardduty.types.organization_analysis

        out["organizationAnalysis"] = (
            capo_guardduty.types.organization_analysis.serialize_json(
                value["organization_analysis"]
            )
        )
    if "key_observations" in value:
        import capo_guardduty.types.key_observations

        out["keyObservations"] = capo_guardduty.types.key_observations.serialize_json(
            value["key_observations"]
        )
    if "recommendations" in value:
        import capo_guardduty.types.recommendations

        out["recommendations"] = capo_guardduty.types.recommendations.serialize_json(
            value["recommendations"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationSummaryData:
    out: InvestigationSummaryData = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("threatAssessment") is not None:
        import capo_guardduty.types.threat_assessment

        out["threat_assessment"] = (
            capo_guardduty.types.threat_assessment.deserialize_json(
                data["threatAssessment"]
            )
        )
    if data.get("countermeasures") is not None:
        import capo_guardduty.types.countermeasures

        out["countermeasures"] = capo_guardduty.types.countermeasures.deserialize_json(
            data["countermeasures"]
        )
    if data.get("accountAnalysis") is not None:
        import capo_guardduty.types.account_analysis

        out["account_analysis"] = (
            capo_guardduty.types.account_analysis.deserialize_json(
                data["accountAnalysis"]
            )
        )
    if data.get("organizationAnalysis") is not None:
        import capo_guardduty.types.organization_analysis

        out["organization_analysis"] = (
            capo_guardduty.types.organization_analysis.deserialize_json(
                data["organizationAnalysis"]
            )
        )
    if data.get("keyObservations") is not None:
        import capo_guardduty.types.key_observations

        out["key_observations"] = (
            capo_guardduty.types.key_observations.deserialize_json(
                data["keyObservations"]
            )
        )
    if data.get("recommendations") is not None:
        import capo_guardduty.types.recommendations

        out["recommendations"] = capo_guardduty.types.recommendations.deserialize_json(
            data["recommendations"]
        )
    return out
