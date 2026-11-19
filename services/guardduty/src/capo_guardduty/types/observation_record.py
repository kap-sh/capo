"""Generated from Smithy shape ``com.amazonaws.guardduty#ObservationRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_overview
    import capo_guardduty.types.detection_coverage
    import capo_guardduty.types.distribution
    import capo_guardduty.types.finding_detail
    import capo_guardduty.types.investigation_indicators
    import capo_guardduty.types.investigation_malware_scan
    import capo_guardduty.types.investigation_resource
    import capo_guardduty.types.kubernetes_activity
    import capo_guardduty.types.network_activity
    import capo_guardduty.types.observation_type
    import capo_guardduty.types.rds_login_activity
    import capo_guardduty.types.recommendations
    import capo_guardduty.types.related_findings
    import capo_guardduty.types.representative_findings
    import capo_guardduty.types.runtime_signals
    import capo_guardduty.types.s3_activity


class ObservationRecord(TypedDict, closed=True):
    observation_type: NotRequired[
        "capo_guardduty.types.observation_type.ObservationType"
    ]
    """<p>The kind of observation. The value identifies the payload member that can be set: <code>FINDING_DETAIL</code> (<code>FindingDetail</code>), <code>RESOURCE</code> (<code>Resource</code>), <code>NETWORK_ACTIVITY</code> (<code>NetworkActivity</code>), <code>RDS_LOGIN_ACTIVITY</code> (<code>RdsLoginActivity</code>), <code>S3_ACTIVITY</code> (<code>S3Activity</code>), <code>KUBERNETES_ACTIVITY</code> (<code>KubernetesActivity</code>), <code>MALWARE_SCAN</code> (<code>MalwareScan</code>), <code>RELATED_FINDINGS</code> (<code>RelatedFindings</code>), <code>DETECTION_COVERAGE</code> (<code>DetectionCoverage</code>), <code>ACCOUNT_OVERVIEW</code> (<code>AccountOverview</code>), <code>RECOMMENDATION</code> (<code>Recommendations</code>), <code>RUNTIME_SIGNALS</code> (<code>RuntimeSignals</code>), <code>DISTRIBUTION</code> (<code>Distribution</code>), and <code>REPRESENTATIVE_RESOURCE</code> (<code>RepresentativeResources</code>).</p>"""
    finding_detail: NotRequired["capo_guardduty.types.finding_detail.FindingDetail"]
    """<p>Details about a GuardDuty finding. Set when <code>ObservationType</code> is <code>FINDING_DETAIL</code>.</p>"""
    resource: NotRequired[
        "capo_guardduty.types.investigation_resource.InvestigationResource"
    ]
    """<p>Details about an affected resource. Set when <code>ObservationType</code> is <code>RESOURCE</code>.</p>"""
    network_activity: NotRequired[
        "capo_guardduty.types.network_activity.NetworkActivity"
    ]
    """<p>Details about network activity. Set when <code>ObservationType</code> is <code>NETWORK_ACTIVITY</code>.</p>"""
    rds_login_activity: NotRequired[
        "capo_guardduty.types.rds_login_activity.RdsLoginActivity"
    ]
    """<p>Details about login activity on an Amazon RDS database. Set when <code>ObservationType</code> is <code>RDS_LOGIN_ACTIVITY</code>.</p>"""
    s3_activity: NotRequired["capo_guardduty.types.s3_activity.S3Activity"]
    """<p>Details about Amazon S3 activity. Set when <code>ObservationType</code> is <code>S3_ACTIVITY</code>.</p>"""
    kubernetes_activity: NotRequired[
        "capo_guardduty.types.kubernetes_activity.KubernetesActivity"
    ]
    """<p>Details about Kubernetes activity. Set when <code>ObservationType</code> is <code>KUBERNETES_ACTIVITY</code>.</p>"""
    malware_scan: NotRequired[
        "capo_guardduty.types.investigation_malware_scan.InvestigationMalwareScan"
    ]
    """<p>Details about a malware scan. Set when <code>ObservationType</code> is <code>MALWARE_SCAN</code>.</p>"""
    related_findings: NotRequired[
        "capo_guardduty.types.related_findings.RelatedFindings"
    ]
    """<p>Details about findings that are related to the investigated activity. Set when <code>ObservationType</code> is <code>RELATED_FINDINGS</code>.</p>"""
    detection_coverage: NotRequired[
        "capo_guardduty.types.detection_coverage.DetectionCoverage"
    ]
    """<p>Details about your detection coverage. Set when <code>ObservationType</code> is <code>DETECTION_COVERAGE</code>.</p>"""
    account_overview: NotRequired[
        "capo_guardduty.types.account_overview.AccountOverview"
    ]
    """<p>Overview information about an account. Set when <code>ObservationType</code> is <code>ACCOUNT_OVERVIEW</code>.</p>"""
    recommendations: NotRequired["capo_guardduty.types.recommendations.Recommendations"]
    """<p>Recommended actions. Set when <code>ObservationType</code> is <code>RECOMMENDATION</code>.</p>"""
    runtime_signals: NotRequired["capo_guardduty.types.runtime_signals.RuntimeSignals"]
    """<p>A summary of runtime signals. Set when <code>ObservationType</code> is <code>RUNTIME_SIGNALS</code>.</p>"""
    distribution: NotRequired["capo_guardduty.types.distribution.Distribution"]
    """<p>A breakdown of findings along one dimension. Set when <code>ObservationType</code> is <code>DISTRIBUTION</code>.</p>"""
    representative_resources: NotRequired[
        "capo_guardduty.types.representative_findings.RepresentativeFindings"
    ]
    """<p>Representative findings for the affected resources, one finding for each resource. Set when <code>ObservationType</code> is <code>REPRESENTATIVE_RESOURCE</code>.</p>"""
    indicators: NotRequired[
        "capo_guardduty.types.investigation_indicators.InvestigationIndicators"
    ]
    """<p>The threat indicators associated with the observation, such as an IP address, a domain, or a file hash.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObservationRecord) -> dict:
    out: dict = {}
    if "observation_type" in value:
        import capo_guardduty.types.observation_type

        out["observationType"] = capo_guardduty.types.observation_type.serialize_json(
            value["observation_type"]
        )
    if "finding_detail" in value:
        import capo_guardduty.types.finding_detail

        out["findingDetail"] = capo_guardduty.types.finding_detail.serialize_json(
            value["finding_detail"]
        )
    if "resource" in value:
        import capo_guardduty.types.investigation_resource

        out["resource"] = capo_guardduty.types.investigation_resource.serialize_json(
            value["resource"]
        )
    if "network_activity" in value:
        import capo_guardduty.types.network_activity

        out["networkActivity"] = capo_guardduty.types.network_activity.serialize_json(
            value["network_activity"]
        )
    if "rds_login_activity" in value:
        import capo_guardduty.types.rds_login_activity

        out["rdsLoginActivity"] = (
            capo_guardduty.types.rds_login_activity.serialize_json(
                value["rds_login_activity"]
            )
        )
    if "s3_activity" in value:
        import capo_guardduty.types.s3_activity

        out["s3Activity"] = capo_guardduty.types.s3_activity.serialize_json(
            value["s3_activity"]
        )
    if "kubernetes_activity" in value:
        import capo_guardduty.types.kubernetes_activity

        out["kubernetesActivity"] = (
            capo_guardduty.types.kubernetes_activity.serialize_json(
                value["kubernetes_activity"]
            )
        )
    if "malware_scan" in value:
        import capo_guardduty.types.investigation_malware_scan

        out["malwareScan"] = (
            capo_guardduty.types.investigation_malware_scan.serialize_json(
                value["malware_scan"]
            )
        )
    if "related_findings" in value:
        import capo_guardduty.types.related_findings

        out["relatedFindings"] = capo_guardduty.types.related_findings.serialize_json(
            value["related_findings"]
        )
    if "detection_coverage" in value:
        import capo_guardduty.types.detection_coverage

        out["detectionCoverage"] = (
            capo_guardduty.types.detection_coverage.serialize_json(
                value["detection_coverage"]
            )
        )
    if "account_overview" in value:
        import capo_guardduty.types.account_overview

        out["accountOverview"] = capo_guardduty.types.account_overview.serialize_json(
            value["account_overview"]
        )
    if "recommendations" in value:
        import capo_guardduty.types.recommendations

        out["recommendations"] = capo_guardduty.types.recommendations.serialize_json(
            value["recommendations"]
        )
    if "runtime_signals" in value:
        import capo_guardduty.types.runtime_signals

        out["runtimeSignals"] = capo_guardduty.types.runtime_signals.serialize_json(
            value["runtime_signals"]
        )
    if "distribution" in value:
        import capo_guardduty.types.distribution

        out["distribution"] = capo_guardduty.types.distribution.serialize_json(
            value["distribution"]
        )
    if "representative_resources" in value:
        import capo_guardduty.types.representative_findings

        out["representativeResources"] = (
            capo_guardduty.types.representative_findings.serialize_json(
                value["representative_resources"]
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


def deserialize_json(data: dict) -> ObservationRecord:
    out: ObservationRecord = {}  # type: ignore[typeddict-item]
    if data.get("observationType") is not None:
        import capo_guardduty.types.observation_type

        out["observation_type"] = (
            capo_guardduty.types.observation_type.deserialize_json(
                data["observationType"]
            )
        )
    if data.get("findingDetail") is not None:
        import capo_guardduty.types.finding_detail

        out["finding_detail"] = capo_guardduty.types.finding_detail.deserialize_json(
            data["findingDetail"]
        )
    if data.get("resource") is not None:
        import capo_guardduty.types.investigation_resource

        out["resource"] = capo_guardduty.types.investigation_resource.deserialize_json(
            data["resource"]
        )
    if data.get("networkActivity") is not None:
        import capo_guardduty.types.network_activity

        out["network_activity"] = (
            capo_guardduty.types.network_activity.deserialize_json(
                data["networkActivity"]
            )
        )
    if data.get("rdsLoginActivity") is not None:
        import capo_guardduty.types.rds_login_activity

        out["rds_login_activity"] = (
            capo_guardduty.types.rds_login_activity.deserialize_json(
                data["rdsLoginActivity"]
            )
        )
    if data.get("s3Activity") is not None:
        import capo_guardduty.types.s3_activity

        out["s3_activity"] = capo_guardduty.types.s3_activity.deserialize_json(
            data["s3Activity"]
        )
    if data.get("kubernetesActivity") is not None:
        import capo_guardduty.types.kubernetes_activity

        out["kubernetes_activity"] = (
            capo_guardduty.types.kubernetes_activity.deserialize_json(
                data["kubernetesActivity"]
            )
        )
    if data.get("malwareScan") is not None:
        import capo_guardduty.types.investigation_malware_scan

        out["malware_scan"] = (
            capo_guardduty.types.investigation_malware_scan.deserialize_json(
                data["malwareScan"]
            )
        )
    if data.get("relatedFindings") is not None:
        import capo_guardduty.types.related_findings

        out["related_findings"] = (
            capo_guardduty.types.related_findings.deserialize_json(
                data["relatedFindings"]
            )
        )
    if data.get("detectionCoverage") is not None:
        import capo_guardduty.types.detection_coverage

        out["detection_coverage"] = (
            capo_guardduty.types.detection_coverage.deserialize_json(
                data["detectionCoverage"]
            )
        )
    if data.get("accountOverview") is not None:
        import capo_guardduty.types.account_overview

        out["account_overview"] = (
            capo_guardduty.types.account_overview.deserialize_json(
                data["accountOverview"]
            )
        )
    if data.get("recommendations") is not None:
        import capo_guardduty.types.recommendations

        out["recommendations"] = capo_guardduty.types.recommendations.deserialize_json(
            data["recommendations"]
        )
    if data.get("runtimeSignals") is not None:
        import capo_guardduty.types.runtime_signals

        out["runtime_signals"] = capo_guardduty.types.runtime_signals.deserialize_json(
            data["runtimeSignals"]
        )
    if data.get("distribution") is not None:
        import capo_guardduty.types.distribution

        out["distribution"] = capo_guardduty.types.distribution.deserialize_json(
            data["distribution"]
        )
    if data.get("representativeResources") is not None:
        import capo_guardduty.types.representative_findings

        out["representative_resources"] = (
            capo_guardduty.types.representative_findings.deserialize_json(
                data["representativeResources"]
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


def redact_sensitive(value: ObservationRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource" in value:
        import capo_guardduty.types.investigation_resource

        out["resource"] = capo_guardduty.types.investigation_resource.redact_sensitive(
            value["resource"]
        )
    if "indicators" in value:
        import capo_guardduty.types.investigation_indicators

        out["indicators"] = (
            capo_guardduty.types.investigation_indicators.redact_sensitive(
                value["indicators"]
            )
        )
    return out
