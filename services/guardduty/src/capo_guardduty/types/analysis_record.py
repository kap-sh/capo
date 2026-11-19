"""Generated from Smithy shape ``com.amazonaws.guardduty#AnalysisRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.analysis_type
    import capo_guardduty.types.investigation_account_analysis
    import capo_guardduty.types.investigation_indicators
    import capo_guardduty.types.investigation_threat_assessment
    import capo_guardduty.types.kubernetes_policy_violation
    import capo_guardduty.types.processes
    import capo_guardduty.types.s3_analysis


class AnalysisRecord(TypedDict, closed=True):
    analysis_type: NotRequired["capo_guardduty.types.analysis_type.AnalysisType"]
    """<p>The kind of analysis. The value identifies the payload member that can be set: <code>REPUTATION</code>, <code>THREAT_ASSESSMENT</code>, and <code>RDS_THREAT_ASSESSMENT</code> (<code>ThreatAssessment</code>); <code>KUBERNETES_POLICY_VIOLATION</code> (<code>KubernetesPolicyViolation</code>); <code>S3_EXPOSURE</code>, <code>S3_ACTOR_CONTEXT</code>, and <code>S3_PEN_TEST</code> (<code>S3Analysis</code>); <code>PROCESS_LINEAGE</code> (<code>Processes</code>); and <code>TREND</code> and <code>BASELINE</code> (<code>AccountAnalysis</code>).</p>"""
    threat_assessment: NotRequired[
        "capo_guardduty.types.investigation_threat_assessment.InvestigationThreatAssessment"
    ]
    """<p>A threat assessment. Set when <code>AnalysisType</code> is <code>REPUTATION</code>, <code>THREAT_ASSESSMENT</code>, or <code>RDS_THREAT_ASSESSMENT</code>.</p>"""
    kubernetes_policy_violation: NotRequired[
        "capo_guardduty.types.kubernetes_policy_violation.KubernetesPolicyViolation"
    ]
    """<p>An assessment of a Kubernetes policy violation. Set when <code>AnalysisType</code> is <code>KUBERNETES_POLICY_VIOLATION</code>.</p>"""
    s3_analysis: NotRequired["capo_guardduty.types.s3_analysis.S3Analysis"]
    """<p>An analysis of Amazon S3 activity or exposure. Set when <code>AnalysisType</code> is <code>S3_EXPOSURE</code>, <code>S3_ACTOR_CONTEXT</code>, or <code>S3_PEN_TEST</code>.</p>"""
    processes: NotRequired["capo_guardduty.types.processes.Processes"]
    """<p>The processes in a process lineage. Set when <code>AnalysisType</code> is <code>PROCESS_LINEAGE</code>.</p>"""
    account_analysis: NotRequired[
        "capo_guardduty.types.investigation_account_analysis.InvestigationAccountAnalysis"
    ]
    """<p>An analysis of the findings in an account over time. Set when <code>AnalysisType</code> is <code>TREND</code> or <code>BASELINE</code>.</p>"""
    indicators: NotRequired[
        "capo_guardduty.types.investigation_indicators.InvestigationIndicators"
    ]
    """<p>The threat indicators associated with the analysis, such as an IP address, a domain, or a file hash.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRecord) -> dict:
    out: dict = {}
    if "analysis_type" in value:
        import capo_guardduty.types.analysis_type

        out["analysisType"] = capo_guardduty.types.analysis_type.serialize_json(
            value["analysis_type"]
        )
    if "threat_assessment" in value:
        import capo_guardduty.types.investigation_threat_assessment

        out["threatAssessment"] = (
            capo_guardduty.types.investigation_threat_assessment.serialize_json(
                value["threat_assessment"]
            )
        )
    if "kubernetes_policy_violation" in value:
        import capo_guardduty.types.kubernetes_policy_violation

        out["kubernetesPolicyViolation"] = (
            capo_guardduty.types.kubernetes_policy_violation.serialize_json(
                value["kubernetes_policy_violation"]
            )
        )
    if "s3_analysis" in value:
        import capo_guardduty.types.s3_analysis

        out["s3Analysis"] = capo_guardduty.types.s3_analysis.serialize_json(
            value["s3_analysis"]
        )
    if "processes" in value:
        import capo_guardduty.types.processes

        out["processes"] = capo_guardduty.types.processes.serialize_json(
            value["processes"]
        )
    if "account_analysis" in value:
        import capo_guardduty.types.investigation_account_analysis

        out["accountAnalysis"] = (
            capo_guardduty.types.investigation_account_analysis.serialize_json(
                value["account_analysis"]
            )
        )
    if "indicators" in value:
        import capo_guardduty.types.investigation_indicators

        out["indicators"] = (
            capo_guardduty.types.investigation_indicators.serialize_json(
                value["indicators"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRecord:
    out: AnalysisRecord = {}  # type: ignore[typeddict-item]
    if data.get("analysisType") is not None:
        import capo_guardduty.types.analysis_type

        out["analysis_type"] = capo_guardduty.types.analysis_type.deserialize_json(
            data["analysisType"]
        )
    if data.get("threatAssessment") is not None:
        import capo_guardduty.types.investigation_threat_assessment

        out["threat_assessment"] = (
            capo_guardduty.types.investigation_threat_assessment.deserialize_json(
                data["threatAssessment"]
            )
        )
    if data.get("kubernetesPolicyViolation") is not None:
        import capo_guardduty.types.kubernetes_policy_violation

        out["kubernetes_policy_violation"] = (
            capo_guardduty.types.kubernetes_policy_violation.deserialize_json(
                data["kubernetesPolicyViolation"]
            )
        )
    if data.get("s3Analysis") is not None:
        import capo_guardduty.types.s3_analysis

        out["s3_analysis"] = capo_guardduty.types.s3_analysis.deserialize_json(
            data["s3Analysis"]
        )
    if data.get("processes") is not None:
        import capo_guardduty.types.processes

        out["processes"] = capo_guardduty.types.processes.deserialize_json(
            data["processes"]
        )
    if data.get("accountAnalysis") is not None:
        import capo_guardduty.types.investigation_account_analysis

        out["account_analysis"] = (
            capo_guardduty.types.investigation_account_analysis.deserialize_json(
                data["accountAnalysis"]
            )
        )
    if data.get("indicators") is not None:
        import capo_guardduty.types.investigation_indicators

        out["indicators"] = (
            capo_guardduty.types.investigation_indicators.deserialize_json(
                data["indicators"]
            )
        )
    return out


def redact_sensitive(value: AnalysisRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "indicators" in value:
        import capo_guardduty.types.investigation_indicators

        out["indicators"] = (
            capo_guardduty.types.investigation_indicators.redact_sensitive(
                value["indicators"]
            )
        )
    return out
