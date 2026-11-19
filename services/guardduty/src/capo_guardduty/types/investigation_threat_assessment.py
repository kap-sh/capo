"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationThreatAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.reputation
    import capo_guardduty.types.threat_confidence


class InvestigationThreatAssessment(TypedDict, closed=True):
    reputation: NotRequired["capo_guardduty.types.reputation.Reputation"]
    """<p>Reputation information about a threat indicator. Set when <code>AnalysisType</code> is <code>REPUTATION</code>.</p>"""
    threat_confidence: NotRequired[
        "capo_guardduty.types.threat_confidence.ThreatConfidence"
    ]
    """<p>The confidence in the threat assessment. Possible values are <code>VERY_HIGH</code>, <code>HIGH</code>, <code>MEDIUM</code>, and <code>LOW</code>.</p>"""
    classification: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The classification of the threat.</p>"""
    assessment: NotRequired["capo_guardduty.types.investigation_text.InvestigationText"]
    """<p>The assessment of the threat.</p>"""
    authentication_context: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>Context about how the identity involved in the activity authenticated.</p>"""
    rds_control_plane_activity: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of Amazon RDS control plane activity that is related to the threat.</p>"""
    ip_account_activity: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of the activity from the IP address in the account.</p>"""
    credential_compromise: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of whether credentials were compromised.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationThreatAssessment) -> dict:
    out: dict = {}
    if "reputation" in value:
        import capo_guardduty.types.reputation

        out["reputation"] = capo_guardduty.types.reputation.serialize_json(
            value["reputation"]
        )
    if "threat_confidence" in value:
        import capo_guardduty.types.threat_confidence

        out["threatConfidence"] = capo_guardduty.types.threat_confidence.serialize_json(
            value["threat_confidence"]
        )
    if "classification" in value:
        out["classification"] = value["classification"]
    if "assessment" in value:
        out["assessment"] = value["assessment"]
    if "authentication_context" in value:
        out["authenticationContext"] = value["authentication_context"]
    if "rds_control_plane_activity" in value:
        out["rdsControlPlaneActivity"] = value["rds_control_plane_activity"]
    if "ip_account_activity" in value:
        out["ipAccountActivity"] = value["ip_account_activity"]
    if "credential_compromise" in value:
        out["credentialCompromise"] = value["credential_compromise"]
    return out


def deserialize_json(data: dict) -> InvestigationThreatAssessment:
    out: InvestigationThreatAssessment = {}  # type: ignore[typeddict-item]
    if data.get("reputation") is not None:
        import capo_guardduty.types.reputation

        out["reputation"] = capo_guardduty.types.reputation.deserialize_json(
            data["reputation"]
        )
    if data.get("threatConfidence") is not None:
        import capo_guardduty.types.threat_confidence

        out["threat_confidence"] = (
            capo_guardduty.types.threat_confidence.deserialize_json(
                data["threatConfidence"]
            )
        )
    if data.get("classification") is not None:
        out["classification"] = data["classification"]
    if data.get("assessment") is not None:
        out["assessment"] = data["assessment"]
    if data.get("authenticationContext") is not None:
        out["authentication_context"] = data["authenticationContext"]
    if data.get("rdsControlPlaneActivity") is not None:
        out["rds_control_plane_activity"] = data["rdsControlPlaneActivity"]
    if data.get("ipAccountActivity") is not None:
        out["ip_account_activity"] = data["ipAccountActivity"]
    if data.get("credentialCompromise") is not None:
        out["credential_compromise"] = data["credentialCompromise"]
    return out
