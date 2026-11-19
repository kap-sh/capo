"""Generated from Smithy shape ``com.amazonaws.guardduty#S3Analysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class S3Analysis(TypedDict, closed=True):
    finding_subtype: NotRequired["capo_guardduty.types.string.String"]
    """<p>The subtype of the finding.</p>"""
    effective_permission: NotRequired["capo_guardduty.types.string.String"]
    """<p>The effective permission of the Amazon S3 resource.</p>"""
    block_public_access_settings: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the Amazon S3 Block Public Access settings.</p>"""
    exposure: NotRequired["capo_guardduty.types.investigation_text.InvestigationText"]
    """<p>An assessment of the exposure of the Amazon S3 resource.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user agent of the caller.</p>"""
    user_agent_classification: NotRequired["capo_guardduty.types.string.String"]
    """<p>The classification of the user agent.</p>"""
    source_ip: NotRequired["capo_guardduty.types.string.String"]
    """<p>The source address of the activity, or a description of the source.</p>"""
    ip_reputation: NotRequired["capo_guardduty.types.string.String"]
    """<p>The reputation of the source IP address.</p>"""
    actor_assessment: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of the identity that performed the activity.</p>"""
    s3_api_activity: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A description of the Amazon S3 API activity.</p>"""
    source_context: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>Context about the source of the activity.</p>"""
    authorization_assessment: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An assessment of whether the activity was authorized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Analysis) -> dict:
    out: dict = {}
    if "finding_subtype" in value:
        out["findingSubtype"] = value["finding_subtype"]
    if "effective_permission" in value:
        out["effectivePermission"] = value["effective_permission"]
    if "block_public_access_settings" in value:
        out["blockPublicAccessSettings"] = value["block_public_access_settings"]
    if "exposure" in value:
        out["exposure"] = value["exposure"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "user_agent_classification" in value:
        out["userAgentClassification"] = value["user_agent_classification"]
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "ip_reputation" in value:
        out["ipReputation"] = value["ip_reputation"]
    if "actor_assessment" in value:
        out["actorAssessment"] = value["actor_assessment"]
    if "s3_api_activity" in value:
        out["s3ApiActivity"] = value["s3_api_activity"]
    if "source_context" in value:
        out["sourceContext"] = value["source_context"]
    if "authorization_assessment" in value:
        out["authorizationAssessment"] = value["authorization_assessment"]
    return out


def deserialize_json(data: dict) -> S3Analysis:
    out: S3Analysis = {}  # type: ignore[typeddict-item]
    if data.get("findingSubtype") is not None:
        out["finding_subtype"] = data["findingSubtype"]
    if data.get("effectivePermission") is not None:
        out["effective_permission"] = data["effectivePermission"]
    if data.get("blockPublicAccessSettings") is not None:
        out["block_public_access_settings"] = data["blockPublicAccessSettings"]
    if data.get("exposure") is not None:
        out["exposure"] = data["exposure"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    if data.get("userAgentClassification") is not None:
        out["user_agent_classification"] = data["userAgentClassification"]
    if data.get("sourceIp") is not None:
        out["source_ip"] = data["sourceIp"]
    if data.get("ipReputation") is not None:
        out["ip_reputation"] = data["ipReputation"]
    if data.get("actorAssessment") is not None:
        out["actor_assessment"] = data["actorAssessment"]
    if data.get("s3ApiActivity") is not None:
        out["s3_api_activity"] = data["s3ApiActivity"]
    if data.get("sourceContext") is not None:
        out["source_context"] = data["sourceContext"]
    if data.get("authorizationAssessment") is not None:
        out["authorization_assessment"] = data["authorizationAssessment"]
    return out
