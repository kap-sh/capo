"""Generated from Smithy shape ``com.amazonaws.guardduty#ProtectionPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.feature_status
    import capo_guardduty.types.investigation_detector_feature


class ProtectionPlan(TypedDict, closed=True):
    name: NotRequired[
        "capo_guardduty.types.investigation_detector_feature.InvestigationDetectorFeature"
    ]
    """<p>The name of the protection plan. Possible values are <code>CLOUD_TRAIL</code>, <code>DNS_LOGS</code>, <code>FLOW_LOGS</code>, <code>S3_DATA_EVENTS</code>, <code>EKS_AUDIT_LOGS</code>, <code>EBS_MALWARE_PROTECTION</code>, <code>RDS_LOGIN_EVENTS</code>, <code>EKS_RUNTIME_MONITORING</code>, <code>EKS_ADDON_MANAGEMENT</code>, <code>LAMBDA_NETWORK_LOGS</code>, <code>RUNTIME_MONITORING</code>, <code>ECS_FARGATE_AGENT_MANAGEMENT</code>, and <code>EC2_AGENT_MANAGEMENT</code>.</p>"""
    status: NotRequired["capo_guardduty.types.feature_status.FeatureStatus"]
    """<p>The status of the protection plan. Possible values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectionPlan) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.investigation_detector_feature

        out["name"] = (
            capo_guardduty.types.investigation_detector_feature.serialize_json(
                value["name"]
            )
        )
    if "status" in value:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ProtectionPlan:
    out: ProtectionPlan = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_guardduty.types.investigation_detector_feature

        out["name"] = (
            capo_guardduty.types.investigation_detector_feature.deserialize_json(
                data["name"]
            )
        )
    if data.get("status") is not None:
        import capo_guardduty.types.feature_status

        out["status"] = capo_guardduty.types.feature_status.deserialize_json(
            data["status"]
        )
    return out
