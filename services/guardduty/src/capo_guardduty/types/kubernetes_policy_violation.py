"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesPolicyViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class KubernetesPolicyViolation(TypedDict, closed=True):
    violation_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the violation.</p>"""
    affected_resource: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes resource that the violation affects.</p>"""
    subject: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes subject, such as a user, a group, or a service account, that the violation involves.</p>"""
    granted_access: NotRequired["capo_guardduty.types.string.String"]
    """<p>The access that the violation grants.</p>"""
    exposure_vector: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>How the misconfiguration exposes the resource.</p>"""
    misconfiguration_impact: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The potential impact of the misconfiguration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesPolicyViolation) -> dict:
    out: dict = {}
    if "violation_type" in value:
        out["violationType"] = value["violation_type"]
    if "affected_resource" in value:
        out["affectedResource"] = value["affected_resource"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "granted_access" in value:
        out["grantedAccess"] = value["granted_access"]
    if "exposure_vector" in value:
        out["exposureVector"] = value["exposure_vector"]
    if "misconfiguration_impact" in value:
        out["misconfigurationImpact"] = value["misconfiguration_impact"]
    return out


def deserialize_json(data: dict) -> KubernetesPolicyViolation:
    out: KubernetesPolicyViolation = {}  # type: ignore[typeddict-item]
    if data.get("violationType") is not None:
        out["violation_type"] = data["violationType"]
    if data.get("affectedResource") is not None:
        out["affected_resource"] = data["affectedResource"]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    if data.get("grantedAccess") is not None:
        out["granted_access"] = data["grantedAccess"]
    if data.get("exposureVector") is not None:
        out["exposure_vector"] = data["exposureVector"]
    if data.get("misconfigurationImpact") is not None:
        out["misconfiguration_impact"] = data["misconfigurationImpact"]
    return out
