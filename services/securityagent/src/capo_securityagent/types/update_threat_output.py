"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateThreatOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.stride_category_list
    import capo_securityagent.types.string_list
    import capo_securityagent.types.threat_actor
    import capo_securityagent.types.threat_anchor_shape
    import capo_securityagent.types.threat_evidence_list
    import capo_securityagent.types.threat_severity
    import capo_securityagent.types.threat_status


class UpdateThreatOutput(TypedDict, closed=True):
    threat_id: "str"
    """<p>The unique identifier of the threat.</p>"""
    threat_job_id: "str"
    """<p>The unique identifier of the threat model job the threat belongs to.</p>"""
    title: NotRequired["str"]
    """<p>A short title summarizing the threat.</p>"""
    statement: NotRequired["str"]
    """<p>The natural-language threat statement.</p>"""
    severity: NotRequired["capo_securityagent.types.threat_severity.ThreatSeverity"]
    """<p>The severity level of the threat.</p>"""
    status: NotRequired["capo_securityagent.types.threat_status.ThreatStatus"]
    """<p>The current status of the threat.</p>"""
    comments: NotRequired["str"]
    """<p>Optional customer comment on the threat.</p>"""
    stride: NotRequired[
        "capo_securityagent.types.stride_category_list.StrideCategoryList"
    ]
    """<p>The STRIDE categories applicable to this threat.</p>"""
    threat_source: NotRequired["str"]
    """<p>The actor or origin of the threat.</p>"""
    prerequisites: NotRequired["str"]
    """<p>The conditions required for the threat to be exploitable.</p>"""
    threat_action: NotRequired["str"]
    """<p>What the threat source can do.</p>"""
    threat_impact: NotRequired["str"]
    """<p>The direct consequence of the threat action.</p>"""
    impacted_goal: NotRequired["capo_securityagent.types.string_list.StringList"]
    """<p>The security goals affected by the threat.</p>"""
    impacted_assets: NotRequired["capo_securityagent.types.string_list.StringList"]
    """<p>The specific assets affected by the threat.</p>"""
    anchor: NotRequired[
        "capo_securityagent.types.threat_anchor_shape.ThreatAnchorShape"
    ]
    """<p>The DFD element this threat is anchored to.</p>"""
    evidence: NotRequired[
        "capo_securityagent.types.threat_evidence_list.ThreatEvidenceList"
    ]
    """<p>The source code files supporting the threat.</p>"""
    recommendation: NotRequired["str"]
    """<p>The recommended mitigation guidance for this threat.</p>"""
    created_by: NotRequired["capo_securityagent.types.threat_actor.ThreatActor"]
    """<p>Who created this threat.</p>"""
    updated_by: NotRequired["capo_securityagent.types.threat_actor.ThreatActor"]
    """<p>Who last updated this threat.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the threat was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThreatOutput) -> dict:
    out: dict = {}
    out["threatId"] = value["threat_id"]
    out["threatJobId"] = value["threat_job_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "statement" in value:
        out["statement"] = value["statement"]
    if "severity" in value:
        import capo_securityagent.types.threat_severity

        out["severity"] = capo_securityagent.types.threat_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_securityagent.types.threat_status

        out["status"] = capo_securityagent.types.threat_status.serialize_json(
            value["status"]
        )
    if "comments" in value:
        out["comments"] = value["comments"]
    if "stride" in value:
        import capo_securityagent.types.stride_category_list

        out["stride"] = capo_securityagent.types.stride_category_list.serialize_json(
            value["stride"]
        )
    if "threat_source" in value:
        out["threatSource"] = value["threat_source"]
    if "prerequisites" in value:
        out["prerequisites"] = value["prerequisites"]
    if "threat_action" in value:
        out["threatAction"] = value["threat_action"]
    if "threat_impact" in value:
        out["threatImpact"] = value["threat_impact"]
    if "impacted_goal" in value:
        import capo_securityagent.types.string_list

        out["impactedGoal"] = capo_securityagent.types.string_list.serialize_json(
            value["impacted_goal"]
        )
    if "impacted_assets" in value:
        import capo_securityagent.types.string_list

        out["impactedAssets"] = capo_securityagent.types.string_list.serialize_json(
            value["impacted_assets"]
        )
    if "anchor" in value:
        import capo_securityagent.types.threat_anchor_shape

        out["anchor"] = capo_securityagent.types.threat_anchor_shape.serialize_json(
            value["anchor"]
        )
    if "evidence" in value:
        import capo_securityagent.types.threat_evidence_list

        out["evidence"] = capo_securityagent.types.threat_evidence_list.serialize_json(
            value["evidence"]
        )
    if "recommendation" in value:
        out["recommendation"] = value["recommendation"]
    if "created_by" in value:
        import capo_securityagent.types.threat_actor

        out["createdBy"] = capo_securityagent.types.threat_actor.serialize_json(
            value["created_by"]
        )
    if "updated_by" in value:
        import capo_securityagent.types.threat_actor

        out["updatedBy"] = capo_securityagent.types.threat_actor.serialize_json(
            value["updated_by"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateThreatOutput:
    out: UpdateThreatOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatId") is not None:
        out["threat_id"] = data["threatId"]
    else:
        out["threat_id"] = ""
    if data.get("threatJobId") is not None:
        out["threat_job_id"] = data["threatJobId"]
    else:
        out["threat_job_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    if data.get("severity") is not None:
        import capo_securityagent.types.threat_severity

        out["severity"] = capo_securityagent.types.threat_severity.deserialize_json(
            data["severity"]
        )
    if data.get("status") is not None:
        import capo_securityagent.types.threat_status

        out["status"] = capo_securityagent.types.threat_status.deserialize_json(
            data["status"]
        )
    if data.get("comments") is not None:
        out["comments"] = data["comments"]
    if data.get("stride") is not None:
        import capo_securityagent.types.stride_category_list

        out["stride"] = capo_securityagent.types.stride_category_list.deserialize_json(
            data["stride"]
        )
    if data.get("threatSource") is not None:
        out["threat_source"] = data["threatSource"]
    if data.get("prerequisites") is not None:
        out["prerequisites"] = data["prerequisites"]
    if data.get("threatAction") is not None:
        out["threat_action"] = data["threatAction"]
    if data.get("threatImpact") is not None:
        out["threat_impact"] = data["threatImpact"]
    if data.get("impactedGoal") is not None:
        import capo_securityagent.types.string_list

        out["impacted_goal"] = capo_securityagent.types.string_list.deserialize_json(
            data["impactedGoal"]
        )
    if data.get("impactedAssets") is not None:
        import capo_securityagent.types.string_list

        out["impacted_assets"] = capo_securityagent.types.string_list.deserialize_json(
            data["impactedAssets"]
        )
    if data.get("anchor") is not None:
        import capo_securityagent.types.threat_anchor_shape

        out["anchor"] = capo_securityagent.types.threat_anchor_shape.deserialize_json(
            data["anchor"]
        )
    if data.get("evidence") is not None:
        import capo_securityagent.types.threat_evidence_list

        out["evidence"] = (
            capo_securityagent.types.threat_evidence_list.deserialize_json(
                data["evidence"]
            )
        )
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    if data.get("createdBy") is not None:
        import capo_securityagent.types.threat_actor

        out["created_by"] = capo_securityagent.types.threat_actor.deserialize_json(
            data["createdBy"]
        )
    if data.get("updatedBy") is not None:
        import capo_securityagent.types.threat_actor

        out["updated_by"] = capo_securityagent.types.threat_actor.deserialize_json(
            data["updatedBy"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
